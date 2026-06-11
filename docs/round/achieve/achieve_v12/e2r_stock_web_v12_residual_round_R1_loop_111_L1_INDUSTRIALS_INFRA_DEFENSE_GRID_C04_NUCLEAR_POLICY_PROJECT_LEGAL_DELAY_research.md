# e2r_stock_web_v12_residual_round_R1_loop_111_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 111
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_CLEARANCE_VS_SMALL_SUPPLIER_THEME_SPIKE_RETEST
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection summary

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` remains a low-coverage canonical bucket in the no-repeat index: 6 rows / 5 symbols, with top covered symbols concentrated in `046120`, `019990`, `034020`, `083650`, and `126720`. The prior local C04 expansion used `052690`, `051600`, and `011700` at `loop 110`; this run therefore uses `loop 111` and focuses on additional supplier/theme names that reacted to the Czech Dukovany preferred-bidder headline but lacked a direct final-contract or named listed-company economics bridge.

The working historical event is the July 2024 Czech selection of KHNP as preferred bidder for two nuclear reactors at Dukovany. The key C04 issue is not whether the headline was real. It was real. The issue is whether a Korean listed supplier’s price move can be justified by a direct contract, legally cleared final agreement, scope, margin, service/O&M, or cash-flow bridge. Reuters reported that KHNP was selected as preferred bidder on 2024-07-17 but that contract specifics were still to be finalized. Later Reuters coverage also showed that EDF and Westinghouse appeals and Czech competition/court steps could temporarily stop signing, confirming why C04 must distinguish preferred-bidder headlines from final-contract/legal-clearance evidence.

## 2. Price source validation

All prices are from `Songdaiki/stock-web` calibration-safe shards under `atlas/ohlcv_tradable_by_symbol_year`. The manifest identifies the source as `FinanceData/marcap`, price adjustment status as `raw_unadjusted_marcap`, and `max_date=2026-02-20`. The selected windows are after each symbol’s last corporate-action caveat where relevant. Raw/unadjusted status is kept explicit; the cases are used for calibration only because the trigger windows themselves do not cross the profile-listed historical corporate-action blocked dates.

## 3. Case table

| case_id | symbol | name | trigger_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | label | calibration use |
|---|---:|---|---:|---:|---:|---:|---:|---|---|
| C04-R1L111-001 | 051600 | 한전KPS | 2024-07-18 | 38,900 | +21.98% / -7.84% | +21.98% / -7.84% | +26.22% / -7.84% | reused positive-control | service/O&M bridge escape hatch |
| C04-R1L111-002 | 032820 | 우리기술 | 2024-07-18 | 2,700 | +22.22% / -33.33% | +22.22% / -33.33% | +22.22% / -46.19% | counterexample | small supplier theme spike |
| C04-R1L111-003 | 105840 | 우진 | 2024-07-18 | 9,300 | +17.74% / -23.44% | +17.74% / -23.44% | +17.74% / -39.46% | counterexample | nuclear measurement/instrumentation label without project economics |
| C04-R1L111-004 | 006910 | 보성파워텍 | 2024-07-18 | 3,630 | +17.91% / -29.48% | +17.91% / -29.48% | +17.91% / -42.15% | counterexample | grid/nuclear supplier theme without named Czech cash bridge |

## 4. Case narratives

### 4.1 한전KPS / 051600 — reused positive-control, not counted as a new independent case

This case is reused only as a balance control. The same-symbol/same-trigger family was already used in the previous local C04 loop, so it is not counted as a new independent case. It is included because C04 needs a comparator showing that not every nuclear-related move should be hard-blocked. O&M and service visibility can make the preferred-bidder headline more investable than generic supplier vocabulary.

Price path: 2024-07-18 close 38,900, same-day high 47,450, 2024-12-03 high 49,100, with the main drawdown low at 2024-08-05 low 35,850. This gives a clean positive-control path: 30D MFE +21.98%, 180D MFE +26.22%, and MAE -7.84%.

Calibration implication: keep a narrow C04 escape hatch where the listed company has service/O&M visibility and a relatively low-MAE path. However, this should not generalize to small supplier theme stocks.

### 4.2 우리기술 / 032820 — small supplier theme spike, high-MAE counterexample

우리기술 reacted violently around the nuclear headline. The 2024-07-18 candle had a high of 3,300 but closed at 2,700. From there, the path deteriorated quickly: 2024-08-05 low 1,800 and 2025-04-09 low 1,453. This is the exact C04 failure mode: the market initially prices an option-like supplier story, but without final contract, named scope, or cash-flow bridge the path becomes high-MAE.

Calibration implication: a supplier theme spike with same-day high but no stable close-follow-through should not receive Stage2-Actionable bonus. It should be capped at Stage2-Watch or local 4B watch until legal clearance and listed-company economics are refreshed.

### 4.3 우진 / 105840 — nuclear instrumentation label without project economics

우진 had a same-day 2024-07-18 spike to 10,950 but closed at 9,300. The first drawdown came quickly with 2024-08-05 low 7,120; the deeper low occurred at 2024-12-09 low 5,630. The high was real but the follow-through was not durable.

Calibration implication: instrumentation/measurement vocabulary is not enough for C04. The profile should require a named project scope or explicit order/revenue bridge before granting a positive Stage2 bonus.

### 4.4 보성파워텍 / 006910 — grid/nuclear supplier label without minority economics

보성파워텍 also spiked on the 2024-07-18 nuclear headline: high 4,280 versus close 3,630. The path then moved to 2024-08-05 low 2,560, 2024-12-09 low 2,290, and 2025-04-04 low 2,100. This is a textbook local-4B watch that becomes hard 4C if no final contract or direct supplier bridge appears.

Calibration implication: grid/nuclear supplier vocabulary should not be treated as a Czech nuclear cash-flow bridge. The model should block Stage3-Green unless legal clearance and listed-company scope are both refreshed.

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12","case_id":"C04-R1L111-001","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_CLEARANCE_VS_SMALL_SUPPLIER_THEME_SPIKE_RETEST","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"051600","name":"한전KPS","trigger_type":"Stage2-Actionable","entry_date":"2024-07-18","entry_close":38900,"high_30d":47450,"low_30d":35850,"mfe_30d_pct":21.98,"mae_30d_pct":-7.84,"high_90d":47450,"low_90d":35850,"mfe_90d_pct":21.98,"mae_90d_pct":-7.84,"high_180d":49100,"low_180d":35850,"mfe_180d_pct":26.22,"mae_180d_pct":-7.84,"label":"positive_control_reused","calibration_usable":true,"new_independent_case":false,"reason":"service/O&M visibility and low-MAE path; reused as balance control only"}
{"row_type":"trigger","schema_version":"v12","case_id":"C04-R1L111-002","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_CLEARANCE_VS_SMALL_SUPPLIER_THEME_SPIKE_RETEST","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"032820","name":"우리기술","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_close":2700,"high_30d":3300,"low_30d":1800,"mfe_30d_pct":22.22,"mae_30d_pct":-33.33,"high_90d":3300,"low_90d":1800,"mfe_90d_pct":22.22,"mae_90d_pct":-33.33,"high_180d":3300,"low_180d":1453,"mfe_180d_pct":22.22,"mae_180d_pct":-46.19,"label":"counterexample","calibration_usable":true,"new_independent_case":true,"reason":"same-day supplier theme spike without final contract or company-specific cash bridge"}
{"row_type":"trigger","schema_version":"v12","case_id":"C04-R1L111-003","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_CLEARANCE_VS_SMALL_SUPPLIER_THEME_SPIKE_RETEST","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"105840","name":"우진","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_close":9300,"high_30d":10950,"low_30d":7120,"mfe_30d_pct":17.74,"mae_30d_pct":-23.44,"high_90d":10950,"low_90d":7120,"mfe_90d_pct":17.74,"mae_90d_pct":-23.44,"high_180d":10950,"low_180d":5630,"mfe_180d_pct":17.74,"mae_180d_pct":-39.46,"label":"counterexample","calibration_usable":true,"new_independent_case":true,"reason":"nuclear instrumentation label without named project scope or margin/revenue bridge"}
{"row_type":"trigger","schema_version":"v12","case_id":"C04-R1L111-004","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_DUKOVANY_PREFERRED_BIDDER_FINAL_CONTRACT_LEGAL_CLEARANCE_VS_SMALL_SUPPLIER_THEME_SPIKE_RETEST","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","symbol":"006910","name":"보성파워텍","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_close":3630,"high_30d":4280,"low_30d":2560,"mfe_30d_pct":17.91,"mae_30d_pct":-29.48,"high_90d":4280,"low_90d":2560,"mfe_90d_pct":17.91,"mae_90d_pct":-29.48,"high_180d":4280,"low_180d":2100,"mfe_180d_pct":17.91,"mae_180d_pct":-42.15,"label":"counterexample","calibration_usable":true,"new_independent_case":true,"reason":"grid/nuclear supplier vocabulary without final contract/legal clearance cash bridge"}
```

