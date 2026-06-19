# E2R Stock-Web v12 Residual Research — R1 Loop 128 / L1 / C05

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 128
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype: EPC_mega_contract_margin_gap_and_quality_break
output_file: e2r_stock_web_v12_residual_round_R1_loop_128_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
generated_at: 2026-06-17
main_execution_prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Execution Scope and Prohibitions

This file is a standalone historical calibration / sector-archetype residual research artifact.
It does **not** create live recommendations, live watchlists, brokerage actions, auto-trading rules, production scoring changes, or any `stock_agent` code patch.

The only price data used here is Stock-Web `tradable_raw` OHLCV. Research artifacts are used only for coverage and duplicate avoidance.

## 2. Coverage-Index Selection

`V12_Research_No_Repeat_Index.md` shows that all C01~C32 archetypes now exceed the early 30/50/80-row fill thresholds. The next research priority is quality reinforcement: URL/proxy repair, missing direct evidence replacement, balance strengthening, false-positive reduction, and 4C timing repair.

Selected target:

```text
selected_priority_bucket = Priority 1 balance strengthening + Priority 0 direct-source/proxy repair
selected_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
selection_reason = C05 has 180 representative rows, 54 symbols, positives/counter 29/39, 4B/4C 23/10.
quality_gap = margin/working-capital failure counterexamples and 4C transition timing supplement
selected_round = R1
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
round_sector_consistency = pass
```

## 3. No-Repeat / Novelty Check

Hard duplicate key tested internally:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows avoid repeating the same key. The loop number follows the observed prior C05/R1 sequence where the latest visible C05 root loop was 127, therefore this file uses loop 128. If the repo root changes after the 2026-06-15 index snapshot, rerun the index before ingest, but the case keys themselves remain valid new rows for this materialization.

## 4. Stock-Web Manifest Validation

Manifest and schema fields used:

| field | value |
|---|---:|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

MFE/MAE formula follows the schema: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 5. Symbol Profile Validation

| symbol | company | profile last_date | corporate_action_candidate_dates relevant to window | 180D usable |
|---|---|---:|---|---|
| 028050 | 삼성E&A / 삼성엔지니어링 | 2026-02-20 | no 2020/2023 overlap; old candidates 1997/1999/2016 | true |
| 047040 | 대우건설 | 2026-02-20 | no 2021 overlap; old candidates 2001/2003/2011 | true |
| 000720 | 현대건설 | 2026-02-20 | no 2023 overlap; old candidates 1998/1999/2001/2004 | true |
| 006360 | GS건설 | 2026-02-20 | no 2023 overlap; old candidates 1999/2014 | true |
| 294870 | HDC현대산업개발 | 2026-02-20 | no 2022 overlap; candidate 2020-03-26 outside window | true |

## 6. Research Thesis

C05 does not need more generic proof that a mega EPC order can move price. The residual question is narrower:

1. A mega contract is **not** enough if realized margin, cash conversion, working-capital discipline, or project execution quality is absent.
2. C05 should allow Green only when contract visibility is tied to realized profitability or backlog-to-margin bridge.
3. Construction quality failures, fatal collapses, rebar omissions, license-cancellation risk, and mandatory rebuild/reputation breaks should hard-route to 4C earlier than price-only damage.

## 7. Evidence Cases

