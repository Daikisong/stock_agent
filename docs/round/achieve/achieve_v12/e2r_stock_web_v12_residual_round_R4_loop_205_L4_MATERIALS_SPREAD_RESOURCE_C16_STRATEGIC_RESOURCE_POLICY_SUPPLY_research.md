# E2R Stock-Web v12 Residual Research — R4 / L4 / C16 Strategic Resource Policy Supply

```text
output_file = e2r_stock_web_v12_residual_round_R4_loop_205_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection / Novelty Audit

```text
selected_round: R4
selected_loop: 205
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_EARTH_EXPORT_CONTROL_PROXY_THEME_AND_DIRECT_SUPPLY_BRIDGE
selected_priority_bucket: Priority 2 quality reinforcement / proxy-theme and direct-supply bridge repair
```

NO-REPEAT INDEX is used only as a duplicate-prevention ledger. Current cumulative v12 corpus is no longer in a simple 30/50/80-row filling phase. C16 already has enough rows, but the L4 sector still carries a high URL/proxy burden and C16 has a structural weakness: strategic-resource policy headlines often look like supply-chain rerating evidence while failing to connect to issuer-level order, offtake, margin, or cash conversion.

This loop intentionally avoids the immediately repeated C01/C02/C05/C10/C13/R13 axes and re-enters L4/C16 with a different micro-regime: **China rare-earth export-control theme spike vs direct copper/lithium supply bridge**.

### Hard duplicate check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
batch_duplicate_status = pass
same_entry_trigger_deduped = true
```

New duplicate keys in this MD:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|000910|Stage4B|2025-04-14
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047400|Stage4B|2025-04-14
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|004560|Stage2|2025-04-14
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|Stage2-Actionable|2024-06-03
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage4B|2023-11-29
```

Narrative-only, not calibration usable:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001570|Stage4C|2024-10-02
blocked_reason = insufficient_forward_window_in_stock_web_after_trading_suspension
```

## 2. Price Atlas Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

All five usable trigger rows have actual entry OHLCV, complete 30D/90D/180D MFE/MAE, positive OHLCV, and 180 tradable rows. No corporate-action contamination was detected in the entry-to-180D calibration windows based on the local Stock-Web tradable shards used for this MD.

| symbol | entry row d/o/h/l/c/v/a/mc/s/m | shard |
|---:|---|---|
| 000910 | 2025-04-14 / 6,770 / 6,850 / 6,270 / 6,330 / 9,928,457 / 65,201,995,320 / 98,821,548,270 / 15,611,619 / KOSPI | atlas/ohlcv_tradable_by_symbol_year/000/000910/2025.csv |
| 047400 | 2025-04-14 / 2,205 / 2,350 / 2,110 / 2,125 / 4,236,395 / 9,378,719,018 / 89,250,000,000 / 42,000,000 / KOSPI | atlas/ohlcv_tradable_by_symbol_year/047/047400/2025.csv |
| 004560 | 2025-04-14 / 11,830 / 12,330 / 11,350 / 12,170 / 207,379 / 2,458,663,440 / 183,509,129,870 / 15,078,811 / KOSPI | atlas/ohlcv_tradable_by_symbol_year/004/004560/2025.csv |
| 006260 | 2024-06-03 / 170,200 / 172,000 / 163,900 / 169,800 / 524,575 / 87,806,363,900 / 5,467,560,000,000 / 32,200,000 / KOSPI | atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv |
| 005490 | 2023-11-29 / 480,000 / 485,500 / 474,000 / 483,000 / 537,203 / 257,440,359,000 / 40,847,904,090,000 / 84,571,230 / KOSPI | atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv |


## 3. Evidence Map

