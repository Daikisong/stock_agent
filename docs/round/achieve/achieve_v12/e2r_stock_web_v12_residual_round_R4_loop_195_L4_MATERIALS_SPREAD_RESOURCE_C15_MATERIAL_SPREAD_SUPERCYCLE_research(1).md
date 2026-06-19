# E2R v12 Stock-Web Residual Research — R4 / C15 Paper-Pulp-Corrugated Spread Gate

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```text
selected_round: R4
selected_loop: 195
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1

loop_objective:
- 기존 C15 철강/정유/시멘트 반복을 피하고, 제지·펄프·골판지 spread 하위축을 보강한다.
- pulp price, wastepaper, corrugated raw-paper price hike, price pass-through headline이 실제 issuer-level margin/cash bridge로 전환되는지 분리한다.
- sector-level price-hike row와 direct issuer margin row를 같은 Stage2-Actionable로 과승격하지 않도록 gate를 만든다.
```

## 2. Required prompt / No-Repeat / price-atlas validation

- MAIN prompt 기준: `stock_agent` 코드 패치와 live scan은 금지이며, Songdaiki/stock-web 실제 1D OHLCV row를 사용해 trigger-level 30/90/180D MFE·MAE를 계산해야 한다.
- NO-REPEAT INDEX 기준: 현재 모든 C01~C32는 80 rows 이상이고, 다음 단계는 URL/proxy 품질과 Priority 1 균형 보강이다. C15는 spread reversal / inventory cycle 반례 보강 대상으로 남아 있다.
- Stock-Web manifest 기준: `price_adjustment_status=raw_unadjusted_marcap`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`, `max_date=2026-02-20`.
- Stock-Web schema 기준: MFE_N은 entry_date부터 N개 tradable row 중 max high, MAE_N은 min low로 계산한다.

```text
price_source: Songdaiki/stock-web
price_basis: tradable_raw
upstream_source: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
block_corporate_action_window: true
```

## 3. Novelty / duplicate check

Hard duplicate key is `canonical_archetype_id + symbol + trigger_type + entry_date`.

```text
new_independent_case_count: 9
new_independent_trigger_count: 9
unique_symbol_count: 8
same_archetype_new_trigger_family_count: 4

stage2_count: 2
stage2_actionable_count: 2
stage4b_count: 4
stage4c_count: 1

positive_or_direct_bridge_count: 2
counterexample_or_guardrail_count: 7
source_proxy_only_count: 4
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

The new trigger family is distinct from prior C15 steel/rebar/pipe/refining/cement cases: this file focuses on `pulp / printing paper / corrugated raw paper / box price pass-through`.

## 4. Evidence map

- `213500 / 2024-05-20`: Hansol Paper Q1 2024 surprise tied to product-price realization and lower pulp cost; Green still blocked because the article itself warned that 1Q strength might not persist.
- `213500 / 2025-04-30`: Hansol Paper Q1 2025 profit decline tests whether pulp-cost rebound / demand weakness should be local 4B rather than sticky 4C.
- `009580 / 2024-07-05`: Moorim P&P tests integrated pulp-paper spread recovery where pulp price rebound and wood-chip stabilization improved losses.
- `002310, 002200, 011280, 014160 / 2024-08-06`: corrugated raw-paper price hike cluster; useful as price-pass-through proxy, but not enough for issuer-level Stage2-Actionable without margin/cash conversion.
- `016590 / 2024-10-25`: Shindaeyang Paper tests hard-4C stickiness after raw-material cost pressure and OP/EBITDA margin deterioration.
- `023600 / 2024-11-26`: Sambo Corrugated tests whether vertical integration and industry report evidence should stay Stage2-capped until realized spread/profit bridge appears.

Evidence URLs used:

```text
main_prompt = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
stock_web_manifest = https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
stock_web_schema = https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json

hansol_2024_profit = https://core.asiae.co.kr/article/2024051616505531833
hansol_financials = https://www.hansolpaper.co.kr/m/eng/ir/finance
hansol_2025_profit_drop = https://biz.chosun.com/en/en-industry/2025/04/30/CYJMWAR4VNEORFMCE7X4NI2NCA/
moorim_pnp_credit_report = https://m.kisrating.com/fileDown.do?fileName=rs20241223-27.pdf&gubun=2&menuCd=R8
moorim_pnp_pulp_recovery = https://v.daum.net/v/ZnBigPWAi1
corrugated_price_hike_2024 = https://biz.chosun.com/industry/business-venture/2024/08/05/52CQ524GURHXNKZMAQMKFWZOBA/
korea_export_packaging_price_hike = https://www.asiae.co.kr/en/article/2024080614044454190
shindaeyang_cost_pressure = https://dealsite.co.kr/articles/130056/068030
sambo_report = https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320000246&docno=&method=search&viewerhost=
```