| case_id | symbol | company | trigger | entry_date | entry_close | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post_peak_DD | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_028050_2020_HUGRS_ORDER_HIGH_MAE | 028050 | 삼성엔지니어링 | Stage2-Actionable | 2020-01-28 | 17,800 | 3.65 | -30.06 | 3.65 | -61.18 | 3.65 | -61.18 | 2020-01-29 / 18,450 | -62.55 | counterexample_high_MAE |
| C05_028050_2023_RESULTS_MARGIN_BRIDGE | 028050 | 삼성엔지니어링 | Stage3-Green | 2023-02-01 | 26,450 | 15.31 | -4.35 | 22.50 | -4.35 | 42.91 | -4.35 | 2023-08-02 / 37,800 | -29.50 | positive_margin_bridge |
| C05_047040_2021_ALFAW_PORT_ORDER | 047040 | 대우건설 | Stage2-Actionable | 2021-01-04 | 5,150 | 30.10 | -1.75 | 55.34 | -1.75 | 85.24 | -1.75 | 2021-06-02 / 9,540 | -33.12 | positive_stage2_actionable |
| C05_000720_2023_AMIRAL_ORDER_NO_MARGIN | 000720 | 현대건설 | Stage2-Actionable | 2023-06-26 | 40,800 | 8.82 | -15.32 | 8.82 | -18.50 | 8.82 | -23.53 | 2023-06-26 / 44,400 | -29.73 | counterexample_order_only |
| C05_006360_2023_GEOMDAN_QUALITY_4C | 006360 | GS건설 | Stage4C | 2023-05-10 | 20,950 | 5.73 | -4.53 | 5.73 | -36.18 | 5.73 | -39.52 | 2023-05-24 / 22,150 | -42.80 | hard_4C_counterexample |
| C05_294870_2022_GWANGJU_COLLAPSE_4C | 294870 | HDC현대산업개발 | Stage4C | 2022-01-12 | 20,850 | 8.87 | -35.25 | 8.87 | -36.93 | 8.87 | -50.84 | 2022-01-12 / 22,700 | -54.85 | hard_4C_counterexample |


## 8. Actual Entry OHLC Rows

| symbol | entry_date | o | h | l | c | v | a | mc | m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 028050 | 2020-01-28 | 17,900 | 18,000 | 17,600 | 17,800 | 1,102,718 | 19,673,890,800 | 3,488,800,000,000 | KOSPI |
| 028050 | 2023-02-01 | 26,100 | 26,900 | 25,600 | 26,450 | 2,500,313 | 66,111,310,450 | 5,184,200,000,000 | KOSPI |
| 047040 | 2021-01-04 | 5,250 | 5,270 | 5,060 | 5,150 | 9,249,864 | 47,703,539,935 | 2,140,456,585,700 | KOSPI |
| 000720 | 2023-06-26 | 42,700 | 44,400 | 40,400 | 40,800 | 8,540,029 | 359,525,992,200 | 4,543,315,212,000 | KOSPI |
| 006360 | 2023-05-10 | 21,200 | 21,500 | 20,850 | 20,950 | 774,236 | 16,363,912,950 | 1,792,932,215,500 | KOSPI |
| 294870 | 2022-01-12 | 21,800 | 22,700 | 20,600 | 20,850 | 11,344,769 | 246,206,254,250 | 1,374,167,830,500 | KOSPI |


## 9. Trigger-Level Backtest Interpretation

### Positive / constructive rows

- `C05_028050_2023_RESULTS_MARGIN_BRIDGE`: a clear positive Green row. The source contains realized revenue, operating profit, YoY operating-profit expansion, new orders, and backlog. Price path reached `MFE_180D_pct=42.91` with limited `MAE_180D_pct=-4.35`.
- `C05_047040_2021_ALFAW_PORT_ORDER`: a strong Stage2-Actionable positive. The Iraq Al Faw order and overseas-order target bridge led to `MFE_180D_pct=85.24` with shallow `MAE_180D_pct=-1.75`.

### Counterexample / residual rows

- `C05_028050_2020_HUGRS_ORDER_HIGH_MAE`: order size was large, but the entry immediately became high-MAE under the 2020 shock. This confirms that C05 order visibility alone should not unlock Green.
- `C05_000720_2023_AMIRAL_ORDER_NO_MARGIN`: the largest-order style headline did not protect price; `MAE_180D_pct=-23.53` while `MFE_180D_pct=8.82`. This is the cleanest order-only false-positive guard.
- `C05_006360_2023_GEOMDAN_QUALITY_4C` and `C05_294870_2022_GWANGJU_COLLAPSE_4C`: these are not ordinary weak-price rows; they are non-price thesis breaks. They should be handled as hard 4C, not as delayed 4B watch.

## 10. Stage2 / Stage2-Actionable / Yellow / Green / 4B / 4C Alignment

| stage label | C05 interpretation from this loop | retained / changed |
|---|---|---|
| Stage2 | contract headline, LOI, early order news without margin bridge | retained, but no Green migration |
| Stage2-Actionable | signed mega order with backlog/order-target bridge but no realized margin proof | retained |
| Stage3-Yellow | signed mega order plus some execution progress, but working-capital/margin visibility incomplete | narrowed |
| Stage3-Green | realized OP/margin/backlog bridge or cash-conversion evidence after mega project revenue recognition | allowed |
| Stage4B | price/valuation exhaustion or local blowoff with no hard evidence break | retained as local watch only |
| Stage4C | construction quality/legal/trust break, collapse, rebar admission, license cancellation/rebuild risk | strengthened |

