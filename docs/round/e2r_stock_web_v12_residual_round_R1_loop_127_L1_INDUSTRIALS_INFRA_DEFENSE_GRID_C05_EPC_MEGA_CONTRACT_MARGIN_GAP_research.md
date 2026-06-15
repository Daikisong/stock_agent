# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_127_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selected_round: R1
selected_loop: 127
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 / under_50_rows_static_ledger / C05 rows 47 need_to_50 3 before this local loop
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 8 new independent cases, 3 counterexamples, and 6 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP. It separates headline EPC order size from the harder bridge: cost rate, margin durability, working capital, trust-break cleanup and cash conversion.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
already_applied_axes_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
```

The current profile already blocks price-only blowoff and routes hard thesis breaks to 4C. The residual C05 error is more surgical: EPC contract amount, customer name and overseas order headlines can still look like rerating evidence even while cost-overrun, PF/residential drag, working-capital pressure or trust-break scars keep the stock from paying for that backlog.

## 2. Round / Large Sector / Canonical Archetype Scope

|field|value|
|---|---|
|round|R1|
|large_sector_id|L1_INDUSTRIALS_INFRA_DEFENSE_GRID|
|canonical_archetype_id|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|
|fine_archetype_id|EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK|
|round_sector_consistency|pass|
|R1_mapping_reason|C01~C05 map to R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID|

## 3. Previous Coverage / Duplicate Avoidance Check

Static No-Repeat Index state: C05 has 47 representative rows and needs 3 rows to reach the 50-row practical calibration zone. In this interactive run, Priority-0 C02/C09/C14/C10/C06/C07/C11/C01/C28 plus Priority-1 C12 were already emitted, so C05 is the next non-duplicate Priority-1 gap.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicates_in_this_file = 0
new_independent_case_ratio = 1.00 among calibration-usable trigger rows
reuse_policy = repeated symbols allowed only where trigger family and entry date differ; all representative rows have independent_evidence_weight=1.0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "source_name": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "caveat": "raw/unadjusted OHLC; share-count stable inside each representative 180D window"}
```

Formula used: `MFE_ND_pct = (max(high from entry_date through N trading rows) / entry_price - 1) * 100`; `MAE_ND_pct = (min(low from entry_date through N trading rows) / entry_price - 1) * 100`. Entry price is the stock-web tradable close on `entry_date`.

## 5. Historical Eligibility Gate

|symbol|entry_date|entry_price|forward_window_trading_days|shares_nunique_180|corporate_action_window_status|calibration_usable|
|---|---|---:|---:|---:|---|---|
|028050|2024-04-03|25300.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|006360|2024-04-03|15630.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|000720|2023-06-26|40800.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|006360|2023-07-06|14520.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|028050|2025-01-23|17440.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|006360|2025-02-05|17300.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|047040|2025-04-29|3520.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|375500|2025-02-06|35150.0|180|1|clean_180D_window_by_local_tradable_rows_share_count_constant|True|

## 6. Canonical Archetype Compression Map

|symbol|fine_archetype_id|compressed_to|role|stage2_key|risk_or_unlock_key|
|---|---|---|---|---|---|
|028050|fadhili_mega_epc_headline_without_near_term_margin_cash_unlock|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|counterexample|public_event_or_disclosure;backlog_or_delivery_visibility;customer_or_order_quality|margin_or_backlog_slowdown;positioning_overheat|
|006360|fadhili_sulfur_recovery_epc_with_recovery_option_after_geondan_reset|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|positive|public_event_or_disclosure;customer_or_order_quality;backlog_or_delivery_visibility|execution_risk_score;margin_or_backlog_slowdown|
|000720|amiral_krw6_5tn_turnkey_epc_headline_margin_gap|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|counterexample|public_event_or_disclosure;customer_or_order_quality;backlog_or_delivery_visibility|valuation_blowoff;margin_or_backlog_slowdown|
|006360|geondan_reconstruction_trust_break_cost_overrun_hard4c|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|counterexample|blocked_or_not_applicable|accounting_or_trust_break;thesis_evidence_broken|
|028050|profit_target_beat_backlog_cost_improvement_margin_bridge|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|positive|public_event_or_disclosure;backlog_or_delivery_visibility;early_revision_signal|confirmed_revision;margin_bridge;financial_visibility;multiple_public_sources|
|006360|post_geondan_profit_turnaround_order_backlog_margin_repair|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|positive|public_event_or_disclosure;early_revision_signal;backlog_or_delivery_visibility|positioning_overheat|
|047040|q1_profit_order_backlog_framework_agreement_overseas_epc_pipeline|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|positive|public_event_or_disclosure;backlog_or_delivery_visibility;early_revision_signal;customer_or_order_quality|financial_visibility|
|375500|selected_order_strategy_cost_rate_adjustment_margin_repair|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|positive|public_event_or_disclosure;early_revision_signal;backlog_or_delivery_visibility|margin_or_backlog_slowdown|

## 7. Case Selection Summary