## 5. Trigger-level price path table

| symbol | name | trigger_type | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough | role |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 213500 | 한솔제지 / Hansol Paper | Stage2-Actionable | 2024-05-20 | 11350 | 2.11/-4.32 | 2.11/-17.18 | 2.11/-26.26 | 2024-05-23 | 2025-02-03 | positive_bridge |
| 213500 | 한솔제지 / Hansol Paper | Stage4B | 2025-04-30 | 8370 | 7.17/-1.67 | 10.87/-1.67 | 12.19/-6.21 | 2025-09-25 | 2025-11-05 | counterexample_watch |
| 009580 | 무림P&P / Moorim P&P | Stage2-Actionable | 2024-07-05 | 3075 | 4.88/-7.64 | 4.88/-19.84 | 11.38/-23.90 | 2025-01-02 | 2024-12-10 | positive_bridge |
| 002310 | 아세아제지 / Asia Paper | Stage4B | 2024-08-06 | 7930 | 6.18/-7.31 | 7.69/-10.47 | 10.84/-18.66 | 2025-04-21 | 2025-04-07 | proxy_guardrail |
| 002200 | 한국수출포장 / Korea Export Packaging | Stage2 | 2024-08-06 | 2055 | 26.52/-0.97 | 39.66/-0.97 | 40.63/-0.97 | 2025-02-04 | 2024-08-06 | sector_price_pass_through_option |
| 011280 | 태림포장 / Taelim Packaging | Stage4B | 2024-08-06 | 2240 | 10.71/-6.25 | 11.16/-18.75 | 24.11/-18.75 | 2025-02-28 | 2024-12-09 | proxy_guardrail |
| 014160 | 대영포장 / Daeyoung Packaging | Stage4B | 2024-08-06 | 1038 | 15.61/-6.55 | 16.76/-10.69 | 143.26/-10.69 | 2025-04-09 | 2024-11-15 | proxy_guardrail |
| 016590 | 신대양제지 / Shindaeyang Paper | Stage4C | 2024-10-25 | 5850 | 3.25/-8.89 | 6.50/-8.89 | 170.09/-8.89 | 2025-07-09 | 2024-12-04 | overhard_4c_stress |
| 023600 | 삼보판지 / Sambo Corrugated Board | Stage2 | 2024-11-26 | 8670 | 1.38/-9.34 | 1.38/-17.07 | 30.33/-17.07 | 2025-07-23 | 2025-04-09 | stage2_cap |

## 6. Case interpretation

### 6.1 Direct positive controls

`213500 / 2024-05-20` and `009580 / 2024-07-05` are the useful positive controls. Both have more than a generic material headline: Hansol had Q1 operating-profit conversion from price and pulp-cost spread, while Moorim P&P had integrated pulp economics and narrowing losses. Even so, the realized stock paths were not strong enough to loosen Stage3-Green. Hansol's 180D MFE was only 2.11% with -26.26% MAE, while Moorim P&P's 180D MFE/MAE was 11.38% / -23.90%.

### 6.2 Sector price-hike cluster

The 2024-08-06 corrugated cluster is the core residual. `002310`, `002200`, `011280`, and `014160` all received a plausible price-pass-through headline. But the evidence was mostly sector-level: raw-paper producers announced increases, not each issuer proving operating-profit or cash conversion on the same date. The later paths split sharply. Korea Export Packaging and Daeyoung Packaging had large 180D MFE, while Asia Paper and Taelim were much more muted. This argues against treating the whole basket as Stage2-Actionable.

### 6.3 4C stickiness stress

`016590 / 2024-10-25` is intentionally marked as a hard-4C stress row because the non-price evidence was issuer-level margin deterioration from raw-material cost pressure. But the 180D path produced 170.09% MFE and only -8.89% MAE. This is not a reason to erase the early warning; it is a reason to avoid sticky hard 4C when the evidence is profit-pressure without confirmed order/cashflow collapse.

