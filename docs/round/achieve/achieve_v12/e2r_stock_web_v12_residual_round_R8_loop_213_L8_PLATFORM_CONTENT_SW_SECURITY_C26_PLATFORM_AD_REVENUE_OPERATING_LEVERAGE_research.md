# E2R Stock-Web v12 Residual Research — R8 / L8 / C26

```text
research_file: e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
created_at: 2026-06-16
research_mode: post_calibrated_residual_historical_research_v12
output_target: standalone_markdown_research_file
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Scheduler / No-Repeat selection

```text
selected_round: R8
selected_loop: 213
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1

selection_basis:
- MAIN prompt coverage_index_first scheduler
- NO-REPEAT INDEX used only as duplicate-prevention ledger
- C28 was handled in the immediately previous L8 run, so this run opens C26 instead of repeating software/security contract-retention.
- C26 currently has enough raw rows, so the goal is not row-count filling. The goal is quality reinforcement:
  platform/ad/commerce headline vs realized operating-leverage bridge.

hard_duplicate_key:
canonical_archetype_id + symbol + trigger_type + entry_date

loop_objective:
- residual_false_positive_mining
- stage2_actionable_bonus_stress_test
- sector_specific_rule_discovery
- canonical_archetype_compression
- holdout_validation
```

## 2. Price source validation

```text
primary_price_source: Songdaiki/stock-web
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_schema: d,o,h,l,c,v,a,mc,s,m

MFE/MAE calculation:
MFE_ND = max(high from entry row through N tradable rows) / entry_close - 1
MAE_ND = min(low from entry row through N tradable rows) / entry_close - 1

corporate_action_contamination:
all selected usable rows have no profile-level corporate-action candidate overlap inside D~D+180.
```

## 3. Coverage matrix

```text
new_independent_case_count: 8
new_independent_trigger_count: 8
unique_symbol_count: 6

stage2_count: 2
stage2_actionable_count: 5
stage4b_count: 1
stage4c_count: 0

positive_or_direct_bridge_count: 4
counterexample_or_guardrail_count: 4

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

