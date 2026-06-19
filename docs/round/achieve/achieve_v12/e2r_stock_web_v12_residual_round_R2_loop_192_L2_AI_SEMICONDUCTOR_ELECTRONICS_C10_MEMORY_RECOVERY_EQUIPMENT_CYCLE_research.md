# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 192
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement — C10 recovery-cycle false positives and order-conversion confirmation
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE
output_filename: e2r_stock_web_v12_residual_round_R2_loop_192_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
```

One-line contribution: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` needs a sharper split between **customer-level memory capex recovery** and **supplier-level order/revenue conversion**. The same memory recovery river lifted early direct-exposure equipment names, but it drowned late beta entries and utilization-rate sympathy names.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
after_profile_id: proposed_C10_memory_order_conversion_shadow_profile
stage2_actionable_evidence_bonus: +2.0 assumed active
stage3_yellow_total_min: 75.0 assumed active
stage3_green_total_min: 87.0 assumed active
price_only_blowoff_blocks_positive_stage: true
full_4b_requires_non_price_evidence: true
hard_4c_thesis_break_routes_to_4c: true
```

This loop does not repeat the global lesson that Stage2 should be earlier than Green. It tests the residual C10 problem: **a memory cycle is not yet an equipment order cycle until supplier conversion appears**.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
selected_round: R2
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE
loop_objectives:
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - residual_missed_structural_mining
```

Scope boundary: C10 covers memory capex recovery, front-end process equipment, test/strip equipment, and supplier revenue conversion. HBM TC-bonder pure packaging cases remain C07 unless they are used only as customer-capex context.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used as the duplicate ledger:

- C10 row state: `210 rows / 68 symbols / positives-counter 27-32 / 4B-4C 27-0`.
- Top repeated C10 symbols include `240810`, `084370`, `095610`, `036930`, `319660`, `166090`, so this loop does not claim novelty merely from ticker names.
- Novelty comes from the paired path: early DRAM resumption positives, later customer-capex false positives, utilization-rate propagation 4B, and a 2025 supplier-revenue confirmation reopening a previously failed PSK route.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
batch_hard_duplicate_count: 0
new_independent_case_count: 6
reused_case_count: 2
new_symbol_count: 6
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
new_trigger_family_count: 6
minimum_new_independent_case_ratio: 0.60
actual_new_independent_case_ratio: 6/8 = 0.75
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest/schema validation:

```text
price_source: Songdaiki/stock-web
source_repo_url: https://github.com/Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
validation_status: usable_for_historical_calibration
```

The schema definition used here is: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100` and `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 5. Historical Eligibility Gate

|symbol|entry_date|open|high|low|close|volume|price_shard_path|
|---|---|---|---|---|---|---|---|
|240810|2022-08-16|29500|30200|29200|29450|395307|atlas/ohlcv_tradable_by_symbol_year/240/240810/2022.csv|
|084370|2024-03-04|38600|39050|37700|38250|212267|atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv|
|095610|2024-03-04|20100|20400|19800|20200|197806|atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv|
|095610|2024-04-25|25750|26900|25500|26100|568070|atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv|
|319660|2024-04-25|29900|30900|29850|30100|242835|atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv|
|036930|2024-07-19|31050|32000|30650|31550|450845|atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv|
|166090|2024-06-26|58600|66600|58600|63900|685393|atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv|
|319660|2025-02-26|21050|21700|20500|20600|252912|atlas/ohlcv_tradable_by_symbol_year/319/319660/2025.csv|

All selected trigger rows have at least 180 tradable rows after entry before the Stock-Web manifest max date. Corporate-action candidate dates in symbol profiles do not overlap any entry~D+180 window used here.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_family:
  1. customer_memory_capex_recovery_headline
  2. supplier_order_revenue_conversion
  3. front_end_advanced_process_equipment
  4. utilization_rate_supplier_propagation
  5. late_customer_capex_after_supplier_peak
compression_rule:
  customer capex headline -> Stage2 only
  customer capex + direct equipment exposure + early cycle timing -> Stage2-Actionable
  supplier order/revenue confirmation -> Stage2-Actionable reopen
  utilization-rate/materials sympathy without order -> local Stage4B watch
  late capex headline after local supplier rerating -> Stage4B or Stage2 cap
```

## 7. Case Selection Summary

|case_id|symbol|company|trigger|trigger_date|entry_date|180D MFE/MAE|case_role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|C10_240810_20220812_STAGE4B|240810|Wonik IPS|Stage4B|2022-08-12|2022-08-16|23.60/-26.66|4B_overlay_success|current_profile_correct|
|C10_084370_20240229_STAGE2A|084370|Eugene Technology|Stage2-Actionable|2024-02-29|2024-03-04|56.86/-15.16|structural_success|current_profile_correct|
|C10_095610_20240229_STAGE2A|095610|TES|Stage2-Actionable|2024-02-29|2024-03-04|62.87/-30.30|high_mae_success|current_profile_correct|
|C10_095610_20240424_STAGE4B|095610|TES|Stage4B|2024-04-24|2024-04-25|6.51/-49.85|4B_overlay_success|current_profile_4B_too_late|
|C10_319660_20240424_STAGE2_FALSE|319660|PSK|Stage2|2024-04-24|2024-04-25|29.90/-48.34|failed_rerating|current_profile_false_positive|
|C10_036930_20240719_STAGE2_HMAE|036930|Jusung Engineering|Stage2|2024-07-19|2024-07-19|37.56/-30.11|high_mae_success|current_profile_too_early|
|C10_166090_20240626_STAGE4B|166090|Hana Materials|Stage4B|2024-06-26|2024-06-26|8.45/-65.81|4B_overlay_success|current_profile_false_positive|
|C10_319660_20250225_STAGE2A|319660|PSK|Stage2-Actionable|2025-02-25|2025-02-26|100.97/-20.97|missed_structural|current_profile_missed_structural|

## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count: 8
calibration_usable_trigger_count: 8
positive_case_count: 3
counterexample_count: 5
4B_case_count: 3
4C_case_count: 0
current_profile_error_count: 5
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
```