### 6.4 Stage2 cap

`023600 / 2024-11-26` had vertical integration and industry evidence, but no immediate realized margin bridge. It therefore remains Stage2-capped. Its 180D MFE/MAE of 30.33% / -17.07% is acceptable but not enough to lift Stage3-Yellow/Green without conversion evidence.

## 7. Score simulation / current calibrated profile stress

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Result:

```text
current_profile_false_positive_risk:
- Treating all corrugated price-hike rows as Stage2-Actionable would be false-positive prone.
- Sector price-hike language needs company-level margin/cash bridge before Actionable credit.

current_profile_too_hard_4c_risk:
- Shindaeyang's hard-4C stress row later rallied strongly, so margin-pressure evidence alone should not create sticky 4C.

current_profile_too_late_risk:
- Direct issuer spread conversion remains valid Stage2 input, but Green should remain blocked unless cashflow/working-capital conversion repeats.
```

## 8. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "213500", "name_kr": "한솔제지", "name_en": "Hansol Paper", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-05-20", "entry_date": "2024-05-20", "entry_price": 11350.0, "entry_open": 11160.0, "entry_high": 11360.0, "entry_low": 11070.0, "entry_volume": 234088, "mfe30_pct": 2.11, "mae30_pct": -4.32, "peak30_date": "2024-05-23", "trough30_date": "2024-06-10", "mfe90_pct": 2.11, "mae90_pct": -17.18, "peak90_date": "2024-05-23", "trough90_date": "2024-09-11", "mfe180_pct": 2.11, "mae180_pct": -26.26, "peak180_date": "2024-05-23", "trough180_date": "2025-02-03", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/213/213500/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/213/213500/2025.csv"], "profile_path": "atlas/symbol_profiles/213/213500.json", "corporate_action_candidate_dates": ["2016-08-18"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Q1 2024 profit surprise was tied to prior price hikes and pulp-cost decline; sustainability still uncertain.", "case_role": "positive_bridge", "score_components": {"eps_fcf_explosion": 20, "earnings_visibility": 20, "bottleneck_pricing": 21, "market_mispricing": 11, "valuation_rerating": 10, "capital_allocation": 6, "information_confidence": 12}, "score_total": 100, "current_profile_alignment": "actionable_correct_but_green_blocked", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|213500|Stage2-Actionable|2024-05-20", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "213500", "name_kr": "한솔제지", "name_en": "Hansol Paper", "trigger_type": "Stage4B", "evidence_date": "2025-04-30", "entry_date": "2025-04-30", "entry_price": 8370.0, "entry_open": 8390.0, "entry_high": 8420.0, "entry_low": 8320.0, "entry_volume": 44712, "mfe30_pct": 7.17, "mae30_pct": -1.67, "peak30_date": "2025-06-12", "trough30_date": "2025-05-19", "mfe90_pct": 10.87, "mae90_pct": -1.67, "peak90_date": "2025-07-15", "trough90_date": "2025-05-19", "mfe180_pct": 12.19, "mae180_pct": -6.21, "peak180_date": "2025-09-25", "trough180_date": "2025-11-05", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/213/213500/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/213/213500/2025.csv", "atlas/ohlcv_tradable_by_symbol_year/213/213500/2026.csv"], "profile_path": "atlas/symbol_profiles/213/213500.json", "corporate_action_candidate_dates": ["2016-08-18"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Q1 2025 operating profit dropped sharply; forward path was not hard-break, so 4B/watch is safer than sticky 4C.", "case_role": "counterexample_watch", "score_components": {"eps_fcf_explosion": 8, "earnings_visibility": 9, "bottleneck_pricing": 13, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 17}, "score_total": 67, "current_profile_alignment": "avoid_hard_4c; watch_only", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|213500|Stage4B|2025-04-30", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "009580", "name_kr": "무림P&P", "name_en": "Moorim P&P", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-07-05", "entry_date": "2024-07-05", "entry_price": 3075.0, "entry_open": 3070.0, "entry_high": 3095.0, "entry_low": 3050.0, "entry_volume": 55086, "mfe30_pct": 4.88, "mae30_pct": -7.64, "peak30_date": "2024-08-16", "trough30_date": "2024-08-05", "mfe90_pct": 4.88, "mae90_pct": -19.84, "peak90_date": "2024-08-16", "trough90_date": "2024-11-15", "mfe180_pct": 11.38, "mae180_pct": -23.9, "peak180_date": "2025-01-02", "trough180_date": "2024-12-10", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/009/009580/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/009/009580/2025.csv"], "profile_path": "atlas/symbol_profiles/009/009580.json", "corporate_action_candidate_dates": ["1999-12-08", "2007-12-10", "2008-05-30", "2011-05-04"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Pulp price rebound and integrated pulp-paper spread improved loss chain into operating profit recovery.", "case_role": "positive_bridge", "score_components": {"eps_fcf_explosion": 20, "earnings_visibility": 20, "bottleneck_pricing": 21, "market_mispricing": 11, "valuation_rerating": 10, "capital_allocation": 6, "information_confidence": 12}, "score_total": 100, "current_profile_alignment": "actionable_correct_but_green_blocked", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|009580|Stage2-Actionable|2024-07-05", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "002310", "name_kr": "아세아제지", "name_en": "Asia Paper", "trigger_type": "Stage4B", "evidence_date": "2024-08-06", "entry_date": "2024-08-06", "entry_price": 7930.0, "entry_open": 7960.0, "entry_high": 8140.0, "entry_low": 7830.0, "entry_volume": 217700, "mfe30_pct": 6.18, "mae30_pct": -7.31, "peak30_date": "2024-09-05", "trough30_date": "2024-09-09", "mfe90_pct": 7.69, "mae90_pct": -10.47, "peak90_date": "2024-10-18", "trough90_date": "2024-12-05", "mfe180_pct": 10.84, "mae180_pct": -18.66, "peak180_date": "2025-04-21", "trough180_date": "2025-04-07", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/002/002310/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/002/002310/2025.csv"], "profile_path": "atlas/symbol_profiles/002/002310.json", "corporate_action_candidate_dates": ["1996-01-03", "1997-01-03", "2013-01-23", "2024-04-19"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Corrugated raw-paper price hike was sector-level; no immediate issuer-level margin conversion at trigger.", "case_role": "proxy_guardrail", "score_components": {"eps_fcf_explosion": 8, "earnings_visibility": 9, "bottleneck_pricing": 13, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 17}, "score_total": 67, "current_profile_alignment": "avoid_hard_4c; watch_only", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|002310|Stage4B|2024-08-06", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "002200", "name_kr": "한국수출포장", "name_en": "Korea Export Packaging", "trigger_type": "Stage2", "evidence_date": "2024-08-06", "entry_date": "2024-08-06", "entry_price": 2055.0, "entry_open": 2035.0, "entry_high": 2245.0, "entry_low": 2035.0, "entry_volume": 515674, "mfe30_pct": 26.52, "mae30_pct": -0.97, "peak30_date": "2024-09-03", "trough30_date": "2024-08-06", "mfe90_pct": 39.66, "mae90_pct": -0.97, "peak90_date": "2024-12-17", "trough90_date": "2024-08-06", "mfe180_pct": 40.63, "mae180_pct": -0.97, "peak180_date": "2025-02-04", "trough180_date": "2024-08-06", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/002/002200/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/002/002200/2025.csv"], "profile_path": "atlas/symbol_profiles/002/002200.json", "corporate_action_candidate_dates": ["1997-01-03", "1997-06-13", "2023-04-17"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Korea Export Packaging reacted to sector price hike, but evidence was still price-pass-through option rather than realized margin bridge.", "case_role": "sector_price_pass_through_option", "score_components": {"eps_fcf_explosion": 14, "earnings_visibility": 14, "bottleneck_pricing": 18, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 5, "information_confidence": 10}, "score_total": 83, "current_profile_alignment": "stage2_cap_correct", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|002200|Stage2|2024-08-06", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "011280", "name_kr": "태림포장", "name_en": "Taelim Packaging", "trigger_type": "Stage4B", "evidence_date": "2024-08-06", "entry_date": "2024-08-06", "entry_price": 2240.0, "entry_open": 2110.0, "entry_high": 2260.0, "entry_low": 2100.0, "entry_volume": 139888, "mfe30_pct": 10.71, "mae30_pct": -6.25, "peak30_date": "2024-08-26", "trough30_date": "2024-08-06", "mfe90_pct": 11.16, "mae90_pct": -18.75, "peak90_date": "2024-12-03", "trough90_date": "2024-12-09", "mfe180_pct": 24.11, "mae180_pct": -18.75, "peak180_date": "2025-02-28", "trough180_date": "2024-12-09", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/011/011280/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/011/011280/2025.csv"], "profile_path": "atlas/symbol_profiles/011/011280.json", "corporate_action_candidate_dates": ["1997-01-03", "1997-03-14", "1999-03-10", "1999-10-12", "2008-05-06"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Taelim Packaging had sector price-hike exposure, but issuer-specific conversion was not visible at trigger.", "case_role": "proxy_guardrail", "score_components": {"eps_fcf_explosion": 8, "earnings_visibility": 9, "bottleneck_pricing": 13, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 17}, "score_total": 67, "current_profile_alignment": "avoid_hard_4c; watch_only", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|011280|Stage4B|2024-08-06", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "014160", "name_kr": "대영포장", "name_en": "Daeyoung Packaging", "trigger_type": "Stage4B", "evidence_date": "2024-08-06", "entry_date": "2024-08-06", "entry_price": 1038.0, "entry_open": 970.0, "entry_high": 1042.0, "entry_low": 970.0, "entry_volume": 394225, "mfe30_pct": 15.61, "mae30_pct": -6.55, "peak30_date": "2024-08-20", "trough30_date": "2024-08-06", "mfe90_pct": 16.76, "mae90_pct": -10.69, "peak90_date": "2024-10-10", "trough90_date": "2024-11-15", "mfe180_pct": 143.26, "mae180_pct": -10.69, "peak180_date": "2025-04-09", "trough180_date": "2024-11-15", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/014/014160/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/014/014160/2025.csv"], "profile_path": "atlas/symbol_profiles/014/014160.json", "corporate_action_candidate_dates": ["1996-10-22", "1997-01-03", "1998-05-12", "1999-06-04", "2001-05-28", "2002-03-15", "2002-12-16", "2007-05-11"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Daeyoung Packaging was a corrugated-box beta row; later MFE was large but trigger lacked direct margin/cash bridge.", "case_role": "proxy_guardrail", "score_components": {"eps_fcf_explosion": 8, "earnings_visibility": 9, "bottleneck_pricing": 13, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 17}, "score_total": 67, "current_profile_alignment": "avoid_hard_4c; watch_only", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|014160|Stage4B|2024-08-06", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "016590", "name_kr": "신대양제지", "name_en": "Shindaeyang Paper", "trigger_type": "Stage4C", "evidence_date": "2024-10-25", "entry_date": "2024-10-25", "entry_price": 5850.0, "entry_open": 5940.0, "entry_high": 5950.0, "entry_low": 5790.0, "entry_volume": 19669, "mfe30_pct": 3.25, "mae30_pct": -8.89, "peak30_date": "2024-11-12", "trough30_date": "2024-12-04", "mfe90_pct": 6.5, "mae90_pct": -8.89, "peak90_date": "2025-03-11", "trough90_date": "2024-12-04", "mfe180_pct": 170.09, "mae180_pct": -8.89, "peak180_date": "2025-07-09", "trough180_date": "2024-12-04", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/016/016590/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/016/016590/2025.csv"], "profile_path": "atlas/symbol_profiles/016/016590.json", "corporate_action_candidate_dates": ["1997-04-16", "1999-12-07", "2023-04-24"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Shindaeyang Paper showed H1 operating profit and EBITDA margin deterioration from raw-material cost pressure; later MFE tests hard-4C stickiness.", "case_role": "overhard_4c_stress", "score_components": {"eps_fcf_explosion": 5, "earnings_visibility": 8, "bottleneck_pricing": 10, "market_mispricing": 7, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 32}, "score_total": 73, "current_profile_alignment": "hard_4c_stress; later_mfe_warns_against_sticky_4c", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|016590|Stage4C|2024-10-25", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "round": "R4", "selected_loop": 195, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1", "symbol": "023600", "name_kr": "삼보판지", "name_en": "Sambo Corrugated Board", "trigger_type": "Stage2", "evidence_date": "2024-11-26", "entry_date": "2024-11-26", "entry_price": 8670.0, "entry_open": 8670.0, "entry_high": 8790.0, "entry_low": 8600.0, "entry_volume": 5744, "mfe30_pct": 1.38, "mae30_pct": -9.34, "peak30_date": "2024-11-26", "trough30_date": "2024-12-09", "mfe90_pct": 1.38, "mae90_pct": -17.07, "peak90_date": "2024-11-26", "trough90_date": "2025-04-09", "mfe180_pct": 30.33, "mae180_pct": -17.07, "peak180_date": "2025-07-23", "trough180_date": "2025-04-09", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "tradable_shards_used": ["atlas/ohlcv_tradable_by_symbol_year/023/023600/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/023/023600/2025.csv"], "profile_path": "atlas/symbol_profiles/023/023600.json", "corporate_action_candidate_dates": ["1996-09-06", "1996-10-31", "1997-12-19", "2013-05-20"], "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "evidence_summary": "Sambo had vertical-integration/industry evidence, but no realized margin conversion at trigger; Stage2 cap only.", "case_role": "stage2_cap", "score_components": {"eps_fcf_explosion": 14, "earnings_visibility": 14, "bottleneck_pricing": 18, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 5, "information_confidence": 10}, "score_total": 83, "current_profile_alignment": "stage2_cap_correct", "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|023600|Stage2|2024-11-26", "production_scoring_changed": false, "shadow_weight_only": true}
```

## 9. Aggregate row

```json
{
  "row_type": "aggregate",
  "round": "R4",
  "selected_loop": 195,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1",
  "new_independent_trigger_count": 9,
  "unique_symbol_count": 8,
  "stage2_count": 2,
  "stage2_actionable_count": 2,
  "stage4b_count": 4,
  "stage4c_count": 1,
  "positive_or_direct_bridge_count": 2,
  "counterexample_or_guardrail_count": 7,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "corporate_action_contaminated_180D_count": 0,
  "insufficient_forward_window_180D_count": 0,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 10. Shadow rule candidate

```text
rule_candidate:
C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1

core residual:
- pulp / wastepaper / corrugated raw-paper / price-hike headline alone cannot create Stage2-Actionable, Stage3-Yellow, or Stage3-Green.
- Stage2-Actionable requires at least one issuer-level second bridge:
  operating-profit conversion, realized spread expansion, price pass-through with shipment stability,
  cost stabilization, cashflow / working-capital improvement, or balance-sheet resilience.
- Sector-wide price hikes and basket reactions remain Stage2 cap or local Stage4B/watch until issuer-level bridge appears.
- Profit-pressure or cost-inflation evidence can trigger 4B/watch; sticky hard 4C requires confirmed margin thesis break plus weak offset quality, not just one half-year of OP decline.
- High MFE after a weak margin row warns against hard-4C stickiness; high MAE after a valid bridge row blocks Green first.
```

## 11. Shadow weight / residual contribution

```json
{
  "row_type": "shadow_weight",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "rule_candidate": "C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1",
  "do_not_propose_global_weight_delta": true,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "suggested_runtime_effect": {
    "stage2_required_bridge": "+ issuer-level margin/cash conversion required for Actionable",
    "local_4b_watch_guard": "+ sector price-hike basket stays watch-only",
    "hard_4c_confirmation": "+ sticky 4C requires confirmed issuer-level thesis break",
    "stage3_green_not_loosened": true
  },
  "residual_contribution_label": "C15_pulp_paper_corrugated_spread_proxy_vs_direct_bridge_repair"
}
```

## 12. Batch Ingest Self-Audit

```text
filename_matches_required_regex: true
filename_round_matches_metadata_round: true
filename_loop_matches_metadata_loop: true
round_sector_pair_valid: true
canonical_archetype_id_valid: true
large_sector_id_valid: true
all_usable_triggers_have_entry_date: true
all_usable_triggers_have_entry_price: true
all_usable_triggers_have_mfe_mae_30_90_180: true
all_usable_triggers_have_stock_web_price_source: true
all_usable_triggers_have_corporate_action_check: true
all_usable_triggers_have_score_components: true
same_entry_duplicate_removed: true
production_scoring_changed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not run this handoff during the research session.

When batch applying v12 residual research outputs, parse this file as a standard v12 result MD.
Use the JSONL rows above to update validation, dedupe, aggregate metrics, and promotion-planner candidates.
Do not apply a global Stage3-Green loosening. Consider only a scoped C15 rule candidate:
C15_PULP_PAPER_CORRUGATED_PRICE_PASS_THROUGH_SPREAD_GATE_V1.
The intended effect is a narrow gate separating issuer-level spread conversion from sector price-hike proxy rows.
```

## 14. Next Research State

```text
completed_round: R4
completed_loop: 195
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
