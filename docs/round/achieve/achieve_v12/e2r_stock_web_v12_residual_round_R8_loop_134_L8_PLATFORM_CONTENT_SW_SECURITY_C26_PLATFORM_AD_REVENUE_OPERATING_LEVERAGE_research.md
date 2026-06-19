# E2R Stock-Web v12 Residual Research — R8 / L8 / C26 PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

```text
MD filename: e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
selected_round: R8
selected_loop: 134
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / over_50_rows_quality_repair / C26 rows 106
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_VS_TRAFFIC_AND_PRODUCT_PROXY
loop_objective: quality_repair | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression | sector_specific_rule_discovery
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
entry_price_basis: close_c_column
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` already lists C26 as a Priority 2 bucket with 106 representative rows, so this loop is not quantity filling. It is a quality-repair loop: URL/proxy replacement, counterexample balance, and C26-specific guardrail tightening. C26 maps to R8 / L8 under the MAIN prompt's canonical-to-round rule.

This loop avoids the prior session's C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05/C23/C27/C08/C19/C31/C18 outputs and adds six C26 trigger rows using six different symbols and six evidence families.

## 2. Price atlas and validation scope

The price basis is `Songdaiki/stock-web` calibration shard `atlas/ohlcv_tradable_by_symbol_year`, columns `d,o,h,l,c,v,a,mc,s,m`. Entry price is the close column `c` on the confirmed entry date. The manifest maximum date is `2026-02-20`, so every row below has a complete 180-trading-day forward window inside the stock-web atlas.

Corporate-action caveat: the atlas is raw/unadjusted. For each symbol, the profile route was checked for candidate corporate-action dates. No candidate date overlaps the entry-date to D+180 window used in this MD, so `calibration_usable=true` for all six trigger rows.

## 3. Research thesis

C26 should not treat “traffic,” “platform,” “AI advertisement,” “ad-tech,” or “new ad product” as a rerating signal by itself. In this archetype, the bridge is a little machine with three gears: ad revenue or paid monetization, cost discipline, and operating-margin conversion. If one gear is missing, the machine hums loudly but the shaft does not turn.

Proposed canonical shadow rule:

```text
C26_AD_REVENUE_OPERATING_LEVERAGE_REQUIRES_DURABLE_AD_PRODUCT_AND_COST_DISCIPLINE_GATE
```

Rule intent:

```text
- Allow Stage2-Actionable / Stage3-Yellow credit when ad revenue or platform monetization is explicitly visible and operating leverage is improving.
- Cap generic platform traffic, AI-ad vocabulary, product launch, media-rep optionality, or top-line-only recovery at Stage2-watch.
- Route severe early-entry drawdown from proxy/overhang cases to local Stage4B guardrail, not hard Stage4C, when later business conversion can still reappear.
```

## 4. Evidence and price-path table

| symbol | company_name | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | case_label |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 035420 | NAVER | Stage2-Actionable | 2024-11-08 | 174600 | 26.0 | -1.78 | 34.88 | -1.78 | 68.96 | -1.78 | positive |
| 035720 | Kakao | Stage2 | 2024-05-09 | 48600 | 4.12 | -13.99 | 4.12 | -32.3 | 4.12 | -33.02 | counterexample |
| 067160 | SOOP | Stage2-Actionable | 2024-11-01 | 94500 | 18.62 | -5.61 | 43.81 | -16.83 | 43.81 | -17.67 | positive |
| 089600 | KT nasmedia | Stage2 | 2024-05-13 | 18420 | 2.77 | -12.16 | 2.77 | -17.64 | 2.77 | -26.71 | counterexample |
| 216050 | Incross | Stage2 | 2024-05-03 | 9310 | 1.4 | -16.11 | 1.4 | -35.34 | 1.4 | -35.34 | counterexample |
| 214270 | FSN | Stage4B | 2024-03-20 | 2580 | 7.17 | -20.93 | 7.17 | -30.16 | 7.17 | -39.92 | counterexample |

## 5. Case notes

### 5.1 NAVER / 035420 — positive control
NAVER is the cleanest positive row here. The evidence is not simply “large platform.” Q3 2024 showed record operating profit, and the Search Platform segment/ad-product improvement supplied the direct C26 bridge. The 90D path then delivered +34.88% MFE with only -1.78% MAE.

