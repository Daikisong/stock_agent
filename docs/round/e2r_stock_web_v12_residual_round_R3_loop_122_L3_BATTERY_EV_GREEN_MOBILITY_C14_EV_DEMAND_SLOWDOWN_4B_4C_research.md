# e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
## 0. Execution metadata
```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R3
selected_loop = 122
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = BATTERY_MATERIAL_COMPONENT_UTILIZATION_AND_PRICE_SLOWDOWN_SEVERITY_SPLIT
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows / C14 rows 11 need_to_30 19 in static index
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```
## 1. Required first-read / scheduler result
MAIN EXECUTION PROMPT was treated as the full procedure. NO-REPEAT INDEX was used only as a duplicate/coverage ledger. Static index still ranks C14 as Priority 0 with 11 representative rows and need_to_30=19. Because the previous local follow-ups already used WCP/SKIET/EcoPro BM/POSCO Future M/SKC/Lotte-like battery-material cases, this loop expands the same canonical into electrolyte additives, silicon anode, nickel-plated steel, aluminum cathode foil, and cell parts.
## 2. Stock-web manifest and validation scope
```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
entry_price_basis = close_c_column
forward_windows = 30 / 90 / 180 trading rows including entry row
corporate_action_policy = block representative use when share-count discontinuity overlaps entry~D+180
```
Local stock-web shard copies used for computation:
- `002710`: `atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv` plus 2025 shard when 180D forward window crosses year-end- `006110`: `atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv` plus 2025 shard when 180D forward window crosses year-end- `078600`: `atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv` plus 2025 shard when 180D forward window crosses year-end- `243840`: `atlas/ohlcv_tradable_by_symbol_year/243/243840/2024.csv` plus 2025 shard when 180D forward window crosses year-end- `278280`: `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv` plus 2025 shard when 180D forward window crosses year-end- `348370`: `atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv` plus 2025 shard when 180D forward window crosses year-end
## 3. Source evidence map
| source key | role | URL |
|---|---|---|
| MAIN_EXECUTION_PROMPT | evidence / procedure | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt |
| NO_REPEAT_INDEX | evidence / procedure | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md |
| stock_web_manifest | evidence / procedure | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json |
| SNE_2024_LIB_components_degrowth | evidence / procedure | https://www.sneresearch.com/en/insight/release_view/249/page/0?s_cat=&s_keyword= |
| Reuters_LGES_slow_EV_demand_CAPEX_cut | evidence / procedure | https://www.reuters.com/business/energy/lg-energy-solution-q3-profit-drops-weak-ev-demand-2024-10-28/ |
| Reuters_lithium_boom_bust | evidence / procedure | https://www.reuters.com/markets/commodities/after-another-boom-bust-where-next-lithium-andy-home-2024-07-11/ |
| TCC_NPS_product | evidence / procedure | https://www.tccsteel.com/en/products/battery-mobility-solutions/nps |
| SamA_supplier_profile | evidence / procedure | https://www.komachine.com/en/companies/sam-a-aluminium |
| ShinHeung_profile | evidence / procedure | https://www.marketscreener.com/quote/stock/SHIN-HEUNG-ENERGY-ELECTRO-38495601/company/ |
| Chunbo_Mirae_2024_09_03 | evidence / procedure | https://securities.miraeasset.com/bbs/download/2130998.pdf?attachmentId=2130998 |
| Daejoo_Mirae_2024_08_14 | evidence / procedure | https://securities.miraeasset.com/bbs/download/2130561.pdf?attachmentId=2130561 |
| Enchem_company | evidence / procedure | https://www.enchem.net/eng/main.php |
| Lotte_Energy_2024_results | evidence / procedure | https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128 |

### Evidence interpretation
SNE Research's March 2024 component-market release gives the top-down context: LIB 4 components declined despite EV volume growth, battery selling price fell, and material companies saw profit pressure. Reuters later framed the same regime as slow EV demand, capex cuts, and a lithium boom-bust. That macro evidence is not enough to score individual companies by itself, so each row below still requires company-level product route or financial bridge.

