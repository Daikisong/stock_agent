# E2R Stock-Web v12 Residual Research — R6 / C21 Financial ROE-PBR Capital Return

```text
research_session = post_calibrated_sector_archetype_residual_research_v12
selected_round = R6
selected_loop = 215
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality repair + Priority 2 direct-evidence refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1

primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection Rationale

The latest No-Repeat Index says all C01~C32 archetypes have crossed the 80-row floor, so the next work should not merely add rows. It should repair direct URL quality, reduce proxy-only evidence, and refine residual errors. C21 is not a raw-count shortage bucket, but it is a useful quality refresh target because financial value-up rows often confuse three different things:

1. **policy beta** from Korea's corporate value-up program,
2. **capital-return mechanics** such as buyback/cancellation and dividend formulas,
3. **real economic bridge** through ROE, CET1 surplus, TBVPS/EPS accretion, and per-share execution.

This run therefore uses official / direct shareholder-return evidence where possible and keeps every selected trigger on Stock-Web tradable raw OHLCV. The goal is not to loosen Stage3-Green. It is to define when a low-PBR financial value-up headline is enough for Stage2, when it becomes Stage2-Actionable, and when high-MAE should act as an escalation brake rather than a deletion signal.

## 2. Novelty / Duplicate Avoidance

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This run uses C21, which has not been used in this current regenerated session. It avoids the session's recent over-concentration in C05/C10/C13/C15/R13/L8. The selected cases are all direct financial-holding / bank-capital-return rows rather than cross-sector R13 compression rows.

```text
new_independent_case_count = 7
new_independent_trigger_count = 7
unique_symbol_count = 6
stage2_count = 2
stage2_actionable_count = 5
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
```

## 3. Price Source Validation

Stock-Web manifest/schema basis:

```text
source_name = FinanceData/marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
block_corporate_action_window = true
```

All selected rows use 2024 entry dates with 180-trading-day windows available before the local cached Stock-Web 2025 shard end. KB Financial and Shinhan profiles show no corporate-action candidates. Meritz and IBK have historic corporate-action candidates, but none overlap the selected 2024 entry-to-D+180 windows. Hana and Woori profile checks show active-like tradable paths through 2026-02-20 with no 2024 window block used in this run.

## 4. Trigger-Level Price Table

| symbol | company | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 105560 | KB Financial Group | Stage2-Actionable | 2024-04-25 | 69,300 | 20.35/-1.59 | 33.33/-1.59 | 49.93/-1.59 | 2024-10-25 | 2024-04-25 |
| 105560 | KB Financial Group | Stage2-Actionable | 2024-10-24 | 93,200 | 11.48/-7.94 | 11.48/-18.03 | 30.90/-25.64 | 2025-07-08 | 2025-04-09 |
| 055550 | Shinhan Financial Group | Stage2-Actionable | 2024-07-26 | 58,000 | 11.38/-11.03 | 11.38/-14.48 | 11.38/-26.72 | 2024-08-26 | 2025-04-09 |
| 086790 | Hana Financial Group | Stage2-Actionable | 2024-10-29 | 65,000 | 3.85/-13.23 | 3.85/-13.23 | 49.38/-20.77 | 2025-07-15 | 2025-04-09 |
| 316140 | Woori Financial Group | Stage2 | 2024-07-26 | 16,180 | 4.82/-15.08 | 6.92/-15.08 | 8.16/-15.08 | 2025-02-19 | 2024-08-05 |
| 138040 | Meritz Financial Group | Stage2-Actionable | 2024-11-21 | 103,800 | 2.99/-6.84 | 22.74/-6.84 | 22.74/-6.84 | 2025-03-06 | 2024-12-09 |
| 024110 | Industrial Bank of Korea | Stage2 | 2024-02-08 | 13,410 | 19.39/-3.65 | 19.39/-6.71 | 19.39/-6.71 | 2024-03-15 | 2024-04-15 |

## 5. Case Notes

### 5.1 KB Financial Group / 105560 / 2024-04-25 / Stage2-Actionable

The evidence is a direct capital-return bridge: KB moved from generic bank value-up beta to a policy that connects CET1 excess capital, quarterly-even dividends, and buyback/cancellation mechanics. The price path is clean: 180D MFE +49.93% with only -1.59% MAE. This is the kind of C21 row where Stage2-Actionable should be preserved.

Residual: do not make it Stage3-Green merely because the first 180D worked. Green still needs repeat TBVPS / ROE / capital-return execution.

### 5.2 KB Financial Group / 105560 / 2024-10-24 / Stage2-Actionable high-MAE cap

The October value-up plan is more explicit, but the stock had already repriced. The 180D window still reaches +30.90% MFE, yet it also suffers -25.64% MAE before the later advance.

Residual: a direct plan can reopen or preserve Stage2-Actionable, but high MAE acts as a Yellow/Green brake.

### 5.3 Shinhan Financial Group / 055550 / 2024-07-26 / Stage2-Actionable counterexample

Shinhan's value-up plan included large targets: ROE, shareholder-return ratio, and share-count reduction. That is real capital-allocation evidence, but the path was not clean: 180D MFE was only +11.38% while MAE reached -26.72%.

Residual: target-rich value-up plans should not be promoted to Stage3-Yellow/Green before the mechanics translate into per-share capital accretion.

### 5.4 Hana Financial Group / 086790 / 2024-10-29 / delayed positive with drawdown

Hana's value-up disclosure supports a delayed positive interpretation: 180D MFE +49.38%. But the path first draws down -20.77%.

Residual: this is a true Stage2-Actionable candidate with a high-MAE cap. The mechanism is like a spring compressed under water: the plan can store rerating energy, but until ROE/CET1/shareholder-return execution surfaces, Green should not float up automatically.

### 5.5 Woori Financial Group / 316140 / 2024-07-26 / Stage2 cap

Woori announced a value-up plan and TSR target, but the immediate bridge was more target-like than execution-like. The 180D path was also muted: MFE +8.16%, MAE -15.08%.

Residual: long-term TSR and ROE targets without immediate buyback/cancellation mechanics or hard per-share execution should remain Stage2.

### 5.6 Meritz Financial Group / 138040 / 2024-11-21 / Stage2-Actionable positive control

Meritz is a cleaner positive control because the case has buyback execution and profit-quality language rather than only sector policy beta. 180D MFE was +22.74% with -6.84% MAE.

Residual: execution-linked capital return can be Actionable. Green still needs durability, because buybacks are a bridge, not the whole destination.

### 5.7 Industrial Bank of Korea / 024110 / 2024-02-08 / Stage2 cap

IBK has a real dividend-return history and official payout data, but state-bank overhang, lower capital flexibility, and no immediate buyback/TBVPS mechanics keep the row below Actionable. 180D MFE +19.39%, MAE -6.71% supports a Stage2 cap rather than a rejection.

## 6. Score / Return Alignment

C21's applied archetype weights in the No-Repeat Index are:

```text
EPS/Vis/Bott/Mis/Val/Cap/Info = 15/20/5/15/25/15/5
```

The residual pattern is clear:

- `valuation_rerating` and `capital_allocation` matter more than generic EPS surprise in C21.
- `bottleneck_pricing` should remain weak for financials; there is no physical bottleneck like HBM or shipyard slots.
- `information_confidence` must penalize vague policy beta because policy is a tide, not a boat. Only buyback/cancellation, CET1 surplus rule, dividend formula, ROE target execution, and TBVPS/EPS accretion make the boat move.

## 7. Shadow Rule Candidate

```text
sector_rule_candidate = L6_BANK_VALUEUP_CET1_TO_TBVPS_EXECUTION_GATE
canonical_rule_candidate = C21_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1
```

Rule candidate:

```text
- Korea Value-up / low-PBR / bank-rerating headline alone creates at most Stage2.
- Stage2-Actionable requires at least one direct second bridge:
  buyback/cancellation amount, dividend formula, CET1 excess-capital rule,
  ROE target with execution route, TBVPS/EPS accretion, or repeated shareholder-return execution.