## 11. Current Calibrated Profile Stress Test

The current proxy profile improved global Stage3 looseness, but C05 still has a sector-specific blind spot: it overvalues headline order visibility when the margin/cash bridge is missing. In this loop, three of six rows are false-positive/high-MAE if order magnitude is allowed to carry the case too far.

Stress-test result:

```text
current_profile_survives:
  - realized margin/backlog bridge positive rows
  - signed order rows as Stage2-Actionable
current_profile_needs_shadow_guard:
  - order-only mega EPC without margin/cash bridge
  - quality/legal thesis breaks requiring immediate Stage4C
```

## 12. Raw Component Score Breakdown

Scale is a proxy 0~10 inspection scale, not production code. It is included to expose which raw axis drives the residual.

| case_id | order/EPS | visibility | bottleneck | margin bridge | valuation | capital/cash | info/legal | profile issue |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| C05_028050_2020_HUGRS_ORDER_HIGH_MAE | 9 | 9 | 6 | 1 | 5 | 4 | 7 | order visibility dominates too much |
| C05_028050_2023_RESULTS_MARGIN_BRIDGE | 9 | 9 | 6 | 9 | 6 | 7 | 8 | clean Green allowed |
| C05_047040_2021_ALFAW_PORT_ORDER | 9 | 9 | 6 | 5 | 5 | 5 | 7 | positive but should remain actionable unless margin bridge appears |
| C05_000720_2023_AMIRAL_ORDER_NO_MARGIN | 10 | 10 | 7 | 2 | 4 | 4 | 8 | order-only false-positive risk |
| C05_006360_2023_GEOMDAN_QUALITY_4C | 0 | 9 | 8 | -8 | -5 | -7 | 10 | hard thesis break |
| C05_294870_2022_GWANGJU_COLLAPSE_4C | 0 | 10 | 8 | -8 | -6 | -8 | 10 | hard thesis break |

## 13. Current vs Proposed Shadow Decision

| case_id | current proxy tendency | proposed C05 shadow decision |
|---|---|---|
| C05_028050_2020_HUGRS_ORDER_HIGH_MAE | could over-promote order visibility | cap at Stage2-Actionable; margin bridge required for Yellow/Green |
| C05_028050_2023_RESULTS_MARGIN_BRIDGE | true positive Green | keep / reinforce Green |
| C05_047040_2021_ALFAW_PORT_ORDER | good Stage2-Actionable | keep as Stage2-Actionable until margin evidence |
| C05_000720_2023_AMIRAL_ORDER_NO_MARGIN | false positive if Green | cap; order headline alone cannot Green |
| C05_006360_2023_GEOMDAN_QUALITY_4C | can be too late if treated as price damage | hard 4C immediately |
| C05_294870_2022_GWANGJU_COLLAPSE_4C | can be too late if treated as price damage | hard 4C immediately |

## 14. 4B Local vs Full-Window Proximity

C05 should not let price-only local rebounds after a damaged contractor thesis become full 4B or renewed Stage2. GS E&C and HDC Hyundai Development show that a post-break rebound can occur after severe drawdowns, but the non-price thesis break remains active. Therefore:

```text
if construction_quality_or_legal_trust_break == true:
  Stage4C overrides local 4B
  full_4B_requires_non_price_repair_evidence = true
  local_bounce_only = watch_not_promotion
```

## 15. Positive and Counterexample Balance

This loop adds:

| type | count | symbols |
|---|---:|---|
| positive / constructive | 2 | 028050, 047040 |
| counterexample / high-MAE | 2 | 028050, 000720 |
| hard 4C thesis break | 2 | 006360, 294870 |
| distinct symbols | 5 | 028050, 047040, 000720, 006360, 294870 |

The balance intentionally leans counterexample-heavy because the index already identifies C05 as needing margin/working-capital failure counterexamples and 4C transition timing supplement.

## 16. Sector-Specific Residual Rule Candidate

### Rule C05-R1-128-A — Mega EPC order-only cap