## 4. Representative trigger rows / price path
|symbol|company|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_180D_date|trough_180D_date|classification|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|002710|TCC Steel|Stage4B|2024-03-15|62700.0|6.4|-19.8|6.4|-42.2|6.4|-56.9|2024-03-21|2024-08-05|positive_for_guardrail|
|006110|Sam-A Aluminium|Stage4B|2024-03-15|91100.0|7.6|-19.5|7.6|-40.4|7.6|-61.5|2024-03-26|2024-11-15|positive_for_guardrail|
|243840|Shin Heung Energy & Electronics|Stage4C|2024-07-12|8430.0|14.8|-24.3|14.8|-37.1|14.8|-55.0|2024-08-13|2025-04-09|positive_for_hard_4c_protection|
|278280|Chunbo|Stage4B|2024-09-03|61300.0|7.2|-15.0|7.2|-42.3|7.2|-51.0|2024-10-08|2025-04-09|mixed_guardrail_not_hard_4c|
|078600|Daejoo Electronic Materials|Stage4B|2024-08-14|126200.0|2.5|-29.2|2.5|-41.7|2.5|-43.7|2024-08-16|2025-01-02|counterexample_to_blunt_hard_4c_but_positive_for_4b_cap|

## 5. Case notes
### 5.1 TCC Steel / 002710 — product route real, but product-identity proxy failed
TCC's NPS route is real: the company describes nickel-plated steel as part of the EV/secondary-battery value chain and lists primary/secondary batteries, EVs, e-mobility, power tools and ESS as applications. But C14 should not upgrade NPS identity alone when the LIB components market is in price/margin contraction. The stock-web window from 2024-03-15 shows only +6.4% MFE against -56.9% 180D MAE, so this is a clean Stage4B proxy-guard case.

### 5.2 Sam-A Aluminium / 006110 — major battery customer route still needed demand survival
Sam-A's battery-material route is also real: supplier profile data describes LIB cathode foil for automotive batteries, top domestic battery customers, SK On exposure, and ACC supply. Yet this route did not protect the price path when the material component cycle was contracting. The 2024-03-15 row produced -61.5% 180D MAE with only +7.6% MFE; C14 should require customer call-off/utilization survival before any Stage2-Actionable promotion.

### 5.3 Shin Heung Energy & Electronics / 243840 — parts exposure turned into full demand-break risk
Shin Heung is a lithium-ion battery parts supplier with medium/large cap assemblies, cans and battery pack modules. MarketScreener's historical segment table shows lithium-ion battery parts sales declining from 540B KRW in 2023 to 433B KRW in 2024 and 408B KRW in 2025, with Hungary sales also declining. The 2024-07-12 row has +14.8% 180D MFE but -55.0% MAE, supporting C14 hard-4C/severe-4B protection when sales and utilization evidence confirm the break.

### 5.4 Chunbo / 278280 — not immediate hard 4C, but still no Yellow without lithium-price survival
Mirae's 2024-09-03 report says Chunbo saw North America-bound shipment growth, but the same report also cut target price, lowered EPS forecasts, and tied the pressure to rapidly falling lithium prices, China oversupply/restructuring and inventory valuation losses. This is exactly the C14 severity split: North America shipments prevent a blunt hard 4C, but depressed lithium ASP and China revenue weakness keep it at Stage4B/watch. The row's 180D path was +7.2% MFE vs -51.0% MAE.

### 5.5 Daejoo Electronic Materials / 078600 — survivor bridge exists, but entry needed reprice cap
Mirae's 2024-08-14 report shows a genuine survivor bridge: 2Q24 revenue +27% YoY, OP +357% YoY, OP margin 14.2%, silicon-anode revenue +205% YoY, and demand tied to mass-market EV model adoption and Stellantis. Therefore C14 must not tag Daejoo as hard 4C merely because EV demand slowed. However the stock-web entry after rerating had +2.5% 180D MFE and -43.7% MAE, so the correct residual rule is Stage2-Actionable only with local 4B cap, not Yellow/Green.

