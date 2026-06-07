# stock-web v12 residual calibration — R1 / loop 107 / C05_EPC_MEGA_CONTRACT_MARGIN_GAP

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
live_candidate_mode = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true

stock_web_price_atlas_access_allowed = true
stock_web_price_atlas_access_required = true
price_route_hunt_allowed = false
price_route_discovery_md_allowed = false

stock_agent_research_artifact_access_allowed = true
stock_agent_research_artifact_access_purpose = coverage_gap_and_duplicate_avoidance_only

output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection

```text
selected_round = R1
selected_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = GAS_EPC_AWARD_MARGIN_CASH_CONVERSION_BRIDGE_VS_CONTRACT_SIZE_AND_PROJECT_QUALITY_FAILURE
```

C05 was selected because the No-Repeat index still marks it as below the 50-row practical calibration target.

```text
auto_selected_coverage_gap = C05 rows 33, 50-row target까지 17 부족
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

## 2. Price source lock

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
stock_web_manifest_max_date = 2026-02-20
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

The v12 run uses only committed stock-web OHLCV rows. It does not patch `stock_agent`, does not infer `src/e2r`, and does not make a live watchlist.

## 3. Why this loop matters

C05 is not simply “large contract announced.” In EPC and construction, a headline can be as loud as a bell but still not become equity value if the margin bridge is missing. The project has to pass through the narrow pipes of scope, procurement, working capital, cost escalation, execution risk, and cash conversion. If any of those pipes narrow, the contract-size number is steam rather than torque.

This loop therefore separates:

1. **signed EPC award with delayed equity response**: contract size plus some later rerating, but high MAE means not Green;
2. **mega-contract size without equity rerating**: the stock fails to hold even though the order book label is large;
3. **project-quality/legal-cost failure**: construction defect or collapse risk overwhelms backlog and creates a hard 4C path.

## 4. Case table

| case_id | symbol | company | trigger | entry | entry_px | peak | trough | MFE | MAE | class |
|---|---:|---|---|---|---:|---|---|---:|---:|---|
| C05_R1L107_006360_2024-04-03_FADHILI_GS_EC | 006360 | GS건설 | 2024-04-02 Aramco Fadhili EPC award | 2024-04-03 | 15,630 | 2024-07-17 / 18,620 | 2024-04-19 / 14,040 | +19.13% | -10.17% | delayed positive / high-MAE watch |
| C05_R1L107_000720_2024-07-01_JAFURAH_HYUNDAI_EC | 000720 | 현대건설 | 2024-06-30 Aramco Jafurah / gas network contracts | 2024-07-01 | 33,200 | 2024-07-17 / 34,900 | 2024-12-09 / 24,100 | +5.12% | -27.41% | mega-contract size counterexample |
| C05_R1L107_294870_2022-01-12_GWANGJU_HDC | 294870 | HDC현대산업개발 | 2022-01-11 Gwangju I-Park collapse | 2022-01-12 | 20,850 | no valid post-close positive MFE | 2022-01-27 / 13,500 | +0.00% | -35.25% | hard 4C project-quality/legal-cost failure |

## 5. Case notes

### 5.1 GS건설 / Fadhili EPC award — delayed positive, but not Green

**External trigger.** Reuters reported on 2024-04-02 that Saudi Aramco awarded USD 7.7B in EPC contracts for the Fadhili gas plant expansion to Samsung Engineering, GS Engineering & Construction, and Nesma & Partners. The expansion was expected to raise processing capacity and be completed by November 2027.

**stock-web path.**

```text
symbol = 006360
entry_date = 2024-04-03
entry_price = 15630
peak_date = 2024-07-17
peak_price = 18620
trough_date = 2024-04-19
trough_price = 14040
MFE = +19.13%
MAE = -10.17%
```

**Interpretation.** This is not a clean Green. The equity path did eventually respond, but the entry experienced a double-digit adverse excursion first. For C05, a contract-size headline can be Stage2-Actionable only after a margin/cash bridge is visible. The equity behaved like a heavy crane: it could lift, but only after stabilizers touched the ground.

**Calibration use.**

```text
classification = Stage2_Actionable_watch_not_Green
residual_error_addressed = over-upgrading signed EPC awards without cash/margin visibility
```

### 5.2 현대건설 / Jafurah and Saudi gas-network contracts — mega contract, weak rerating

**External trigger.** Reuters reported on 2024-06-30 that Saudi Aramco signed more than USD 25B of deals for Jafurah gas field expansion and main gas network expansion, including a consortium involving Hyundai Engineering & Construction.

**stock-web path.**

```text
symbol = 000720
entry_date = 2024-07-01
entry_price = 33200
peak_date = 2024-07-17
peak_price = 34900
trough_date = 2024-12-09
trough_price = 24100
MFE = +5.12%
MAE = -27.41%
```

**Interpretation.** This is the clean contract-size counterexample. The order-book headline is huge, but the stock gave only a small forward peak and then a deep drawdown. In C05 terms, this is what happens when “signed contract” is treated as a destination rather than a departure gate. The plane still has to pass through procurement, margin, working capital, and execution weather.

**Calibration use.**

```text
classification = 4C_or_reject_without_margin_bridge
residual_error_addressed = mega-contract headline false positive
```

### 5.3 HDC현대산업개발 / Gwangju I-Park collapse — hard project-quality 4C

**External trigger.** The Gwangju Hwajeong I-Park exterior wall collapse occurred on 2022-01-11. Public reporting records six deaths, government investigation, and scrutiny of HDC Hyundai Development Company.

**stock-web path.**

```text
symbol = 294870
entry_date = 2022-01-12
entry_price = 20850
post_close_valid_peak_price = 20850
trough_date = 2022-01-27
trough_price = 13500
MFE = +0.00%
MAE = -35.25%
```

**Interpretation.** This is not “bad sentiment.” It is a C05 hard failure: project quality, legal overhang, possible remediation cost, brand damage, and execution governance all hit the equity path at once. This case is useful because a normal backlog or development pipeline score would be dangerously blind here.

**Calibration use.**

```text
classification = hard_4C
residual_error_addressed = project-quality/legal-cost blind spot
verified_url_repair_needed = true
```

## 6. Residual rule candidate

```text
new_axis_proposed = c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only
```

### Rule draft

For `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`, do not let project size alone lift a case above Stage2-watch.

A C05 case can be treated as **Stage2-Actionable** only when at least two of the following are present:

```text
- signed contract or legally binding award, not just preferred bidder / MOU
- company-specific scope and share of package disclosed
- margin or cost-pass-through visibility
- funding / working-capital burden manageable
- execution timeline and procurement risk visible
- prior quality/legal-cost overhang absent or explicitly resolved
```

A C05 case should be **4B / 4C watch** when any of the following dominate:

```text
- contract size is clear but company-level margin is opaque
- headline is sector-wide and not company-specific
- prior project defect / safety / legal overhang exists
- working capital or cost escalation can absorb the order-book benefit
- stock path shows high MFE followed by high MAE without new non-price confirmation
```

## 7. Current profile residual errors

```text
current_profile_error_count = 3
```

1. `006360`: a signed EPC award did produce forward MFE, but the path had a large initial adverse move. Green would be too generous.
2. `000720`: a massive contract headline created almost no durable forward peak and ended in a deep drawdown.
3. `294870`: project-quality/legal-cost failure produced immediate hard 4C; backlog and construction exposure should not mask this.

## 8. Machine-readable rows

```jsonl
{"row_type": "case", "case_id": "C05_R1L107_006360_2024-04-03_FADHILI_GS_EC", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "GAS_EPC_AWARD_MARGIN_CASH_CONVERSION_BRIDGE_VS_CONTRACT_SIZE_ONLY", "symbol": "006360", "name": "GS건설", "trigger_date": "2024-04-02", "entry_date": "2024-04-03", "entry_price": 15630, "peak_date": "2024-07-17", "peak_price": 18620, "trough_date": "2024-04-19", "trough_price": 14040, "mfe_pct": 19.13, "mae_pct": -10.17, "label": "delayed_positive_high_mae_watch", "classification": "Stage2_Actionable_watch_not_Green", "evidence_family": "signed_epc_contract_size_with_margin_cash_bridge_unverified", "source_url": "https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/", "stock_web_price_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv", "calibration_usable": true}
{"row_type": "case", "case_id": "C05_R1L107_000720_2024-07-01_JAFURAH_HYUNDAI_EC", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "GAS_EPC_AWARD_MARGIN_CASH_CONVERSION_BRIDGE_VS_CONTRACT_SIZE_ONLY", "symbol": "000720", "name": "현대건설", "trigger_date": "2024-06-30", "entry_date": "2024-07-01", "entry_price": 33200, "peak_date": "2024-07-17", "peak_price": 34900, "trough_date": "2024-12-09", "trough_price": 24100, "mfe_pct": 5.12, "mae_pct": -27.41, "label": "mega_contract_size_counterexample", "classification": "4C_or_reject_without_margin_bridge", "evidence_family": "signed_mega_contract_but_no_equity_rerating", "source_url": "https://www.reuters.com/business/energy/aramco-signs-over-25-bln-deals-main-gas-network-jafurah-gas-field-2024-06-30/", "stock_web_price_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "calibration_usable": true}
{"row_type": "case", "case_id": "C05_R1L107_294870_2022-01-12_GWANGJU_HDC", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "CONSTRUCTION_PROJECT_DEFECT_COST_OVERHANG_VS_PROJECT_SCALE_BACKLOG", "symbol": "294870", "name": "HDC현대산업개발", "trigger_date": "2022-01-11", "entry_date": "2022-01-12", "entry_price": 20850, "peak_date": "n/a_post_entry_high_below_entry", "peak_price": 20850, "trough_date": "2022-01-27", "trough_price": 13500, "mfe_pct": 0.0, "mae_pct": -35.25, "label": "hard_cost_legal_quality_counterexample", "classification": "hard_4C", "evidence_family": "project_quality_failure_and_legal_cost_overhang", "source_url": "https://en.wikipedia.org/wiki/Gwangju_Hwajeong_I-Park_exterior_wall_collapse", "stock_web_price_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "calibration_usable": true, "verified_url_repair_needed": true}
{"row_type": "trigger", "trigger_id": "TRG_C05_R1L107_006360_2024-04-03_FADHILI_GS_EC", "case_id": "C05_R1L107_006360_2024-04-03_FADHILI_GS_EC", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "symbol": "006360", "trigger_date": "2024-04-02", "entry_date": "2024-04-03", "entry_price": 15630, "mfe_pct": 19.13, "mae_pct": -10.17, "trigger_family": "signed_epc_contract_size_with_margin_cash_bridge_unverified", "calibration_usable": true}
{"row_type": "trigger", "trigger_id": "TRG_C05_R1L107_000720_2024-07-01_JAFURAH_HYUNDAI_EC", "case_id": "C05_R1L107_000720_2024-07-01_JAFURAH_HYUNDAI_EC", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "symbol": "000720", "trigger_date": "2024-06-30", "entry_date": "2024-07-01", "entry_price": 33200, "mfe_pct": 5.12, "mae_pct": -27.41, "trigger_family": "signed_mega_contract_but_no_equity_rerating", "calibration_usable": true}
{"row_type": "trigger", "trigger_id": "TRG_C05_R1L107_294870_2022-01-12_GWANGJU_HDC", "case_id": "C05_R1L107_294870_2022-01-12_GWANGJU_HDC", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "symbol": "294870", "trigger_date": "2022-01-11", "entry_date": "2022-01-12", "entry_price": 20850, "mfe_pct": 0.0, "mae_pct": -35.25, "trigger_family": "project_quality_failure_and_legal_cost_overhang", "calibration_usable": true}
{"row_type": "score_simulation", "axis": "c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only", "current_profile_error_addressed": "contract_size_headline_over_scores_EPC_without_margin_cash_evidence", "expected_effect": "demote mega-contract-only C05 cases from Stage3-Yellow/Green to Stage2-watch or 4B/4C unless backlog-to-margin bridge is present", "positive_control": "006360_2024_Fadhili_delayed_positive_high_mae_watch", "counterexamples": ["000720_2024_Jafurah_contract_size_low_MFE_high_MAE", "294870_2022_project_quality_hard_4C"], "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "aggregate", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "selected_round": "R1", "selected_loop": 107, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "new_independent_case_count": 3, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 3, "verified_url_repair_needed_count": 1, "auto_selected_coverage_gap": "C05 rows 33, 50-row target까지 17 부족", "loop_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "shadow_weight", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "proposed_axis": "c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only", "direction": "negative_gate_on_contract_size_only; positive_bonus_only_if_margin_cash_bridge", "suggested_shadow_delta": {"contract_size_only": -1.0, "signed_contract_with_scope_and_margin_bridge": 0.75, "project_quality_or_cost_overhang": -2.0, "working_capital_cash_drain": -1.25}, "do_not_apply_to_production": true}
{"row_type": "residual_contribution", "residual_error_type": "C05 contract headline false-positive and cost-overrun blind spot", "contribution": "Separates gas/EPC contract-size headlines from company-specific conversion into margin, cash, and working capital, while hard-flagging quality/legal-cost failures.", "new_axis_proposed": "c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only"}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in Songdaiki/stock_agent. Do not perform live trading or brokerage integration.

Use this research file only as a batch calibration input for the v12 residual research corpus.

Task:
1. Ingest the JSONL rows from this Markdown into the v12 research registry / calibration artifact pipeline.
2. Preserve the following no-repeat identity:
   canonical_archetype_id + symbol + trigger_type/evidence_family + entry_date
3. Do not directly change production scoring from this single file.
4. If enough C05 files accumulate, evaluate a shadow-only axis:
   c05_margin_cash_working_capital_bridge_required_for_stage2_actionable_shadow_only
5. Treat the suggested deltas as research hints, not production constants:
   - contract_size_only: negative gate
   - signed_contract_with_scope_and_margin_bridge: modest positive
   - project_quality_or_cost_overhang: hard negative gate
   - working_capital_cash_drain: negative gate
6. Run existing tests before any patch.
7. Add migration notes explaining that the axis separates signed EPC award from margin/cash conversion and project-quality/legal-cost failure.
```

## 10. Final status

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 3
verified_url_repair_needed_count = 1

diversity_score_summary = C05 Priority 1 보강 + Fadhili delayed positive/high-MAE + Jafurah mega-contract false-positive + HDC project-quality hard 4C
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C05 EPC/project-size headlines
existing_axis_weakened = null
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```
