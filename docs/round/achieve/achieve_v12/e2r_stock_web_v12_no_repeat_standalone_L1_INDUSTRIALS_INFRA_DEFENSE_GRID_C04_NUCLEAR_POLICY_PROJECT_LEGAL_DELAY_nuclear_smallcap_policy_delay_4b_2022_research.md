# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy project legal delay / small-cap policy 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_SMALLCAP_POLICY_PROJECT_DELAY_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_gap_fill|nuclear_policy_to_project_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_nuclear_smallcap_policy_delay_4b_2022_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY current coverage:
rows=9, symbols=5, date range=2024-07-18~2024-12-03, good/bad S2=1/5, 4B/4C=1/0
top covered symbols: 034020(3), 051600(2), 052690(2), 000720(1), 083650(1)
```

This run avoids those top-covered C04 symbols and adds 006910, 094820, and 105840.  
Each row uses a new `C04 + symbol + trigger_type + entry_date` hard key:
```text
C04 + 006910 + Stage2-Actionable + 2022-03-10
C04 + 094820 + Stage3-Yellow + 2022-03-24
C04 + 105840 + 4B-local-price-only + 2022-05-09
```

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
006910 보성파워텍: selected 2022 forward window clean; historical corporate-action candidates are outside selected trigger window.
094820 일진파워: selected post-2011 forward window clean; profile corporate-action candidates are 2011 and outside selected trigger window.
105840 우진: selected post-2012 forward window clean; profile corporate-action candidates are 2012 and outside selected trigger window.
```

## 3. Research thesis

C04 should distinguish real nuclear-policy project discovery from small-cap nuclear basket premium already paid in price:

```text
nuclear policy reversal / project restart
→ project or order visibility
→ legal-delay clearance and regulatory durability
→ equipment relevance and delivery backlog
→ customer quality and margin revision
→ Stage2/Green or local 4B cap
```

A nuclear policy shock opens the project gate. Stage2 can buy when the gate is opening and the company has a real path to orders. Green should not buy every name standing near the gate after the whole basket has already rerated.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_006910_BOSUNGPOWER_20220310_NUCLEAR_POLICY_STAGE2 | 006910 | positive_nuclear_policy_smallcap_stage2_success_with_later_4b_refresh | 2022-03-10 | 6840 | 9050 on 2022-03-25 | 4245 on 2022-09-28 | 32.31% | 32.31% | 32.31% | -37.94% | -53.09% |
| C04_094820_ILJINPOWER_20220324_NUCLEAR_POLICY_PRICE_CONFIRMATION_FALSE_GREEN | 094820 | nuclear_policy_price_confirmation_false_green_counterexample | 2022-03-24 | 27600 | 30300 on 2022-03-24 | 13250 on 2022-09-28 | 9.78% | 9.78% | 9.78% | -51.99% | -56.27% |
| C04_105840_WOOJIN_20220509_NUCLEAR_PROJECT_PREMIUM_4B | 105840 | nuclear_project_price_premium_4b_counterexample | 2022-05-09 | 15050 | 16300 on 2022-05-09 | 9000 on 2022-09-28 | 8.31% | 8.31% | 8.31% | -40.2% | -44.79% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 006910 is the positive anchor. The March 2022 nuclear-policy reversal route produced strong local MFE before the later policy basket premium required 4B refresh discipline.
- Stage2 is allowed only when policy salience maps to project/order visibility, equipment relevance, legal-delay clearance, delivery backlog and margin/revision visibility.

### Stage3 / Green
- C04 Green should require signed order or project award, regulatory/legal delay clearance, delivery schedule, customer/backlog quality, margin revision and valuation runway.
- 094820 is the false-Green/Yellow guard: nuclear maintenance/project price confirmation was visible, but the March 2022 price had limited residual upside and much larger forward MAE when new project-to-margin evidence did not refresh.

### 4B
- 105840 fills the nuclear instrumentation/project price-premium 4B pocket. The May 2022 trigger had small residual upside and a much larger drawdown.
- 094820 shows the same failure in nuclear maintenance beta form: policy optionality can remain directionally real while the listed-company earnings bridge is too stale for Green.
- 006910 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the nuclear-policy option.