current_profile_error_count: 5
new_independent_ratio: 1.00
ready_for_batch_ingest: true
```

## 4. Case ledger

| Symbol | Company | Trigger | Entry date | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Case role |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 035420 | NAVER | Stage2-Actionable | 2024-05-03 | 194,600 | 2.00/-15.16 | 2.00/-22.35 | 15.11/-22.35 | guarded_positive_high_MAE |
| 035420 | NAVER | Stage2-Actionable | 2024-11-08 | 174,600 | 26.00/-1.78 | 34.88/-1.78 | 68.96/-1.78 | positive_control |
| 035720 | Kakao | Stage2 | 2024-05-09 | 48,600 | 4.12/-13.99 | 4.12/-32.30 | 4.12/-33.02 | false_positive_control |
| 067160 | SOOP | Stage2-Actionable | 2024-07-31 | 103,500 | 20.58/-17.97 | 20.58/-17.97 | 31.30/-24.83 | guarded_positive_high_MAE |
| 042000 | Cafe24 | Stage2-Actionable | 2024-06-21 | 40,900 | 5.01/-32.89 | 5.01/-44.13 | 70.42/-44.13 | long_run_positive_high_MAE |
| 042000 | Cafe24 | Stage4B | 2025-02-26 | 68,500 | 1.75/-32.85 | 1.75/-36.86 | 1.75/-55.69 | local_4B_overextension_after_strong_result |
| 089600 | Nasmedia | Stage2 | 2025-05-13 | 15,600 | 10.71/-5.45 | 14.74/-10.19 | 14.74/-23.85 | stage2_cap_low_base_turnaround |
| 216050 | Incross | Stage2-Actionable | 2025-05-07 | 7,260 | 26.31/-4.27 | 29.61/-4.27 | 29.61/-12.67 | positive_control |

## 5. Case notes

### 5.1 NAVER — direct search/commerce operating leverage, but early row still needs Green brake

NAVER 1Q24 showed a real operating-leverage bridge: Search Platform and Commerce both grew, and EBITDA/operating-profit margins improved. The row is valid Stage2-Actionable, but the 180D MAE was -22.35%, so the correct residual is not Stage2 deletion; it is a Stage3-Green brake until repeat margin/cash evidence appears.

The 2024-11-08 NAVER Q3 row is a stronger positive control: record operating profit, Search Platform + commerce growth, and ad targeting/product improvement produced 180D MFE +68.96% with shallow MAE. This is the cleaner C26 bridge pattern: ad/search/commerce revenue plus margin conversion.

### 5.2 Kakao — single-quarter OP rebound is not a conversion bridge

Kakao's 2024 Q1 operating profit rebound is not enough by itself. Because the row did not carry enough durable ad/commerce operating-leverage evidence and the forward path was weak, it remains a Stage2 cap rather than Stage2-Actionable/Yellow.

### 5.3 SOOP — platform/ad bridge works, but volatility prevents Green

SOOP's Q2 row had record revenue/OP with platform and advertising revenue growth, plus activity/user-time indicators. That is Actionable evidence. Still, the 180D MAE was -24.83%, so the profile should preserve Stage2-Actionable but block Yellow/Green until repeated revenue/margin retention appears.

### 5.4 Cafe24 — YouTube commerce route is powerful, but timing matters

Cafe24's YouTube Shopping route has a real GMV/commission bridge: Cafe24 earns fee revenue as YouTube-linked shopping-mall transactions grow. The 2024-06-21 row eventually delivered +70.42% 180D MFE, but also carried -44.13% MAE. This is a classic C26 case where the business route is valid but entry timing creates a high-MAE Green blocker.

The 2025-02-26 Q4/FY2024 surprise row is different: the result was strong, but the article explicitly warned about valuation pressure if the stock rose too steeply. The stock-web path peaked at the entry window and had -55.69% 180D MAE, so this is a local Stage4B/valuation-extension guardrail, not a fresh Green trigger.

### 5.5 Nasmedia and Incross — ad-agency turnaround must be split by realized bridge quality

Nasmedia's Q1 2025 profit recovery and new media/OTT/OOH opportunities are valid Stage2 evidence, but still lighter as a recurring-retention/operating-leverage bridge. Incross is stronger: Q1 2025 revenue, OP, net profit, ad-transaction volume, ad revenue, AOR, media-portfolio and commerce-rep growth all point to realized ad/commerce conversion, so it qualifies as Stage2-Actionable.

## 6. Residual rule candidate

```text
canonical_rule_candidate:
C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1

sector_rule_candidate:
L8_PLATFORM_AD_COMMERCE_MARGIN_SECOND_BRIDGE_GATE_V1

core_residual:
- Platform / ad / AI / commerce profile alone does not create Stage2-Actionable, Stage3-Yellow, or Stage3-Green.
- Stage2-Actionable requires at least one direct second bridge:
  search/ad revenue acceleration, commerce GMV or fee route, platform engagement/viewing-time growth,
  realized operating-profit / EBITDA-margin conversion, or cost-efficiency conversion.
- Single-quarter operating-profit rebound without durable ad/commerce bridge remains Stage2 cap.
- High MAE on a valid direct bridge blocks Yellow/Green first; it does not erase Stage2-Actionable.
- Local Stage4B is preferred when positive evidence arrives after a fast valuation rerating
  and the next evidence is estimate raise / earnings surprise rather than repeat cash or margin conversion.
- Hard Stage4C requires confirmed non-price thesis break:
  traffic loss, advertiser-budget collapse, take-rate/margin break, retention failure,
  accounting/trust break, or weak offset quality.
```

## 7. Current-profile stress test

```text
stage2_actionable_evidence_bonus:
keep, but require direct second bridge for C26.

stage3_yellow_total_min:
keep strict; do not let single-quarter OP recovery or profile-only AI/ad language qualify.

