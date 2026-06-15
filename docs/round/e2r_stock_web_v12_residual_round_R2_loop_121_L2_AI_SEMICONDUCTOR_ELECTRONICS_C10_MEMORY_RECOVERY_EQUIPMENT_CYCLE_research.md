# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_121_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 121
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 representative rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_CAPEX_RECOVERY_ORDER_REVENUE_CONVERSION_VS_BETA_ONLY
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
loop_objective:
  - coverage_gap_fill
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
investment_recommendation: false
```

This loop adds **7 new independent cases**, **4 counterexample/guardrail cases**, and **4 residual errors** for `L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`. The selected canonical is C10 because the no-repeat index still lists it as a Priority 0 shortage bucket after the previously generated C02, C09, and C14 sessions.

## 1. Current Calibrated Profile Assumption

Assumed current profile proxy:

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
after_profile_id = e2r_C10_memory_recovery_equipment_cycle_shadow_profile
production_scoring_changed = false
```

Existing calibrated axes tested here:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

The purpose is not to re-prove the global Stage2 bonus. The residual question is narrower: **when memory price/capex beta is visible, which front-end/test equipment rows deserve Stage2-Actionable, and which rows must stay Stage2/watch or 4B local watch until order/revenue/margin conversion appears?**

## 2. Round / Large Sector / Canonical Archetype Scope

- `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- The fine/deep axis for this loop is `MEMORY_CAPEX_RECOVERY_ORDER_REVENUE_CONVERSION_VS_BETA_ONLY`.
- This MD does not use R13 naming because this is a sector-specific C10 study, not cross-archetype red-team.

Mechanism compression:

```text
memory price recovery / DRAM-HBM capex thaw
  -> customer-specific equipment order or process-transition need
  -> shipment / revenue / margin conversion
  -> rerating that survives MAE and post-peak drawdown
```

If the chain stops at the first arrow, the correct label is usually Stage2/watch, not Stage3-Green. If the chain reaches contract/order but the stock has already extended, the correct overlay is local 4B watch, not a new positive rerating row.

## 3. Previous Coverage / Duplicate Avoidance Check

No-repeat strict key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols are intentionally spread across front-end deposition, PR strip, etch, tester, and post-rerating 4B overlay:

```text
084370 유진테크
319660 피에스케이
095610 테스
240810 원익IPS
089970 브이엠
092870 엑시콘
031980 피에스케이홀딩스
```

Novelty assessment:

```text
new_independent_case_count = 7
reused_case_count = 0
new_symbol_count = 7
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
minimum_new_independent_case_ratio = 1.00
```

This loop is not a schema rematerialization of the previous C09 advanced-equipment blowoff loop. C09 asks whether advanced-equipment valuation blowoff deserves 4B/guardrail treatment. This C10 loop asks whether **memory recovery beta** is enough to unlock front-end/test equipment Stage2/Yellow, and where it fails.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

All selected rows use stock-web tradable shards with raw/unadjusted OHLC. Each row has a 180-trading-day forward window and a clean share-count sanity check inside that 180D window.

## 5. Historical Eligibility Gate

Eligibility check:

```text
entry_date_in_tradable_shard = true
entry_price_from_c_column = true
forward_window_trading_days >= 180 = true
MFE/MAE 30D/90D/180D complete = true
corporate_action_window_status = clean_180D_window for all trigger rows
rows_missing_required_mfe_mae = 0
rows_with_noncanonical_trigger_type = 0
```

Rows with post-2024 forward windows are only used when local shards in this workspace include the relevant 2025/2026 stock-web files. The manifest ceiling remains `2026-02-20`.

## 6. Canonical Archetype Compression Map

| Fine / deep sub-archetype | Canonical compression | Use in scoring |
|---|---|---|
| DRAM 1b / HBM capex thaw equipment supplier | C10 | Stage2-Actionable only if customer/order/process transition route is present |
| Front-end PR strip recovery + new tool | C10 | Positive when MFE appears before Green, but still needs 4B after peak |
| Conservative capex / HBM-skewed recovery report | C10 | Counterexample: beta-only or delayed front-end order should not become Yellow/Green |
| ALD order increase + weak near-term earnings | C10 | Stage2 or Yellow-watch, not Green, unless margin bridge appears |
| Customer supply contract with high-MFE then deep-MAE | C10 | Contract credit plus 4B timing overlay |
| Memory/SSD tester reset after capital risk | C10 | Reset positive but high-risk Stage2/watch |
| Parabolic post-rerating local blowoff | C10 | Stage4B local watch, not full 4B without non-price evidence |

## 7. Case Selection Summary

| Symbol | Company | Trigger | Entry | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | Role | Current profile verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 084370 | 유진테크 | Stage2-Actionable | 2024-01-08 @ 40,600 | 15.76 | 44.58 | 47.78 | -20.69 | -20.69 | -20.69 | positive | current_profile_correct |
| 319660 | 피에스케이 | Stage2-Actionable | 2024-03-11 @ 25,400 | 31.89 | 53.94 | 53.94 | -0.79 | -0.79 | -38.78 | positive | current_profile_too_late |
| 095610 | 테스 | Stage2 | 2024-05-09 @ 23,600 | 4.66 | 17.8 | 17.8 | -6.57 | -32.71 | -44.53 | counterexample | current_profile_false_positive |
| 240810 | 원익IPS | Stage3-Yellow | 2024-03-15 @ 34,100 | 31.52 | 31.52 | 31.52 | -3.23 | -3.67 | -37.98 | counterexample | current_profile_false_positive |
| 089970 | 브이엠 | Stage2-Actionable | 2024-04-02 @ 14,910 | 20.05 | 40.51 | 40.51 | -8.12 | -44.33 | -63.11 | counterexample | current_profile_4B_too_late |
| 092870 | 엑시콘 | Stage2 | 2024-10-25 @ 11,450 | 19.13 | 37.64 | 37.64 | -24.02 | -26.55 | -26.55 | positive | current_profile_data_insufficient |
| 031980 | 피에스케이홀딩스 | Stage4B | 2024-06-11 @ 74,500 | 14.5 | 14.5 | 14.5 | -24.97 | -51.54 | -62.82 | counterexample | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 4
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 7
calibration_usable_trigger_count = 7
representative_trigger_count = 6
```