### 5.6 Enchem / 348370 — narrative route useful, but price row blocked
Enchem has a real electrolyte route and global production footprint, but stock-web rows around 2024 showed multiple share-count changes across the forward window. Therefore the case is kept as narrative-only / corporate-action-sanity-check, not representative aggregate input. This avoids teaching the calibrator from raw-unadjusted discontinuity.

## 6. Current calibrated profile stress test
| profile assumption | result in this loop | adjustment implied |
|---|---|---|
| stage2_actionable_evidence_bonus = +2.0 | Useful for Daejoo only, where OP/revenue bridge exists. Dangerous for TCC/Sam-A/Shinheung if product identity is treated as bridge. | Keep global bonus; add C14 component-specific demand-survival gate. |
| price_only_blowoff_blocks_positive_stage | Supported. TCC/Sam-A/Chunbo paths show early product narratives without forward survival. | Strengthen local 4B guard after rapid theme reprice. |
| full_4b_requires_non_price_evidence | Supported. Shinheung has sales decline evidence; Chunbo has lithium ASP/inventory evidence. | Maintain. |
| hard_4c_thesis_break_routes_to_4c | Needs severity split. Daejoo has real operating leverage despite sector slowdown, while Shinheung shows sales break. | Hard 4C only when utilization/call-off/sales/margin break is company-specific. |

## 7. Raw component score simulation
|case_id|symbol|eps_fcf_revision|earnings_visibility|bottleneck_pricing|market_mispricing|valuation_rerating|capital_allocation|information_confidence|stage2_actionable_bonus_applied|simulated_total_score|simulated_profile_verdict|price_alignment_flag|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C14_TCSTEEL_20240315_PROXY_4B|002710|2|3|5|3|2|1|7|0.0|23|Stage4B proxy guard|bad_entry_or_guardrail_success|
|C14_SAMA_20240315_FOIL_4B|006110|2|3|5|3|2|1|7|0.0|23|Stage4B proxy guard|bad_entry_or_guardrail_success|
|C14_SHINHEUNG_20240712_PARTS_4C|243840|1|2|3|2|1|1|8|0.0|18|Stage4C protection candidate|bad_entry_or_guardrail_success|
|C14_CHUNBO_20240903_ELECTROLYTE_4B|278280|3|5|7|5|2|1|10|0.0|33|Stage4B watch; reopen only after lithium ASP/utilization survival|bad_entry_or_guardrail_success|
|C14_DAEJOO_20240814_SILICON_ANODE_4B_CAP|078600|12|10|9|4|3|2|11|2.0|53.0|Stage2-Actionable but 4B cap; no Yellow/Green after reprice|bad_entry_or_guardrail_success|