stage3_green_total_min:
do not loosen. Green needs repeat conversion across at least two evidence families:
ad/search/commerce revenue + margin/cash/retention bridge.

price_only_blowoff_blocks_positive_stage:
keep. Cafe24 2025-02-26 demonstrates that a strong result at a local valuation peak needs 4B/watch.

full_4b_requires_non_price_evidence:
keep. Cafe24's valuation-pressure warning is non-price 4B support.

hard_4c_thesis_break_routes_to_4c:
keep, but no selected C26 row had enough non-price break evidence for hard 4C.
```

## 8. Shadow-weight notes

```text
do_not_propose_new_weight_delta: false
production_scoring_changed: false
shadow_weight_only: true

shadow_delta_candidate:
+ small C26-specific credit for realized ad/search/commerce revenue + operating-margin conversion
+ small C26-specific credit for GMV/commission route when tied to visible platform distribution
- cap for single-quarter profit rebound without retention/revenue bridge
- cap for profile-only AI/ad/commerce theme
- Green blocker for 180D MAE <= -20% unless repeat margin/cash evidence appears
```

## 9. Machine-readable JSONL

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_NAVER_2024Q1_SEARCH_COMMERCE_OP_LEVERAGE", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:035420:Stage2-Actionable:2024-05-03", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "035420", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-03"}, "symbol": "035420", "company_name": "NAVER", "evidence_date": "2024-05-03", "entry_date": "2024-05-03", "entry_price": 194600.0, "actual_entry_ohlcv": {"d": "2024-05-03", "o": 195000, "h": 196400, "l": 191500, "c": 194600, "v": 2291415, "a": "445400711900.0", "mc": 31604712392400, "s": "162408594", "m": "KOSPI"}, "trigger_type": "Stage2-Actionable", "case_role": "guarded_positive_high_MAE", "evidence_family": "issuer_earnings_search_commerce_margin", "evidence_summary": "1Q24 search platform and commerce revenue growth with EBITDA/OP margin improvement; operating leverage visible but forward MAE remained meaningful.", "evidence_urls": ["https://www.navercorp.com/investment/earningsRelease/2024Q1.pdf"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 2.0, "mae_pct": -15.16, "peak_date": "2024-05-07", "peak_price": 198500, "trough_date": "2024-06-19", "trough_price": 165100, "post_peak_drawdown_pct": -16.83}, "90D": {"mfe_pct": 2.0, "mae_pct": -22.35, "peak_date": "2024-05-07", "peak_price": 198500, "trough_date": "2024-08-05", "trough_price": 151100, "post_peak_drawdown_pct": -23.88}, "180D": {"mfe_pct": 15.11, "mae_pct": -22.35, "peak_date": "2025-02-04", "peak_price": 224000, "trough_date": "2024-08-05", "trough_price": 151100, "post_peak_drawdown_pct": -3.12}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 13, "earnings_visibility": 16, "bottleneck_pricing": 11, "market_mispricing": 11, "valuation_rerating": 10, "capital_allocation": 3, "information_confidence": 4}, "stage2_actionable_evidence_bonus_applied": 2.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 70.0, "simulated_revision_score": 61.7, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "too_early_yellow_if_green_or_yellow_without_repeat_margin_cash_bridge", "green_blocker": true, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": null}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|2024-05-03", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_NAVER_2024Q3_SEARCH_AD_COMMERCE_RECORD_OP", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:035420:Stage2-Actionable:2024-11-08", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "035420", "trigger_type": "Stage2-Actionable", "entry_date": "2024-11-08"}, "symbol": "035420", "company_name": "NAVER", "evidence_date": "2024-11-08", "entry_date": "2024-11-08", "entry_price": 174600.0, "actual_entry_ohlcv": {"d": "2024-11-08", "o": 182600, "h": 182800, "l": 173700, "c": 174600, "v": 1233287, "a": "218420272900.0", "mc": 28072975096800, "s": "160784508", "m": "KOSPI"}, "trigger_type": "Stage2-Actionable", "case_role": "positive_control", "evidence_family": "issuer_earnings_search_ad_product_commerce_margin", "evidence_summary": "Q3 record operating profit, search-platform and commerce growth, ad targeting/ad product improvement; direct operating-leverage bridge.", "evidence_urls": ["https://www.kedglobal.com/tech,-media-telecom/newsView/ked202411080009"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 26.0, "mae_pct": -1.78, "peak_date": "2024-12-12", "peak_price": 220000, "trough_date": "2024-11-11", "trough_price": 171500, "post_peak_drawdown_pct": -6.82}, "90D": {"mfe_pct": 34.88, "mae_pct": -1.78, "peak_date": "2025-02-07", "peak_price": 235500, "trough_date": "2024-11-11", "trough_price": 171500, "post_peak_drawdown_pct": -13.8}, "180D": {"mfe_pct": 68.96, "mae_pct": -1.78, "peak_date": "2025-06-23", "peak_price": 295000, "trough_date": "2024-11-11", "trough_price": 171500, "post_peak_drawdown_pct": -24.07}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 17, "bottleneck_pricing": 13, "market_mispricing": 12, "valuation_rerating": 12, "capital_allocation": 3, "information_confidence": 5}, "stage2_actionable_evidence_bonus_applied": 2.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 79.0, "simulated_revision_score": 65.0, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "none_or_stage3_yellow_candidate_but_green_blocked_until_repeat_cash_bridge", "green_blocker": false, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": null}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|2024-11-08", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_KAKAO_2024Q1_OP_RECOVERY_BUT_WEAK_BRIDGE", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:035720:Stage2:2024-05-09", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "035720", "trigger_type": "Stage2", "entry_date": "2024-05-09"}, "symbol": "035720", "company_name": "Kakao", "evidence_date": "2024-05-09", "entry_date": "2024-05-09", "entry_price": 48600.0, "actual_entry_ohlcv": {"d": "2024-05-09", "o": 50200, "h": 50600, "l": 48400, "c": 48600, "v": 2000421, "a": "98061699550.0", "mc": 21638852908200, "s": "445243887", "m": "KOSPI"}, "trigger_type": "Stage2", "case_role": "false_positive_control", "evidence_family": "issuer_earnings_single_quarter_recovery_below_consensus", "evidence_summary": "Q1 operating-profit rebound but below consensus and without enough durable ad/commerce operating-leverage bridge.", "evidence_urls": ["https://www.kedglobal.com/tech,-media-telecom/newsView/ked202405090010"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 4.12, "mae_pct": -13.99, "peak_date": "2024-05-09", "peak_price": 50600, "trough_date": "2024-06-19", "trough_price": 41800, "post_peak_drawdown_pct": -17.39}, "90D": {"mfe_pct": 4.12, "mae_pct": -32.3, "peak_date": "2024-05-09", "peak_price": 50600, "trough_date": "2024-09-09", "trough_price": 32900, "post_peak_drawdown_pct": -34.98}, "180D": {"mfe_pct": 4.12, "mae_pct": -33.02, "peak_date": "2024-05-09", "peak_price": 50600, "trough_date": "2024-11-14", "trough_price": 32550, "post_peak_drawdown_pct": -35.67}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 12, "bottleneck_pricing": 8, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 3, "information_confidence": 4}, "stage2_actionable_evidence_bonus_applied": 0.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 55.0, "simulated_revision_score": 46.6, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "stage2_actionable_bonus_false_positive_if_single_quarter_OP_rebound_promoted", "green_blocker": true, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": null}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|2024-05-09", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_SOOP_2024Q2_PLATFORM_AD_RECORD", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:067160:Stage2-Actionable:2024-07-31", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "067160", "trigger_type": "Stage2-Actionable", "entry_date": "2024-07-31"}, "symbol": "067160", "company_name": "SOOP", "evidence_date": "2024-07-31", "entry_date": "2024-07-31", "entry_price": 103500.0, "actual_entry_ohlcv": {"d": "2024-07-31", "o": 122200, "h": 124800, "l": 103000, "c": 103500, "v": 619314, "a": "67423255500.0", "mc": 1189708384500, "s": "11494767", "m": "KOSDAQ GLOBAL"}, "trigger_type": "Stage2-Actionable", "case_role": "guarded_positive_high_MAE", "evidence_family": "issuer_earnings_platform_ad_viewer_time", "evidence_summary": "Record quarterly sales/OP with platform/ad revenue and user-time growth; valid direct bridge, but high MAE blocks Green.", "evidence_urls": ["https://www.kedglobal.com/tech,-media-telecom/newsView/ked202407310012"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 20.58, "mae_pct": -17.97, "peak_date": "2024-07-31", "peak_price": 124800, "trough_date": "2024-08-05", "trough_price": 84900, "post_peak_drawdown_pct": -31.97}, "90D": {"mfe_pct": 20.58, "mae_pct": -17.97, "peak_date": "2024-07-31", "peak_price": 124800, "trough_date": "2024-08-05", "trough_price": 84900, "post_peak_drawdown_pct": -31.97}, "180D": {"mfe_pct": 31.3, "mae_pct": -24.83, "peak_date": "2025-02-06", "peak_price": 135900, "trough_date": "2025-04-09", "trough_price": 77800, "post_peak_drawdown_pct": -42.75}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 14, "earnings_visibility": 16, "bottleneck_pricing": 12, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 3, "information_confidence": 4}, "stage2_actionable_evidence_bonus_applied": 2.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 73.0, "simulated_revision_score": 63.0, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "green_blocker_needed_due_high_MAE_and_platform_execution_volatility", "green_blocker": true, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": null}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|2024-07-31", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_CAFE24_YOUTUBE_SHOPPING_GMV_COMMISSION_ROUTE", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:042000:Stage2-Actionable:2024-06-21", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "042000", "trigger_type": "Stage2-Actionable", "entry_date": "2024-06-21"}, "symbol": "042000", "company_name": "Cafe24", "evidence_date": "2024-06-21", "entry_date": "2024-06-21", "entry_price": 40900.0, "actual_entry_ohlcv": {"d": "2024-06-21", "o": 41750, "h": 42150, "l": 38900, "c": 40900, "v": 2879800, "a": "116576257700.0", "mc": 991949908600, "s": "24253054", "m": "KOSDAQ"}, "trigger_type": "Stage2-Actionable", "case_role": "long_run_positive_high_MAE", "evidence_family": "platform_commerce_GMV_commission_youtube_shopping", "evidence_summary": "YouTube Shopping service/store launch, GMV/fee model, cost-reduction/profit-turnaround bridge; positive but volatile after initial spike.", "evidence_urls": ["https://en.topdaily.kr/articles/1424", "https://www.cafe24.com/channel/youtubeshopping/about.html"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv", "profile_path": "atlas/symbol_profiles/042/042000.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 5.01, "mae_pct": -32.89, "peak_date": "2024-06-26", "peak_price": 42950, "trough_date": "2024-07-19", "trough_price": 27450, "post_peak_drawdown_pct": -36.09}, "90D": {"mfe_pct": 5.01, "mae_pct": -44.13, "peak_date": "2024-06-26", "peak_price": 42950, "trough_date": "2024-10-24", "trough_price": 22850, "post_peak_drawdown_pct": -46.8}, "180D": {"mfe_pct": 70.42, "mae_pct": -44.13, "peak_date": "2025-02-26", "peak_price": 69700, "trough_date": "2024-10-24", "trough_price": 22850, "post_peak_drawdown_pct": -25.68}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 15, "bottleneck_pricing": 12, "market_mispricing": 13, "valuation_rerating": 13, "capital_allocation": 3, "information_confidence": 4}, "stage2_actionable_evidence_bonus_applied": 2.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 77.0, "simulated_revision_score": 61.5, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "green_blocker_due_high_MAE_before_revenue_repeat", "green_blocker": true, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": null}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|042000|2024-06-21", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_CAFE24_2024Q4_EARNINGS_SURPRISE_VALUATION_PRESSURE", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:042000:Stage4B:2025-02-26", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "042000", "trigger_type": "Stage4B", "entry_date": "2025-02-26"}, "symbol": "042000", "company_name": "Cafe24", "evidence_date": "2025-02-26", "entry_date": "2025-02-26", "entry_price": 68500.0, "actual_entry_ohlcv": {"d": "2025-02-26", "o": 62100, "h": 69700, "l": 59400, "c": 68500, "v": 5084248, "a": "336056460000.0", "mc": 1661334199000, "s": "24253054", "m": "KOSDAQ"}, "trigger_type": "Stage4B", "case_role": "local_4B_overextension_after_strong_result", "evidence_family": "earnings_surprise_but_valuation_pressure_warning", "evidence_summary": "FY2024 profit turnaround/Q4 earnings surprise, but article explicitly warned steep future rise could face valuation pressure; forward path confirms local 4B risk.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2025022609185047710"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042000/2025.csv", "profile_path": "atlas/symbol_profiles/042/042000.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 1.75, "mae_pct": -32.85, "peak_date": "2025-02-26", "peak_price": 69700, "trough_date": "2025-04-09", "trough_price": 46000, "post_peak_drawdown_pct": -34.0}, "90D": {"mfe_pct": 1.75, "mae_pct": -36.86, "peak_date": "2025-02-26", "peak_price": 69700, "trough_date": "2025-05-20", "trough_price": 43250, "post_peak_drawdown_pct": -37.95}, "180D": {"mfe_pct": 1.75, "mae_pct": -55.69, "peak_date": "2025-02-26", "peak_price": 69700, "trough_date": "2025-11-21", "trough_price": 30350, "post_peak_drawdown_pct": -56.46}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 16, "earnings_visibility": 15, "bottleneck_pricing": 10, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 2, "information_confidence": 4}, "stage2_actionable_evidence_bonus_applied": 0.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 61.0, "simulated_revision_score": 62.8, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "positive_earnings_surprise_must_not_override_valuation_extension_guard", "green_blocker": true, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": true}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|042000|2025-02-26", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_NASMEDIA_2025Q1_LOW_BASE_TURNAROUND_BUT_STAGE2_CAP", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:089600:Stage2:2025-05-13", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "089600", "trigger_type": "Stage2", "entry_date": "2025-05-13"}, "symbol": "089600", "company_name": "Nasmedia", "evidence_date": "2025-05-13", "entry_date": "2025-05-13", "entry_price": 15600.0, "actual_entry_ohlcv": {"d": "2025-05-13", "o": 15510, "h": 15630, "l": 15300, "c": 15600, "v": 32041, "a": "497674165.0", "mc": 180463342800, "s": "11568163", "m": "KOSDAQ"}, "trigger_type": "Stage2", "case_role": "stage2_cap_low_base_turnaround", "evidence_family": "ad_agency_turnaround_new_media_low_base", "evidence_summary": "Q1 OP grew from a low base and new OTT/OOH media opportunity exists, but recurring platform retention/operating-leverage bridge remains lighter.", "evidence_urls": ["https://www.nasmedia.co.kr/%ED%9A%8C%EC%82%AC%EC%86%8C%EA%B0%9C/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/", "https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2025031209314055K_02_03.pdf&inlineYn=Y&saveKey=research.pdf"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2025.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 10.71, "mae_pct": -5.45, "peak_date": "2025-06-24", "peak_price": 17270, "trough_date": "2025-05-22", "trough_price": 14750, "post_peak_drawdown_pct": -5.56}, "90D": {"mfe_pct": 14.74, "mae_pct": -10.19, "peak_date": "2025-07-03", "peak_price": 17900, "trough_date": "2025-08-27", "trough_price": 14010, "post_peak_drawdown_pct": -21.73}, "180D": {"mfe_pct": 14.74, "mae_pct": -23.85, "peak_date": "2025-07-03", "peak_price": 17900, "trough_date": "2026-01-21", "trough_price": 11880, "post_peak_drawdown_pct": -33.63}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 13, "bottleneck_pricing": 9, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 3, "information_confidence": 4}, "stage2_actionable_evidence_bonus_applied": 0.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 57.0, "simulated_revision_score": 49.4, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "stage2_actionable_false_positive_if_low_base_turnaround_is_promoted_without_retention_bridge", "green_blocker": true, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": null}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|089600|2025-05-13", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "case_id": "C26_INCROSS_2025Q1_AD_COMMERCE_OPERATING_LEVERAGE", "trigger_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:216050:Stage2-Actionable:2025-05-07", "hard_duplicate_key": {"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "symbol": "216050", "trigger_type": "Stage2-Actionable", "entry_date": "2025-05-07"}, "symbol": "216050", "company_name": "Incross", "evidence_date": "2025-05-07", "entry_date": "2025-05-07", "entry_price": 7260.0, "actual_entry_ohlcv": {"d": "2025-05-07", "o": 7300, "h": 7350, "l": 7200, "c": 7260, "v": 52224, "a": "380160925.0", "mc": 93241791720, "s": "12843222", "m": "KOSDAQ"}, "trigger_type": "Stage2-Actionable", "case_role": "positive_control", "evidence_family": "ad_transaction_volume_revenue_OP_conversion", "evidence_summary": "Q1 revenue/OP/net-profit surge driven by advertising division, AOR, media-portfolio diversification, and commerce rep growth.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2025050713380786171"], "price_source_validation": {"repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/216/216050/2025.csv", "profile_path": "atlas/symbol_profiles/216/216050.json", "corporate_action_window_status": "clean_180D_no_candidate_overlap", "zero_volume_or_zero_ohlc_excluded": true, "calibration_usable": true, "block_reason": []}, "forward_path": {"30D": {"mfe_pct": 26.31, "mae_pct": -4.27, "peak_date": "2025-06-20", "peak_price": 9170, "trough_date": "2025-05-22", "trough_price": 6950, "post_peak_drawdown_pct": -5.56}, "90D": {"mfe_pct": 29.61, "mae_pct": -4.27, "peak_date": "2025-06-24", "peak_price": 9410, "trough_date": "2025-05-22", "trough_price": 6950, "post_peak_drawdown_pct": -19.45}, "180D": {"mfe_pct": 29.61, "mae_pct": -12.67, "peak_date": "2025-06-24", "peak_price": 9410, "trough_date": "2026-01-15", "trough_price": 6340, "post_peak_drawdown_pct": -32.62}}, "score_simulation": {"raw_component_breakdown": {"eps_fcf_explosion": 14, "earnings_visibility": 16, "bottleneck_pricing": 12, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 3, "information_confidence": 5}, "stage2_actionable_evidence_bonus_applied": 2.0, "stage3_cross_evidence_green_buffer_applied": 0.0, "weighted_total_after_profile_bonus": 74.0, "simulated_revision_score": 63.0, "profile_id": "e2r_2_2_current_stress_test", "production_scoring_changed": false}, "residual_diagnosis": {"expected_profile_error": "none_but_green_blocked_until_repeat_revenue_margin_retention", "green_blocker": false, "stage2_delete_signal": false, "local_4b_preferred_over_hard_4c": null}, "dedupe": {"same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|2025-05-07", "dedupe_for_aggregate": true, "new_independent_case": true, "representative_row": true}, "shadow_weight": {"scope": "large_sector_and_canonical_only", "before": "active e2r_2_2 profile", "after": "candidate_rule_only", "production_scoring_changed": false}}
{"row_type": "aggregate_summary", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "selected_round": "R8", "selected_loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "new_independent_case_count": 8, "new_independent_trigger_count": 8, "unique_symbol_count": 6, "stage2_count": 2, "stage2_actionable_count": 5, "stage4b_count": 1, "stage4c_count": 0, "positive_or_direct_bridge_count": 4, "counterexample_or_guardrail_count": 4, "source_proxy_only_count": 0, "evidence_url_pending_count": 0, "missing_required_mfe_mae_count": 0, "corporate_action_contaminated_180D_count": 0, "insufficient_forward_window_180D_count": 0, "production_scoring_changed": false, "shadow_weight_only": true, "ready_for_batch_ingest": true}
{"row_type": "residual_contribution", "research_file": "e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "rule_candidate": "C26_AD_COMMERCE_OPERATING_LEVERAGE_SECOND_BRIDGE_GATE_V1", "sector_rule_candidate": "L8_PLATFORM_AD_COMMERCE_MARGIN_SECOND_BRIDGE_GATE_V1", "new_axis_proposed": "no_global_axis", "existing_axis_strengthened": ["stage2_required_bridge", "stage3_green_not_loosened", "high_MAE_green_blocker"], "existing_axis_refined": ["platform_profile_only_stage2_cap", "valuation_extension_4B_watch"], "do_not_propose_new_weight_delta": false, "production_scoring_changed": false}
```