|symbol|company_name|case_type|positive_or_counterexample|calibration_usable|current_profile_verdict|score_price_alignment|
|---|---|---|---|---|---|---|
|028050|Samsung E&A|failed_rerating|counterexample|True|current_profile_false_positive|counterexample_contract_size_not_enough_without_margin_cash_timing|
|006360|GS E&C|stage2_promote_candidate|positive|True|current_profile_correct|positive_stage2_actionable_not_green|
|000720|Hyundai E&C|failed_rerating|counterexample|True|current_profile_false_positive|counterexample_mega_order_does_not_override_pf_and_margin_discount|
|006360|GS E&C|4C_success|counterexample|True|current_profile_correct|4C_guardrail_not_short_signal_but_blocks_positive_stage|
|028050|Samsung E&A|structural_success|positive|True|current_profile_missed_structural|positive_margin_cash_bridge_stronger_than_contract_headline|
|006360|GS E&C|structural_success|positive|True|current_profile_too_late|positive_reopen_after_4c_requires_profit_and_cost_reset_evidence|
|047040|Daewoo E&C|structural_success|positive|True|current_profile_too_late|positive_stage2_actionable_with_clean_MAE|
|375500|DL E&C|structural_success|positive|True|current_profile_too_late|positive_when_bad_debt_cost_rate_is_explicitly_measured_and_order_quality_is_selected|

## 8. Positive vs Counterexample Balance

|metric|value|
|---|---:|
|calibration_usable_trigger_count|8|
|representative_trigger_count|8|
|positive_case_count|5|
|counterexample_count|3|
|stage4b_overlay_count|3|
|stage4c_case_count|1|
|current_profile_error_count|6|

## 9. Evidence Source Map

|symbol|company_name|trigger_date|evidence_summary|evidence_source|
|---|---|---|---|---|
|028050|Samsung E&A|2024-04-03|SAMSUNG E&A won Fadhili Gas Increment Program Packages #1 and #4; the contract was a large EPC award but the 180D path showed a deep drawdown before later 2025 profit proof arrived.|https://www.samsungena.com/en/newsroom/news/view?idx=15577; https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/|
|006360|GS E&C|2024-04-03|GS E&C won Fadhili Gas Increment Program Package 2 sulfur recovery facilities; the order supplied plant backlog after a 2023 loss/reset period.|https://www.asiae.co.kr/en/article/2024040309065572598; https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/|
|000720|Hyundai E&C|2023-06-26|Hyundai E&C signed a USD 5bn / KRW 6.5tn Saudi Amiral petrochemical EPC contract covering Packages 1 and 4.|https://www.korea.net/NewsFocus/Business/view?articleId=234605; https://www.asiae.co.kr/en/article/2023062516232823346; https://koreajoongangdaily.joins.com/2023/06/25/business/industry/Hyundai-EC-5-billion/20230625165454180.html|
|006360|GS E&C|2023-07-06|GS E&C decided to rebuild 17 apartment buildings after the Incheon Geomdan parking-lot collapse, with analysts estimating up to KRW 1tn of cost; later reports showed large reconstruction costs and operating loss.|https://en.yna.co.kr/view/AEN20230706002200320; https://www.asiae.co.kr/en/article/2024013111305931564; https://www.kedglobal.com/construction/newsView/ked202307260020|
|028050|Samsung E&A|2025-01-23|SAMSUNG E&A reported 2024 operating profit above target, Q4 operating profit growth, and 2024 order/backlog figures; management attributed performance to profitability and operational efficiency.|https://www.samsungena.com/en/newsroom/news/view?idx=15673; https://en.yna.co.kr/view/AEN20250123007151320; https://en.yna.co.kr/view/AEN20250117001551320|
|006360|GS E&C|2025-02-05|GS E&C shifted to 2024 net profit after a 2023 loss, and reports described the turnaround after the Geomdan reconstruction cost shock.|https://en.yna.co.kr/view/AEN20250205002400320; https://en.topdaily.kr/articles/4578; https://www.mk.co.kr/en/realestate/11232869|
|047040|Daewoo E&C|2025-04-29|Daewoo E&C Q1 2025 profit increased, new orders rose, order backlog stood at KRW45tn, and management cited the intent to secure large overseas contracts after a fertilizer-plant framework agreement.|https://en.yna.co.kr/view/AEN20250429001851320; https://www.theinvestor.co.kr/article/10495942|
|375500|DL E&C|2025-02-06|DL E&C announced 2024 results: operating profit fell due to bad debts and cost-rate adjustments, but the release explicitly tied order strategy to high-value projects that guarantee profitability.|https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword=; https://www.dlenc.co.kr/eng/ir/financial/Highlight.do|

## 10. Price Data Source Map