### 5.2 Kakao / 035720 — broad platform rebound counterexample
Kakao's Q1 2024 operating profit rebound looked like a platform recovery signal, but the result missed consensus and did not provide enough direct ad-revenue + operating-leverage bridge. The 90D path produced only +4.12% MFE and -32.30% MAE, so a C26-specific gate should downscore this from Actionable/Yellow.

### 5.3 SOOP / 067160 — ad ecosystem positive control
SOOP's Q3 2024 evidence ties revenue and operating profit growth to the platform/ad ecosystem. That makes it a C26 positive rather than a generic traffic row. The 90D path reached +43.81% MFE; the moderate MAE says the signal was powerful but still needs staged-entry discipline.

### 5.4 KT nasmedia / 089600 — ad-tech vocabulary without durable leverage
Nasmedia has clear ad-tech/media-rep vocabulary, but the 2024 result later showed contraction in revenue and operating profit. The path had only +2.77% MFE and -26.71% 180D MAE. The model should avoid treating OTT/OOH/platform-Biz optionality as C26 Actionable unless operating leverage is already visible.

### 5.5 Incross / 216050 — revenue up, operating leverage down
Incross is useful because it is not just a weak revenue story. FY2024 revenue rose, but operating profit declined, and one-off costs hit profitability. That is exactly the C26 trap: top-line and new ad business can sound like leverage, while the income statement says otherwise. The 90D and 180D MAE both reached -35.34%.

### 5.6 FSN / 214270 — local 4B guardrail, not hard 4C
FSN later showed marketing/AI-ad response and a return to operating profit in the advertising-marketing segment, but the early entry window had severe drawdown. This should be a local Stage4B/proxy-overhang row rather than a permanent hard Stage4C, because later business conversion was possible.

## 6. Machine-readable case rows

```jsonl
{"calibration_usable": true, "case_label": "positive", "company_name": "NAVER", "evidence_family": "Q3_2024_record_OP_search_platform_ad_revenue_growth", "price_source": "Songdaiki/stock-web", "residual_error_type": "positive_control", "row_type": "case_summary", "score_return_alignment": "aligned_positive_high_MFE_low_MAE", "symbol": "035420"}
{"calibration_usable": true, "case_label": "counterexample", "company_name": "Kakao", "evidence_family": "Q1_2024_profit_rebound_below_consensus_platform_content_mix", "price_source": "Songdaiki/stock-web", "residual_error_type": "stage2_false_positive_high_MAE", "row_type": "case_summary", "score_return_alignment": "misaligned_low_MFE_high_MAE", "symbol": "035720"}
{"calibration_usable": true, "case_label": "positive", "company_name": "SOOP", "evidence_family": "Q3_2024_platform_and_ad_ecosystem_growth", "price_source": "Songdaiki/stock-web", "residual_error_type": "positive_control_with_moderate_MAE", "row_type": "case_summary", "score_return_alignment": "aligned_positive_high_MFE_moderate_MAE", "symbol": "067160"}
{"calibration_usable": true, "case_label": "counterexample", "company_name": "KT nasmedia", "evidence_family": "digital_ad_recovery_expectation_vs_2024_revenue_OP_decline", "price_source": "Songdaiki/stock-web", "residual_error_type": "stage2_false_positive_low_MFE_late_180D_MAE", "row_type": "case_summary", "score_return_alignment": "misaligned_low_MFE_late_high_MAE", "symbol": "089600"}
{"calibration_usable": true, "case_label": "counterexample", "company_name": "Incross", "evidence_family": "Q1_2024_ad_revenue_contraction_then_FY2024_revenue_up_OP_down", "price_source": "Songdaiki/stock-web", "residual_error_type": "stage2_false_positive_high_MAE", "row_type": "case_summary", "score_return_alignment": "misaligned_low_MFE_high_MAE", "symbol": "216050"}
{"calibration_usable": true, "case_label": "counterexample", "company_name": "FSN", "evidence_family": "AI_ad_marketing_response_later_conversion_but_entry_window_drawdown", "price_source": "Songdaiki/stock-web", "residual_error_type": "local_4B_timing_guardrail_high_MAE", "row_type": "case_summary", "score_return_alignment": "misaligned_early_entry_high_MAE_but_later_business_repair_possible", "symbol": "214270"}
```