## 10. Batch Ingest Self-Audit

```text
standard_v12_filename: pass
round_sector_consistency: pass
selected_round_derived_from_canonical: pass
no_stock_agent_code_patch: pass
no_live_scan: pass
no_production_scoring_change: pass
stock_web_actual_1D_OHLCV_used: pass
entry_close_present: pass
actual_entry_ohlcv_present: pass
30D_MFE_MAE_present: pass
90D_MFE_MAE_present: pass
180D_MFE_MAE_present: pass
peak_date_and_trough_date_present: pass
same_entry_dedupe_checked: pass
duplicate_key_collision_known: none_detected_in_this_batch
corporate_action_contamination_checked: pass
insufficient_forward_window_checked: pass
source_proxy_only_rows_promoted: 0
evidence_url_pending_rows_promoted: 0
calibration_usable_rows: 8
narrative_only_rows: 0
jsonl_trigger_rows_present: pass
residual_contribution_present: pass
shadow_weight_present: pass
ready_for_batch_ingest: true
```

## 11. Next Research State

```text
next_recommended_archetypes:
- C27_CONTENT_IP_GLOBAL_MONETIZATION_ONE_OFF_HIT_VS_REPEATABILITY_REPAIR
- C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_RETENTION_AND_CASHFLOW_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```

## 12. Source notes

- MAIN prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- NAVER 1Q24 earnings: https://www.navercorp.com/investment/earningsRelease/2024Q1.pdf
- NAVER Q3 record OP article: https://www.kedglobal.com/tech,-media-telecom/newsView/ked202411080009
- Kakao Q1 2024 article: https://www.kedglobal.com/tech,-media-telecom/newsView/ked202405090010
- SOOP Q2 2024 article: https://www.kedglobal.com/tech,-media-telecom/newsView/ked202407310012
- Cafe24 / YouTube commerce article: https://en.topdaily.kr/articles/1424
- Cafe24 official YouTube Shopping page: https://www.cafe24.com/channel/youtubeshopping/about.html
- Cafe24 FY2024/Q4 performance article: https://www.asiae.co.kr/en/article/2025022609185047710
- Nasmedia 1Q25 press / IR page: https://www.nasmedia.co.kr/%ED%9A%8C%EC%82%AC%EC%86%8C%EA%B0%9C/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/
- Nasmedia Samsung Securities report: https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2025031209314055K_02_03.pdf&inlineYn=Y&saveKey=research.pdf
- Incross Q1 2025 article: https://www.asiae.co.kr/en/article/2025050713380786171