| case_id | evidence timing | source quality | evidence summary | URLs |
|---|---|---|---|---|
| C16L205_001_000910_20250414_RARE_EARTH_PARENT_PROXY_4B | 2025-04-14 | verified_market_theme_source | China rare-earth and magnet export-control headline drove Union/Union Materials theme spike; Union is parent of Union Materials, but no issuer-level resource volume, offtake, margin, or cashflow bridge was confirmed. | https://www.mk.co.kr/en/stock/11290565<br>https://www.asiae.co.kr/en/article/2025041410122919612 |
| C16L205_002_047400_20250414_FERRITE_MAGNET_PROXY_4B | 2025-04-14 | verified_market_theme_source | Union Materials was cited as a ferrite magnet producer and rare-earth substitute theme beneficiary, but the evidence did not establish customer pull, shipment conversion, ASP, margin, or capacity allocation. | https://www.mk.co.kr/en/stock/11290565<br>https://www.asiae.co.kr/en/article/2025041410122919612 |
| C16L205_003_004560_20250414_SEONGLIM_STAKE_STAGE2_CAP | 2025-04-14 | verified_market_source_with_indirect_company_bridge | Hyundai BNG Steel was cited as holding shares in Seongrim Advanced Industry, described as Korea’s only domestic rare-earth permanent magnet manufacturer; the bridge is better than a pure theme proxy but still indirect. | https://www.asiae.co.kr/en/article/2025041410122919612<br>https://www.mk.co.kr/en/stock/11290565 |
| C16L205_004_006260_20240603_LSMNM_BHP_CONTRACT_LATE_STAGE2_FAIL | 2024-06-02 | verified_company_or_business_source | LS MnM signed a five-year BHP copper-concentrate purchase agreement for 1.73 million tons; this is a direct strategic supply bridge, but the equity entry occurred near a local peak and failed the forward return test. | https://www.asiae.co.kr/en/article/2024053120012819289 |
| C16L205_005_005490_20231129_LITHIUM_HYDROXIDE_LONG_LEAD_4B | 2023-11-30 | verified_company_or_business_source | POSCO-Pilbara Lithium Solution opened Train 1 of the Gwangyang lithium hydroxide facility; the plant created resource-supply optionality, but the evidence was long-lead capacity rather than near-term margin/cashflow conversion. | https://www.pls.com/news-stories/posco-pilbara-minerals-jv-opens-south-korean-lithium-hydroxide-facility/ |
| C16L205_N001_001570_20241002_KUMYANG_RESOURCE_TRUST_BREAK_BLOCKED | 2024-10-01 | narrative_only_blocked | Kumyang’s battery-resource pivot later moved into severe accounting/listing-risk territory; the 2024-10-02 row has only 111 post-entry tradable rows in the available local shard because trading stopped in 2025, so it is kept as narrative-only rather than a calibration trigger row. | https://www.chosun.com/english/industry-en/2025/04/01/UAUGAWGAEBFDPNGAVAD2JYGGPU/<br>https://www.kyc.co.kr/eng/03/01.php |


## 4. Trigger-Level Backtest Summary

| case | symbol | trigger | entry | entry c | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak/trough-after-peak | role |
|---|---:|---|---|---:|---:|---:|---:|---|---|
| Union Corp | 000910 | Stage4B | 2025-04-14 | 6,330 | 8.69/-28.75 | 8.69/-28.75 | 8.69/-35.86 | 2025-04-16→2025-12-10 -40.99% | counterexample |
| Union Materials | 047400 | Stage4B | 2025-04-14 | 2,125 | 10.59/-25.88 | 10.59/-27.53 | 26.12/-40.24 | 2025-10-14→2025-12-26 -51.87% | counterexample |
| Hyundai BNG Steel | 004560 | Stage2 | 2025-04-14 | 12,170 | 9.78/-7.15 | 12.74/-7.15 | 12.74/-14.13 | 2025-07-16→2025-11-25 -23.83% | guardrail_positive |
| LS Corp | 006260 | Stage2-Actionable | 2024-06-03 | 169,800 | 1.30/-24.32 | 1.30/-45.05 | 1.30/-50.24 | 2024-06-03→2024-11-18 -50.87% | counterexample |
| POSCO Holdings | 005490 | Stage4B | 2023-11-29 | 483,000 | 5.18/-9.32 | 5.18/-21.22 | 5.18/-36.02 | 2023-12-27→2024-08-05 -39.17% | counterexample |


Batch price-result distribution:

```text
usable_trigger_count = 5
source_proxy_only_count = 2
narrative_only_blocked_count = 1
positive_or_guardrail_positive_count = 1
counterexample_or_guardrail_count = 4
avg_MFE90 = 7.7
avg_MAE90 = -25.94
avg_MFE180 = 10.81
avg_MAE180 = -35.3
```