## 7. Machine-readable trigger rows

```jsonl
{"MAE_180D_pct": -1.78, "MAE_30D_pct": -1.78, "MAE_90D_pct": -1.78, "MFE_180D_pct": 68.96, "MFE_30D_pct": 26.0, "MFE_90D_pct": 34.88, "aggregate_role": "representative_for_aggregate", "calibration_block_reason": "", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_label": "positive", "company_name": "NAVER", "component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 7, "earnings_visibility": 14, "eps_fcf_revision": 16, "information_confidence": 12, "market_mispricing": 10, "total_after_c26_gate": 80, "total_current_proxy": 78, "valuation_rerating": 11}, "corporate_action_check": "profile candidate dates checked; no candidate date inside entry_date~D+180 window", "corporate_action_overlap_180D": false, "current_profile_error": false, "current_profile_verdict": "mostly_correct_positive_but_C26_specific_gate_should_reward_direct_ad_revenue_plus_margin_bridge", "dedupe_key": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|Stage2-Actionable|2024-11-08", "dedupe_role": "representative", "entry_date": "2024-11-08", "entry_price": 174600, "entry_price_basis": "close_c_column", "evidence_date": "2024-11-08", "evidence_family": "Q3_2024_record_OP_search_platform_ad_revenue_growth", "evidence_summary": "Q3 2024 operating profit reached a quarterly high; search platform revenue/ad product improvement gave direct ad-revenue + margin bridge rather than mere traffic proxy.", "fine_archetype_id": "SEARCH_PLATFORM_AD_REVENUE_MARGIN_LEVERAGE", "forward_180D_available": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market": "KOSPI", "peak_180D_date": "2025-06-23", "peak_180D_price": 295000, "peak_30D_price": 220000, "peak_90D_price": 235500, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "positive_control", "round": "R8", "same_entry_group_id": "C26:035420:Stage2-Actionable:2024-11-08", "score_return_alignment": "aligned_positive_high_MFE_low_MAE", "source_doc": "e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_proxy_only": false, "source_urls": ["https://en.yna.co.kr/view/AEN20241108001152320", "https://www.ajupress.com/view/20241108103437767"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "035420", "trigger_date": "2024-11-08", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-11-11", "trough_180D_price": 171500, "trough_30D_price": 171500, "trough_90D_price": 171500, "window_180D_end_date": "2025-08-05"}
{"MAE_180D_pct": -33.02, "MAE_30D_pct": -13.99, "MAE_90D_pct": -32.3, "MFE_180D_pct": 4.12, "MFE_30D_pct": 4.12, "MFE_90D_pct": 4.12, "aggregate_role": "representative_for_aggregate", "calibration_block_reason": "", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_label": "counterexample", "company_name": "Kakao", "component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 5, "earnings_visibility": 12, "eps_fcf_revision": 10, "information_confidence": 11, "market_mispricing": 10, "total_after_c26_gate": 65, "total_current_proxy": 73, "valuation_rerating": 9}, "corporate_action_check": "profile candidate dates checked; no candidate date inside entry_date~D+180 window", "corporate_action_overlap_180D": false, "current_profile_error": true, "current_profile_verdict": "false_positive_risk_if_broad_platform_rebound_is_scored_as_C26_ad_operating_leverage", "dedupe_key": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage2|2024-05-09", "dedupe_role": "representative", "entry_date": "2024-05-09", "entry_price": 48600, "entry_price_basis": "close_c_column", "evidence_date": "2024-05-09", "evidence_family": "Q1_2024_profit_rebound_below_consensus_platform_content_mix", "evidence_summary": "Operating profit rebounded sharply but missed consensus; the signal is broad platform/content recovery, not enough durable ad-revenue + operating-leverage bridge for Yellow.", "fine_archetype_id": "PLATFORM_PROFIT_REBOUND_WITH_WEAK_AD_LEVERAGE_BRIDGE", "forward_180D_available": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market": "KOSPI", "peak_180D_date": "2024-05-09", "peak_180D_price": 50600, "peak_30D_price": 50600, "peak_90D_price": 50600, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "stage2_false_positive_high_MAE", "round": "R8", "same_entry_group_id": "C26:035720:Stage2:2024-05-09", "score_return_alignment": "misaligned_low_MFE_high_MAE", "source_doc": "e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_proxy_only": true, "source_urls": ["https://koreajoongangdaily.joins.com/news/2024-05-09/business/industry/Kakao-reports-strong-Q1-operating-profit/2042952"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "035720", "trigger_date": "2024-05-09", "trigger_type": "Stage2", "trough_180D_date": "2024-11-14", "trough_180D_price": 32550, "trough_30D_price": 41800, "trough_90D_price": 32900, "window_180D_end_date": "2025-02-06"}
{"MAE_180D_pct": -17.67, "MAE_30D_pct": -5.61, "MAE_90D_pct": -16.83, "MFE_180D_pct": 43.81, "MFE_30D_pct": 18.62, "MFE_90D_pct": 43.81, "aggregate_role": "representative_for_aggregate", "calibration_block_reason": "", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_label": "positive", "company_name": "SOOP", "component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 5, "earnings_visibility": 13, "eps_fcf_revision": 14, "information_confidence": 12, "market_mispricing": 11, "total_after_c26_gate": 77, "total_current_proxy": 73, "valuation_rerating": 10}, "corporate_action_check": "profile candidate dates checked; no candidate date inside entry_date~D+180 window", "corporate_action_overlap_180D": false, "current_profile_error": false, "current_profile_verdict": "positive_control_C26_can_promote_when_ad_ecosystem_growth_and_margin_bridge_are_visible", "dedupe_key": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage2-Actionable|2024-11-01", "dedupe_role": "representative", "entry_date": "2024-11-01", "entry_price": 94500, "entry_price_basis": "close_c_column", "evidence_date": "2024-10-31", "evidence_family": "Q3_2024_platform_and_ad_ecosystem_growth", "evidence_summary": "Q3 2024 revenue and operating profit growth were tied to platform/ad ecosystem expansion, making this a cleaner C26 positive than generic traffic or rebrand narratives.", "fine_archetype_id": "CREATOR_PLATFORM_AD_ECOSYSTEM_OPERATING_LEVERAGE", "forward_180D_available": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market": "KOSDAQ GLOBAL", "peak_180D_date": "2025-02-06", "peak_180D_price": 135900, "peak_30D_price": 112100, "peak_90D_price": 135900, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "positive_control_with_moderate_MAE", "round": "R8", "same_entry_group_id": "C26:067160:Stage2-Actionable:2024-11-01", "score_return_alignment": "aligned_positive_high_MFE_moderate_MAE", "source_doc": "e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_proxy_only": false, "source_urls": ["https://v.daum.net/v/BoCoVLHERK?f=p"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "067160", "trigger_date": "2024-10-31", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-09", "trough_180D_price": 77800, "trough_30D_price": 89200, "trough_90D_price": 78600, "window_180D_end_date": "2025-07-29"}
{"MAE_180D_pct": -26.71, "MAE_30D_pct": -12.16, "MAE_90D_pct": -17.64, "MFE_180D_pct": 2.77, "MFE_30D_pct": 2.77, "MFE_90D_pct": 2.77, "aggregate_role": "representative_for_aggregate", "calibration_block_reason": "", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_label": "counterexample", "company_name": "KT nasmedia", "component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 4, "earnings_visibility": 8, "eps_fcf_revision": 7, "information_confidence": 9, "market_mispricing": 8, "total_after_c26_gate": 58, "total_current_proxy": 66, "valuation_rerating": 7}, "corporate_action_check": "profile candidate dates checked; no candidate date inside entry_date~D+180 window", "corporate_action_overlap_180D": false, "current_profile_error": true, "current_profile_verdict": "false_positive_risk_when_ad_tech_platform_language_lacks_actual_operating_leverage", "dedupe_key": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|089600|Stage2|2024-05-13", "dedupe_role": "representative", "entry_date": "2024-05-13", "entry_price": 18420, "entry_price_basis": "close_c_column", "evidence_date": "2024-05-13", "evidence_family": "digital_ad_recovery_expectation_vs_2024_revenue_OP_decline", "evidence_summary": "Ad-tech/media-rep platform vocabulary and OTT/OOH optionality did not yet produce durable 2024 operating leverage; official FY2024 release later showed revenue/OP contraction.", "fine_archetype_id": "MEDIA_REP_AD_TECH_PLATFORM_WITH_NO_DURABLE_OPERATING_LEVERAGE", "forward_180D_available": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market": "KOSDAQ", "peak_180D_date": "2024-05-16", "peak_180D_price": 18930, "peak_30D_price": 18930, "peak_90D_price": 18930, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "stage2_false_positive_low_MFE_late_180D_MAE", "round": "R8", "same_entry_group_id": "C26:089600:Stage2:2024-05-13", "score_return_alignment": "misaligned_low_MFE_late_high_MAE", "source_doc": "e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_proxy_only": true, "source_urls": ["https://www.nasmedia.co.kr/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/%EB%82%98%EC%8A%A4%EB%AF%B8%EB%94%94%EC%96%B4-4%EB%B6%84%EA%B8%B0-%EC%8B%A4%EC%A0%81-%EC%95%84%EC%89%AC%EC%9B%80-%EC%86%8D-%ED%94%8C%EB%9E%AB%ED%8F%BCbiz%EB%B6%80%EB%AC%B8-%EB%B0%98%EB%93%B1/"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "089600", "trigger_date": "2024-05-13", "trigger_type": "Stage2", "trough_180D_date": "2025-02-07", "trough_180D_price": 13500, "trough_30D_price": 16180, "trough_90D_price": 15170, "window_180D_end_date": "2025-02-10"}
{"MAE_180D_pct": -35.34, "MAE_30D_pct": -16.11, "MAE_90D_pct": -35.34, "MFE_180D_pct": 1.4, "MFE_30D_pct": 1.4, "MFE_90D_pct": 1.4, "aggregate_role": "representative_for_aggregate", "calibration_block_reason": "", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_label": "counterexample", "company_name": "Incross", "component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 4, "earnings_visibility": 8, "eps_fcf_revision": 6, "information_confidence": 10, "market_mispricing": 9, "total_after_c26_gate": 56, "total_current_proxy": 65, "valuation_rerating": 7}, "corporate_action_check": "profile candidate dates checked; no candidate date inside entry_date~D+180 window", "corporate_action_overlap_180D": false, "current_profile_error": true, "current_profile_verdict": "false_positive_risk_if_revenue_growth_without_durable_margin_leverage_gets_C26_credit", "dedupe_key": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage2|2024-05-03", "dedupe_role": "representative", "entry_date": "2024-05-03", "entry_price": 9310, "entry_price_basis": "close_c_column", "evidence_date": "2024-05-03", "evidence_family": "Q1_2024_ad_revenue_contraction_then_FY2024_revenue_up_OP_down", "evidence_summary": "Q1 weakness and later FY2024 revenue growth with OP decline show that top-line or new ad business alone is not enough; operating leverage must be durable.", "fine_archetype_id": "AD_AGENCY_TOPLINE_WITH_ONE_OFF_COST_AND_MARGIN_LEVERAGE_FAILURE", "forward_180D_available": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market": "KOSDAQ", "peak_180D_date": "2024-05-03", "peak_180D_price": 9440, "peak_30D_price": 9440, "peak_90D_price": 9440, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "stage2_false_positive_high_MAE", "round": "R8", "same_entry_group_id": "C26:216050:Stage2:2024-05-03", "score_return_alignment": "misaligned_low_MFE_high_MAE", "source_doc": "e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_proxy_only": true, "source_urls": ["https://www.incross.com/ko/investment/ir.asp?idx=10203&mode=view&page=1&pageSize=10&searchStr=&serboardsort="], "stock_web_manifest_max_date": "2026-02-20", "symbol": "216050", "trigger_date": "2024-05-03", "trigger_type": "Stage2", "trough_180D_date": "2024-08-06", "trough_180D_price": 6020, "trough_30D_price": 7810, "trough_90D_price": 6020, "window_180D_end_date": "2025-02-03"}
{"MAE_180D_pct": -39.92, "MAE_30D_pct": -20.93, "MAE_90D_pct": -30.16, "MFE_180D_pct": 7.17, "MFE_30D_pct": 7.17, "MFE_90D_pct": 7.17, "aggregate_role": "representative_for_aggregate_stage4b_overlay", "calibration_block_reason": "", "calibration_usable": true, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "case_label": "counterexample", "company_name": "FSN", "component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 2, "earnings_visibility": 7, "eps_fcf_revision": 7, "information_confidence": 8, "market_mispricing": 11, "total_after_c26_gate": 54, "total_current_proxy": 64, "valuation_rerating": 7}, "corporate_action_check": "profile candidate dates checked; no candidate date inside entry_date~D+180 window", "corporate_action_overlap_180D": false, "current_profile_error": true, "current_profile_verdict": "local_4B_watch_guard_needed; do_not_route_to_hard_4C_because_later_business_conversion_reappeared", "dedupe_key": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214270|Stage4B|2024-03-20", "dedupe_role": "representative", "entry_date": "2024-03-20", "entry_price": 2580, "entry_price_basis": "close_c_column", "evidence_date": "2024-03-19", "evidence_family": "AI_ad_marketing_response_later_conversion_but_entry_window_drawdown", "evidence_summary": "FSN later showed AI-ad/marketing segment improvement, but the early 2024 entry window had capital-raise/overhang and severe drawdown; treat as local 4B guardrail, not hard 4C.", "fine_archetype_id": "AI_AD_RESPONSE_WITH_CAPITAL_RAISE_AND_EARLY_PRICE_OVERHANG", "forward_180D_available": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "market": "KOSDAQ", "peak_180D_date": "2024-03-20", "peak_180D_price": 2765, "peak_30D_price": 2765, "peak_90D_price": 2765, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "local_4B_timing_guardrail_high_MAE", "round": "R8", "same_entry_group_id": "C26:214270:Stage4B:2024-03-20", "score_return_alignment": "misaligned_early_entry_high_MAE_but_later_business_repair_possible", "source_doc": "e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_proxy_only": false, "source_urls": ["https://fsn.co.kr/ir/news/82"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "214270", "trigger_date": "2024-03-19", "trigger_type": "Stage4B", "trough_180D_date": "2024-08-06", "trough_180D_price": 1550, "trough_30D_price": 2040, "trough_90D_price": 1802, "window_180D_end_date": "2024-12-12"}
```