|symbol|price_shard_path|profile_path|price_basis|entry_date|
|---|---|---|---|---|
|028050|atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv|atlas/symbol_profiles/028/028050.json|tradable_raw|2024-04-03|
|006360|atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv|atlas/symbol_profiles/006/006360.json|tradable_raw|2024-04-03|
|000720|atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv|atlas/symbol_profiles/000/000720.json|tradable_raw|2023-06-26|
|006360|atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv|atlas/symbol_profiles/006/006360.json|tradable_raw|2023-07-06|
|028050|atlas/ohlcv_tradable_by_symbol_year/028/028050/2025.csv|atlas/symbol_profiles/028/028050.json|tradable_raw|2025-01-23|
|006360|atlas/ohlcv_tradable_by_symbol_year/006/006360/2025.csv|atlas/symbol_profiles/006/006360.json|tradable_raw|2025-02-05|
|047040|atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv|atlas/symbol_profiles/047/047040.json|tradable_raw|2025-04-29|
|375500|atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv|atlas/symbol_profiles/375/375500.json|tradable_raw|2025-02-06|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|case_polarity|current_profile_verdict|aggregate_group_role|
|---|---|---|---|---|---|---|
|TRG_R1L127_C05_028050_20240403_01|028050|Stage2|2024-04-03|counterexample|current_profile_false_positive|representative|
|TRG_R1L127_C05_006360_20240403_02|006360|Stage2-Actionable|2024-04-03|positive|current_profile_correct|representative|
|TRG_R1L127_C05_000720_20230626_03|000720|Stage2|2023-06-26|counterexample|current_profile_false_positive|representative|
|TRG_R1L127_C05_006360_20230706_04|006360|Stage4C|2023-07-06|counterexample|current_profile_correct|representative|
|TRG_R1L127_C05_028050_20250123_05|028050|Stage3-Yellow|2025-01-23|positive|current_profile_missed_structural|representative|
|TRG_R1L127_C05_006360_20250205_06|006360|Stage3-Yellow|2025-02-05|positive|current_profile_too_late|representative|
|TRG_R1L127_C05_047040_20250429_07|047040|Stage2-Actionable|2025-04-29|positive|current_profile_too_late|representative|
|TRG_R1L127_C05_375500_20250206_08|375500|Stage2-Actionable|2025-02-06|positive|current_profile_too_late|representative|

## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|trough_date|trough_price|drawdown_after_peak_pct|
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
|028050|2024-04-03|25300.0|6.72|-5.34|15.81|-14.62|15.81|-35.57|2024-07-30|29300.0|2024-12-09|16300.0|-44.37|
|006360|2024-04-03|15630.0|6.97|-10.17|30.52|-10.17|39.16|-10.17|2024-08-27|21750.0|2024-11-13|16860.0|-22.48|
|000720|2023-06-26|40800.0|8.82|-15.32|8.82|-18.5|8.82|-23.53|2023-06-26|44400.0|2024-01-25|31200.0|-29.73|
|006360|2023-07-06|14520.0|10.12|-7.92|10.12|-12.74|19.83|-12.74|2023-11-23|17400.0|2024-01-23|13860.0|-20.34|
|028050|2025-01-23|17440.0|10.38|-6.08|33.6|-6.08|75.75|-6.08|2025-10-23|30650.0|2025-10-23|28000.0|-8.65|
|006360|2025-02-05|17300.0|14.45|-0.29|43.64|-12.2|43.64|-12.2|2025-06-12|24850.0|2025-09-03|17790.0|-28.41|
|047040|2025-04-29|3520.0|36.51|-3.12|36.51|-3.12|63.64|-5.68|2026-01-23|5760.0|2026-01-23|5020.0|-12.85|
|375500|2025-02-06|35150.0|33.57|-11.66|59.89|-11.66|69.84|-11.66|2025-06-26|59700.0|2025-10-20|40050.0|-32.91|

## 13. Current Calibrated Profile Stress Test

|symbol|actual_path_label|current_profile_verdict|detail|
|---|---|---|---|
|028050|mega_epc_headline_positive_but_margin_cash_bridge_missing_deep_180D_MAE|current_profile_false_positive|As-of award evidence supports Stage2-watch only. It should not unlock Yellow until execution margin and cash conversion are visible.|
|006360|plant_epc_order_after_loss_reset_positive_but_yellow_needs_margin_confirmation|current_profile_correct|Unlike pure price blowoff, the contract had a named customer, package scope and duration. Still, 2023 trust/margin scars keep it out of Green at trigger date.|
|000720|largest_order_headline_failed_180D_rerating_due_no_margin_cash_bridge|current_profile_false_positive|The headline was large and credible, but the first 180 trading days did not pay for Stage2-Actionable/Yellow without cost, working-capital and margin evidence.|
|006360|hard4c_trust_break_blocks_future_contract_headline_promotion_until_cleanup|current_profile_correct|The 4C value is not that MAE explodes immediately after entry; it tells the agent not to let later contract headlines promote Stage3 before cleanup evidence.|
|028050|profitability_efficiency_bridge_reopens_C05_after_2024_award_drawdown|current_profile_missed_structural|This is the paired positive control for Samsung E&A: the same award complex became useful only after profitability/backlog proof, not at headline date.|
|006360|cleanup_plus_profit_turn_positive_after_hard4c_decay|current_profile_too_late|C05 needs a decay/reopen lane: after a trust/cost 4C, later contract and profit-turn evidence can restore Stage2-Actionable/Yellow.|
|047040|order_backlog_plus_profit_visibility_positive_but_green_waits_contract_finalization|current_profile_too_late|The framework agreement is not full Green, but the Q1 profit/backlog bridge deserved earlier Actionable credit than a pure order headline.|
|375500|cost_rate_disclosure_and_selected_order_strategy_positive_after_margin_gap_acknowledgement|current_profile_too_late|This is not a mega-order headline. It is a C05 repair signal: margin damage is named, bounded and paired with profitability-focused order selection.|

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green trigger is emitted. The useful comparison is Stage2/Stage2-Actionable at award date versus Stage3-Yellow after margin/profit/backlog confirmation. The Samsung E&A pair is the cleanest internal control: the same company/contract complex produced only `MFE_180D_pct=15.81` with `MAE_180D_pct=-35.57` at the 2024 Fadhili headline, then `MFE_180D_pct=75.75` with `MAE_180D_pct=-6.08` after 2024 profit/backlog proof. That is exactly the bridge C05 should demand.