```text
scope = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
if evidence_family == mega_EPC_contract_headline
and realized_margin_bridge == false
and cash_conversion_or_working_capital_bridge == false:
    max_stage = Stage2-Actionable
    block_Stage3_Green = true
```

### Rule C05-R1-128-B — Realized margin/backlog unlock

```text
if signed_order_visibility == true
and realized_operating_profit_improvement == true
and backlog_or_new_order_visibility == true
and no_project_quality_legal_break == true:
    Stage3_Green_allowed = true
```

### Rule C05-R1-128-C — Quality/legal trust hard 4C

```text
if builder_quality_failure_admitted == true
or collapse_fatality_or_rebuild_risk == true
or government_license_cancellation_or_business_suspension_risk == true:
    route_to = Stage4C
    override_Stage2_Stage3_and_full_4B = true
```

## 17. Shadow Weight Candidate

| axis | before C05 runtime | proposed shadow | reason |
|---|---:|---:|---|
| EPS/order | 18 | 16 | headline order should not dominate |
| visibility | 22 | 23 | direct evidence and large public contract remain useful |
| bottleneck | 10 | 8 | EPC capacity scarcity weaker than execution evidence |
| margin/working-capital | 12 | 14 | key residual axis for C05 |
| valuation | 10 | 9 | valuation less predictive than cash/margin bridge |
| capital/cash | 8 | 10 | working-capital stress critical in EPC |
| info/legal/trust | 20 | 20 | keep high; routes hard 4C |

CSV-style row:

```csv
row_type,scope,axis_before,axis_after,expected_effect
shadow_weight,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,18/22/10/12/10/8/20,16/23/8/14/9/10/20,reduce_order_headline_false_positive_and_accelerate_4C
```

## 18. Machine-Readable JSONL Rows