## 8. Score simulation rows

These are research-only shadow simulations, not production scoring changes.

```jsonl
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 7, "earnings_visibility": 14, "eps_fcf_revision": 16, "information_confidence": 12, "market_mispricing": 10, "total_after_c26_gate": 80, "total_current_proxy": 78, "valuation_rerating": 11}, "current_profile_verdict": "mostly_correct_positive_but_C26_specific_gate_should_reward_direct_ad_revenue_plus_margin_bridge", "production_scoring_changed": false, "proposed_shadow_rule_effect": "downscore source-proxy platform/ad vocabulary unless ad revenue + margin bridge is explicit; upscore direct ad revenue operating leverage positives", "row_type": "score_simulation", "shadow_weight_only": true, "symbol": "035420", "trigger_type": "Stage2-Actionable"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 5, "earnings_visibility": 12, "eps_fcf_revision": 10, "information_confidence": 11, "market_mispricing": 10, "total_after_c26_gate": 65, "total_current_proxy": 73, "valuation_rerating": 9}, "current_profile_verdict": "false_positive_risk_if_broad_platform_rebound_is_scored_as_C26_ad_operating_leverage", "production_scoring_changed": false, "proposed_shadow_rule_effect": "downscore source-proxy platform/ad vocabulary unless ad revenue + margin bridge is explicit; upscore direct ad revenue operating leverage positives", "row_type": "score_simulation", "shadow_weight_only": true, "symbol": "035720", "trigger_type": "Stage2"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 5, "earnings_visibility": 13, "eps_fcf_revision": 14, "information_confidence": 12, "market_mispricing": 11, "total_after_c26_gate": 77, "total_current_proxy": 73, "valuation_rerating": 10}, "current_profile_verdict": "positive_control_C26_can_promote_when_ad_ecosystem_growth_and_margin_bridge_are_visible", "production_scoring_changed": false, "proposed_shadow_rule_effect": "downscore source-proxy platform/ad vocabulary unless ad revenue + margin bridge is explicit; upscore direct ad revenue operating leverage positives", "row_type": "score_simulation", "shadow_weight_only": true, "symbol": "067160", "trigger_type": "Stage2-Actionable"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 4, "earnings_visibility": 8, "eps_fcf_revision": 7, "information_confidence": 9, "market_mispricing": 8, "total_after_c26_gate": 58, "total_current_proxy": 66, "valuation_rerating": 7}, "current_profile_verdict": "false_positive_risk_when_ad_tech_platform_language_lacks_actual_operating_leverage", "production_scoring_changed": false, "proposed_shadow_rule_effect": "downscore source-proxy platform/ad vocabulary unless ad revenue + margin bridge is explicit; upscore direct ad revenue operating leverage positives", "row_type": "score_simulation", "shadow_weight_only": true, "symbol": "089600", "trigger_type": "Stage2"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 4, "earnings_visibility": 8, "eps_fcf_revision": 6, "information_confidence": 10, "market_mispricing": 9, "total_after_c26_gate": 56, "total_current_proxy": 65, "valuation_rerating": 7}, "current_profile_verdict": "false_positive_risk_if_revenue_growth_without_durable_margin_leverage_gets_C26_credit", "production_scoring_changed": false, "proposed_shadow_rule_effect": "downscore source-proxy platform/ad vocabulary unless ad revenue + margin bridge is explicit; upscore direct ad revenue operating leverage positives", "row_type": "score_simulation", "shadow_weight_only": true, "symbol": "216050", "trigger_type": "Stage2"}
{"canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 2, "earnings_visibility": 7, "eps_fcf_revision": 7, "information_confidence": 8, "market_mispricing": 11, "total_after_c26_gate": 54, "total_current_proxy": 64, "valuation_rerating": 7}, "current_profile_verdict": "local_4B_watch_guard_needed; do_not_route_to_hard_4C_because_later_business_conversion_reappeared", "production_scoring_changed": false, "proposed_shadow_rule_effect": "downscore source-proxy platform/ad vocabulary unless ad revenue + margin bridge is explicit; upscore direct ad revenue operating leverage positives", "row_type": "score_simulation", "shadow_weight_only": true, "symbol": "214270", "trigger_type": "Stage4B"}
```