Interpretation: this is not a simple “strategic resource policy is bearish” batch. The more precise residual is that **policy chokepoint language and theme exposure are too easy to over-credit unless the issuer-level bridge is visible**. The market can briefly reward the symbol, but the forward path often behaves like a snapped rubber band: initial stretch, then recoil, unless actual supply, contract, offtake, shipment, or margin conversion holds the elastic tension.

## 5. Case Notes

### 5.1 000910 Union Corp — parent proxy theme, local 4B not Actionable

China rare-earth export-control news created a sharp KOSPI theme move in Union and Union Materials. The evidence verifies the theme and the parent-subsidiary relationship, but does not verify issuer-level revenue or margin conversion for Union itself.

```text
classification = local_4B_proxy_theme_overextension
current_profile_failure = possible false positive if policy/regulatory score and relative strength are allowed to substitute for bridge evidence
shadow_result = cap_to_4B_watch_or_Stage2_cap
```

### 5.2 047400 Union Materials — product exposure but no offtake bridge

Ferrite magnet exposure is more concrete than a pure parent proxy, yet the trigger evidence still lacks customer pull, shipment schedule, pricing, and margin conversion. The 180D path shows deep interim MAE and a later whipsaw, which is exactly the profile of a policy-theme row that should not become Yellow/Green.

```text
classification = product_exposure_without_customer_or_margin_bridge
shadow_result = Stage2_cap / local_4B_watch
```

### 5.3 004560 Hyundai BNG Steel — indirect Seongrim stake, Stage2 cap

Hyundai BNG Steel had an indirect bridge through Seongrim Advanced Industry, described by market sources as Korea’s domestic rare-earth permanent magnet producer. That improves information quality versus a pure theme proxy, but the issuer-level bridge remains indirect.

```text
classification = indirect_strategic_resource_bridge
shadow_result = keep Stage2 watch, block Actionable/Yellow until order/revenue/margin bridge appears
```

### 5.4 006260 LS Corp — direct copper concentrate contract, but late equity entry

LS MnM’s five-year BHP copper concentrate contract is genuine strategic supply evidence. However, the equity forward window shows a poor entry profile: 180D MFE of only 1.30% versus MAE of -50.24%. Direct bridge evidence should preserve Stage2-Actionable quality, but it should not loosen Yellow/Green if the entry is already price-extended and lacks near-term earnings revision confirmation.

```text
classification = direct_supply_bridge_but_late_extension_fail
shadow_result = keep evidence quality but apply high-MAE / late-extension Green blocker
```

### 5.5 005490 POSCO Holdings — lithium hydroxide capacity bridge, long-lead 4B

The POSCO-Pilbara lithium hydroxide plant opening is company-specific and materially linked to battery-material sovereignty. But at the trigger date the bridge was long-lead capacity/ramp evidence rather than immediate offtake, margin, or cashflow conversion. The price path deteriorated after a small 30D/90D peak.

```text
classification = long_lead_resource_capacity_without_near_term_cashflow
shadow_result = local_4B / Stage2 cap, not Stage2-Actionable or Yellow
```

## 6. Score Simulation / Current Profile Stress Test

This score simulation is research-only. It does not read or patch `stock_agent` runtime code.

| symbol | current proxy total | shadow total | delta | error label |
|---:|---:|---:|---:|---|
| 000910 | 65 | 52 | -13 | false_positive_if_promoted_above_stage2_cap |
| 047400 | 68 | 56 | -12 | false_positive_if_promoted_above_stage2_cap |
| 004560 | 66 | 61 | -5 | stage2_cap_correct_not_actionable |
| 006260 | 79 | 68 | -11 | direct_bridge_but_late_extension_green_block |
| 005490 | 70 | 57 | -13 | long_lead_capacity_without_near_term_cashflow_green_block |


### Raw component breakdown