```jsonl
{"row_type": "price_source_validation", "source_name": "FinanceData/marcap", "price_data_source": "Songdaiki/stock-web", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_tradable_row_count": 14354401, "manifest_raw_row_count": 15214118, "manifest_symbol_count": 5414, "MFE_MAE_formula_basis": "max high/min low from entry_date through N tradable rows divided by entry close"}
{"row_type": "case", "case_id": "C05_028050_2020_HUGRS_ORDER_HIGH_MAE", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "028050", "company": "Samsung Engineering / 삼성엔지니어링", "event_summary": "Saudi Aramco HUGRS EPC order, US$1.85B, completion expected 2023; order visibility high but immediate realized margin/working-capital bridge not confirmed.", "case_role": "counterexample_high_MAE", "evidence_family": "mega_EPC_order_without_realized_margin_bridge", "evidence_url": "https://www.euro-petrole.com/samsung-engineering-signs-dollars-1-85-billion-aramco-gas-project-in-saudi-arabia-n-i-20303", "calibration_usable": true}
{"row_type": "case", "case_id": "C05_028050_2023_RESULTS_MARGIN_BRIDGE", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "028050", "company": "Samsung Engineering / 삼성엔지니어링", "event_summary": "2022 results: KRW 10.5T revenue, KRW 702.9B operating profit, +69.6% YoY OP, backlog/new-order visibility; margin bridge visible.", "case_role": "positive_margin_bridge", "evidence_family": "realized_margin_backlog_bridge_after_mega_projects", "evidence_url": "https://www.samsungena.com/en/newsroom/news/view?idx=15493", "calibration_usable": true}
{"row_type": "case", "case_id": "C05_047040_2021_ALFAW_PORT_ORDER", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "047040", "company": "Daewoo E&C / 대우건설", "event_summary": "Iraq Al Faw port KRW 2.9T contract plus 2020 overseas-order target beat; contract visibility was strong and price path confirmed.", "case_role": "positive_stage2_actionable", "evidence_family": "large_overseas_infra_package_with_order_target_bridge", "evidence_url": "https://en.yna.co.kr/view/AEN20210104002000320", "calibration_usable": true}
{"row_type": "case", "case_id": "C05_000720_2023_AMIRAL_ORDER_NO_MARGIN", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "000720", "company": "Hyundai E&C / 현대건설", "event_summary": "Saudi Aramco Amiral US$5B petrochemical plant contract; order magnitude very high but price path failed and margin bridge was not immediate.", "case_role": "counterexample_order_only", "evidence_family": "mega_EPC_order_without_near_term_margin_confirmation", "evidence_url": "https://en.yna.co.kr/view/AEN20230625002000320", "calibration_usable": true}
{"row_type": "case", "case_id": "C05_006360_2023_GEOMDAN_QUALITY_4C", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "006360", "company": "GS E&C / GS건설", "event_summary": "GS E&C admitted missed rebar in over 30 places after Geomdan underground parking collapse; explicit quality/reputation/legal thesis break.", "case_role": "hard_4C_counterexample", "evidence_family": "quality_failure_rebar_admission_thesis_break", "evidence_url": "https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon", "calibration_usable": true}
{"row_type": "case", "case_id": "C05_294870_2022_GWANGJU_COLLAPSE_4C", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "294870", "company": "HDC Hyundai Development / HDC현대산업개발", "event_summary": "Gwangju apartment collapse triggered >10% intraday plunge and later license cancellation risk; a trust/legal thesis break for construction/EPC names.", "case_role": "hard_4C_counterexample", "evidence_family": "fatal_construction_collapse_brand_trust_break", "evidence_url": "https://view.asiae.co.kr/en/article/2022011210052236794", "calibration_usable": true}
{"row_type": "trigger", "case_id": "C05_028050_2020_HUGRS_ORDER_HIGH_MAE", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "028050", "company": "Samsung Engineering / 삼성엔지니어링", "trigger_date": "2020-01-28", "trigger_type": "Stage2-Actionable", "entry_date": "2020-01-28", "entry_price": 17800.0, "entry_open": 17900.0, "entry_high": 18000.0, "entry_low": 17600.0, "entry_close": 17800.0, "entry_volume": 1102718, "entry_amount": 19673890800, "entry_market_cap": 3488800000000, "MFE_30D_pct": 3.65, "MFE_90D_pct": 3.65, "MFE_180D_pct": 3.65, "MAE_30D_pct": -30.06, "MAE_90D_pct": -61.18, "MAE_180D_pct": -61.18, "peak_date": "2020-01-29", "peak_price": 18450.0, "drawdown_after_peak_pct": -62.55, "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "evidence_url": "https://www.euro-petrole.com/samsung-engineering-signs-dollars-1-85-billion-aramco-gas-project-in-saudi-arabia-n-i-20303", "outcome_tag": "counterexample_high_MAE", "current_profile_result": "false_positive_if_allowed_to_green"}
{"row_type": "trigger", "case_id": "C05_028050_2023_RESULTS_MARGIN_BRIDGE", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "028050", "company": "Samsung Engineering / 삼성엔지니어링", "trigger_date": "2023-01-31", "trigger_type": "Stage3-Green", "entry_date": "2023-02-01", "entry_price": 26450.0, "entry_open": 26100.0, "entry_high": 26900.0, "entry_low": 25600.0, "entry_close": 26450.0, "entry_volume": 2500313, "entry_amount": 66111310450, "entry_market_cap": 5184200000000, "MFE_30D_pct": 15.31, "MFE_90D_pct": 22.5, "MFE_180D_pct": 42.91, "MAE_30D_pct": -4.35, "MAE_90D_pct": -4.35, "MAE_180D_pct": -4.35, "peak_date": "2023-08-02", "peak_price": 37800.0, "drawdown_after_peak_pct": -29.5, "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "evidence_url": "https://www.samsungena.com/en/newsroom/news/view?idx=15493", "outcome_tag": "positive_margin_bridge", "current_profile_result": "true_positive"}
{"row_type": "trigger", "case_id": "C05_047040_2021_ALFAW_PORT_ORDER", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "047040", "company": "Daewoo E&C / 대우건설", "trigger_date": "2021-01-04", "trigger_type": "Stage2-Actionable", "entry_date": "2021-01-04", "entry_price": 5150.0, "entry_open": 5250.0, "entry_high": 5270.0, "entry_low": 5060.0, "entry_close": 5150.0, "entry_volume": 9249864, "entry_amount": 47703539935, "entry_market_cap": 2140456585700, "MFE_30D_pct": 30.1, "MFE_90D_pct": 55.34, "MFE_180D_pct": 85.24, "MAE_30D_pct": -1.75, "MAE_90D_pct": -1.75, "MAE_180D_pct": -1.75, "peak_date": "2021-06-02", "peak_price": 9540.0, "drawdown_after_peak_pct": -33.12, "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "evidence_url": "https://en.yna.co.kr/view/AEN20210104002000320", "outcome_tag": "positive_stage2_actionable", "current_profile_result": "true_positive_stage2"}
{"row_type": "trigger", "case_id": "C05_000720_2023_AMIRAL_ORDER_NO_MARGIN", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "000720", "company": "Hyundai E&C / 현대건설", "trigger_date": "2023-06-25", "trigger_type": "Stage2-Actionable", "entry_date": "2023-06-26", "entry_price": 40800.0, "entry_open": 42700.0, "entry_high": 44400.0, "entry_low": 40400.0, "entry_close": 40800.0, "entry_volume": 8540029, "entry_amount": 359525992200, "entry_market_cap": 4543315212000, "MFE_30D_pct": 8.82, "MFE_90D_pct": 8.82, "MFE_180D_pct": 8.82, "MAE_30D_pct": -15.32, "MAE_90D_pct": -18.5, "MAE_180D_pct": -23.53, "peak_date": "2023-06-26", "peak_price": 44400.0, "drawdown_after_peak_pct": -29.73, "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "evidence_url": "https://en.yna.co.kr/view/AEN20230625002000320", "outcome_tag": "counterexample_order_only", "current_profile_result": "false_positive_if_green"}
{"row_type": "trigger", "case_id": "C05_006360_2023_GEOMDAN_QUALITY_4C", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "006360", "company": "GS E&C / GS건설", "trigger_date": "2023-05-09", "trigger_type": "Stage4C", "entry_date": "2023-05-10", "entry_price": 20950.0, "entry_open": 21200.0, "entry_high": 21500.0, "entry_low": 20850.0, "entry_close": 20950.0, "entry_volume": 774236, "entry_amount": 16363912950, "entry_market_cap": 1792932215500, "MFE_30D_pct": 5.73, "MFE_90D_pct": 5.73, "MFE_180D_pct": 5.73, "MAE_30D_pct": -4.53, "MAE_90D_pct": -36.18, "MAE_180D_pct": -39.52, "peak_date": "2023-05-24", "peak_price": 22150.0, "drawdown_after_peak_pct": -42.8, "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "evidence_url": "https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon", "outcome_tag": "hard_4C_counterexample", "current_profile_result": "4C_needed_early"}
{"row_type": "trigger", "case_id": "C05_294870_2022_GWANGJU_COLLAPSE_4C", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "symbol": "294870", "company": "HDC Hyundai Development / HDC현대산업개발", "trigger_date": "2022-01-12", "trigger_type": "Stage4C", "entry_date": "2022-01-12", "entry_price": 20850.0, "entry_open": 21800.0, "entry_high": 22700.0, "entry_low": 20600.0, "entry_close": 20850.0, "entry_volume": 11344769, "entry_amount": 246206254250, "entry_market_cap": 1374167830500, "MFE_30D_pct": 8.87, "MFE_90D_pct": 8.87, "MFE_180D_pct": 8.87, "MAE_30D_pct": -35.25, "MAE_90D_pct": -36.93, "MAE_180D_pct": -50.84, "peak_date": "2022-01-12", "peak_price": 22700.0, "drawdown_after_peak_pct": -54.85, "calibration_usable": true, "corporate_action_contaminated_180D": false, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "evidence_url": "https://view.asiae.co.kr/en/article/2022011210052236794", "outcome_tag": "hard_4C_counterexample", "current_profile_result": "4C_needed_immediate"}
{"row_type": "score_simulation", "case_id": "C05_028050_2020_HUGRS_ORDER_HIGH_MAE", "symbol": "028050", "trigger_type": "Stage2-Actionable", "current_proxy_total": 78, "proposed_shadow_total": 71, "current_proxy_decision": "false_positive_if_allowed_to_green", "proposed_shadow_decision": "Stage2-Actionable", "rule_delta": "C05 order-only cap; realized margin bridge unlock; construction quality/legal break hard routes to 4C"}
{"row_type": "score_simulation", "case_id": "C05_028050_2023_RESULTS_MARGIN_BRIDGE", "symbol": "028050", "trigger_type": "Stage3-Green", "current_proxy_total": 91, "proposed_shadow_total": 94, "current_proxy_decision": "true_positive", "proposed_shadow_decision": "Stage3-Green", "rule_delta": "C05 order-only cap; realized margin bridge unlock; construction quality/legal break hard routes to 4C"}
{"row_type": "score_simulation", "case_id": "C05_047040_2021_ALFAW_PORT_ORDER", "symbol": "047040", "trigger_type": "Stage2-Actionable", "current_proxy_total": 82, "proposed_shadow_total": 83, "current_proxy_decision": "true_positive_stage2", "proposed_shadow_decision": "Stage2-Actionable", "rule_delta": "C05 order-only cap; realized margin bridge unlock; construction quality/legal break hard routes to 4C"}
{"row_type": "score_simulation", "case_id": "C05_000720_2023_AMIRAL_ORDER_NO_MARGIN", "symbol": "000720", "trigger_type": "Stage2-Actionable", "current_proxy_total": 81, "proposed_shadow_total": 72, "current_proxy_decision": "false_positive_if_green", "proposed_shadow_decision": "Stage2-Actionable", "rule_delta": "C05 order-only cap; realized margin bridge unlock; construction quality/legal break hard routes to 4C"}
{"row_type": "score_simulation", "case_id": "C05_006360_2023_GEOMDAN_QUALITY_4C", "symbol": "006360", "trigger_type": "Stage4C", "current_proxy_total": 54, "proposed_shadow_total": 28, "current_proxy_decision": "4C_needed_early", "proposed_shadow_decision": "Stage4C", "rule_delta": "C05 order-only cap; realized margin bridge unlock; construction quality/legal break hard routes to 4C"}
{"row_type": "score_simulation", "case_id": "C05_294870_2022_GWANGJU_COLLAPSE_4C", "symbol": "294870", "trigger_type": "Stage4C", "current_proxy_total": 48, "proposed_shadow_total": 22, "current_proxy_decision": "4C_needed_immediate", "proposed_shadow_decision": "Stage4C", "rule_delta": "C05 order-only cap; realized margin bridge unlock; construction quality/legal break hard routes to 4C"}
{"row_type": "residual_contribution", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "usable_trigger_rows": 6, "positive_rows": 2, "counterexample_rows": 4, "hard_4C_rows": 2, "sample_false_positive_or_high_MAE_count": 3, "sample_true_positive_count": 2, "expected_profile_effect": "reduce C05 mega-order false positives and accelerate 4C thesis-break routing", "shadow_weight_before": "18/22/10/12/10/8/20", "shadow_weight_after": "16/23/8/14/9/10/20"}
```