### 4C
- No hard project cancellation, legal block, customer loss, or accounting break is asserted.
- The C04 break mode here is project-to-margin exhaustion: the policy may remain directionally real, but incremental project order, backlog delivery and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C04_006910_BOSUNGPOWER_20220310_NUCLEAR_POLICY_STAGE2": {
    "customer_backlog_quality": 4,
    "equipment_relevance": 7,
    "information_confidence": 4,
    "legal_delay_risk_control": 5,
    "margin_revision_bridge": 4,
    "market_mispricing": 9,
    "nuclear_policy_salience": 10,
    "project_or_order_visibility": 5,
    "total": 56,
    "valuation_rerating_runway": 8
  },
  "C04_094820_ILJINPOWER_20220324_NUCLEAR_POLICY_PRICE_CONFIRMATION_FALSE_GREEN": {
    "customer_backlog_quality": 2,
    "equipment_relevance": 6,
    "information_confidence": 3,
    "legal_delay_risk_control": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "nuclear_policy_salience": 9,
    "project_or_order_visibility": 3,
    "total": 33,
    "valuation_rerating_runway": 1
  },
  "C04_105840_WOOJIN_20220509_NUCLEAR_PROJECT_PREMIUM_4B": {
    "customer_backlog_quality": 2,
    "equipment_relevance": 6,
    "information_confidence": 3,
    "legal_delay_risk_control": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "nuclear_policy_salience": 8,
    "project_or_order_visibility": 3,
    "total": 32,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if nuclear_policy and project_order_legal_clearance_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if nuclear_policy_basket_price_premium and no incremental_project_order_backlog_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and project_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 094820 / 2022-03-24: nuclear project confirmation can be over-promoted if price strength substitutes for signed order and margin proof.
- 105840 / 2022-05-09: nuclear instrumentation premium can look actionable, but fails without project/backlog conversion and margin revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -37.94, "MAE_30D_pct": -6.87, "MAE_90D_pct": -12.87, "MFE_180D_pct": 32.31, "MFE_30D_pct": 32.31, "MFE_90D_pct": 32.31, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_006910_BOSUNGPOWER_20220310_NUCLEAR_POLICY_STAGE2", "case_role": "positive_nuclear_policy_smallcap_stage2_success_with_later_4b_refresh", "company_name": "보성파워텍", "corporate_action_window_status": "selected 2022 forward window clean; profile corporate-action candidates are historical and outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful only at the early nuclear-policy reversal moment when policy salience, nuclear-grid equipment relevance and project-optionality were visible before the small-cap basket fully rerated. Green still requires named project/order conversion, customer quality, delivery backlog, margin/revision bridge and policy durability; after the March 2022 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.09, "entry_date": "2022-03-10", "entry_price": 6840, "evidence_family": "nuclear_policy_reversal_transmission_equipment_project_option_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_POLICY_PROJECT_DELAY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-09-28", "low_price_180d": 4245, "peak_date": "2022-03-25", "peak_price": 9050, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006910.json", "raw_component_score_breakdown": {"customer_backlog_quality": 4, "equipment_relevance": 7, "information_confidence": 4, "legal_delay_risk_control": 5, "margin_revision_bridge": 4, "market_mispricing": 9, "nuclear_policy_salience": 10, "project_or_order_visibility": 5, "total": 56, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C04_006910_BOSUNGPOWER_20220310_NUCLEAR_POLICY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_reversal_salience", "project_or_order_visibility", "equipment_relevance_and_margin_revision_route"], "stage3_evidence_fields": ["project_award_or_signed_order_required", "legal_delay_clearance_and_delivery_schedule_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["nuclear_policy_basket_price_premium", "project_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_delay_or_legal_block", "order_backlog_conversion_failure", "margin_revision_bridge_failure"], "symbol": "006910", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv", "trigger_date": "2022-03-10", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -51.99, "MAE_30D_pct": -21.38, "MAE_90D_pct": -36.59, "MFE_180D_pct": 9.78, "MFE_30D_pct": 9.78, "MFE_90D_pct": 9.78, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_094820_ILJINPOWER_20220324_NUCLEAR_POLICY_PRICE_CONFIRMATION_FALSE_GREEN", "case_role": "nuclear_policy_price_confirmation_false_green_counterexample", "company_name": "일진파워", "corporate_action_window_status": "selected 2022 forward window clean; profile corporate-action candidates are historical and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Nuclear policy price confirmation should remain Yellow or route to local 4B when policy salience is not followed by fresh project award, signed order, backlog delivery, legal clearance and margin/revision evidence. The March 2022 trigger had limited residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.27, "entry_date": "2022-03-24", "entry_price": 27600, "evidence_family": "nuclear_policy_maintenance_project_theme_price_confirmation_without_incremental_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_POLICY_PROJECT_DELAY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-09-28", "low_price_180d": 13250, "peak_date": "2022-03-24", "peak_price": 30300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/094/094820.json", "raw_component_score_breakdown": {"customer_backlog_quality": 2, "equipment_relevance": 6, "information_confidence": 3, "legal_delay_risk_control": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "nuclear_policy_salience": 9, "project_or_order_visibility": 3, "total": 33, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_094820_ILJINPOWER_20220324_NUCLEAR_POLICY_PRICE_CONFIRMATION_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_reversal_salience", "project_or_order_visibility", "equipment_relevance_and_margin_revision_route"], "stage3_evidence_fields": ["project_award_or_signed_order_required", "legal_delay_clearance_and_delivery_schedule_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["nuclear_policy_basket_price_premium", "project_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_delay_or_legal_block", "order_backlog_conversion_failure", "margin_revision_bridge_failure"], "symbol": "094820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2022.csv", "trigger_date": "2022-03-24", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -40.2, "MAE_30D_pct": -19.6, "MAE_90D_pct": -40.2, "MFE_180D_pct": 8.31, "MFE_30D_pct": 8.31, "MFE_90D_pct": 8.31, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_105840_WOOJIN_20220509_NUCLEAR_PROJECT_PREMIUM_4B", "case_role": "nuclear_project_price_premium_4b_counterexample", "company_name": "우진", "corporate_action_window_status": "selected post-2012 forward window clean; profile corporate-action candidates are 2012 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Nuclear project price premium should route to local 4B/counterexample when the policy basket has already capitalized restart optionality and incremental project award, backlog conversion, delivery schedule, legal-delay clearance and margin/revision evidence do not refresh. The May 2022 trigger had small residual upside and a much larger drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.79, "entry_date": "2022-05-09", "entry_price": 15050, "evidence_family": "nuclear_instrumentation_policy_project_price_premium_without_incremental_project_backlog_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_POLICY_PROJECT_DELAY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-09-28", "low_price_180d": 9000, "peak_date": "2022-05-09", "peak_price": 16300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/105/105840.json", "raw_component_score_breakdown": {"customer_backlog_quality": 2, "equipment_relevance": 6, "information_confidence": 3, "legal_delay_risk_control": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "nuclear_policy_salience": 8, "project_or_order_visibility": 3, "total": 32, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_105840_WOOJIN_20220509_NUCLEAR_PROJECT_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_reversal_salience", "project_or_order_visibility", "equipment_relevance_and_margin_revision_route"], "stage3_evidence_fields": ["project_award_or_signed_order_required", "legal_delay_clearance_and_delivery_schedule_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["nuclear_policy_basket_price_premium", "project_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_delay_or_legal_block", "order_backlog_conversion_failure", "margin_revision_bridge_failure"], "symbol": "105840", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2022.csv", "trigger_date": "2022-05-09", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "NUCLEAR_SMALLCAP_POLICY_PROJECT_DELAY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_project_delay_smallcap_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 nuclear-policy rows should allow Stage2 only when policy salience maps to project/order visibility, legal-delay clearance, equipment relevance, backlog delivery and margin revision; late nuclear-policy basket premiums should route to Yellow/local 4B when project-to-margin evidence has not refreshed.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C04 + symbol + trigger_type + entry_date.
3. Add C04-specific nuclear policy / project order / legal delay / delivery backlog / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_STAGE2_ALLOWED_ON_PROJECT_ORDER_LEGAL_CLEARANCE_MARGIN_REVISION_BRIDGE
- C04_GREEN_REQUIRES_SIGNED_ORDER_PROJECT_AWARD_DELIVERY_BACKLOG_REVISION
- C04_NUCLEAR_POLICY_BASKET_PRICE_PREMIUM_LOCAL_4B
- C04_PRICE_CONFIRMATION_WITHOUT_PROJECT_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