## 6. Score-return alignment and current-profile stress test

The current C04 profile already carries legal-delay and supplier-theme skepticism, but these paths sharpen the routing rule.

- 한전KPS confirms the escape hatch: service/O&M visibility + low-MAE path can keep Stage2-Actionable.
- 우리기술, 우진, 보성파워텍 confirm the block: small supplier vocabulary can generate intraday/same-day MFE but then produce deep MAE.
- The error is not the headline itself. The headline was true. The error is letting a preferred-bidder headline travel down the supplier chain without final-contract, legal clearance, named order scope, and listed-company cash bridge.

## 7. Rule candidate

```text
if canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
and nuclear_policy_or_preferred_bidder_headline == true
and final_contract_signed_or_legal_clearance == false
and listed_company_named_scope_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C04
and MFE_30D_pct >= +15
and MAE_90D_pct <= -20
and refreshed_contract_scope_or_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C04
and service_OM_visibility == true
and MFE_90D_pct >= +15
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    do_not_apply_supplier_theme_block = true
```

## 8. Residual contribution summary

```yaml
new_independent_case_count: 3
reused_positive_control_count: 1
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
counterexample_count: 3
current_profile_error_count: 3
same_archetype_new_symbol_count_visible_index_basis: 3
same_archetype_new_trigger_family_count: 3
loop_contribution_label: canonical_archetype_rule_candidate
existing_axis_strengthened:
  - C04_final_contract_legal_clearance_requirement
  - C04_supplier_theme_stage2_block_without_listed_company_cash_bridge
  - C04_local_4B_watch_after_intraday_supplier_spike
  - C04_service_OM_low_MAE_escape_hatch
new_axis_proposed: C04_INTRADAY_SUPPLIER_SPIKE_HIGH_MAE_BLOCK
production_scoring_changed: false
shadow_weight_only: true
```

## 9. Next recommended archetypes

`C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C15_MATERIAL_SPREAD_SUPERCYCLE, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`