## 19. Residual Contribution Summary

This loop contributes a specific C05 residual: **contract magnitude needs margin/cash bridge, and safety/legal trust breaks must be hard 4C**. It is not a generic “mega orders work” reinforcement. It directly repairs:

- order-only false positives,
- high-MAE after headline contract news,
- delayed recognition of construction-quality thesis breaks,
- local bounce misread as full 4B repair after non-price damage.

## 20. Price Source Validation Notes

All entry dates exist in `tradable_raw` shards. All 30D/90D/180D MFE/MAE fields are populated. No selected 180D window overlaps the listed corporate-action candidate dates in the symbol profiles.

## 21. Batch Ingest Self-Audit

| gate | result |
|---|---|
| filename_regex | pass |
| round/loop metadata consistency | pass |
| canonical stage labels only | pass |
| MFE/MAE 30/90/180 present in every trigger row | pass |
| stock_agent code access | not used |
| live scan / current discovery | not used |
| production scoring changed | false |
| duplicate key materialization | no hard duplicate selected |
| corporate_action_180D_contamination | false for all selected rows |
| direct evidence URL present | true for all selected cases |

## 22. Rejected Candidate Notes

Rejected from this run:

- DL이앤씨 375500 2022 rows: profile has 2022 corporate-action candidate dates, creating avoidable contamination risk in the intended forward window.
- Additional 2024 Saudi gas expansion rows: too recent for full 180D only if chosen near manifest edge? Not needed for the current residual because stronger clean historical rows already exist.
- Generic construction order rows without direct evidence URLs: would add quantity but not repair Priority 0/1 quality.