The positive half says early direct-exposure equipment names and later supplier-confirmation names can work. The counterexample half says generic customer capex and utilization-rate sympathy become a trap once the supplier’s own order bridge is missing.

## 9. Evidence Source Map

|source_key|role|url|
|---|---|---|
|MAIN_PROMPT|control/source|https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt|
|NO_REPEAT_INDEX|control/source|https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md|
|STOCK_WEB_MANIFEST|control/source|https://raw.githubusercontent.com/Daikisong/stock-web/refs/heads/main/atlas/manifest.json|
|STOCK_WEB_SCHEMA|control/source|https://raw.githubusercontent.com/Daikisong/stock-web/main/atlas/schema.json|
|BusinessKorea_Wonik_2022_capex_delay|evidence/source|https://www.businesskorea.co.kr/news/articleView.html?idxno=98412|
|Chosun_DRAM_expansion_2024_02_29|evidence/source|https://www.chosun.com/english/industry-en/2024/02/29/SGS2LHTAAJAIHBDRMMJLBHGSFA/|
|Reuters_SKHynix_recovery_2024_04_25|evidence/source|https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/|
|Reuters_SKHynix_M15X_2024_04_24|evidence/source|https://www.reuters.com/technology/sk-hynix-invest-386-bln-dram-chip-production-base-south-korea-2024-04-24/|
|AsiaBusiness_advanced_process_2024_07_19|evidence/source|https://www.asiae.co.kr/en/article/2024071907585690985|
|Counterpoint_test_equipment_2025_02_25|evidence/source|https://counterpointresearch.com/en/insights/semiconductor-test-equipment-makers-revenue-grows-18-yoy-in-2024-on-strong-ai-compute-hbm-dram-demand|
|MK_Hana_memory_utilization_2024_06_26|evidence/source|https://www.mk.co.kr/en/stock/11051593|
|Eugene_official_financial|evidence/source|https://www.eugenetech.co.kr/eng/sub/investment_1.php|
|TES_official_financial|evidence/source|https://hites.co.kr/eng/bbs/board.php?bo_table=d1|
|PSK_official_financial|evidence/source|https://www.pskinc.com/ir/financial_summary.php|
|Jusung_official_semiconductor|evidence/source|https://jusung.com/eng/document/semiconductor|

Evidence timing notes:

- Unknown publication-time sources use next stock-web tradable close.
- Reuters Apr. 24 UTC customer-capex evidence uses Apr. 25 KRX close.
- Asia Business Jul. 19 source was before-market KST and uses same-day close.
- MK Jun. 26 source was intraday and uses same-day close.
- Official company financial pages are used as later validation/confirmation, not backdated evidence for earlier entries.

## 10. Price Data Source Map

```text
profile_paths:
  240810: atlas/symbol_profiles/240/240810.json
  084370: atlas/symbol_profiles/084/084370.json
  095610: atlas/symbol_profiles/095/095610.json
  319660: atlas/symbol_profiles/319/319660.json
  036930: atlas/symbol_profiles/036/036930.json
  166090: atlas/symbol_profiles/166/166090.json
corporate_action_window_status:
  all selected 180D windows: clean_180D_window
price_adjustment_status:
  raw_unadjusted_marcap
```

## 11. Case-by-Case Trigger Grid


### C10_240810_20220812_STAGE4B — Wonik IPS (240810)

```text
trigger_type: Stage4B
trigger_date: 2022-08-12
entry_date: 2022-08-16
entry_price: 29450
case_role: 4B_overlay_success
positive_or_counterexample: counterexample
evidence_source: BusinessKorea_Wonik_2022_capex_delay
current_profile_verdict: current_profile_correct
```

Evidence available at trigger: BusinessKorea/NH analyst evidence: memory chipmakers expected to significantly reduce 2023 capex; Wonik orders and sales momentum limited until 2023; improvement deferred to 2H23.

Backtest read: 4B watch was directionally useful: immediate 30/90D MFE only 2.55% versus MAE around -26%; later 180D MFE came only after a long trough.

### C10_084370_20240229_STAGE2A — Eugene Technology (084370)

```text
trigger_type: Stage2-Actionable
trigger_date: 2024-02-29
entry_date: 2024-03-04
entry_price: 38250
case_role: structural_success
positive_or_counterexample: positive
evidence_source: Chosun_DRAM_expansion_2024_02_29 + Eugene_official_financial
current_profile_verdict: current_profile_correct
```

Evidence available at trigger: Samsung/SK Hynix DRAM plant/equipment investment resumption headline plus Eugene official financial validation of FY2024 operating income improvement over FY2023.

Backtest read: Early DRAM resumption window captured most upside: 90D/180D MFE 56.86% with MAE -10.20%/-15.16%.