```json
{
  "000910": {
    "contract_score": 5,
    "backlog_visibility_score": 5,
    "margin_bridge_score": 3,
    "revision_score": 2,
    "relative_strength_score": 18,
    "customer_quality_score": 4,
    "policy_or_regulatory_score": 20,
    "valuation_repricing_score": 10,
    "execution_risk_score": -12,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "raw_total_before_risk_cap": 67,
    "raw_total_after_risk_cap": 122
  },
  "047400": {
    "contract_score": 5,
    "backlog_visibility_score": 5,
    "margin_bridge_score": 3,
    "revision_score": 2,
    "relative_strength_score": 18,
    "customer_quality_score": 4,
    "policy_or_regulatory_score": 20,
    "valuation_repricing_score": 10,
    "execution_risk_score": -12,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "raw_total_before_risk_cap": 67,
    "raw_total_after_risk_cap": 122
  },
  "004560": {
    "contract_score": 8,
    "backlog_visibility_score": 8,
    "margin_bridge_score": 4,
    "revision_score": 3,
    "relative_strength_score": 10,
    "customer_quality_score": 8,
    "policy_or_regulatory_score": 18,
    "valuation_repricing_score": 7,
    "execution_risk_score": -6,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "raw_total_before_risk_cap": 66,
    "raw_total_after_risk_cap": 126
  },
  "006260": {
    "contract_score": 18,
    "backlog_visibility_score": 12,
    "margin_bridge_score": 6,
    "revision_score": 3,
    "relative_strength_score": 14,
    "customer_quality_score": 14,
    "policy_or_regulatory_score": 12,
    "valuation_repricing_score": 10,
    "execution_risk_score": -8,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "raw_total_before_risk_cap": 89,
    "raw_total_after_risk_cap": 170
  },
  "005490": {
    "contract_score": 10,
    "backlog_visibility_score": 10,
    "margin_bridge_score": 4,
    "revision_score": 3,
    "relative_strength_score": 6,
    "customer_quality_score": 12,
    "policy_or_regulatory_score": 14,
    "valuation_repricing_score": 10,
    "execution_risk_score": -12,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "raw_total_before_risk_cap": 69,
    "raw_total_after_risk_cap": 126
  }
}
```

## 7. Residual Contribution

```text
sector_specific_rule_candidate = L4_STRATEGIC_RESOURCE_POLICY_TO_CASHFLOW_GATE
canonical_rule_candidate = C16_PROXY_THEME_AND_DIRECT_SUPPLY_BRIDGE_GATE
production_scoring_changed = false
shadow_weight_only = true
```

Proposed shadow rule:

```text
if canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:
    if evidence is only policy / export-control / national-security / commodity-shortage headline:
        cap positive stage at Stage2 or local Stage4B watch
        block Stage2-Actionable / Yellow / Green
    if issuer-level bridge exists but is indirect equity stake or product profile only:
        allow Stage2 watch
        require second bridge for Actionable
    if issuer-level bridge is direct contract / offtake / procurement / plant shipment:
        allow Stage2-Actionable
        but block Yellow/Green if 90D/180D MAE is deep and no near-term revision/margin/cashflow confirmation exists
    if accounting trust, listing risk, approval failure, or resource-development credibility breaks:
        route to 4C only when forward-window and non-price thesis-break evidence are both usable
```

Bridge hierarchy for C16:

```text
lowest_quality = pure policy headline / rare-earth theme basket / parent proxy
mid_quality = product exposure / equity stake / long-lead facility
high_quality = signed offtake or raw-material procurement / shipment / plant production / customer pull / margin bridge
promotion_quality = high_quality + near-term revision or cashflow bridge + acceptable MAE profile
```

## 8. Coverage Matrix

| metric | value |
|---|---:|
| new_independent_case_count | 5 |
| reused_symbol_new_trigger_family_count | 2 |
| new_symbol_count_vs_recent_c16_loop | 3 |
| new_independent_trigger_count | 5 |
| calibration_usable_trigger_count | 5 |
| narrative_only_blocked_count | 1 |
| positive_or_guardrail_positive_count | 1 |
| counterexample_or_guardrail_count | 4 |
| Stage2_count | 1 |
| Stage2_Actionable_count | 1 |
| Stage4B_count | 3 |
| Stage4C_usable_count | 0 |
| source_proxy_only_count | 2 |
| evidence_url_pending_count | 0 |
| missing_required_mfe_mae_count | 0 |
| corporate_action_contaminated_180D_count | 0 |
| insufficient_forward_window_180D_count_for_usable_rows | 0 |
| current_profile_error_count | 4 |
| production_scoring_changed | false |
| shadow_weight_only | true |