## 9. Aggregate row

```json
{"avg_counterexample_MAE_90D_pct": -28.86, "avg_counterexample_MFE_90D_pct": 3.87, "avg_positive_MAE_90D_pct": -9.3, "avg_positive_MFE_90D_pct": 39.34, "calibration_usable_case_count": 6, "calibration_usable_trigger_count": 6, "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "canonical_archetype_rule_candidate": "C26_AD_REVENUE_OPERATING_LEVERAGE_REQUIRES_DURABLE_AD_PRODUCT_AND_COST_DISCIPLINE_GATE", "counterexample_count": 4, "current_profile_error_count": 4, "fine_archetype_id": "PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_VS_TRAFFIC_AND_PRODUCT_PROXY", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "new_independent_case_count": 6, "new_independent_ratio": 1.0, "positive_case_count": 2, "production_scoring_changed": false, "representative_trigger_count": 6, "reused_case_count": 0, "round": "R8", "row_type": "aggregate_summary", "same_archetype_new_symbol_count": 6, "same_archetype_new_trigger_family_count": 6, "selected_loop": 134, "shadow_weight_only": true, "source_doc": "e2r_stock_web_v12_residual_round_R8_loop_134_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "stage4b_overlay_count": 1, "stage4c_case_count": 0}
```

## 10. Shadow weight candidate