### C10_095610_20240229_STAGE2A — TES (095610)

```text
trigger_type: Stage2-Actionable
trigger_date: 2024-02-29
entry_date: 2024-03-04
entry_price: 20200
case_role: high_mae_success
positive_or_counterexample: positive
evidence_source: Chosun_DRAM_expansion_2024_02_29 + TES_official_financial
current_profile_verdict: current_profile_correct
```

Evidence available at trigger: Same early DRAM equipment investment resumption setup, mapped to TES front-end equipment exposure; TES official financial page later shows FY2024 operating profit recovery from FY2023 loss.

Backtest read: Early trigger worked, but the cycle peaked quickly; MFE90 62.87% while 180D MAE widened to -30.30%, so Green must remain blocked without fresh order conversion.

### C10_095610_20240424_STAGE4B — TES (095610)

```text
trigger_type: Stage4B
trigger_date: 2024-04-24
entry_date: 2024-04-25
entry_price: 26100
case_role: 4B_overlay_success
positive_or_counterexample: counterexample
evidence_source: Reuters_SKHynix_recovery_2024_04_25 + Reuters_SKHynix_M15X_2024_04_24
current_profile_verdict: current_profile_4B_too_late
```

Evidence available at trigger: SK Hynix full memory recovery and M15X/HBM capex headlines were strong at customer level, but no TES-specific order conversion evidence was present at this later point after the early TES move.

Backtest read: Late customer capex headline without TES-specific order conversion was a bad entry: MFE180 6.51% versus MAE180 -49.85%.

### C10_319660_20240424_STAGE2_FALSE — PSK (319660)

```text
trigger_type: Stage2
trigger_date: 2024-04-24
entry_date: 2024-04-25
entry_price: 30100
case_role: failed_rerating
positive_or_counterexample: counterexample
evidence_source: Reuters_SKHynix_recovery_2024_04_25 + Reuters_SKHynix_M15X_2024_04_24
current_profile_verdict: current_profile_false_positive
```

Evidence available at trigger: SK Hynix recovery/capex evidence supported a broad equipment-cycle narrative, but PSK-specific 2024 order/revenue conversion had not yet been confirmed at trigger date.

Backtest read: Generic capex beta delivered MFE90 29.90% but MAE180 -48.34%; current profile would over-count customer capex without supplier conversion.

### C10_036930_20240719_STAGE2_HMAE — Jusung Engineering (036930)

```text
trigger_type: Stage2
trigger_date: 2024-07-19
entry_date: 2024-07-19
entry_price: 31550
case_role: high_mae_success
positive_or_counterexample: counterexample
evidence_source: AsiaBusiness_advanced_process_2024_07_19 + Jusung_official_semiconductor
current_profile_verdict: current_profile_too_early
```

Evidence available at trigger: Asia Business/DS noted advanced-process equipment investment justification from 2H24/2025; Jusung official page maps its ALD equipment directly to ultra-fine DRAM and 200+ layer 3D NAND processes.

Backtest read: This was not a clean Actionable entry: 30D MAE -29.79% and 90D MAE -30.11% came before 180D MFE 37.56%.

### C10_166090_20240626_STAGE4B — Hana Materials (166090)

```text
trigger_type: Stage4B
trigger_date: 2024-06-26
entry_date: 2024-06-26
entry_price: 63900
case_role: 4B_overlay_success
positive_or_counterexample: counterexample
evidence_source: MK_Hana_memory_utilization_2024_06_26
current_profile_verdict: current_profile_false_positive
```

Evidence available at trigger: MK reported Hana Materials rising on memory utilization-rate recovery. This is a supplier-propagation headline, not direct equipment order conversion.

Backtest read: Excellent 4B guard example: entry was near local top; MFE180 8.45% versus MAE180 -65.81%.

### C10_319660_20250225_STAGE2A — PSK (319660)

```text
trigger_type: Stage2-Actionable
trigger_date: 2025-02-25
entry_date: 2025-02-26
entry_price: 20600
case_role: missed_structural
positive_or_counterexample: positive
evidence_source: Counterpoint_test_equipment_2025_02_25 + PSK_official_financial
current_profile_verdict: current_profile_missed_structural
```

Evidence available at trigger: Counterpoint reported test equipment maker revenue growth in 2024 on AI/HBM/DRAM demand; PSK official financials later show 2024 sales and operating profit recovery from 2023.

Backtest read: Actual revenue confirmation changed the sign: 180D MFE 100.97% with MAE180 -20.97%, after the 2024 generic capex entry failed.

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|DD_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|
|C10_240810_20220812_STAGE4B_CAPEX_DELAY|29450.0|2.55|-23.26|2.55|-26.66|23.6|-26.66|2023-03-30|36400|-19.23|
|C10_084370_20240229_STAGE2A_DRAM_RESUME|38250.0|37.78|-10.2|56.86|-10.2|56.86|-15.16|2024-05-28|60000|-45.92|
|C10_095610_20240229_STAGE2A_DRAM_RESUME|20200.0|44.31|-6.68|62.87|-6.68|62.87|-30.3|2024-04-17|32900|-57.2|
|C10_095610_20240424_STAGE4B_ORDER_CONVERSION_MISSING|26100.0|4.79|-15.33|6.51|-38.7|6.51|-49.85|2024-06-27|27800|-52.91|
|C10_319660_20240424_STAGE2_CUSTOMER_CAPEX_FALSE|30100.0|14.45|-8.64|29.9|-24.58|29.9|-48.34|2024-07-11|39100|-60.23|
|C10_036930_20240719_STAGE2_ADV_PROCESS_FRONTEND|31550.0|1.43|-29.79|7.92|-30.11|37.56|-30.11|2025-03-21|43400|-22.58|
|C10_166090_20240626_STAGE4B_UTILIZATION_PROPAGATION|63900.0|8.45|-38.73|8.45|-56.65|8.45|-65.81|2024-07-02|69300|-68.47|
|C10_319660_20250225_STAGE2A_REVENUE_CONFIRMATION|20600.0|10.44|-20.97|10.44|-20.97|100.97|-20.97|2025-11-06|41400|-23.43|