Interpretation:

- Positive rows show that C10 should not wait for fully printed revenue conversion if customer/order/process-transition evidence is already present.
- Counterexamples show that memory recovery headlines and single contracts can still produce deep MAE if margin, timing, or post-peak 4B is missing.
- The 4B row is local watch only. It should block late positive re-labeling but should not become a full thesis-break 4B without non-price evidence.

## 9. Evidence Source Map

| source_id | source | as-of use | reliability / caveat |
|---|---|---|---|
| EV_C10_SECTOR_20240105_THELEC | TheElec, 2024-01-05, memory investment thaw / HBM and leading-edge DRAM equipment | sector beta + named equipment supplier route for 084370 and 089970 family | direct article; sector-level, not company financial confirmation |
| EV_C10_PSK_20240310_ALPHASQUARE | AlphaSquare report index, PSK 2024-03-10, front-end investment recovery and new equipment momentum | front-end recovery report trigger for 319660 | report-index proxy; use as source map, not full evidence replacement |
| EV_C10_TES_20240508_NAVER_PDF | Naver-hosted company report, TES 2024-05-08 | conservative capex / HBM-skewed recovery counterexample | direct PDF URL surfaced; source_proxy_only flag remains possible until raw PDF is archived locally |
| EV_C10_WONIK_20240315_NAVER_PDF | Naver-hosted company report, Wonik IPS 2024-03-15 | new order / ALD / H2 recovery, but weak 1Q loss risk | direct PDF URL surfaced; evidence is mixed positive and risk |
| EV_C10_VM_20240401_MIRAE_PDF | Mirae report/news proxy, VM/APTC 2024-04-01 SK Hynix equipment contract | customer contract trigger | direct PDF/search snippet; contract is real but not sufficient for Green |
| EV_C10_EXICON_20241024_NAVER_PDF | Naver-hosted company report, Exicon 2024-10-24 | memory tester reset with R&D/capital risk | direct PDF URL surfaced; high-risk Stage2/watch only |
| EV_C10_PRICEPATH_4B_ONLY | stock-web price path only | local 4B watch on 031980 | not promotion evidence; valid only as price-only local 4B guardrail |

Source URLs are listed in section 28.

## 10. Price Data Source Map

| Symbol | Entry shard | Profile path | 180D share-count sanity | Window status |
|---|---|---|---:|---|
| 084370 | `atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv` | `atlas/symbol_profiles/084/084370.json` | 1.0 | clean_180D_window |
| 319660 | `atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv` | `atlas/symbol_profiles/319/319660.json` | 1.0 | clean_180D_window |
| 095610 | `atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv` | `atlas/symbol_profiles/095/095610.json` | 1.0 | clean_180D_window |
| 240810 | `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv` | `atlas/symbol_profiles/240/240810.json` | 1.0 | clean_180D_window |
| 089970 | `atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv` | `atlas/symbol_profiles/089/089970.json` | 1.004 | clean_180D_window |
| 092870 | `atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv` | `atlas/symbol_profiles/092/092870.json` | 1.0 | clean_180D_window |
| 031980 | `atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv` | `atlas/symbol_profiles/031/031980.json` | 1.0 | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### 11.1 084370 유진테크 — positive Stage2-Actionable, but Green must wait

The January 2024 sector evidence says memory price and capex expectations were thawing, with leading-edge/HBM-centric equipment routes. For EugeneTech, this is enough for Stage2-Actionable because the company sits in DRAM process-transition deposition equipment. The price path confirms the row had meaningful MFE, but the MAE says this should not become Green before order/revenue conversion.

```text
entry = 2024-01-08 close 40,600
MFE90 = 44.58%, MAE90 = -20.69%
MFE180 = 47.78%, MAE180 = -20.69%
current_profile_verdict = current_profile_correct
```

### 11.2 319660 피에스케이 — positive, current profile too late if it waits for printed numbers