```json
{"axis": "C26_AD_REVENUE_OPERATING_LEVERAGE_REQUIRES_DURABLE_AD_PRODUCT_AND_COST_DISCIPLINE_GATE", "candidate_effect": "Require direct ad-revenue/product monetization plus cost discipline or margin expansion before Stage2-Actionable/Stage3-Yellow credit; downgrade traffic/product/AI-ad proxy without monetization bridge to Stage2-watch or Stage4B overlay.", "do_not_propose_new_weight_delta": false, "evidence_support": "NAVER and SOOP positives have direct ad revenue + operating leverage and high MFE; Kakao, KT nasmedia, Incross, FSN show low-MFE/high-MAE when the bridge is broad, weak, or overhang-contaminated.", "production_scoring_changed": false, "row_type": "shadow_weight_candidate", "scope": "canonical_archetype_id=C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "shadow_weight_only": true}
```

## 11. Residual contribution

```json
{"current_profile_remaining_error": "C26 can still over-score generic platform traffic, AI advertising buzzword, or top-line growth without durable ad revenue and operating-margin bridge.", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": [], "expected_batch_ingest_value": "Adds 6 representative C26 rows with verified URLs and complete 30/90/180D MFE/MAE, useful for Priority 2 URL/proxy quality repair.", "new_axis_proposed": "C26_AD_REVENUE_OPERATING_LEVERAGE_REQUIRES_DURABLE_AD_PRODUCT_AND_COST_DISCIPLINE_GATE", "residual_type": "quality_repair_and_source_proxy_replacement", "row_type": "residual_contribution"}
```