## 13. Current Calibrated Profile Stress Test

|case_id|trigger|score_before|stage_before|score_after|stage_after|profile_verdict|alignment|
|---|---|---|---|---|---|---|---|
|C10_240810_20220812_STAGE4B|Stage4B|58|Stage4B|54|Stage4B|current_profile_correct|risk_overlay_correct|
|C10_084370_20240229_STAGE2A|Stage2-Actionable|78|Stage2-Actionable|80|Stage2-Actionable|current_profile_correct|score_return_aligned_positive|
|C10_095610_20240229_STAGE2A|Stage2-Actionable|76|Stage2-Actionable|78|Stage2-Actionable|current_profile_correct|early_stage2_positive_but_green_block_needed|
|C10_095610_20240424_STAGE4B|Stage4B|74|Stage2-Actionable|58|Stage4B|current_profile_4B_too_late|late_generic_capex_false_positive|
|C10_319660_20240424_STAGE2_FALSE|Stage2|72|Stage2-Actionable|60|Stage2|current_profile_false_positive|customer_capex_beta_high_mae_false_positive|
|C10_036930_20240719_STAGE2_HMAE|Stage2|70|Stage2-Actionable|64|Stage2|current_profile_too_early|delayed_positive_high_mae|
|C10_166090_20240626_STAGE4B|Stage4B|68|Stage2|49|Stage4B|current_profile_false_positive|propagation_without_order_conversion_false_positive|
|C10_319660_20250225_STAGE2A|Stage2-Actionable|70|Stage2|76|Stage2-Actionable|current_profile_missed_structural|confirmed_conversion_reopened_positive|

Interpretation:

- The current profile is directionally correct for the early 2024 Eugene/TES direct-exposure window.
- It is too permissive when customer capex is treated as supplier order conversion after supplier stocks have already rerated.
- It is too late/muted when actual supplier revenue/test-equipment confirmation appears after an earlier false start.

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green trigger is proposed in this loop.

```text
green_lateness_ratio: not_applicable
reason: no confirmed Stage3-Green trigger; all positives remain Stage2-Actionable or Stage2 pending supplier-specific order/revenue bridge.
```

Stage2-Actionable comparison:

- Eugene 2024-03-04: MFE90 56.86 / MAE90 -10.20.
- TES 2024-03-04: MFE90 62.87 / MAE90 -6.68, but later 180D drawdown confirms Green should not loosen.
- PSK 2025-02-26: MFE180 100.97 after supplier confirmation, but first 90D was still high-MAE, so Yellow/Green still need revision durability.

## 15. 4B Local vs Full-window Timing Audit

|case|4B_evidence_type|local_peak_proximity|full_window_peak_proximity|verdict|
|---|---|---|---|---|
|240810_2022|capex_delay / margin_slowdown|not_applicable|not_applicable|good 4B risk watch; protected against 30/90D drawdown|
|095610_2024_late|late customer capex without supplier order|0.46|0.46|post-local-peak 4B; not a positive Stage2-Actionable entry|
|166090_2024|utilization-rate propagation / positioning overheat|near local top|near local top|strong 4B guard; MFE180 8.45 vs MAE180 -65.81|

The 4B lesson is not price-only blowoff. The non-price problem is that the evidence was **generic customer capex or utilization recovery**, not supplier-specific order conversion.

## 16. 4C Protection Audit

```text
hard_4c_rows: 0
four_c_protection_score: not_applicable
hard_4c_success: none
hard_4c_late: none
thesis_break_watch_only: 240810 capex delay, 166090 utilization propagation, 095610 late-capex entry
```

No case had direct customer order cancellation, equipment qualification failure, accounting break, or explicit thesis evidence broken enough to route hard Stage4C at the trigger date.

## 17. Sector-Specific Rule Candidate

```text
rule_id: L2_MEMORY_EQUIPMENT_CUSTOMER_CAPEX_TO_SUPPLIER_CONVERSION_GATE
rule_scope: sector_specific
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
hypothesis:
  In L2 semiconductor equipment, customer capex recovery can create a broad Stage2 watch,
  but Stage2-Actionable needs either direct equipment exposure early in the cycle
  or supplier-specific order/revenue confirmation.
positive_support:
  - 084370 Eugene Technology early DRAM resumption case
  - 095610 TES early DRAM resumption case
  - 319660 PSK 2025 supplier/test-equipment confirmation case
counterexample_support:
  - 319660 PSK 2024 generic customer capex beta
  - 166090 Hana Materials utilization-rate propagation
  - 095610 TES late customer-capex headline after local rerating
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id: C10_MEMORY_ORDER_CONVERSION_REQUIRED_BRIDGE
rule_scope: canonical_archetype_specific
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
candidate_logic:
  if evidence == customer_memory_capex_recovery_only:
      max_stage = Stage2
  if evidence includes direct_equipment_exposure and early_cycle_timing:
      allow Stage2-Actionable
  if evidence includes supplier_order, supplier_revenue_growth, or confirmed test/front-end equipment conversion:
      allow Stage2-Actionable reopen
  if evidence is utilization_rate_recovery or materials sympathy without order conversion:
      route to local Stage4B watch, not Stage2 promotion
  if late capex headline follows local supplier peak and lacks supplier-specific order:
      downgrade Actionable to Stage4B or Stage2 cap
```