## 23. Sensitivity / Robustness Checks

- If 028050 2023 entry is shifted from same-day evidence to next tradable day, the result remains positive: the next-day row still shows `MFE_180D_pct=42.91` and `MAE_180D_pct=-4.35`.
- If 006360 Geomdan is treated as May 10 next-tradable entry after May 9 after-market coverage, it still produces a hard negative path: `MAE_180D_pct=-39.52`.
- If order-only cases are not blocked from Green, Hyundai E&C Amiral and Samsung Engineering HUGRS become the archetypal false-positive rows.

## 24. Failure Mode Map

| failure mode | case support | proposed guard |
|---|---|---|
| order magnitude overweights score | 028050_2020, 000720_2023 | order-only cap |
| Green without realized margin bridge | 000720_2023 | require margin/cash bridge |
| post-break local bounce misread | 006360_2023 | 4C overrides local 4B |
| trust/legal break recognized late | 294870_2022, 006360_2023 | hard 4C routing |
| positive order/backlog ignored | 047040_2021, 028050_2023 | allow Stage2/Green when bridge exists |

## 25. Next Research State

```text
completed_round = R1
completed_loop = 128
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance strengthening + Priority 0 direct-source/proxy repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C15_MATERIAL_SPREAD_SUPERCYCLE, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

## 26. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not re-run this research as live stock discovery.
Read this MD as one batch candidate for E2R v12 calibration ingestion.

Scope:
- large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
- canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
- file = e2r_stock_web_v12_residual_round_R1_loop_128_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md

Implement only after batch review:
1. Add a C05-specific shadow rule candidate that caps mega EPC contract headlines at Stage2-Actionable unless realized margin bridge and cash/working-capital bridge are present.
2. Add a C05 hard 4C route for builder quality/legal/trust breaks such as collapse, rebar omission admission, mandatory rebuild risk, license cancellation, or business suspension risk.
3. Preserve Stage3-Green for rows where mega project revenue has already converted into operating-profit/backlog bridge.
4. Do not alter production scoring from this single MD alone; combine with other v12 residual MDs and promotion decisions.
5. Maintain all machine-readable trigger rows exactly; do not drop MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
```