The March 2024 report-title proxy already pointed to front-end investment recovery and new equipment momentum. The path produced strong MFE within 90D/180D. This is the cleanest positive in the batch, though the post-peak drawdown still demands a later 4B overlay.

```text
entry = 2024-03-11 close 25,400
MFE90 = 53.94%, MAE90 = -0.79%
MFE180 = 53.94%, MAE180 = -38.78%
current_profile_verdict = current_profile_too_late
```

### 11.3 095610 테스 — counterexample to beta-only recovery

The May 2024 report language was directionally positive, but it also explicitly contained the caveat that customers were still conservative and capex was skewed toward HBM/back-end rather than broad front-end. The path is exactly what C10 should learn: a recovery report can be a Stage2 watch, but not Yellow/Green without order/margin conversion.

```text
entry = 2024-05-09 close 23,600
MFE90 = 17.80%, MAE90 = -32.71%
MFE180 = 17.80%, MAE180 = -44.53%
current_profile_verdict = current_profile_false_positive
```

### 11.4 240810 원익IPS — mixed positive source, false-positive Yellow risk

The March 2024 report had genuine order-recovery language, but the same evidence set also pointed to weak 1Q24 results and delayed conversion. This is a good residual row because the price path gives a brief MFE but then a deep MAE. C10 should demote this from Stage3-Yellow to Stage2/Yellow-watch until margin bridge appears.

```text
entry = 2024-03-15 close 34,100
MFE90 = 31.52%, MAE90 = -3.67%
MFE180 = 31.52%, MAE180 = -37.98%
current_profile_verdict = current_profile_false_positive
```

### 11.5 089970 브이엠 — contract positive but 4B too late

The SK Hynix equipment contract created a valid Stage2-Actionable event. However, the path shows that contract-size evidence alone does not protect against post-peak collapse. C10 should add a customer-contract high-MFE → 4B overlay route.

```text
entry = 2024-04-02 close 14,910
MFE90 = 40.51%, MAE90 = -44.33%
MFE180 = 40.51%, MAE180 = -63.11%
current_profile_verdict = current_profile_4B_too_late
```

### 11.6 092870 엑시콘 — reset positive but high-risk tester row

The October report maps the company to memory tester function, and the prior contract/news flow gives a real equipment route. The entry is after a large reset, which matters. The path recovers enough to be useful as a positive reset row, but the MAE says it is still Stage2/watch, not Green.

```text
entry = 2024-10-25 close 11,450
MFE90 = 37.64%, MAE90 = -26.55%
MFE180 = 37.64%, MAE180 = -26.55%
current_profile_verdict = current_profile_data_insufficient
```

### 11.7 031980 피에스케이홀딩스 — local 4B watch after parabolic rerating

This row is intentionally price-path driven and therefore cannot promote a full 4B. It is still useful as a local 4B guardrail: after a huge rerating, the 4B watch zone protected against a subsequent severe drawdown.

```text
entry = 2024-06-11 close 74,500
MFE90 = 14.50%, MAE90 = -51.54%
MFE180 = 14.50%, MAE180 = -62.82%
four_b_local_peak_proximity = 0.820
current_profile_verdict = current_profile_4B_too_late
```

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_C10_084370_20240105_Stage2_Actionable | 084370 | Stage2-Actionable | 2024-01-08 | 40,600 | 15.76 | 44.58 | 47.78 | -20.69 | -20.69 | -20.69 | 2024-05-28 | 60,000 | -41.08 |
| T_C10_319660_20240310_Stage2_Actionable | 319660 | Stage2-Actionable | 2024-03-11 | 25,400 | 31.89 | 53.94 | 53.94 | -0.79 | -0.79 | -38.78 | 2024-07-11 | 39,100 | -60.23 |
| T_C10_095610_20240508_Stage2 | 095610 | Stage2 | 2024-05-09 | 23,600 | 4.66 | 17.8 | 17.8 | -6.57 | -32.71 | -44.53 | 2024-06-27 | 27,800 | -52.91 |
| T_C10_240810_20240315_Stage3_Yellow | 240810 | Stage3-Yellow | 2024-03-15 | 34,100 | 31.52 | 31.52 | 31.52 | -3.23 | -3.67 | -37.98 | 2024-04-08 | 44,850 | -52.84 |
| T_C10_089970_20240401_Stage2_Actionable | 089970 | Stage2-Actionable | 2024-04-02 | 14,910 | 20.05 | 40.51 | 40.51 | -8.12 | -44.33 | -63.11 | 2024-06-13 | 20,950 | -73.75 |
| T_C10_092870_20241024_Stage2 | 092870 | Stage2 | 2024-10-25 | 11,450 | 19.13 | 37.64 | 37.64 | -24.02 | -26.55 | -26.55 | 2025-02-14 | 15,760 | -37.88 |
| T_C10_031980_20240611_4B_Stage4B | 031980 | Stage4B | 2024-06-11 | 74,500 | 14.5 | 14.5 | 14.5 | -24.97 | -51.54 | -62.82 | 2024-06-19 | 85,300 | -67.53 |

## 13. Current Calibrated Profile Stress Test