## 19. Before / After Backtest Comparison

|profile|profile_id|scope|hypothesis|eligible_triggers|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|verdict|
|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|current calibrated proxy|accepts broad customer capex beta too easily in C10|8|23.19|-26.82|40.84|-35.9|false positives remain in generic capex headline cases|
|P0b|e2r_2_0_baseline_reference|rollback reference|earlier Stage2 but weaker 4B routing|8|23.19|-26.82|40.84|-35.9|would over-promote utilization/relative-strength sympathy|
|P1|L2 sector candidate|sector-specific bridge gate|customer capex counts only with supplier exposure/order route|5|32.05|-17.46|56.24|-29.31|better than P0 but still includes high-MAE front-end cases|
|P2|C10 canonical candidate|order-conversion required profile|promote only early customer capex + direct exposure or confirmed supplier revenue/order conversion|3|43.39|-12.62|73.57|-22.14|best score-return alignment; fewer false positives|
|P3|counterexample guard profile|utilization-propagation/late-capex guard|routes materials-utilization and late capex headline to 4B watch|4|13.82|-33.21|19.61|-47.67|best protection for 4B/high-MAE rows|

## 20. Score-Return Alignment Matrix

```text
best_alignment:
  P2 canonical order-conversion required profile
why:
  It keeps early direct-exposure positives and PSK 2025 supplier-confirmed rebound,
  while demoting generic capex and utilization-rate propagation traps.
false_positive_rate_reduction:
  qualitative improvement from 4/8 problematic entries to 1~2/8 watch-level entries
late_green_count:
  0 because no Green is proposed
avg_green_lateness_ratio:
  not_applicable
```

## 21. Coverage Matrix

|coverage_item|value|notes|
|---|---|---|
|selected canonical|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|210 representative rows / 68 symbols / positives-counter 27-32 / 4B-4C 27-0 per No-Repeat Index|
|new unique symbols in this MD|6|Wonik IPS, Eugene Technology, TES, PSK, Jusung Engineering, Hana Materials|
|positive/counterexample|3/5|positive requires early direct exposure or later supplier confirmation; counterexamples test generic customer-capex and utilization propagation|
|4B/4C contribution|3/0|adds C10 4B quality path; no hard 4C because none of the cases had direct order cancellation/thesis break within evidence date|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 2
new_symbol_count: 6
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
new_trigger_family_count: 6
positive_case_count: 3
counterexample_count: 5
current_profile_error_count: 5
diversity_score_summary: high — 6 symbols, 6 trigger families, early-cycle positives, late generic-capex false positives, utilization-propagation 4B, and supplier-confirmation reopen path
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

Residual error types found:

```text
- generic_customer_capex_false_positive
- utilization_propagation_false_positive
- late_capex_after_supplier_peak_4B
- high_mae_delayed_success
- confirmed_supplier_conversion_missed_structural
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual Stock-Web tradable 1D OHLC rows for all entries.
- Entry close, 30/90/180D MFE and MAE.
- Peak date, peak price, drawdown after peak.
- Corporate action window status from symbol profile dates.
- Round/large-sector/canonical consistency.
- Hard duplicate key uniqueness inside this batch.

Not validated:

- Intraday exact publication timestamp for Chosun/Counterpoint/BusinessKorea. Conservative next-tradable close was used when publication time was unknown.
- Production scoring code. This run does not open or patch `stock_agent` code.
- Current live watchlist or current investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_supplier_order_conversion_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"generic customer capex headline produced PSK/TES/Hana false positives unless supplier order/revenue conversion existed","reduce false positives while keeping Eugene/TES early and PSK 2025 confirmed positives","C10_095610_20240424_STAGE4B_ORDER_CONVERSION_MISSING|C10_319660_20240424_STAGE2_CUSTOMER_CAPEX_FALSE|C10_319660_20250225_STAGE2A_REVENUE_CONFIRMATION",8,6,5,medium,canonical_shadow_only,"not production; use as v12 residual candidate"
shadow_weight,C10_utilization_supplier_propagation_to_4B,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"materials/utilization-rate propagation had low MFE and severe MAE in Hana Materials","routes non-order sympathy into local 4B watch","C10_166090_20240626_STAGE4B_UTILIZATION_PROPAGATION",1,1,1,medium,canonical_shadow_only,"do not promote to Stage2 without order or revenue bridge"
shadow_weight,C10_stage2_reopen_on_supplier_financial_confirmation,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"after customer-capex beta failed in 2024, confirmed 2024 revenue/test-equipment demand reopened PSK successfully in 2025","captures missed structural rebound after actual conversion evidence","C10_319660_20250225_STAGE2A_REVENUE_CONFIRMATION",1,0,0,low,canonical_shadow_only,"requires more cases before promotion"
```