## 8. Machine-readable rows
### 8.1 trigger_rows_jsonl
```jsonl
{"row_type": "trigger", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "selected_round": "R3", "selected_loop": 122, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_UTILIZATION_AND_PRICE_SLOWDOWN_SEVERITY_SPLIT", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_price_basis": "close_c_column", "case_id": "C14_TCSTEEL_20240315_PROXY_4B", "symbol": "002710", "company": "TCC Steel", "trigger_date": "2024-03-15", "entry_date": "2024-03-15", "entry_price": 62700.0, "trigger_type": "Stage4B", "evidence_family": "nickel_plated_steel_secondary_battery_component_proxy_after_LIB_component_degrowth", "classification": "positive_for_guardrail", "current_profile_verdict": "likely_stage2_false_positive_if_product_identity_is_overweighted", "calibration_usable": true, "MFE_30D_pct": 6.4, "MAE_30D_pct": -19.8, "MFE_90D_pct": 6.4, "MAE_90D_pct": -42.2, "MFE_180D_pct": 6.4, "MAE_180D_pct": -56.9, "peak_180D_date": "2024-03-21", "peak_180D_price": 66700.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 27000.0, "forward_180D_end": "2024-12-10", "corporate_action_check": "shares_stable_in_180D_window", "residual_error": "component identity was real, but no named EV/customer order or margin bridge; price path behaved like post-theme unwind", "dedupe_key": "C14_EV_DEMAND_SLOWDOWN_4B_4C|002710|Stage4B|2024-03-15"}
{"row_type": "trigger", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "selected_round": "R3", "selected_loop": 122, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_UTILIZATION_AND_PRICE_SLOWDOWN_SEVERITY_SPLIT", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_price_basis": "close_c_column", "case_id": "C14_SAMA_20240315_FOIL_4B", "symbol": "006110", "company": "Sam-A Aluminium", "trigger_date": "2024-03-15", "entry_date": "2024-03-15", "entry_price": 91100.0, "trigger_type": "Stage4B", "evidence_family": "LIB_cathode_foil_supplier_exposure_after_material_component_degrowth", "classification": "positive_for_guardrail", "current_profile_verdict": "likely_stage2_false_positive_if_major_customer_supply_is_not_checked_against_demand_slowdown", "calibration_usable": true, "MFE_30D_pct": 7.6, "MAE_30D_pct": -19.5, "MFE_90D_pct": 7.6, "MAE_90D_pct": -40.4, "MFE_180D_pct": 7.6, "MAE_180D_pct": -61.5, "peak_180D_date": "2024-03-26", "peak_180D_price": 98000.0, "trough_180D_date": "2024-11-15", "trough_180D_price": 35050.0, "forward_180D_end": "2024-12-10", "corporate_action_check": "shares_stable_in_180D_window", "residual_error": "customer/material route existed, but EV material price and component-market contraction dominated; needs call-off/utilization gate", "dedupe_key": "C14_EV_DEMAND_SLOWDOWN_4B_4C|006110|Stage4B|2024-03-15"}
{"row_type": "trigger", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "selected_round": "R3", "selected_loop": 122, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_UTILIZATION_AND_PRICE_SLOWDOWN_SEVERITY_SPLIT", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_price_basis": "close_c_column", "case_id": "C14_SHINHEUNG_20240712_PARTS_4C", "symbol": "243840", "company": "Shin Heung Energy & Electronics", "trigger_date": "2024-07-12", "entry_date": "2024-07-12", "entry_price": 8430.0, "trigger_type": "Stage4C", "evidence_family": "secondary_battery_parts_sales_decline_and_customer_utilization_risk", "classification": "positive_for_hard_4c_protection", "current_profile_verdict": "too_late_if_only_price_drawdown_is_used", "calibration_usable": true, "MFE_30D_pct": 14.8, "MAE_30D_pct": -24.3, "MFE_90D_pct": 14.8, "MAE_90D_pct": -37.1, "MFE_180D_pct": 14.8, "MAE_180D_pct": -55.0, "peak_180D_date": "2024-08-13", "peak_180D_price": 9680.0, "trough_180D_date": "2025-04-09", "trough_180D_price": 3790.0, "forward_180D_end": "2025-04-11", "corporate_action_check": "shares_stable_in_180D_window_after_prior_split", "residual_error": "parts exposure alone should not reopen; 2024/2025 sales contraction turns C14 into full thesis-break candidate", "dedupe_key": "C14_EV_DEMAND_SLOWDOWN_4B_4C|243840|Stage4C|2024-07-12"}
{"row_type": "trigger", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "selected_round": "R3", "selected_loop": 122, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_UTILIZATION_AND_PRICE_SLOWDOWN_SEVERITY_SPLIT", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_price_basis": "close_c_column", "case_id": "C14_CHUNBO_20240903_ELECTROLYTE_4B", "symbol": "278280", "company": "Chunbo", "trigger_date": "2024-09-03", "entry_date": "2024-09-03", "entry_price": 61300.0, "trigger_type": "Stage4B", "evidence_family": "electrolyte_additive_NA_shipments_offset_by_lithium_price_inventory_loss", "classification": "mixed_guardrail_not_hard_4c", "current_profile_verdict": "would_be_false_positive_if_NA_shipments_are_promoted_without_lithium_ASP_survival", "calibration_usable": true, "MFE_30D_pct": 7.2, "MAE_30D_pct": -15.0, "MFE_90D_pct": 7.2, "MAE_90D_pct": -42.3, "MFE_180D_pct": 7.2, "MAE_180D_pct": -51.0, "peak_180D_date": "2024-10-08", "peak_180D_price": 65700.0, "trough_180D_date": "2025-04-09", "trough_180D_price": 30050.0, "forward_180D_end": "2025-06-09", "corporate_action_check": "shares_stable_in_180D_window", "residual_error": "North-America shipment bridge prevents immediate hard 4C, but depressed lithium/China oversupply keeps it out of Yellow", "dedupe_key": "C14_EV_DEMAND_SLOWDOWN_4B_4C|278280|Stage4B|2024-09-03"}
{"row_type": "trigger", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "selected_round": "R3", "selected_loop": 122, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_UTILIZATION_AND_PRICE_SLOWDOWN_SEVERITY_SPLIT", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_price_basis": "close_c_column", "case_id": "C14_DAEJOO_20240814_SILICON_ANODE_4B_CAP", "symbol": "078600", "company": "Daejoo Electronic Materials", "trigger_date": "2024-08-14", "entry_date": "2024-08-14", "entry_price": 126200.0, "trigger_type": "Stage4B", "evidence_family": "silicon_anode_OP_surprise_but_late_value_chain_entry_and_high_MAE", "classification": "counterexample_to_blunt_hard_4c_but_positive_for_4b_cap", "current_profile_verdict": "stage2_actionable_ok_but_yellow_or_green_too_aggressive_after_reprice", "calibration_usable": true, "MFE_30D_pct": 2.5, "MAE_30D_pct": -29.2, "MFE_90D_pct": 2.5, "MAE_90D_pct": -41.7, "MFE_180D_pct": 2.5, "MAE_180D_pct": -43.7, "peak_180D_date": "2024-08-16", "peak_180D_price": 129400.0, "trough_180D_date": "2025-01-02", "trough_180D_price": 71000.0, "forward_180D_end": "2025-05-19", "corporate_action_check": "shares_stable_in_180D_window", "residual_error": "company bridge was strong, so hard 4C is too harsh; however entry timing after value-chain reprice needs local 4B/profit-lock cap", "dedupe_key": "C14_EV_DEMAND_SLOWDOWN_4B_4C|078600|Stage4B|2024-08-14"}
```