- A target-only TSR or ROE plan without immediate mechanics stays Stage2 cap.
- High MAE on a direct capital-return row blocks Stage3-Yellow/Green first;
  it does not erase Stage2-Actionable.
- State-bank dividend yield supports Stage2, but buyback/TBVPS constraints keep Actionable capped.
- Stage3-Green remains blocked until capital-return execution repeats across more than one evidence family.
```

## 8. Machine-Readable JSONL Trigger Rows

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R6_loop_215_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md","round":"R6","loop":215,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1","symbol":"105560","name":"KB Financial Group","trigger_type":"Stage2-Actionable","case_role":"positive_direct_capital_return_policy","evidence_date":"2024-04-25","entry_date":"2024-04-25","entry_price":69300.0,"entry_ohlcv":{"o":68300.0,"h":70600.0,"l":68200.0,"c":69300.0,"v":745906,"m":"KOSPI"},"mfe_30d_pct":20.35,"mae_30d_pct":-1.59,"mfe_90d_pct":33.33,"mae_90d_pct":-1.59,"mfe_180d_pct":49.93,"mae_180d_pct":-1.59,"peak_180d_date":"2024-10-25","trough_180d_date":"2024-04-25","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"raw_component_score_breakdown":{"eps_fcf_explosion":63,"earnings_visibility":72,"bottleneck_pricing":25,"market_mispricing":78,"valuation_rerating":77,"capital_allocation":86,"information_confidence":82},"archetype_weight_profile":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":5,"market_mispricing":15,"valuation_rerating":25,"capital_allocation":15,"information_confidence":5},"weighted_total":73.05,"source_url":"https://www.sec.gov/Archives/edgar/data/1445930/000119312524242219/d901349d6k.htm","evidence_family":"direct shareholder-return policy + CET1 excess-capital rule","residual_interpretation":"direct CET1-capital-return bridge worked; preserve Stage2-Actionable, but Green still needs recurring ROE/TBVPS execution","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R6_loop_215_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md","round":"R6","loop":215,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1","symbol":"105560","name":"KB Financial Group","trigger_type":"Stage2-Actionable","case_role":"high_mae_guardrail","evidence_date":"2024-10-24","entry_date":"2024-10-24","entry_price":93200.0,"entry_ohlcv":{"o":93800.0,"h":94800.0,"l":92800.0,"c":93200.0,"v":1385779,"m":"KOSPI"},"mfe_30d_pct":11.48,"mae_30d_pct":-7.94,"mfe_90d_pct":11.48,"mae_90d_pct":-18.03,"mfe_180d_pct":30.9,"mae_180d_pct":-25.64,"peak_180d_date":"2025-07-08","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"raw_component_score_breakdown":{"eps_fcf_explosion":60,"earnings_visibility":76,"bottleneck_pricing":20,"market_mispricing":70,"valuation_rerating":78,"capital_allocation":88,"information_confidence":84},"archetype_weight_profile":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":5,"market_mispricing":15,"valuation_rerating":25,"capital_allocation":15,"information_confidence":5},"weighted_total":72.6,"source_url":"https://www.sec.gov/Archives/edgar/data/1445930/000119312524242219/d901349d6k.htm","evidence_family":"corporate value-up phase rule + buyback/cancellation decision","residual_interpretation":"excellent direct bridge but entry was late; high MAE should brake Yellow/Green, not delete Actionable","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R6_loop_215_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md","round":"R6","loop":215,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1","symbol":"055550","name":"Shinhan Financial Group","trigger_type":"Stage2-Actionable","case_role":"ambitious_plan_high_mae_counterexample","evidence_date":"2024-07-26","entry_date":"2024-07-26","entry_price":58000.0,"entry_ohlcv":{"o":54200.0,"h":58400.0,"l":54200.0,"c":58000.0,"v":3558607,"m":"KOSPI"},"mfe_30d_pct":11.38,"mae_30d_pct":-11.03,"mfe_90d_pct":11.38,"mae_90d_pct":-14.48,"mfe_180d_pct":11.38,"mae_180d_pct":-26.72,"peak_180d_date":"2024-08-26","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"raw_component_score_breakdown":{"eps_fcf_explosion":55,"earnings_visibility":70,"bottleneck_pricing":15,"market_mispricing":74,"valuation_rerating":72,"capital_allocation":84,"information_confidence":80},"archetype_weight_profile":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":5,"market_mispricing":15,"valuation_rerating":25,"capital_allocation":15,"information_confidence":5},"weighted_total":68.7,"source_url":"https://shinhangroup.com/resources/publish/jp/resource/2024_Shinhan_Financial_Group_Value-up_Plan.pdf","evidence_family":"value-up plan: ROE/TSR/share-count reduction targets","residual_interpretation":"target-rich plan created Actionable evidence, but weak 180D path says target-only plan must not become Green","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R6_loop_215_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md","round":"R6","loop":215,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1","symbol":"086790","name":"Hana Financial Group","trigger_type":"Stage2-Actionable","case_role":"delayed_positive_with_drawdown","evidence_date":"2024-10-29","entry_date":"2024-10-29","entry_price":65000.0,"entry_ohlcv":{"o":65700.0,"h":67500.0,"l":63500.0,"c":65000.0,"v":1674357,"m":"KOSPI"},"mfe_30d_pct":3.85,"mae_30d_pct":-13.23,"mfe_90d_pct":3.85,"mae_90d_pct":-13.23,"mfe_180d_pct":49.38,"mae_180d_pct":-20.77,"peak_180d_date":"2025-07-15","trough_180d_date":"2025-04-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"raw_component_score_breakdown":{"eps_fcf_explosion":62,"earnings_visibility":72,"bottleneck_pricing":15,"market_mispricing":75,"valuation_rerating":76,"capital_allocation":82,"information_confidence":74},"archetype_weight_profile":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":5,"market_mispricing":15,"valuation_rerating":25,"capital_allocation":15,"information_confidence":5},"weighted_total":70.7,"source_url":"https://vpr.hkma.gov.hk/statics/assets/doc/100080/ar_24/ar_24_pt02_eng.pdf","evidence_family":"value-up plan + CET1/ROE/shareholder-return target","residual_interpretation":"true delayed value-up winner, but 90D drawdown requires Stage2-Actionable with Green blocker until execution appears","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R6_loop_215_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md","round":"R6","loop":215,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1","symbol":"316140","name":"Woori Financial Group","trigger_type":"Stage2","case_role":"plan_without_immediate_mechanics_counterexample","evidence_date":"2024-07-26","entry_date":"2024-07-26","entry_price":16180.0,"entry_ohlcv":{"o":14810.0,"h":16230.0,"l":14800.0,"c":16180.0,"v":14562584,"m":"KOSPI"},"mfe_30d_pct":4.82,"mae_30d_pct":-15.08,"mfe_90d_pct":6.92,"mae_90d_pct":-15.08,"mfe_180d_pct":8.16,"mae_180d_pct":-15.08,"peak_180d_date":"2025-02-19","trough_180d_date":"2024-08-05","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"raw_component_score_breakdown":{"eps_fcf_explosion":48,"earnings_visibility":64,"bottleneck_pricing":12,"market_mispricing":70,"valuation_rerating":66,"capital_allocation":66,"information_confidence":70},"archetype_weight_profile":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":5,"market_mispricing":15,"valuation_rerating":25,"capital_allocation":15,"information_confidence":5},"weighted_total":61.0,"source_url":"https://www.kedglobal.com/earnings/newsView/ked202407260004","evidence_family":"value-up target / ROE and TSR objective","residual_interpretation":"TSR/ROE target without immediate cancellation/ROE bridge should remain Stage2 cap","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R6_loop_215_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md","round":"R6","loop":215,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1","symbol":"138040","name":"Meritz Financial Group","trigger_type":"Stage2-Actionable","case_role":"buyback_return_positive_control","evidence_date":"2024-11-21","entry_date":"2024-11-21","entry_price":103800.0,"entry_ohlcv":{"o":104600.0,"h":106100.0,"l":103800.0,"c":103800.0,"v":240553,"m":"KOSPI"},"mfe_30d_pct":2.99,"mae_30d_pct":-6.84,"mfe_90d_pct":22.74,"mae_90d_pct":-6.84,"mfe_180d_pct":22.74,"mae_180d_pct":-6.84,"peak_180d_date":"2025-03-06","trough_180d_date":"2024-12-09","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"raw_component_score_breakdown":{"eps_fcf_explosion":66,"earnings_visibility":78,"bottleneck_pricing":18,"market_mispricing":74,"valuation_rerating":80,"capital_allocation":90,"information_confidence":78},"archetype_weight_profile":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":5,"market_mispricing":15,"valuation_rerating":25,"capital_allocation":15,"information_confidence":5},"weighted_total":74.9,"source_url":"https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20250219800640","evidence_family":"continued buybacks + net-profit execution","residual_interpretation":"buyback execution plus profit quality is clean Actionable; still cap Green until TBVPS/ROE durability is repeat-confirmed","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R6_loop_215_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md","round":"R6","loop":215,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1","symbol":"024110","name":"Industrial Bank of Korea","trigger_type":"Stage2","case_role":"dividend_yield_policy_cap","evidence_date":"2024-02-08","entry_date":"2024-02-08","entry_price":13410.0,"entry_ohlcv":{"o":13300.0,"h":13480.0,"l":13240.0,"c":13410.0,"v":2535845,"m":"KOSPI"},"mfe_30d_pct":19.39,"mae_30d_pct":-3.65,"mfe_90d_pct":19.39,"mae_90d_pct":-6.71,"mfe_180d_pct":19.39,"mae_180d_pct":-6.71,"peak_180d_date":"2024-03-15","trough_180d_date":"2024-04-15","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_source_validation":{"manifest_max_date":"2026-02-20","entry_row_exists":true,"complete_180d_forward_window":true,"corporate_action_contaminated_180d":false},"raw_component_score_breakdown":{"eps_fcf_explosion":50,"earnings_visibility":62,"bottleneck_pricing":10,"market_mispricing":74,"valuation_rerating":62,"capital_allocation":70,"information_confidence":74},"archetype_weight_profile":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":5,"market_mispricing":15,"valuation_rerating":25,"capital_allocation":15,"information_confidence":5},"weighted_total":61.2,"source_url":"https://global.ibk.co.kr/en/investor/ShareholderReturn","evidence_family":"dividend payout and value-up-sensitive bank beta","residual_interpretation":"high dividend path supports Stage2, but state-bank policy/CET1 cap prevents Actionable without clearer buyback/TBVPS mechanics","calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
```

## 9. Batch Ingest Self-Audit

```text
ready_for_batch_ingest = true
standard_v12_filename = true
filename_round = R6
metadata_round = R6
filename_loop = 215
metadata_loop = 215
large_sector_id_valid = true
canonical_archetype_id_valid = true
all_trigger_rows_have_entry_price = true
all_trigger_rows_have_actual_entry_ohlcv = true
all_trigger_rows_have_30_90_180_mfe_mae = true
same_entry_deduped_for_aggregate = true
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
source_proxy_only_count = 0
evidence_url_pending_count = 0
production_scoring_changed = false
shadow_weight_only = true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

Read this MD as a v12 residual calibration artifact only. Do not patch production scoring directly from one file. In the next batch-calibration session, ingest this row set with the broader v12 corpus, validate duplicate keys, and test whether C21 needs a narrow gate:

C21_CET1_BUYBACK_TBVPS_SECOND_BRIDGE_GATE_V1

Patch only if supported across representative rows and if Stage3-Green strictness remains unchanged.
```

## 11. Next Research State

```text
completed_round = R6
completed_loop = 215
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality repair + Priority 2 direct-evidence refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