Existing applied axis status:

```text
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - earlier_thesis_break_watch
existing_axis_weakened: none
new_axis_proposed: C10_supplier_order_conversion_required_bridge
production_scoring_changed: false
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10_240810_20220812_STAGE4B","symbol":"240810","company_name":"Wonik IPS","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"risk_overlay_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"4B watch was directionally useful: immediate 30/90D MFE only 2.55% versus MAE around -26%; later 180D MFE came only after a long trough."}
{"row_type":"trigger","trigger_id":"C10_240810_20220812_STAGE4B_CAPEX_DELAY","case_id":"C10_240810_20220812_STAGE4B","symbol":"240810","company_name":"Wonik IPS","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2022-08-12","entry_date":"2022-08-16","entry_price":29450.0,"evidence_available_at_that_date":"BusinessKorea/NH analyst evidence: memory chipmakers expected to significantly reduce 2023 capex; Wonik orders and sales momentum limited until 2023; improvement deferred to 2H23.","evidence_source":"BusinessKorea_Wonik_2022_capex_delay","evidence_url":"https://www.businesskorea.co.kr/news/articleView.html?idxno=98412","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2022.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.55,"MFE_90D_pct":2.55,"MFE_180D_pct":23.6,"MAE_30D_pct":-23.26,"MAE_90D_pct":-26.66,"MAE_180D_pct":-26.66,"peak_date":"2023-03-30","peak_price":36400.0,"drawdown_after_peak_pct":-19.23,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"risk_overlay_correct","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|240810|Stage4B|2022-08-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_240810_20220812_STAGE4B","trigger_id":"C10_240810_20220812_STAGE4B_CAPEX_DELAY","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":35,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":30,"execution_risk_score":75,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":20,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":85,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":54,"stage_label_after":"Stage4B","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"kept as 4B overlay; capex delay and lack of near-term order conversion block Stage2 recovery promotion.","MFE_90D_pct":2.55,"MAE_90D_pct":-26.66,"score_return_alignment_label":"risk_overlay_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10_084370_20240229_STAGE2A","symbol":"084370","company_name":"Eugene Technology","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Early DRAM resumption window captured most upside: 90D/180D MFE 56.86% with MAE -10.20%/-15.16%."}
{"row_type":"trigger","trigger_id":"C10_084370_20240229_STAGE2A_DRAM_RESUME","case_id":"C10_084370_20240229_STAGE2A","symbol":"084370","company_name":"Eugene Technology","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":38250.0,"evidence_available_at_that_date":"Samsung/SK Hynix DRAM plant/equipment investment resumption headline plus Eugene official financial validation of FY2024 operating income improvement over FY2023.","evidence_source":"Chosun_DRAM_expansion_2024_02_29 + Eugene_official_financial","evidence_url":"https://www.chosun.com/english/industry-en/2024/02/29/SGS2LHTAAJAIHBDRMMJLBHGSFA/","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.78,"MFE_90D_pct":56.86,"MFE_180D_pct":56.86,"MAE_30D_pct":-10.2,"MAE_90D_pct":-10.2,"MAE_180D_pct":-15.16,"peak_date":"2024-05-28","peak_price":60000.0,"drawdown_after_peak_pct":-45.92,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|084370|Stage2-Actionable|2024-03-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_084370_20240229_STAGE2A","trigger_id":"C10_084370_20240229_STAGE2A_DRAM_RESUME","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":45,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":45,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":20,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"retain Stage2-Actionable only when customer capex resumption is paired with direct memory/front-end equipment exposure.","MFE_90D_pct":56.86,"MAE_90D_pct":-10.2,"score_return_alignment_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10_095610_20240229_STAGE2A","symbol":"095610","company_name":"TES","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"structural_success_with_4b_need","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early_stage2_positive_but_green_block_needed","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Early trigger worked, but the cycle peaked quickly; MFE90 62.87% while 180D MAE widened to -30.30%, so Green must remain blocked without fresh order conversion."}
{"row_type":"trigger","trigger_id":"C10_095610_20240229_STAGE2A_DRAM_RESUME","case_id":"C10_095610_20240229_STAGE2A","symbol":"095610","company_name":"TES","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":20200.0,"evidence_available_at_that_date":"Same early DRAM equipment investment resumption setup, mapped to TES front-end equipment exposure; TES official financial page later shows FY2024 operating profit recovery from FY2023 loss.","evidence_source":"Chosun_DRAM_expansion_2024_02_29 + TES_official_financial","evidence_url":"https://www.chosun.com/english/industry-en/2024/02/29/SGS2LHTAAJAIHBDRMMJLBHGSFA/","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":44.31,"MFE_90D_pct":62.87,"MFE_180D_pct":62.87,"MAE_30D_pct":-6.68,"MAE_90D_pct":-6.68,"MAE_180D_pct":-30.3,"peak_date":"2024-04-17","peak_price":32900.0,"drawdown_after_peak_pct":-57.2,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"early_stage2_positive_but_green_block_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|095610|Stage2-Actionable|2024-03-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_095610_20240229_STAGE2A","trigger_id":"C10_095610_20240229_STAGE2A_DRAM_RESUME","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":40,"margin_bridge_score":30,"revision_score":25,"relative_strength_score":75,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":30,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":40,"margin_bridge_score":30,"revision_score":25,"relative_strength_score":75,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"allow early Stage2-Actionable, but add quick 4B watch if no company-specific order appears after the first MFE burst.","MFE_90D_pct":62.87,"MAE_90D_pct":-6.68,"score_return_alignment_label":"early_stage2_positive_but_green_block_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10_095610_20240424_STAGE4B","symbol":"095610","company_name":"TES","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same symbol as early positive but new trigger family: later customer-capex headline after local supplier peak","independent_evidence_weight":0.5,"score_price_alignment":"late_generic_capex_false_positive","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Late customer capex headline without TES-specific order conversion was a bad entry: MFE180 6.51% versus MAE180 -49.85%."}
{"row_type":"trigger","trigger_id":"C10_095610_20240424_STAGE4B_ORDER_CONVERSION_MISSING","case_id":"C10_095610_20240424_STAGE4B","symbol":"095610","company_name":"TES","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-04-24","entry_date":"2024-04-25","entry_price":26100.0,"evidence_available_at_that_date":"SK Hynix full memory recovery and M15X/HBM capex headlines were strong at customer level, but no TES-specific order conversion evidence was present at this later point after the early TES move.","evidence_source":"Reuters_SKHynix_recovery_2024_04_25 + Reuters_SKHynix_M15X_2024_04_24","evidence_url":"https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.79,"MFE_90D_pct":6.51,"MFE_180D_pct":6.51,"MAE_30D_pct":-15.33,"MAE_90D_pct":-38.7,"MAE_180D_pct":-49.85,"peak_date":"2024-06-27","peak_price":27800.0,"drawdown_after_peak_pct":-52.91,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.46,"four_b_full_window_peak_proximity":0.46,"trigger_outcome_label":"late_generic_capex_false_positive","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|095610|Stage4B|2024-04-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same symbol as early positive but new trigger family: later customer-capex headline after local supplier peak","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_095610_20240424_STAGE4B","trigger_id":"C10_095610_20240424_STAGE4B_ORDER_CONVERSION_MISSING","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":70,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"generic customer capex is not enough after supplier stock already rerated; require TES order/revenue conversion or downgrade to local 4B watch.","MFE_90D_pct":6.51,"MAE_90D_pct":-38.7,"score_return_alignment_label":"late_generic_capex_false_positive","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C10_319660_20240424_STAGE2_FALSE","symbol":"319660","company_name":"PSK","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer_capex_beta_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Generic capex beta delivered MFE90 29.90% but MAE180 -48.34%; current profile would over-count customer capex without supplier conversion."}
{"row_type":"trigger","trigger_id":"C10_319660_20240424_STAGE2_CUSTOMER_CAPEX_FALSE","case_id":"C10_319660_20240424_STAGE2_FALSE","symbol":"319660","company_name":"PSK","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-04-24","entry_date":"2024-04-25","entry_price":30100.0,"evidence_available_at_that_date":"SK Hynix recovery/capex evidence supported a broad equipment-cycle narrative, but PSK-specific 2024 order/revenue conversion had not yet been confirmed at trigger date.","evidence_source":"Reuters_SKHynix_recovery_2024_04_25 + Reuters_SKHynix_M15X_2024_04_24","evidence_url":"https://www.reuters.com/technology/sk-hynix-invest-386-bln-dram-chip-production-base-south-korea-2024-04-24/","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.45,"MFE_90D_pct":29.9,"MFE_180D_pct":29.9,"MAE_30D_pct":-8.64,"MAE_90D_pct":-24.58,"MAE_180D_pct":-48.34,"peak_date":"2024-07-11","peak_price":39100.0,"drawdown_after_peak_pct":-60.23,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"customer_capex_beta_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|319660|Stage2|2024-04-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_319660_20240424_STAGE2_FALSE","trigger_id":"C10_319660_20240424_STAGE2_CUSTOMER_CAPEX_FALSE","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":15,"relative_strength_score":60,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":15,"relative_strength_score":60,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":50,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":60,"stage_label_after":"Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"subtract Actionable status until PSK revenue/order evidence confirms the customer capex route.","MFE_90D_pct":29.9,"MAE_90D_pct":-24.58,"score_return_alignment_label":"customer_capex_beta_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10_036930_20240719_STAGE2_HMAE","symbol":"036930","company_name":"Jusung Engineering","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"delayed_positive_high_mae","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"This was not a clean Actionable entry: 30D MAE -29.79% and 90D MAE -30.11% came before 180D MFE 37.56%."}
{"row_type":"trigger","trigger_id":"C10_036930_20240719_STAGE2_ADV_PROCESS_FRONTEND","case_id":"C10_036930_20240719_STAGE2_HMAE","symbol":"036930","company_name":"Jusung Engineering","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-07-19","entry_date":"2024-07-19","entry_price":31550.0,"evidence_available_at_that_date":"Asia Business/DS noted advanced-process equipment investment justification from 2H24/2025; Jusung official page maps its ALD equipment directly to ultra-fine DRAM and 200+ layer 3D NAND processes.","evidence_source":"AsiaBusiness_advanced_process_2024_07_19 + Jusung_official_semiconductor","evidence_url":"https://www.asiae.co.kr/en/article/2024071907585690985","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["execution_risk_score"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.43,"MFE_90D_pct":7.92,"MFE_180D_pct":37.56,"MAE_30D_pct":-29.79,"MAE_90D_pct":-30.11,"MAE_180D_pct":-30.11,"peak_date":"2025-03-21","peak_price":43400.0,"drawdown_after_peak_pct":-22.58,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"delayed_positive_high_mae","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|036930|Stage2|2024-07-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_036930_20240719_STAGE2_HMAE","trigger_id":"C10_036930_20240719_STAGE2_ADV_PROCESS_FRONTEND","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":15,"revision_score":15,"relative_strength_score":45,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":15,"revision_score":15,"relative_strength_score":45,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":64,"stage_label_after":"Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"front-end investment justification is Stage2 only until explicit order/revenue timing reduces high-MAE risk.","MFE_90D_pct":7.92,"MAE_90D_pct":-30.11,"score_return_alignment_label":"delayed_positive_high_mae","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"C10_166090_20240626_STAGE4B","symbol":"166090","company_name":"Hana Materials","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"propagation_without_order_conversion_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Excellent 4B guard example: entry was near local top; MFE180 8.45% versus MAE180 -65.81%."}
{"row_type":"trigger","trigger_id":"C10_166090_20240626_STAGE4B_UTILIZATION_PROPAGATION","case_id":"C10_166090_20240626_STAGE4B","symbol":"166090","company_name":"Hana Materials","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":63900.0,"evidence_available_at_that_date":"MK reported Hana Materials rising on memory utilization-rate recovery. This is a supplier-propagation headline, not direct equipment order conversion.","evidence_source":"MK_Hana_memory_utilization_2024_06_26","evidence_url":"https://www.mk.co.kr/en/stock/11051593","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.45,"MFE_90D_pct":8.45,"MFE_180D_pct":8.45,"MAE_30D_pct":-38.73,"MAE_90D_pct":-56.65,"MAE_180D_pct":-65.81,"peak_date":"2024-07-02","peak_price":69300.0,"drawdown_after_peak_pct":-68.47,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"propagation_without_order_conversion_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|166090|Stage4B|2024-06-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_166090_20240626_STAGE4B","trigger_id":"C10_166090_20240626_STAGE4B_UTILIZATION_PROPAGATION","symbol":"166090","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":80,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":80,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":65,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":90,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":49,"stage_label_after":"Stage4B","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"memory utilization-rate propagation without company-specific order conversion should not promote C10 Stage2; route to local 4B watch.","MFE_90D_pct":8.45,"MAE_90D_pct":-56.65,"score_return_alignment_label":"propagation_without_order_conversion_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10_319660_20250225_STAGE2A","symbol":"319660","company_name":"PSK","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same symbol as 2024 failed capex-beta case but new trigger family: supplier revenue/test-equipment confirmation","independent_evidence_weight":0.5,"score_price_alignment":"confirmed_conversion_reopened_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Actual revenue confirmation changed the sign: 180D MFE 100.97% with MAE180 -20.97%, after the 2024 generic capex entry failed."}
{"row_type":"trigger","trigger_id":"C10_319660_20250225_STAGE2A_REVENUE_CONFIRMATION","case_id":"C10_319660_20250225_STAGE2A","symbol":"319660","company_name":"PSK","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-25","entry_date":"2025-02-26","entry_price":20600.0,"evidence_available_at_that_date":"Counterpoint reported test equipment maker revenue growth in 2024 on AI/HBM/DRAM demand; PSK official financials later show 2024 sales and operating profit recovery from 2023.","evidence_source":"Counterpoint_test_equipment_2025_02_25 + PSK_official_financial","evidence_url":"https://counterpointresearch.com/en/insights/semiconductor-test-equipment-makers-revenue-grows-18-yoy-in-2024-on-strong-ai-compute-hbm-dram-demand","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2025.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.44,"MFE_90D_pct":10.44,"MFE_180D_pct":100.97,"MAE_30D_pct":-20.97,"MAE_90D_pct":-20.97,"MAE_180D_pct":-20.97,"peak_date":"2025-11-06","peak_price":41400.0,"drawdown_after_peak_pct":-23.43,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"confirmed_conversion_reopened_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|319660|Stage2-Actionable|2025-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same symbol as 2024 failed capex-beta case but new trigger family: supplier revenue/test-equipment confirmation","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow","case_id":"C10_319660_20250225_STAGE2A","trigger_id":"C10_319660_20250225_STAGE2A_REVENUE_CONFIRMATION","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":45,"revision_score":35,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":40,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":35,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":40,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"supplier revenue/order conversion evidence can reopen Stage2-Actionable even after prior customer-capex false positive.","MFE_90D_pct":10.44,"MAE_90D_pct":-20.97,"score_return_alignment_label":"confirmed_conversion_reopened_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"residual_contribution","round":"R2","loop":"192","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":2,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","earlier_thesis_break_watch","stage3_green_not_loosened_by_v12"],"residual_error_types_found":["generic_customer_capex_false_positive","utilization_propagation_false_positive","late_confirmation_missed_structural","high_mae_delayed_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<pre>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<pre>/<ticker>.json.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
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
completed_round: R2
completed_loop: 192
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement — C10 recovery-cycle false positives and order conversion confirmation
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_4C_DIRECT_THESIS_BREAK_REPAIR
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

## 28. Source Notes

Control sources:

- MAIN execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Daikisong/stock-web/refs/heads/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Daikisong/stock-web/main/atlas/schema.json

Evidence sources are listed in Section 9. This Markdown is a historical calibration artifact, not a current stock recommendation, live scan, auto-trading instruction, or production scoring patch.