### 8.2 score_simulation_rows_jsonl
```jsonl
{"row_type": "score_simulation", "case_id": "C14_TCSTEEL_20240315_PROXY_4B", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "eps_fcf_revision": 2, "earnings_visibility": 3, "bottleneck_pricing": 5, "market_mispricing": 3, "valuation_rerating": 2, "capital_allocation": 1, "information_confidence": 7, "stage2_actionable_bonus_applied": 0.0, "simulated_total_score": 23, "simulated_profile_verdict": "Stage4B proxy guard", "price_alignment_flag": "bad_entry_or_guardrail_success"}
{"row_type": "score_simulation", "case_id": "C14_SAMA_20240315_FOIL_4B", "symbol": "006110", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "eps_fcf_revision": 2, "earnings_visibility": 3, "bottleneck_pricing": 5, "market_mispricing": 3, "valuation_rerating": 2, "capital_allocation": 1, "information_confidence": 7, "stage2_actionable_bonus_applied": 0.0, "simulated_total_score": 23, "simulated_profile_verdict": "Stage4B proxy guard", "price_alignment_flag": "bad_entry_or_guardrail_success"}
{"row_type": "score_simulation", "case_id": "C14_SHINHEUNG_20240712_PARTS_4C", "symbol": "243840", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "eps_fcf_revision": 1, "earnings_visibility": 2, "bottleneck_pricing": 3, "market_mispricing": 2, "valuation_rerating": 1, "capital_allocation": 1, "information_confidence": 8, "stage2_actionable_bonus_applied": 0.0, "simulated_total_score": 18, "simulated_profile_verdict": "Stage4C protection candidate", "price_alignment_flag": "bad_entry_or_guardrail_success"}
{"row_type": "score_simulation", "case_id": "C14_CHUNBO_20240903_ELECTROLYTE_4B", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "eps_fcf_revision": 3, "earnings_visibility": 5, "bottleneck_pricing": 7, "market_mispricing": 5, "valuation_rerating": 2, "capital_allocation": 1, "information_confidence": 10, "stage2_actionable_bonus_applied": 0.0, "simulated_total_score": 33, "simulated_profile_verdict": "Stage4B watch; reopen only after lithium ASP/utilization survival", "price_alignment_flag": "bad_entry_or_guardrail_success"}
{"row_type": "score_simulation", "case_id": "C14_DAEJOO_20240814_SILICON_ANODE_4B_CAP", "symbol": "078600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "eps_fcf_revision": 12, "earnings_visibility": 10, "bottleneck_pricing": 9, "market_mispricing": 4, "valuation_rerating": 3, "capital_allocation": 2, "information_confidence": 11, "stage2_actionable_bonus_applied": 2.0, "simulated_total_score": 53.0, "simulated_profile_verdict": "Stage2-Actionable but 4B cap; no Yellow/Green after reprice", "price_alignment_flag": "bad_entry_or_guardrail_success"}
```