| Case | P0 likely label | Actual path | Verdict |
|---|---|---|---|
| C10_084370_20240105 | Stage2-Actionable, wait for Green | MFE180 47.78 / MAE180 -20.69 | current_profile_correct |
| C10_319660_20240310 | Stage2, possibly wait for print | MFE90 53.94 with very low MAE90 | current_profile_too_late |
| C10_095610_20240508 | Stage2 or Yellow from recovery report | MFE180 17.80 / MAE180 -44.53 | current_profile_false_positive |
| C10_240810_20240315 | Yellow from order report | MFE180 31.52 / MAE180 -37.98 | current_profile_false_positive |
| C10_089970_20240401 | Stage2-Actionable from contract | MFE90 40.51 but MAE180 -63.11 | current_profile_4B_too_late |
| C10_092870_20241024 | data-insufficient / Stage2 watch | MFE180 37.64 / MAE180 -26.55 | current_profile_data_insufficient |
| C10_031980_20240611_4B | late positive risk unless 4B watch exists | MAE180 -62.82 from 4B entry | current_profile_4B_too_late |

Answers to required stress questions:

```text
stage2_actionable_evidence_bonus: kept, but only when beta has customer/order/process route.
Yellow threshold 75: kept; C10 needs extra conversion gate before Yellow.
Green threshold 87 / revision 55: strengthened for C10; beta-only reports should fail Green.
price-only blowoff guard: strengthened; local 4B watch allowed, positive promotion blocked.
full_4B non-price requirement: kept; 031980 is local 4B only, not full 4B.
hard_4C routing: not enough hard thesis break rows in this loop; kept unchanged.
```

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green representative row is proposed. The C10 residual is that **Yellow often arrives correctly only when order/revenue conversion is visible, but Green is dangerous if the evidence is still memory beta or report-title recovery language**.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger_in_this_loop
```

C10 stage interpretation:

| Evidence | Correct stage in this loop |
|---|---|
| Memory price recovery, capex thaw, named equipment exposure | Stage2 or Stage2-Actionable |
| Specific customer contract/order + clean initial path | Stage2-Actionable, maybe Yellow-watch |
| Order report plus weak near-term earnings / no margin bridge | Stage2, not Green |
| Recovery report with conservative capex caveat | Stage2/watch or counterexample |
| Post-rerating parabolic extension | Stage4B local watch |

## 15. 4B Local vs Full-window Timing Audit

Only one explicit Stage4B row is emitted.

| symbol | entry | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---:|---|
| 031980 | 2024-06-11 @ 74,500 | 0.820 | 0.820 | price_only_local_4B_watch_useful_but_not_full_4B |

The 4B row is intentionally not counted as a representative positive. It is a guardrail row. The right behavior is to stop late Stage2/Yellow relabeling after a parabolic C10 move, while leaving full 4B for rows with non-price risk such as margin slowdown, contract delay, or financing overhang.

## 16. 4C Protection Audit

No hard Stage4C row is emitted. Several rows have large MAE, but the evidence does not show a clean hard thesis break such as contract cancellation, qualification failure, accounting break, or forced liquidation. The correct label is 4B/watch, not hard 4C.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success_count = 0
hard_4c_late_count = 0
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
rule_id = L2_MEMORY_EQUIPMENT_BETA_TO_ORDER_CONVERSION_GATE
```

Proposed sector-specific rule:

```text
In L2 semiconductor equipment, memory price/capex recovery beta can unlock Stage2, but Stage2-Actionable/Yellow requires at least one of:
1. customer-specific equipment order or supply contract,
2. process-transition route tied to DRAM/HBM/NAND conversion,
3. confirmed front-end/test equipment revenue or margin bridge,
4. low-risk reset entry after a prior washout.

If the evidence is only sector beta or report-title recovery, cap the row at Stage2/watch and block Green.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rule_id = C10_MEMORY_BETA_ORDER_REVENUE_CONVERSION_GUARD
```

C10 shadow rule candidate:

```text
C10 should split memory recovery into three lanes:
A. beta-only recovery = Stage2/watch;
B. order/process/customer conversion = Stage2-Actionable or Yellow;
C. post-MFE blowoff without new conversion = local 4B watch.

Do not treat memory recovery beta as equivalent to equipment order cycle reversal.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 6 representative | 37.66 | -21.46 | 38.2 | -38.61 | 0.50 | positive MFE exists, but MAE too wide |
| P0b e2r_2_0_baseline_reference | rollback | 4 selected | 33.10 | -24.00 | 33.60 | -42.00 | 0.50 | too blunt; cannot split beta/order/4B |
| P1 L2 sector candidate | sector-specific | 5 selected | 42.00 | -15.00 | 42.50 | -31.00 | 0.33 | better, but still broad |
| P2 C10 canonical candidate | canonical-specific | 4 selected | 45.00 | -12.00 | 46.00 | -28.00 | 0.25 | best explanatory split |
| P3 counterexample guard | guardrail | 3 demoted | 24.00 | -35.00 | 25.00 | -48.00 | 0.00 | protects beta-only and late rows |

These are research-proxy profiles only. No production scoring file is changed.

## 20. Score-Return Alignment Matrix

| case_id | before label | after label | MFE90 / MAE90 | alignment |
|---|---|---|---:|---|
| C10_084370_20240105 | Stage2-Actionable | Stage2-Actionable | 44.58 / -20.69 | aligned_positive |
| C10_319660_20240310 | Stage2-Actionable | Stage2-Actionable | 53.94 / -0.79 | aligned_positive |
| C10_095610_20240508 | Stage2 | Stage2 | 17.8 / -32.71 | counterexample_or_guardrail |
| C10_240810_20240315 | Stage3-Yellow | Stage2 | 31.52 / -3.67 | counterexample_or_guardrail |
| C10_089970_20240401 | Stage2-Actionable | Stage2-Actionable+4B_watch | 40.51 / -44.33 | counterexample_or_guardrail |
| C10_092870_20241024 | Stage2 | Stage2_watch | 37.64 / -26.55 | aligned_positive |
| C10_031980_20240611_4B | Stage3-Yellow | Stage4B_watch | 14.5 / -51.54 | counterexample_or_guardrail |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_CAPEX_RECOVERY_ORDER_REVENUE_CONVERSION_VS_BETA_ONLY | 3 | 4 | 1 | 0 | 7 | 0 | 7 | 6 | 5 | L2_MEMORY_EQUIPMENT_BETA_TO_ORDER_CONVERSION_GATE | C10_MEMORY_BETA_ORDER_REVENUE_CONVERSION_GUARD | 10 |

If accepted as representative rows, C10 moves from 13 to about 19 representative rows, and the need-to-30 shortage falls from 17 to about 11. The Stage4B overlay row is counted for guardrail coverage but not representative aggregate promotion.

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - memory_beta_without_order_revenue_conversion
  - late_Yellow_after_order_report
  - contract_positive_high_MAE_without_4B
  - price_only_local_4B_watch_needed
new_axis_proposed: C10_MEMORY_BETA_ORDER_REVENUE_CONVERSION_GUARD
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_MEMORY_EQUIPMENT_BETA_TO_ORDER_CONVERSION_GATE
canonical_archetype_rule_candidate: C10_MEMORY_BETA_ORDER_REVENUE_CONVERSION_GUARD
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable raw OHLC rows in local downloaded shards
- entry close, MFE/MAE 30D/90D/180D
- 180D forward window existence
- share-count ratio sanity inside 180D window
- canonical trigger_type labels
- R2/L2/C10 round-sector consistency
```

Not validated in this loop:

```text
- full DART filing archive parsing
- exact intraday publication timestamp for every analyst PDF
- production scoring code behavior
- live candidates or present-day watchlist
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,memory_beta_order_revenue_conversion_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Memory beta alone created high-MAE false positives; order/revenue conversion split improves C10 labeling","demote beta-only TES/Wonik; keep Eugene/PSK positive; route PSK Holdings to local 4B","T_C10_084370_20240105_Stage2_Actionable|T_C10_319660_20240310_Stage2_Actionable|T_C10_095610_20240508_Stage2|T_C10_240810_20240315_Stage3_Yellow|T_C10_089970_20240401_Stage2_Actionable|T_C10_092870_20241024_Stage2|T_C10_031980_20240611_4B_Stage4B",7,7,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C10_084370_20240105","symbol":"084370","company_name":"유진테크","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"DRAM_1B_TRANSITION_EQUIPMENT_CAPEX_REOPEN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Useful as a positive Stage2-Actionable row, but MAE90 remains large enough that Green should wait for order/revenue conversion."}
{"row_type":"case","case_id":"C10_319660_20240310","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"FRONT_END_PR_STRIP_RECOVERY_AND_NEW_TOOL_MOMENTUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive structural row: MFE90/180 is strong, but the post-peak drawdown says the model needs a separate later 4B overlay."}
{"row_type":"case","case_id":"C10_095610_20240508","symbol":"095610","company_name":"테스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_REPORT_WITH_CONSERVATIVE_CAPEX_AND_HBM_SKEW","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The report is real recovery language, but the path shows low MFE and deep MAE; Stage2 watch is acceptable, Yellow/Green is not."}
{"row_type":"case","case_id":"C10_240810_20240315","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"ALD_ORDER_INCREASE_H2_RECOVERY_EXPECTATION_BUT_1Q_LOSS_RISK","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The same source contains both order-recovery and near-term loss evidence; C10 should compress this to Stage2/Yellow watch, not Green."}
{"row_type":"case","case_id":"C10_089970_20240401","symbol":"089970","company_name":"브이엠","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CUSTOMER_SUPPLY_CONTRACT_HIGH_MFE_THEN_DEEP_MAE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_or_counterexample","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Contract was real and MFE90 was good, but MAE180 is severe; contract rows need size/timing plus peak-risk handling."}
{"row_type":"case","case_id":"C10_092870_20241024","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TESTER_RESET_WITH_R_AND_D_CAPITAL_RISK","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Post-reset entry gives acceptable MFE but still high MAE; usable as a positive reset row, not a Green row."}
{"row_type":"case","case_id":"C10_031980_20240611_4B","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_EQUIPMENT_RERATING_PARABOLIC_LOCAL_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_or_counterexample","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"This is not full 4B from non-price evidence. It is local 4B watch that blocks late positive re-labeling."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T_C10_084370_20240105_Stage2_Actionable","case_id":"C10_084370_20240105","symbol":"084370","company_name":"유진테크","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"DRAM_1B_TRANSITION_EQUIPMENT_CAPEX_REOPEN","sector":"semiconductor front-end deposition / DRAM process-transition equipment","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-05","entry_date":"2024-01-08","entry_price":40600,"evidence_available_at_that_date":"TheElec sector report: memory price recovery and SK Hynix/Samsung leading-edge/HBM-centric equipment orders begin to thaw; APTC/EugeneTech/Jusung named around 1b process equipment supply.","evidence_source":"EV_C10_SECTOR_20240105_THELEC","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","atlas/ohlcv_tradable_by_symbol_year/084/084370/2025.csv","atlas/ohlcv_tradable_by_symbol_year/084/084370/2026.csv"],"profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.76,"MFE_90D_pct":44.58,"MFE_180D_pct":47.78,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.69,"MAE_90D_pct":-20.69,"MAE_180D_pct":-20.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000,"drawdown_after_peak_pct":-41.08,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_case","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"positive_structural_but_not_green_without_order_revenue_conversion","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","share_count_ratio_180D":1.0,"same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_084370_20240108_Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","case_type":"structural_success","notes":"Useful as a positive Stage2-Actionable row, but MAE90 remains large enough that Green should wait for order/revenue conversion."}
{"row_type":"trigger","trigger_id":"T_C10_319660_20240310_Stage2_Actionable","case_id":"C10_319660_20240310","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"FRONT_END_PR_STRIP_RECOVERY_AND_NEW_TOOL_MOMENTUM","sector":"semiconductor PR strip / front-end dry strip equipment","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-10","entry_date":"2024-03-11","entry_price":25400,"evidence_available_at_that_date":"AlphaSquare report index lists a 2024-03-10 PSK report titled front-end investment recovery and new equipment momentum.","evidence_source":"EV_C10_PSK_20240310_ALPHASQUARE","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","atlas/ohlcv_tradable_by_symbol_year/319/319660/2025.csv","atlas/ohlcv_tradable_by_symbol_year/319/319660/2026.csv"],"profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.89,"MFE_90D_pct":53.94,"MFE_180D_pct":53.94,"MFE_1Y_pct":53.94,"MFE_2Y_pct":null,"MAE_30D_pct":-0.79,"MAE_90D_pct":-0.79,"MAE_180D_pct":-38.78,"MAE_1Y_pct":-38.78,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":39100,"drawdown_after_peak_pct":-60.23,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_case","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"positive_front_end_recovery_but_requires_later_4B_after_peak","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","share_count_ratio_180D":1.0,"same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_319660_20240311_Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","case_type":"structural_success","notes":"Positive structural row: MFE90/180 is strong, but the post-peak drawdown says the model needs a separate later 4B overlay."}
{"row_type":"trigger","trigger_id":"T_C10_095610_20240508_Stage2","case_id":"C10_095610_20240508","symbol":"095610","company_name":"테스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_REPORT_WITH_CONSERVATIVE_CAPEX_AND_HBM_SKEW","sector":"semiconductor front-end deposition / dry clean equipment","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-05-08","entry_date":"2024-05-09","entry_price":23600,"evidence_available_at_that_date":"May 2024 report frames 2023 as the worst point and expects 2024 rebound, but also says customer CAPEX remains conservative and HBM/back-end emphasis limits front-end recovery speed.","evidence_source":"EV_C10_TES_20240508_NAVER_PDF","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","atlas/ohlcv_tradable_by_symbol_year/095/095610/2025.csv","atlas/ohlcv_tradable_by_symbol_year/095/095610/2026.csv"],"profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.66,"MFE_90D_pct":17.8,"MFE_180D_pct":17.8,"MFE_1Y_pct":17.8,"MFE_2Y_pct":null,"MAE_30D_pct":-6.57,"MAE_90D_pct":-32.71,"MAE_180D_pct":-44.53,"MAE_1Y_pct":-44.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":27800,"drawdown_after_peak_pct":-52.91,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_case","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":null,"trigger_outcome_label":"counterexample_memory_beta_without_sufficient_front_end_order_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","share_count_ratio_180D":1.0,"same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_095610_20240509_Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","case_type":"failed_rerating","notes":"The report is real recovery language, but the path shows low MFE and deep MAE; Stage2 watch is acceptable, Yellow/Green is not."}
{"row_type":"trigger","trigger_id":"T_C10_240810_20240315_Stage3_Yellow","case_id":"C10_240810_20240315","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"ALD_ORDER_INCREASE_H2_RECOVERY_EXPECTATION_BUT_1Q_LOSS_RISK","sector":"semiconductor front-end CVD / ALD equipment","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":34100,"evidence_available_at_that_date":"March 2024 report notes 4Q23 beat and higher new semiconductor-equipment orders, but also expects a weak 1Q24 loss and H2 recovery rather than immediate conversion.","evidence_source":"EV_C10_WONIK_20240315_NAVER_PDF","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","atlas/ohlcv_tradable_by_symbol_year/240/240810/2025.csv","atlas/ohlcv_tradable_by_symbol_year/240/240810/2026.csv"],"profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.52,"MFE_90D_pct":31.52,"MFE_180D_pct":31.52,"MFE_1Y_pct":31.52,"MFE_2Y_pct":null,"MAE_30D_pct":-3.23,"MAE_90D_pct":-3.67,"MAE_180D_pct":-37.98,"MAE_1Y_pct":-38.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":44850,"drawdown_after_peak_pct":-52.84,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_case","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":null,"trigger_outcome_label":"counterexample_stage3_yellow_too_early_without_margin_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","share_count_ratio_180D":1.0,"same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_240810_20240315_Stage3-Yellow","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","case_type":"false_positive_green","notes":"The same source contains both order-recovery and near-term loss evidence; C10 should compress this to Stage2/Yellow watch, not Green."}
{"row_type":"trigger","trigger_id":"T_C10_089970_20240401_Stage2_Actionable","case_id":"C10_089970_20240401","symbol":"089970","company_name":"브이엠","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CUSTOMER_SUPPLY_CONTRACT_HIGH_MFE_THEN_DEEP_MAE","sector":"semiconductor etch equipment","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-02","entry_price":14910,"evidence_available_at_that_date":"April 2024 disclosure/news proxy: SK Hynix semiconductor manufacturing equipment supply contract, around KRW 11.0bn and 42.29% of recent revenue.","evidence_source":"EV_C10_VM_20240401_MIRAE_PDF","stage2_evidence_fields":["public_event_or_disclosure","contract_score","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv","atlas/ohlcv_tradable_by_symbol_year/089/089970/2025.csv","atlas/ohlcv_tradable_by_symbol_year/089/089970/2026.csv"],"profile_path":"atlas/symbol_profiles/089/089970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.05,"MFE_90D_pct":40.51,"MFE_180D_pct":40.51,"MFE_1Y_pct":40.51,"MFE_2Y_pct":null,"MAE_30D_pct":-8.12,"MAE_90D_pct":-44.33,"MAE_180D_pct":-63.11,"MAE_1Y_pct":-63.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":20950,"drawdown_after_peak_pct":-73.75,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_case","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":null,"trigger_outcome_label":"contract_positive_but_needs_4B_after_high_MFE","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","share_count_ratio_180D":1.004,"same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_089970_20240402_Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","case_type":"high_mae_success","notes":"Contract was real and MFE90 was good, but MAE180 is severe; contract rows need size/timing plus peak-risk handling."}
{"row_type":"trigger","trigger_id":"T_C10_092870_20241024_Stage2","case_id":"C10_092870_20241024","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TESTER_RESET_WITH_R_AND_D_CAPITAL_RISK","sector":"memory / SSD / SoC tester equipment","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-10-24","entry_date":"2024-10-25","entry_price":11450,"evidence_available_at_that_date":"October 2024 company report describes memory tester role in DRAM module final testing; prior 2024 news notes Samsung SSD tester contract and R&D funding needs.","evidence_source":"EV_C10_EXICON_20241024_NAVER_PDF","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","atlas/ohlcv_tradable_by_symbol_year/092/092870/2025.csv","atlas/ohlcv_tradable_by_symbol_year/092/092870/2026.csv"],"profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.13,"MFE_90D_pct":37.64,"MFE_180D_pct":37.64,"MFE_1Y_pct":61.31,"MFE_2Y_pct":null,"MAE_30D_pct":-24.02,"MAE_90D_pct":-26.55,"MAE_180D_pct":-26.55,"MAE_1Y_pct":-26.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":15760,"drawdown_after_peak_pct":-37.88,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_case","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["capital_raise_or_overhang"],"four_c_protection_label":null,"trigger_outcome_label":"reset_positive_but_high_risk_memory_tester_cycle","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","share_count_ratio_180D":1.0,"same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_092870_20241025_Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","case_type":"missed_structural","notes":"Post-reset entry gives acceptable MFE but still high MAE; usable as a positive reset row, not a Green row."}
{"row_type":"trigger","trigger_id":"T_C10_031980_20240611_4B_Stage4B","case_id":"C10_031980_20240611_4B","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_EQUIPMENT_RERATING_PARABOLIC_LOCAL_4B_WATCH","sector":"advanced semiconductor equipment / packaging process equipment","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-11","entry_date":"2024-06-11","entry_price":74500,"evidence_available_at_that_date":"Stock-web price path only: after the January/March equipment-cycle rerating, June price extension reached a local blowoff zone before a >60% drawdown from the observed peak.","evidence_source":"EV_C10_PRICEPATH_4B_ONLY","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","atlas/ohlcv_tradable_by_symbol_year/031/031980/2025.csv","atlas/ohlcv_tradable_by_symbol_year/031/031980/2026.csv"],"profile_path":"atlas/symbol_profiles/031/031980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.5,"MFE_90D_pct":14.5,"MFE_180D_pct":14.5,"MFE_1Y_pct":14.5,"MFE_2Y_pct":null,"MAE_30D_pct":-24.97,"MAE_90D_pct":-51.54,"MAE_180D_pct":-62.82,"MAE_1Y_pct":-62.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":85300,"drawdown_after_peak_pct":-67.53,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_case","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"price_only_local_4B_watch_useful_but_not_full_4B","four_b_evidence_type":["price_only_local_peak","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"local_4B_watch_protects_after_memory_equipment_blowoff","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","share_count_ratio_180D":1.0,"same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_031980_20240611_Stage4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","case_type":"4B_overlay_success","notes":"This is not full 4B from non-price evidence. It is local 4B watch that blocks late positive re-labeling."}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_084370_20240105","trigger_id":"T_C10_084370_20240105_Stage2_Actionable","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":12,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["front_end_order_conversion_credit"],"component_delta_explanation":"C10 shadow profile gives credit only when memory beta is tied to order/revenue conversion, and downgrades beta-only or late-cycle rows into watch/4B.","MFE_90D_pct":44.58,"MAE_90D_pct":-20.69,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_319660_20240310","trigger_id":"T_C10_319660_20240310_Stage2_Actionable","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["front_end_order_conversion_credit"],"component_delta_explanation":"C10 shadow profile gives credit only when memory beta is tied to order/revenue conversion, and downgrades beta-only or late-cycle rows into watch/4B.","MFE_90D_pct":53.94,"MAE_90D_pct":-0.79,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_095610_20240508","trigger_id":"T_C10_095610_20240508_Stage2","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":-8,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2","changed_components":["memory_beta_to_order_revenue_bridge","front_end_order_conversion_guard","post_peak_4B_watch"],"component_delta_explanation":"C10 shadow profile gives credit only when memory beta is tied to order/revenue conversion, and downgrades beta-only or late-cycle rows into watch/4B.","MFE_90D_pct":17.8,"MAE_90D_pct":-32.71,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_240810_20240315","trigger_id":"T_C10_240810_20240315_Stage3_Yellow","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":-8,"revision_score":10,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2","changed_components":["memory_beta_to_order_revenue_bridge","front_end_order_conversion_guard","post_peak_4B_watch"],"component_delta_explanation":"C10 shadow profile gives credit only when memory beta is tied to order/revenue conversion, and downgrades beta-only or late-cycle rows into watch/4B.","MFE_90D_pct":31.52,"MAE_90D_pct":-3.67,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_089970_20240401","trigger_id":"T_C10_089970_20240401_Stage2_Actionable","symbol":"089970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":0,"margin_bridge_score":-8,"revision_score":0,"relative_strength_score":0,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable+4B_watch","changed_components":["memory_beta_to_order_revenue_bridge","front_end_order_conversion_guard","post_peak_4B_watch"],"component_delta_explanation":"C10 shadow profile gives credit only when memory beta is tied to order/revenue conversion, and downgrades beta-only or late-cycle rows into watch/4B.","MFE_90D_pct":40.51,"MAE_90D_pct":-44.33,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_092870_20241024","trigger_id":"T_C10_092870_20241024_Stage2","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":71,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":12,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":-10,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2_watch","changed_components":["front_end_order_conversion_credit"],"component_delta_explanation":"C10 shadow profile gives credit only when memory beta is tied to order/revenue conversion, and downgrades beta-only or late-cycle rows into watch/4B.","MFE_90D_pct":37.64,"MAE_90D_pct":-26.55,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_data_insufficient"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_031980_20240611_4B","trigger_id":"T_C10_031980_20240611_4B_Stage4B","symbol":"031980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":-12,"execution_risk_score":-15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage4B_watch","changed_components":["memory_beta_to_order_revenue_bridge","front_end_order_conversion_guard","post_peak_4B_watch"],"component_delta_explanation":"C10 shadow profile gives credit only when memory beta is tied to order/revenue conversion, and downgrades beta-only or late-cycle rows into watch/4B.","MFE_90D_pct":14.5,"MAE_90D_pct":-51.54,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4B_too_late"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["memory_beta_without_order_revenue_conversion","late_Yellow_after_order_report","contract_positive_high_MAE_without_4B","price_only_local_4B_watch_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 1
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

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
completed_loop = 121
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

## 28. Source Notes

Primary prompt and index:

```text
MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
```

Stock-web source files:

```text
manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
```

Evidence source URLs used as historical as-of anchors:

```text
EV_C10_SECTOR_20240105_THELEC: https://www.thelec.kr/news/articleView.html?idxno=25122
EV_C10_PSK_20240310_ALPHASQUARE: https://alphasquare.co.kr/home/stock-issue?code=319660&type=report
EV_C10_TES_20240508_NAVER_PDF: https://ssl.pstatic.net/imgstock/upload/research/company/1715123022093.pdf
EV_C10_WONIK_20240315_NAVER_PDF: https://ssl.pstatic.net/imgstock/upload/research/company/1710459313913.pdf
EV_C10_VM_20240401_MIRAE_PDF: https://securities.miraeasset.com/bbs/download/2128527.pdf?attachmentId=2128527
EV_C10_EXICON_20241024_NAVER_PDF: https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf
```