```text
green_lateness_ratio = not_applicable_no_confirmed_Stage3_Green_trigger
Yellow gate implication = contract amount + named customer is not enough; require margin/cost/cash or bounded cleanup evidence
```

## 15. 4B Local vs Full-window Timing Audit

C05 4B must remain an overlay, not a generic sell label. The bad award-date rows are not price-only local peaks; they are evidence-risk rows where cost, PF/residential trust, execution risk, or absent cash bridge should cap promotion. GS E&C 2023 is the hard 4C anchor, while 2025 GS E&C is the decay/reopen anchor after profit restoration.

|symbol|four_b_evidence_type|four_b_timing_verdict|
|---|---|---|
|028050|margin_or_backlog_slowdown / positioning_overheat|award_date_not_full_4B_but_blocks_yellow_until_profit_bridge|
|006360|legal_or_regulatory_block / margin_or_backlog_slowdown|2023_hard4c_then_2025_decay_reopen|
|000720|valuation_blowoff / margin_or_backlog_slowdown|mega_order_stage2_watch_not_yellow|
|047040|none|positive_stage2_actionable_watch|
|375500|margin_or_backlog_slowdown|bad_debt_cost_rate_named_and_bounded_so_positive_repair_watch|

## 16. 4C Protection Audit

|symbol|four_c_protection_label|interpretation|
|---|---|---|
|006360|hard_4c_success|Trust/cost break from Geomdan should block future C05 positive promotion until cleanup evidence exists.|
|028050|thesis_break_watch_only|Contract headline failed 180D path but later profit proof means not permanent 4C.|
|000720|thesis_break_watch_only|Large order did not rerate within 180D; margin/PF bridge missing, but no hard contract cancellation.|
|047040|false_break|Order backlog plus Q1 profit created clean positive asymmetry.|
|375500|false_break|Bad debt/cost-rate issue was explicitly quantified and paired with selected high-value order strategy.|

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L1_EPC_CONTRACT_SIZE_REQUIRES_MARGIN_CASH_AND_TRUST_REPAIR_GATE
rule_scope = sector_specific
proposal_type = shadow_only
rule = In L1 EPC/construction, overseas mega contract size can support Stage2-watch. Stage2-Actionable or Stage3-Yellow requires at least one validated bridge: cost-rate/margin repair, profit target beat, backlog-to-revenue conversion, working-capital/cash visibility, or explicit trust-break cleanup after prior 4C.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C05_EPC_ORDER_TO_MARGIN_CASH_BRIDGE_GATE
new_axis_proposed = C05_EPC_ORDER_TO_MARGIN_CASH_BRIDGE_GATE
existing_axis_strengthened = stage2_required_bridge | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
```

C05 should score like a bridge test, not like a press-release meter. Contract amount is the door; cost/margin/cash/trust repair is the key. Without the key, the door opens into a corridor that often bends down before the 180D mark.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current|Current profile with generic stage2 bridge and 4B/4C guards. It still treats mega EPC contract + named customer too generously when margin/cash bridge is not yet available.|8|all_representative_triggers|29.86|-11.14|42.06|-14.7|0.25|3|0|mixed_contract_size_false_positive_residual|
|P0b_e2r_2_0_baseline_reference|rollback_reference|Older profile would have over-credited contract amount and relative-strength reactions, while lacking explicit construction margin/cost-trust repair gates.|8|all_representative_triggers|29.86|-11.14|42.06|-14.7|0.5|1|0|weaker_than_current_for_counterexamples|
|P1_L1_EPC_margin_cash_bridge_sector_shadow|sector_specific|Within L1 EPC/infra, Stage2-Actionable requires not only customer/order size but also one of cost-rate repair, profit bridge, or working-capital/cash visibility.|8|positive_bridge_rows_only_for_actionable|40.83|-8.65|58.41|-9.16|0.12|1|0|better_positive_selection|
|P2_C05_contract_to_margin_cash_canonical_shadow|canonical_archetype_specific|For C05, mega EPC order alone is Stage2-watch. Yellow requires margin/cost/revision/cash bridge or bounded cleanup after prior trust break.|8|C05_bridge_rows|40.83|-8.65|58.41|-9.16|0.0|0|0|best_explains_samsung_pair_and_gs_decay_reopen|
|P3_C05_counterexample_guard_profile|counterexample_guard|Blocks Stage2-Actionable/Yellow for mega awards if PF/residential trust break, cost overrun, margin gap or working-capital strain remains unresolved.|8|blocked_counterexamples_and_4C_routes|11.58|-15.29|14.82|-23.95|0.0|2|0|prevents_mega_contract_headline_false_positive|

## 20. Score-Return Alignment Matrix

|symbol|trigger_type|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|score_return_alignment_label|
|---|---|---:|---|---:|---|---|
|028050|Stage2|73|Stage2-Actionable|58|Stage2|counterexample_contract_size_not_enough_without_margin_cash_timing|
|006360|Stage2-Actionable|76|Stage3-Yellow|80|Stage3-Yellow|positive_stage2_actionable_not_green|
|000720|Stage2|73|Stage2-Actionable|58|Stage2|counterexample_mega_order_does_not_override_pf_and_margin_discount|
|006360|Stage4C|42|Stage4C|35|Stage4C|4C_guardrail_not_short_signal_but_blocks_positive_stage|
|028050|Stage3-Yellow|82|Stage3-Yellow|84|Stage3-Yellow|positive_margin_cash_bridge_stronger_than_contract_headline|
|006360|Stage3-Yellow|82|Stage3-Yellow|84|Stage3-Yellow|positive_reopen_after_4c_requires_profit_and_cost_reset_evidence|
|047040|Stage2-Actionable|76|Stage3-Yellow|80|Stage3-Yellow|positive_stage2_actionable_with_clean_MAE|
|375500|Stage2-Actionable|76|Stage3-Yellow|80|Stage3-Yellow|positive_when_bad_debt_cost_rate_is_explicitly_measured_and_order_quality_is_selected|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L1_INDUSTRIALS_INFRA_DEFENSE_GRID|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK|5|3|3|1|8|0|8|8|6|L1_EPC_CONTRACT_SIZE_REQUIRES_MARGIN_CASH_AND_TRUST_REPAIR_GATE|C05_EPC_ORDER_TO_MARGIN_CASH_BRIDGE_GATE|C05 static rows 47 + 8 usable local rows = 55; need_to_50 becomes 0|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [mega_contract_headline_false_positive, margin_cash_bridge_missing, trust_break_decay_reopen_needed, hard4c_blocks_future_headline_promotion]
new_axis_proposed: C05_EPC_ORDER_TO_MARGIN_CASH_BRIDGE_GATE
existing_axis_strengthened: stage2_required_bridge | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min | stage3_green_total_min | price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L1_EPC_CONTRACT_SIZE_REQUIRES_MARGIN_CASH_AND_TRUST_REPAIR_GATE
canonical_archetype_rule_candidate: C05_EPC_ORDER_TO_MARGIN_CASH_BRIDGE_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web tradable close entries, 30/90/180D MFE/MAE, clean local share-count windows, canonical trigger labels, round/sector mapping, positive/counterexample balance. Not validated: production scoring code, live candidate status, post-manifest prices, adjusted OHLC, or any brokerage action.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C05_EPC_ORDER_TO_MARGIN_CASH_BRIDGE_GATE,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"contract headline must be bridged by margin/cost/cash/trust repair evidence","counterexamples show weak 180D path without bridge; positives improve after profit/backlog/cost repair proof","TRG_R1L127_C05_028050_20240403_01|TRG_R1L127_C05_006360_20240403_02|TRG_R1L127_C05_000720_20230626_03|TRG_R1L127_C05_006360_20230706_04|TRG_R1L127_C05_028050_20250123_05|TRG_R1L127_C05_006360_20250205_06|TRG_R1L127_C05_047040_20250429_07|TRG_R1L127_C05_375500_20250206_08",8,8,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L1_EPC_CONTRACT_SIZE_REQUIRES_MARGIN_CASH_AND_TRUST_REPAIR_GATE,sector_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"L1 EPC awards need execution-quality gate","reduces false positives in 028050/000720 and preserves 006360/047040/375500 positives","TRG_R1L127_C05_028050_20240403_01|TRG_R1L127_C05_006360_20240403_02|TRG_R1L127_C05_000720_20230626_03|TRG_R1L127_C05_006360_20230706_04|TRG_R1L127_C05_028050_20250123_05|TRG_R1L127_C05_006360_20250205_06|TRG_R1L127_C05_047040_20250429_07|TRG_R1L127_C05_375500_20250206_08",8,8,3,medium,sector_shadow_only,"not production; apply only through later batch promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; share-count stable inside each representative 180D window"}
{"row_type":"case","case_id":"CASE_R1L127_C05_028050_20240403_FADHILI_CONTRACT_MARGIN_GAP","symbol":"028050","company_name":"Samsung E&A","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R1L127_C05_028050_20240403_01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_contract_size_not_enough_without_margin_cash_timing","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"As-of award evidence supports Stage2-watch only. It should not unlock Yellow until execution margin and cash conversion are visible."}
{"row_type":"case","case_id":"CASE_R1L127_C05_006360_20240403_FADHILI_SRU_TURNAROUND_WATCH","symbol":"006360","company_name":"GS E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"TRG_R1L127_C05_006360_20240403_02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_stage2_actionable_not_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Unlike pure price blowoff, the contract had a named customer, package scope and duration. Still, 2023 trust/margin scars keep it out of Green at trigger date."}
{"row_type":"case","case_id":"CASE_R1L127_C05_000720_20230626_AMIRAL_MEGA_CONTRACT_GAP","symbol":"000720","company_name":"Hyundai E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R1L127_C05_000720_20230626_03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_mega_order_does_not_override_pf_and_margin_discount","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The headline was large and credible, but the first 180 trading days did not pay for Stage2-Actionable/Yellow without cost, working-capital and margin evidence."}
{"row_type":"case","case_id":"CASE_R1L127_C05_006360_20230706_GEOMDAN_RECONSTRUCTION_4C","symbol":"006360","company_name":"GS E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R1L127_C05_006360_20230706_04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C_guardrail_not_short_signal_but_blocks_positive_stage","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"The 4C value is not that MAE explodes immediately after entry; it tells the agent not to let later contract headlines promote Stage3 before cleanup evidence."}
{"row_type":"case","case_id":"CASE_R1L127_C05_028050_20250123_PROFIT_BACKLOG_MARGIN_BRIDGE","symbol":"028050","company_name":"Samsung E&A","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R1L127_C05_028050_20250123_05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_margin_cash_bridge_stronger_than_contract_headline","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"This is the paired positive control for Samsung E&A: the same award complex became useful only after profitability/backlog proof, not at headline date."}
{"row_type":"case","case_id":"CASE_R1L127_C05_006360_20250205_PROFIT_TURNAROUND_AFTER_RESET","symbol":"006360","company_name":"GS E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R1L127_C05_006360_20250205_06","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_reopen_after_4c_requires_profit_and_cost_reset_evidence","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C05 needs a decay/reopen lane: after a trust/cost 4C, later contract and profit-turn evidence can restore Stage2-Actionable/Yellow."}
{"row_type":"case","case_id":"CASE_R1L127_C05_047040_20250429_ORDER_BACKLOG_Q1_PROFIT","symbol":"047040","company_name":"Daewoo E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R1L127_C05_047040_20250429_07","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_stage2_actionable_with_clean_MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"The framework agreement is not full Green, but the Q1 profit/backlog bridge deserved earlier Actionable credit than a pure order headline."}
{"row_type":"case","case_id":"CASE_R1L127_C05_375500_20250206_SELECTED_ORDER_STRATEGY_COST_RATE","symbol":"375500","company_name":"DL E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R1L127_C05_375500_20250206_08","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_when_bad_debt_cost_rate_is_explicitly_measured_and_order_quality_is_selected","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"This is not a mega-order headline. It is a C05 repair signal: margin damage is named, bounded and paired with profitability-focused order selection."}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_028050_20240403_01","case_id":"CASE_R1L127_C05_028050_20240403_FADHILI_CONTRACT_MARGIN_GAP","symbol":"028050","company_name":"Samsung E&A","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":25300.0,"evidence_available_at_that_date":"SAMSUNG E&A won Fadhili Gas Increment Program Packages #1 and #4; the contract was a large EPC award but the 180D path showed a deep drawdown before later 2025 profit proof arrived.","evidence_source":"https://www.samsungena.com/en/newsroom/news/view?idx=15577; https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.72,"MFE_90D_pct":15.81,"MFE_180D_pct":15.81,"MFE_1Y_pct":15.81,"MFE_2Y_pct":null,"MAE_30D_pct":-5.34,"MAE_90D_pct":-14.62,"MAE_180D_pct":-35.57,"MAE_1Y_pct":-35.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":29300.0,"drawdown_after_peak_pct":-44.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"mega_epc_headline_positive_but_margin_cash_bridge_missing_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_028050_20240403","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_006360_20240403_02","case_id":"CASE_R1L127_C05_006360_20240403_FADHILI_SRU_TURNAROUND_WATCH","symbol":"006360","company_name":"GS E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":15630.0,"evidence_available_at_that_date":"GS E&C won Fadhili Gas Increment Program Package 2 sulfur recovery facilities; the order supplied plant backlog after a 2023 loss/reset period.","evidence_source":"https://www.asiae.co.kr/en/article/2024040309065572598; https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["execution_risk_score","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.97,"MFE_90D_pct":30.52,"MFE_180D_pct":39.16,"MFE_1Y_pct":39.16,"MFE_2Y_pct":null,"MAE_30D_pct":-10.17,"MAE_90D_pct":-10.17,"MAE_180D_pct":-10.17,"MAE_1Y_pct":-10.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750.0,"drawdown_after_peak_pct":-22.48,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":["execution_risk_score","margin_or_backlog_slowdown"],"four_c_protection_label":"false_break","trigger_outcome_label":"plant_epc_order_after_loss_reset_positive_but_yellow_needs_margin_confirmation","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_006360_20240403","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_000720_20230626_03","case_id":"CASE_R1L127_C05_000720_20230626_AMIRAL_MEGA_CONTRACT_GAP","symbol":"000720","company_name":"Hyundai E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2023-06-26","entry_date":"2023-06-26","entry_price":40800.0,"evidence_available_at_that_date":"Hyundai E&C signed a USD 5bn / KRW 6.5tn Saudi Amiral petrochemical EPC contract covering Packages 1 and 4.","evidence_source":"https://www.korea.net/NewsFocus/Business/view?articleId=234605; https://www.asiae.co.kr/en/article/2023062516232823346; https://koreajoongangdaily.joins.com/2023/06/25/business/industry/Hyundai-EC-5-billion/20230625165454180.html","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.82,"MFE_90D_pct":8.82,"MFE_180D_pct":8.82,"MFE_1Y_pct":8.82,"MFE_2Y_pct":108.58,"MAE_30D_pct":-15.32,"MAE_90D_pct":-18.5,"MAE_180D_pct":-23.53,"MAE_1Y_pct":-23.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-26","peak_price":44400.0,"drawdown_after_peak_pct":-29.73,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"largest_order_headline_failed_180D_rerating_due_no_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_000720_20230626","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_006360_20230706_04","case_id":"CASE_R1L127_C05_006360_20230706_GEOMDAN_RECONSTRUCTION_4C","symbol":"006360","company_name":"GS E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2023-07-06","entry_date":"2023-07-06","entry_price":14520.0,"evidence_available_at_that_date":"GS E&C decided to rebuild 17 apartment buildings after the Incheon Geomdan parking-lot collapse, with analysts estimating up to KRW 1tn of cost; later reports showed large reconstruction costs and operating loss.","evidence_source":"https://en.yna.co.kr/view/AEN20230706002200320; https://www.asiae.co.kr/en/article/2024013111305931564; https://www.kedglobal.com/construction/newsView/ked202307260020","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["accounting_or_trust_break","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.12,"MFE_90D_pct":10.12,"MFE_180D_pct":19.83,"MFE_1Y_pct":23.62,"MFE_2Y_pct":71.14,"MAE_30D_pct":-7.92,"MAE_90D_pct":-12.74,"MAE_180D_pct":-12.74,"MAE_1Y_pct":-12.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-23","peak_price":17400.0,"drawdown_after_peak_pct":-20.34,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard4c_trust_break_blocks_future_contract_headline_promotion_until_cleanup","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_006360_20230706","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_028050_20250123_05","case_id":"CASE_R1L127_C05_028050_20250123_PROFIT_BACKLOG_MARGIN_BRIDGE","symbol":"028050","company_name":"Samsung E&A","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2025-01-23","entry_date":"2025-01-23","entry_price":17440.0,"evidence_available_at_that_date":"SAMSUNG E&A reported 2024 operating profit above target, Q4 operating profit growth, and 2024 order/backlog figures; management attributed performance to profitability and operational efficiency.","evidence_source":"https://www.samsungena.com/en/newsroom/news/view?idx=15673; https://en.yna.co.kr/view/AEN20250123007151320; https://en.yna.co.kr/view/AEN20250117001551320","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2025.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.38,"MFE_90D_pct":33.6,"MFE_180D_pct":75.75,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.08,"MAE_90D_pct":-6.08,"MAE_180D_pct":-6.08,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-23","peak_price":30650.0,"drawdown_after_peak_pct":-8.65,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":[],"four_c_protection_label":"false_break","trigger_outcome_label":"profitability_efficiency_bridge_reopens_C05_after_2024_award_drawdown","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_028050_20250123","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_006360_20250205_06","case_id":"CASE_R1L127_C05_006360_20250205_PROFIT_TURNAROUND_AFTER_RESET","symbol":"006360","company_name":"GS E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2025-02-05","entry_date":"2025-02-05","entry_price":17300.0,"evidence_available_at_that_date":"GS E&C shifted to 2024 net profit after a 2023 loss, and reports described the turnaround after the Geomdan reconstruction cost shock.","evidence_source":"https://en.yna.co.kr/view/AEN20250205002400320; https://en.topdaily.kr/articles/4578; https://www.mk.co.kr/en/realestate/11232869","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2025.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.45,"MFE_90D_pct":43.64,"MFE_180D_pct":43.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.29,"MAE_90D_pct":-12.2,"MAE_180D_pct":-12.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2025-06-12","peak_price":24850.0,"drawdown_after_peak_pct":-28.41,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"false_break","trigger_outcome_label":"cleanup_plus_profit_turn_positive_after_hard4c_decay","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_006360_20250205","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_047040_20250429_07","case_id":"CASE_R1L127_C05_047040_20250429_ORDER_BACKLOG_Q1_PROFIT","symbol":"047040","company_name":"Daewoo E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-29","entry_date":"2025-04-29","entry_price":3520.0,"evidence_available_at_that_date":"Daewoo E&C Q1 2025 profit increased, new orders rose, order backlog stood at KRW45tn, and management cited the intent to secure large overseas contracts after a fertilizer-plant framework agreement.","evidence_source":"https://en.yna.co.kr/view/AEN20250429001851320; https://www.theinvestor.co.kr/article/10495942","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.51,"MFE_90D_pct":36.51,"MFE_180D_pct":63.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.12,"MAE_90D_pct":-3.12,"MAE_180D_pct":-5.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-01-23","peak_price":5760.0,"drawdown_after_peak_pct":-12.85,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":[],"four_c_protection_label":"false_break","trigger_outcome_label":"order_backlog_plus_profit_visibility_positive_but_green_waits_contract_finalization","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_047040_20250429","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L127_C05_375500_20250206_08","case_id":"CASE_R1L127_C05_375500_20250206_SELECTED_ORDER_STRATEGY_COST_RATE","symbol":"375500","company_name":"DL E&C","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_TO_MARGIN_CASH_BRIDGE_VS_COST_OVERHEAD_TRUST_BREAK","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-06","entry_date":"2025-02-06","entry_price":35150.0,"evidence_available_at_that_date":"DL E&C announced 2024 results: operating profit fell due to bad debts and cost-rate adjustments, but the release explicitly tied order strategy to high-value projects that guarantee profitability.","evidence_source":"https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword=; https://www.dlenc.co.kr/eng/ir/financial/Highlight.do","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.57,"MFE_90D_pct":59.89,"MFE_180D_pct":69.84,"MFE_1Y_pct":69.84,"MFE_2Y_pct":null,"MAE_30D_pct":-11.66,"MAE_90D_pct":-11.66,"MAE_180D_pct":-11.66,"MAE_1Y_pct":-11.66,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-06-26","peak_price":59700.0,"drawdown_after_peak_pct":-32.91,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_price_only_full_4b; evidence_bridge_gate_applied","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"false_break","trigger_outcome_label":"cost_rate_disclosure_and_selected_order_strategy_positive_after_margin_gap_acknowledgement","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R1L127_C05_375500_20250206","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_028050_20240403_FADHILI_CONTRACT_MARGIN_GAP","trigger_id":"TRG_R1L127_C05_028050_20240403_01","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":6,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":58,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":15.81,"MAE_90D_pct":-14.62,"score_return_alignment_label":"counterexample_contract_size_not_enough_without_margin_cash_timing","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_006360_20240403_FADHILI_SRU_TURNAROUND_WATCH","trigger_id":"TRG_R1L127_C05_006360_20240403_02","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":30.52,"MAE_90D_pct":-10.17,"score_return_alignment_label":"positive_stage2_actionable_not_green","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_000720_20230626_AMIRAL_MEGA_CONTRACT_GAP","trigger_id":"TRG_R1L127_C05_000720_20230626_03","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":6,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":58,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":8.82,"MAE_90D_pct":-18.5,"score_return_alignment_label":"counterexample_mega_order_does_not_override_pf_and_margin_discount","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_006360_20230706_GEOMDAN_RECONSTRUCTION_4C","trigger_id":"TRG_R1L127_C05_006360_20230706_04","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_before":42,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":35,"stage_label_after":"Stage4C","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":10.12,"MAE_90D_pct":-12.74,"score_return_alignment_label":"4C_guardrail_not_short_signal_but_blocks_positive_stage","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_028050_20250123_PROFIT_BACKLOG_MARGIN_BRIDGE","trigger_id":"TRG_R1L127_C05_028050_20250123_05","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":33.6,"MAE_90D_pct":-6.08,"score_return_alignment_label":"positive_margin_cash_bridge_stronger_than_contract_headline","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_006360_20250205_PROFIT_TURNAROUND_AFTER_RESET","trigger_id":"TRG_R1L127_C05_006360_20250205_06","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":43.64,"MAE_90D_pct":-12.2,"score_return_alignment_label":"positive_reopen_after_4c_requires_profit_and_cost_reset_evidence","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_047040_20250429_ORDER_BACKLOG_Q1_PROFIT","trigger_id":"TRG_R1L127_C05_047040_20250429_07","symbol":"047040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":36.51,"MAE_90D_pct":-3.12,"score_return_alignment_label":"positive_stage2_actionable_with_clean_MAE","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R1L127_C05_375500_20250206_SELECTED_ORDER_STRATEGY_COST_RATE","trigger_id":"TRG_R1L127_C05_375500_20250206_08","symbol":"375500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C05 shadow gate caps pure mega-contract credit and rewards verified margin/cost/cash bridge or bounded cleanup evidence.","MFE_90D_pct":59.89,"MAE_90D_pct":-11.66,"score_return_alignment_label":"positive_when_bad_debt_cost_rate_is_explicitly_measured_and_order_quality_is_selected","current_profile_verdict":"current_profile_too_late"}
{"row_type":"residual_contribution","round":"R1","loop":"127","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["mega_contract_headline_false_positive","margin_cash_bridge_missing","trust_break_decay_reopen_needed","hard4c_blocks_future_headline_promotion"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R1
completed_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / C05 rows 47 need_to_50 3 before this loop
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | C27_CONTENT_IP_GLOBAL_MONETIZATION | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_quality_repair | C05_followup_url_proxy_repair_only
```

## 28. Source Notes

- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Evidence URLs are embedded in `evidence_source` fields. They are used only to establish historical as-of evidence, not current/live recommendations.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```