### 8.3 narrative_only_rows_jsonl
```jsonl
{"row_type": "narrative_only_price_blocked", "case_id": "C14_ENCHEM_20240814_ELECTROLYTE_CA_BLOCK", "symbol": "348370", "company": "Enchem", "trigger_date": "2024-08-14", "entry_date": "2024-08-14", "entry_price": 185000.0, "trigger_type": "Stage4B", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "MFE_30D_pct": 20.8, "MAE_30D_pct": -14.0, "MFE_90D_pct": 20.8, "MAE_90D_pct": -41.6, "MFE_180D_pct": 20.8, "MAE_180D_pct": -69.2, "calibration_usable": false, "blocked_reason": "corporate_action_contaminated_180D_window_by_multiple_share_count_changes_in_stock_web_rows", "use_in_md": "narrative_only_corporate_action_sanity_check_not_representative_aggregate"}
```

### 8.4 aggregate_rows_jsonl
```jsonl
{"row_type": "aggregate", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "selected_round": "R3", "selected_loop": 122, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "usable_trigger_count": 5, "representative_trigger_count": 5, "narrative_only_blocked_count": 1, "new_symbol_count": 6, "same_archetype_new_symbol_count": 6, "new_trigger_family_count": 6, "positive_case_count": 4, "counterexample_count": 2, "stage4b_overlay_count": 4, "stage4c_case_count": 1, "avg_MFE_90D_pct": 7.7, "avg_MAE_90D_pct": -40.74, "max_180D_drawdown_case": "006110 Sam-A Aluminium MAE_180D -61.5%; 002710 TCC Steel MAE_180D -56.9%; 243840 Shin Heung -55.0%", "production_scoring_changed": false, "shadow_weight_only": true}
```

### 8.5 shadow_weight_rows_jsonl
```jsonl
{"row_type": "shadow_weight", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "proposed_axis": "C14_COMPONENT_PRICE_UTILIZATION_SLOWDOWN_REQUIRES_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE", "direction": "increase_guardrail_specificity_no_global_weight_change", "stage2_required_bridge_delta": "+sector_specific", "full_4b_requires_non_price_evidence": "strengthen", "hard_4c_thesis_break_routes_to_4c": "severity_split_not_blunt", "rationale": "component suppliers with real product routes still had -40% to -60% MAE when utilization/call-off/material price survival was absent; Daejoo shows hard 4C must not override genuine operating-leverage survivors."}
```