## 27. Final Research Conclusion

C05’s residual is no longer “does the market like mega contracts?” The better question is whether the contract has crossed the bridge from **headline backlog** to **realized margin/cash quality**. When the bridge is visible, Samsung Engineering 2023 and Daewoo E&C 2021 show clean positive paths. When it is missing, Samsung Engineering 2020 and Hyundai E&C 2023 show order-only false-positive risk. When the builder trust/legal thesis breaks, GS E&C 2023 and HDC 2022 should route directly to Stage4C.

## 28. Source Notes

### Prompt / index / atlas

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json

### Price shards

- `028050_2020`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/028/028050/2020.csv
- `028050_2021`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/028/028050/2021.csv
- `028050_2023`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/028/028050/2023.csv
- `028050_2024`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv
- `047040_2021`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/047/047040/2021.csv
- `047040_2022`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv
- `000720_2023`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv
- `000720_2024`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv
- `006360_2023`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv
- `006360_2024`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv
- `294870_2022`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv
- `294870_2023`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/294/294870/2023.csv

### Symbol profiles

- `028050`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/028/028050.json
- `047040`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/047/047040.json
- `000720`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/000/000720.json
- `006360`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/006/006360.json
- `294870`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/294/294870.json

### Event evidence

- `C05_028050_2020_HUGRS_ORDER_HIGH_MAE` evidence: https://www.euro-petrole.com/samsung-engineering-signs-dollars-1-85-billion-aramco-gas-project-in-saudi-arabia-n-i-20303
- `C05_028050_2023_RESULTS_MARGIN_BRIDGE` evidence: https://www.samsungena.com/en/newsroom/news/view?idx=15493
- `C05_047040_2021_ALFAW_PORT_ORDER` evidence: https://en.yna.co.kr/view/AEN20210104002000320
- `C05_000720_2023_AMIRAL_ORDER_NO_MARGIN` evidence: https://en.yna.co.kr/view/AEN20230625002000320
- `C05_006360_2023_GEOMDAN_QUALITY_4C` evidence: https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon
- `C05_294870_2022_GWANGJU_COLLAPSE_4C` evidence: https://view.asiae.co.kr/en/article/2022011210052236794