## 12. Batch-ingest self audit

```text
required_filename_regex: pass
compact_filename_forbidden: pass
filename_round_matches_metadata_round: pass
filename_loop_matches_metadata_loop: pass
round_sector_consistency: pass
canonical_archetype_id_present: pass
large_sector_id_present: pass
price_source_present: pass
price_basis_present: pass
price_adjustment_status_present: pass
entry_price_basis_close_c_column: pass
complete_30_90_180_mfe_mae_in_every_trigger_row: pass
trigger_type_canonical_stage_label: pass
same_entry_group_id_present: pass
dedupe_role_present: pass
calibration_usable_flag_present: pass
positive_case_count: 2
counterexample_count: 4
stage4b_overlay_count: 1
stage4c_case_count: 0
new_independent_case_count: 6
new_symbol_count: 6
hard_duplicate_count: 0
source_proxy_replacement_or_URL_repair: pass
current_profile_stress_test_included: pass
score_return_alignment_included: pass
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 13. Sources

- MAIN_EXECUTION_PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO_REPEAT_INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- STOCK_WEB_MANIFEST: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- NAVER_Q3_2024_YNA: https://en.yna.co.kr/view/AEN20241108001152320
- NAVER_Q3_2024_AJUPRESS: https://www.ajupress.com/view/20241108103437767
- KAKAO_Q1_2024_KOREA_JOONGANG: https://koreajoongangdaily.joins.com/news/2024-05-09/business/industry/Kakao-reports-strong-Q1-operating-profit/2042952
- SOOP_Q3_2024_DAUM_EN: https://v.daum.net/v/BoCoVLHERK?f=p
- NASMEDIA_FY2024_OFFICIAL: https://www.nasmedia.co.kr/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C/%EB%82%98%EC%8A%A4%EB%AF%B8%EB%94%94%EC%96%B4-4%EB%B6%84%EA%B8%B0-%EC%8B%A4%EC%A0%81-%EC%95%84%EC%89%AC%EC%9B%80-%EC%86%8D-%ED%94%8C%EB%9E%AB%ED%8F%BCbiz%EB%B6%80%EB%AC%B8-%EB%B0%98%EB%93%B1/
- INCROSS_FY2024_OFFICIAL_IR: https://www.incross.com/ko/investment/ir.asp?idx=10203&mode=view&page=1&pageSize=10&searchStr=&serboardsort=
- FSN_FY2024_OFFICIAL: https://fsn.co.kr/ir/news/82

## 14. Next research state

```text
completed_round: R8
completed_loop: 134
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / over_50_rows_quality_repair / C26 rows 106
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_4B_4C_REPAIR
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_COUNTEREXAMPLE_REPAIR
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_HARD_4C_REPAIR
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_URL_REPAIR
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_URL_REPAIR
```

## 15. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batch-applying v12 research artifacts later, ingest this MD as a standard v12 result file. Validate all trigger rows using canonical keys, complete 30/90/180D MFE/MAE fields, and dedupe key canonical_archetype_id + symbol + trigger_type + entry_date. Treat the rule candidate C26_AD_REVENUE_OPERATING_LEVERAGE_REQUIRES_DURABLE_AD_PRODUCT_AND_COST_DISCIPLINE_GATE as a shadow candidate only until merged with other C26 quality-repair rows.

Implementation intent for a later coding agent:
- In C26, raise confidence only when direct ad revenue / platform monetization / paid product growth and operating-margin leverage are both present.
- Cap broad platform traffic, AI-ad vocabulary, product launch, media-rep optionality, and top-line-only recovery at Stage2-watch unless margin bridge exists.
- Treat FSN-like severe early-entry drawdown with later business repair as local Stage4B guardrail, not automatic hard Stage4C.
- Do not change production scoring from this single MD alone.
```