### 8.6 residual_contribution_rows_jsonl
```jsonl
{"row_type": "residual_contribution", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_122_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "current_profile_error_type": "sector_component_proxy_and_late_entry_risk", "residual_summary": "Generic battery-component exposure remained too easy to over-promote. The missing gate is not EV-demand-slowdown vocabulary, but utilization/call-off/material-price survival plus survivor reopen logic.", "rule_candidate": "C14_COMPONENT_PRICE_UTILIZATION_SLOWDOWN_REQUIRES_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE"}
```

## 9. Novelty / no-repeat check
```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
all_representative_keys_new_in_this_local_loop = true
reused_case_count = 0
new_independent_case_count = 5
narrative_only_blocked_count = 1
source_proxy_only_reduced_by_company_product_or_financial_source = partial
```
- `C14_EV_DEMAND_SLOWDOWN_4B_4C|002710|Stage4B|2024-03-15`
- `C14_EV_DEMAND_SLOWDOWN_4B_4C|006110|Stage4B|2024-03-15`
- `C14_EV_DEMAND_SLOWDOWN_4B_4C|243840|Stage4C|2024-07-12`
- `C14_EV_DEMAND_SLOWDOWN_4B_4C|278280|Stage4B|2024-09-03`
- `C14_EV_DEMAND_SLOWDOWN_4B_4C|078600|Stage4B|2024-08-14`

## 10. Residual contribution summary
```text
sector_specific_rule_candidate = L3_BATTERY_COMPONENT_SLOWDOWN_REQUIRES_UTILIZATION_CALLOFF_PRICE_AND_MARGIN_SURVIVAL_GATE
canonical_archetype_rule_candidate = C14_COMPONENT_PRICE_UTILIZATION_SLOWDOWN_REQUIRES_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE
new_axis_proposed = C14_COMPONENT_PRICE_UTILIZATION_SLOWDOWN_REQUIRES_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE
existing_axis_strengthened = full_4b_requires_non_price_evidence; price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c_with_severity_split
existing_axis_weakened = blunt_hard_4c_on_all_battery_material_names
production_scoring_changed = false
shadow_weight_only = true
```
Recommended rule wording:

> For C14, downgrade generic battery-material/component exposure to Stage2-watch or Stage4B unless company-specific utilization, customer call-off, sales decline, inventory valuation loss, lithium/metal ASP pressure, or margin/FCF break is visible. Escalate to hard 4C only when the break is company-specific and persistent. If a survivor bridge exists, such as Daejoo's silicon-anode OP leverage or Chunbo's North America shipment route, keep decay/reopen open but cap fresh Yellow/Green until price/material survival is confirmed.

## 11. Deferred Coding Agent Handoff Prompt — do not execute now
```text
You are the later batch implementation agent for Songdaiki/stock_agent. Do not re-run live scans. Read this MD as one v12 historical calibration research artifact. Parse trigger_rows_jsonl, score_simulation_rows_jsonl, narrative_only_rows_jsonl, aggregate_rows_jsonl, shadow_weight_rows_jsonl, and residual_contribution_rows_jsonl. Validate the standard filename, selected_round=R3, large_sector_id=L3_BATTERY_EV_GREEN_MOBILITY, canonical_archetype_id=C14_EV_DEMAND_SLOWDOWN_4B_4C, and complete 30/90/180D MFE/MAE fields. Use narrative-only Enchem only for corporate-action block testing, not aggregate. Consider adding or strengthening a C14-specific runtime note: component/product identity does not equal demand-survival; require utilization/call-off/material-price/margin survival before Stage2-Actionable or Yellow, while preserving survivor reopen logic for Daejoo/Chunbo-like cases.
```
## 12. Next research state
```text
completed_round = R3
completed_loop = 122
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C14 follow-up / new symbol-date-family expansion
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_followup_counterexample, C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_symbols_only, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_followup_new_order_route, C11_BATTERY_ORDERBOOK_RERATING_followup_margin_FCF_bridge, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_if_source_proxy_repair_needed
```