## 9. Batch Ingest Self-Audit

```text
required_filename_regex_pass = true
filename_round_matches_metadata = true
filename_loop_matches_metadata = true
large_sector_id_present = true
canonical_archetype_id_present = true
fine_archetype_id_present = true
price_source_validation_present = true
actual_entry_ohlcv_present_for_all_usable_triggers = true
complete_30_90_180_mfe_mae_present_for_all_usable_triggers = true
trigger_type_canonical_stage_label = true
same_entry_duplicate_removed = true
narrative_only_rows_excluded_from_weight_calibration = true
source_proxy_only_rows_not_used_for_promotion = true
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 10. Machine-Readable JSONL Rows

```jsonl
{"MAE_180D_pct": -35.86, "MAE_30D_pct": -28.75, "MAE_90D_pct": -28.75, "MFE_180D_pct": 8.69, "MFE_30D_pct": 8.69, "MFE_90D_pct": 8.69, "actual_entry_ohlcv": {"a": 65201995320, "c": 6330, "d": "2025-04-14", "h": 6850, "l": 6270, "m": "KOSPI", "mc": 98821548270, "o": 6770, "s": 15611619, "v": 9928457}, "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16L205_001_000910_20250414_RARE_EARTH_PARENT_PROXY_4B", "case_role": "counterexample", "company": "Union Corp", "drawdown_after_peak_pct": -40.99, "duplicate_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|000910|Stage4B|2025-04-14", "entry_date": "2025-04-14", "entry_price": 6330.0, "evidence_family": "rare_earth_export_control_theme_parent_proxy", "evidence_summary": "China rare-earth and magnet export-control headline drove Union/Union Materials theme spike; Union is parent of Union Materials, but no issuer-level resource volume, offtake, margin, or cashflow bridge was confirmed.", "evidence_urls": ["https://www.mk.co.kr/en/stock/11290565", "https://www.asiae.co.kr/en/article/2025041410122919612"], "fine_archetype_id": "RARE_EARTH_EXPORT_CONTROL_PARENT_PROXY_4B", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_date": "2025-04-16", "peak_price": 6880.0, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2025.csv", "calibration_usable": true, "corporate_action_contaminated_180d_window": false, "entry_row_exists": true, "forward_180d_tradable_rows_available": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000910.json", "upstream_source": "FinanceData/marcap"}, "production_scoring_changed": false, "research_version": "v12", "row_type": "trigger", "score_simulation": {"component_score_breakdown": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 5, "contract_score": 5, "customer_quality_score": 4, "dilution_cb_risk_score": 0, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "margin_bridge_score": 3, "policy_or_regulatory_score": 20, "raw_total_after_risk_cap": 122, "raw_total_before_risk_cap": 67, "relative_strength_score": 18, "revision_score": 2, "valuation_repricing_score": 10}, "current_calibrated_proxy_total": 65, "current_profile_error_label": "false_positive_if_promoted_above_stage2_cap", "score_delta": -13, "shadow_rule_result": "cap_to_stage2_or_4b_watch", "shadow_rule_total": 52}, "selected_loop": 205, "selected_round": "R4", "shadow_weight_only": true, "symbol": "000910", "trigger_date": "2025-04-14", "trigger_type": "Stage4B", "trough_after_peak_date": "2025-12-10", "trough_after_peak_price": 4060.0, "window_180D_end": "2026-01-08"}
{"MAE_180D_pct": -40.24, "MAE_30D_pct": -25.88, "MAE_90D_pct": -27.53, "MFE_180D_pct": 26.12, "MFE_30D_pct": 10.59, "MFE_90D_pct": 10.59, "actual_entry_ohlcv": {"a": 9378719018, "c": 2125, "d": "2025-04-14", "h": 2350, "l": 2110, "m": "KOSPI", "mc": 89250000000, "o": 2205, "s": 42000000, "v": 4236395}, "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16L205_002_047400_20250414_FERRITE_MAGNET_PROXY_4B", "case_role": "counterexample", "company": "Union Materials", "drawdown_after_peak_pct": -51.87, "duplicate_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047400|Stage4B|2025-04-14", "entry_date": "2025-04-14", "entry_price": 2125.0, "evidence_family": "rare_earth_substitute_product_exposure_without_contract", "evidence_summary": "Union Materials was cited as a ferrite magnet producer and rare-earth substitute theme beneficiary, but the evidence did not establish customer pull, shipment conversion, ASP, margin, or capacity allocation.", "evidence_urls": ["https://www.mk.co.kr/en/stock/11290565", "https://www.asiae.co.kr/en/article/2025041410122919612"], "fine_archetype_id": "RARE_EARTH_SUBSTITUTE_FERRITE_MAGNET_PROXY_4B", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_date": "2025-10-14", "peak_price": 2680.0, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2025.csv", "calibration_usable": true, "corporate_action_contaminated_180d_window": false, "entry_row_exists": true, "forward_180d_tradable_rows_available": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/047/047400.json", "upstream_source": "FinanceData/marcap"}, "production_scoring_changed": false, "research_version": "v12", "row_type": "trigger", "score_simulation": {"component_score_breakdown": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 5, "contract_score": 5, "customer_quality_score": 4, "dilution_cb_risk_score": 0, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "margin_bridge_score": 3, "policy_or_regulatory_score": 20, "raw_total_after_risk_cap": 122, "raw_total_before_risk_cap": 67, "relative_strength_score": 18, "revision_score": 2, "valuation_repricing_score": 10}, "current_calibrated_proxy_total": 68, "current_profile_error_label": "false_positive_if_promoted_above_stage2_cap", "score_delta": -12, "shadow_rule_result": "cap_to_stage2_or_4b_watch", "shadow_rule_total": 56}, "selected_loop": 205, "selected_round": "R4", "shadow_weight_only": true, "symbol": "047400", "trigger_date": "2025-04-14", "trigger_type": "Stage4B", "trough_after_peak_date": "2025-12-26", "trough_after_peak_price": 1290.0, "window_180D_end": "2026-01-08"}
{"MAE_180D_pct": -14.13, "MAE_30D_pct": -7.15, "MAE_90D_pct": -7.15, "MFE_180D_pct": 12.74, "MFE_30D_pct": 9.78, "MFE_90D_pct": 12.74, "actual_entry_ohlcv": {"a": 2458663440, "c": 12170, "d": "2025-04-14", "h": 12330, "l": 11350, "m": "KOSPI", "mc": 183509129870, "o": 11830, "s": 15078811, "v": 207379}, "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16L205_003_004560_20250414_SEONGLIM_STAKE_STAGE2_CAP", "case_role": "guardrail_positive", "company": "Hyundai BNG Steel", "drawdown_after_peak_pct": -23.83, "duplicate_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|004560|Stage2|2025-04-14", "entry_date": "2025-04-14", "entry_price": 12170.0, "evidence_family": "rare_earth_permanent_magnet_equity_stake", "evidence_summary": "Hyundai BNG Steel was cited as holding shares in Seongrim Advanced Industry, described as Korea’s only domestic rare-earth permanent magnet manufacturer; the bridge is better than a pure theme proxy but still indirect.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2025041410122919612", "https://www.mk.co.kr/en/stock/11290565"], "fine_archetype_id": "RARE_EARTH_MAGNET_STAKE_STAGE2_CAP", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_date": "2025-07-16", "peak_price": 13720.0, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004560/2025.csv", "calibration_usable": true, "corporate_action_contaminated_180d_window": false, "entry_row_exists": true, "forward_180d_tradable_rows_available": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004560.json", "upstream_source": "FinanceData/marcap"}, "production_scoring_changed": false, "research_version": "v12", "row_type": "trigger", "score_simulation": {"component_score_breakdown": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "contract_score": 8, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "margin_bridge_score": 4, "policy_or_regulatory_score": 18, "raw_total_after_risk_cap": 126, "raw_total_before_risk_cap": 66, "relative_strength_score": 10, "revision_score": 3, "valuation_repricing_score": 7}, "current_calibrated_proxy_total": 66, "current_profile_error_label": "stage2_cap_correct_not_actionable", "score_delta": -5, "shadow_rule_result": "cap_to_stage2_or_4b_watch", "shadow_rule_total": 61}, "selected_loop": 205, "selected_round": "R4", "shadow_weight_only": true, "symbol": "004560", "trigger_date": "2025-04-14", "trigger_type": "Stage2", "trough_after_peak_date": "2025-11-25", "trough_after_peak_price": 10450.0, "window_180D_end": "2026-01-08"}
{"MAE_180D_pct": -50.24, "MAE_30D_pct": -24.32, "MAE_90D_pct": -45.05, "MFE_180D_pct": 1.3, "MFE_30D_pct": 1.3, "MFE_90D_pct": 1.3, "actual_entry_ohlcv": {"a": 87806363900, "c": 169800, "d": "2024-06-03", "h": 172000, "l": 163900, "m": "KOSPI", "mc": 5467560000000, "o": 170200, "s": 32200000, "v": 524575}, "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16L205_004_006260_20240603_LSMNM_BHP_CONTRACT_LATE_STAGE2_FAIL", "case_role": "counterexample", "company": "LS Corp", "drawdown_after_peak_pct": -50.87, "duplicate_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|Stage2-Actionable|2024-06-03", "entry_date": "2024-06-03", "entry_price": 169800.0, "evidence_family": "copper_concentrate_multi_year_procurement_contract", "evidence_summary": "LS MnM signed a five-year BHP copper-concentrate purchase agreement for 1.73 million tons; this is a direct strategic supply bridge, but the equity entry occurred near a local peak and failed the forward return test.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2024053120012819289"], "fine_archetype_id": "COPPER_CONCENTRATE_PROCUREMENT_DIRECT_BRIDGE_LATE_CYCLE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_date": "2024-06-03", "peak_price": 172000.0, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv", "calibration_usable": true, "corporate_action_contaminated_180d_window": false, "entry_row_exists": true, "forward_180d_tradable_rows_available": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006260.json", "upstream_source": "FinanceData/marcap"}, "production_scoring_changed": false, "research_version": "v12", "row_type": "trigger", "score_simulation": {"component_score_breakdown": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 12, "contract_score": 18, "customer_quality_score": 14, "dilution_cb_risk_score": 0, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "margin_bridge_score": 6, "policy_or_regulatory_score": 12, "raw_total_after_risk_cap": 170, "raw_total_before_risk_cap": 89, "relative_strength_score": 14, "revision_score": 3, "valuation_repricing_score": 10}, "current_calibrated_proxy_total": 79, "current_profile_error_label": "direct_bridge_but_late_extension_green_block", "score_delta": -11, "shadow_rule_result": "cap_to_stage2_or_4b_watch", "shadow_rule_total": 68}, "selected_loop": 205, "selected_round": "R4", "shadow_weight_only": true, "symbol": "006260", "trigger_date": "2024-06-02", "trigger_type": "Stage2-Actionable", "trough_after_peak_date": "2024-11-18", "trough_after_peak_price": 84500.0, "window_180D_end": "2025-02-28"}
{"MAE_180D_pct": -36.02, "MAE_30D_pct": -9.32, "MAE_90D_pct": -21.22, "MFE_180D_pct": 5.18, "MFE_30D_pct": 5.18, "MFE_90D_pct": 5.18, "actual_entry_ohlcv": {"a": 257440359000, "c": 483000, "d": "2023-11-29", "h": 485500, "l": 474000, "m": "KOSPI", "mc": 40847904090000, "o": 480000, "s": 84571230, "v": 537203}, "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16L205_005_005490_20231129_LITHIUM_HYDROXIDE_LONG_LEAD_4B", "case_role": "counterexample", "company": "POSCO Holdings", "drawdown_after_peak_pct": -39.17, "duplicate_key": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage4B|2023-11-29", "entry_date": "2023-11-29", "entry_price": 483000.0, "evidence_family": "lithium_hydroxide_facility_opening_without_near_term_margin", "evidence_summary": "POSCO-Pilbara Lithium Solution opened Train 1 of the Gwangyang lithium hydroxide facility; the plant created resource-supply optionality, but the evidence was long-lead capacity rather than near-term margin/cashflow conversion.", "evidence_urls": ["https://www.pls.com/news-stories/posco-pilbara-minerals-jv-opens-south-korean-lithium-hydroxide-facility/"], "fine_archetype_id": "LITHIUM_HYDROXIDE_CAPACITY_LONG_LEAD_PRICE_PATH_4B", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "peak_date": "2023-12-27", "peak_price": 508000.0, "price_source_validation": {"calibration_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "calibration_usable": true, "corporate_action_contaminated_180d_window": false, "entry_row_exists": true, "forward_180d_tradable_rows_available": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "upstream_source": "FinanceData/marcap"}, "production_scoring_changed": false, "research_version": "v12", "row_type": "trigger", "score_simulation": {"component_score_breakdown": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 10, "contract_score": 10, "customer_quality_score": 12, "dilution_cb_risk_score": 0, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "margin_bridge_score": 4, "policy_or_regulatory_score": 14, "raw_total_after_risk_cap": 126, "raw_total_before_risk_cap": 69, "relative_strength_score": 6, "revision_score": 3, "valuation_repricing_score": 10}, "current_calibrated_proxy_total": 70, "current_profile_error_label": "long_lead_capacity_without_near_term_cashflow_green_block", "score_delta": -13, "shadow_rule_result": "cap_to_stage2_or_4b_watch", "shadow_rule_total": 57}, "selected_loop": 205, "selected_round": "R4", "shadow_weight_only": true, "symbol": "005490", "trigger_date": "2023-11-30", "trigger_type": "Stage4B", "trough_after_peak_date": "2024-08-05", "trough_after_peak_price": 309000.0, "window_180D_end": "2024-08-22"}
{"actual_entry_ohlcv": {"a": 30674143150, "c": 51400, "d": "2024-10-02", "h": 53000, "l": 49100, "m": "KOSPI", "mc": 2983771901800, "o": 49800, "s": 58050037, "v": 602268}, "available_rows_180": 111, "blocked_reason": "insufficient_forward_window_in_stock_web_after_trading_suspension", "calibration_usable": false, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16L205_N001_001570_20241002_KUMYANG_RESOURCE_TRUST_BREAK_BLOCKED", "company": "Kumyang", "entry_date": "2024-10-02", "entry_price": 51400.0, "evidence_summary": "Kumyang’s battery-resource pivot later moved into severe accounting/listing-risk territory; the 2024-10-02 row has only 111 post-entry tradable rows in the available local shard because trading stopped in 2025, so it is kept as narrative-only rather than a calibration trigger row.", "evidence_urls": ["https://www.chosun.com/english/industry-en/2025/04/01/UAUGAWGAEBFDPNGAVAD2JYGGPU/", "https://www.kyc.co.kr/eng/03/01.php"], "fine_archetype_id": "RESOURCE_DEVELOPMENT_ACCOUNTING_TRUST_BREAK_WITH_INSUFFICIENT_180D", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "production_scoring_changed": false, "research_version": "v12", "row_type": "narrative_only", "selected_loop": 205, "selected_round": "R4", "shadow_weight_only": true, "symbol": "001570", "trigger_date": "2024-10-01", "trigger_type": "Stage4C"}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent for Songdaiki/stock_agent. Do not execute this prompt unless explicitly instructed in a later coding session.

Input research MD:
e2r_stock_web_v12_residual_round_R4_loop_205_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md

Goal:
Parse the v12 JSONL rows, validate required price fields, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and add the rows to the v12 calibration batch only if all validation gates pass.

Candidate rule to evaluate, not directly apply:
C16_PROXY_THEME_AND_DIRECT_SUPPLY_BRIDGE_GATE

Implementation caution:
- Do not loosen Stage3-Green globally.
- Do not turn rare-earth export-control / strategic-resource policy headlines into Actionable evidence without issuer-level bridge.
- Treat source_proxy_only rows as guardrail/counterexample material, not promotion evidence.
- Preserve direct contract/of-take/resource-supply rows as Stage2-Actionable candidates only when second bridge and acceptable MAE profile exist.
- Keep narrative-only Kumyang row out of weight calibration because 180D forward window is insufficient.
```

## 12. Next Research State

```text
completed_round = R4
completed_loop = 205
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality reinforcement / C16 proxy-theme and direct-supply bridge repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = [
  C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFftAKE_POSITIVE_CONTROL_REPAIR,
  C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY,
  C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR,
  C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR,
  R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
]
```
