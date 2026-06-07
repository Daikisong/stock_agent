# E2R v12 Residual Calibration Research — R1 / Loop 113 / C05_EPC_MEGA_CONTRACT_MARGIN_GAP

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
output_format: one_standalone_markdown_file
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_atlas_repo: Songdaiki/stock-web
price_basis: tradable_raw
selected_round: R1
selected_loop: 113
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: NEOM_GIGA_PROJECT_CM_DESIGN_ENGINEERING_SCOPE_MARGIN_BRIDGE_VS_PROJECT_LABEL_THEME_BLOWOFF
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 1. Execution Boundary

This run is **not** a live scan, not a recommendation list, and not a production-code patch. It only creates a standalone historical calibration / residual research Markdown artifact.

The active prompt states that the run must not open `stock_agent` code, must not infer `src/e2r`, must not patch scoring, and must not change production scoring. The only allowed research-agent repository access is for duplicate avoidance / coverage-gap inspection, while `Songdaiki/stock-web` is required as the price atlas. The run must verify actual OHLCV rows and calculate entry, MFE, MAE, peak, drawdown, and residual contribution.

## 2. Why C05 Was Selected

The No-Repeat / Coverage index still lists `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` as Priority 1 with 33 rows and 17 rows needed to reach the 50-row practical calibration target.

Already-used C05 case families were avoided:

- DL이앤씨
- 대우건설
- 삼성E&A
- GS건설
- 현대건설
- HDC현대산업개발
- 삼성물산
- 태영건설
- 동아지질

This loop uses a new C05 boundary axis: **Saudi/NEOM giga-project exposure through CM / design / engineering labels**. The point is not whether NEOM is big. The point is whether a listed Korean small/mid contractor’s actual revenue, margin, working-capital profile, and signed scope can carry the equity path. In other words, a mega-project headline is a lighthouse; C05 calibration must still check whether the company owns the shipping lane or is only lit by the lighthouse.

## 3. Price Atlas Sanity Check

`Songdaiki/stock-web` manifest:

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis: tradable_raw
corporate_action_policy: corporate-action-contaminated windows blocked by default
```

All three selected windows are outside the listed corporate-action-candidate dates for the selected symbols, based on each symbol profile.

## 4. External Evidence Spine

### 4.1 NEOM / Saudi Vision 2030 is a real giga-project complex

NEOM / The Line / Trojena / Sindalah are real Saudi Vision 2030 giga-projects. Public sources describe NEOM as a very large Saudi megaproject, with The Line and Trojena as flagship sub-projects.

### 4.2 But size does not equal equity cash conversion

Later reporting describes NEOM as facing cost pressure, scale-back / prioritization issues, leadership changes, and delays. That matters for C05: a huge total addressable project can still be a poor equity signal if the listed company’s exact signed scope, margin structure, working capital, and revenue recognition are unclear.

Therefore, for C05 scoring, “NEOM / Saudi project label” should not automatically produce Stage2-Actionable or Stage3. It should be treated as **theme entry** unless the case has firm-level contract scope, contract amount, schedule, margin visibility, and cash-conversion evidence.

## 5. Calibration Cases

### Case 1 — HanmiGlobal / 한미글로벌 (053690): CM / PM exposure can create a strong route, but still needs full 4B watch

```json
{
  "case_id": "C05_R1_L113_053690_2022-06-29_NEOM_CM_PM_ROUTE",
  "ticker": "053690",
  "name": "한미글로벌",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "NEOM_CM_PM_SCOPE_MARGIN_BRIDGE_POSITIVE_BUT_THEME_EXTENSION_4B_WATCH",
  "trigger_date": "2022-06-29",
  "entry_date": "2022-06-29",
  "entry_price": 11100,
  "peak_date": "2022-11-07",
  "peak_price": 48900,
  "local_low_date": "2022-07-15",
  "local_low_price": 10500,
  "mfe_pct": 340.54,
  "mae_pct": -5.41,
  "classification": "positive_with_full_4B_watch",
  "calibration_usable": true,
  "source_quality": "price_rows_verified_external_project_spine_company_scope_repair_needed"
}
```

**Price path.** The stock-web row for 2022-06-29 gives close 11,100. The route peaked at 48,900 on 2022-11-07, giving MFE +340.54%. The lowest post-entry row before the route established was 10,500 on 2022-07-15, giving MAE -5.41%.

**Interpretation.** HanmiGlobal is the cleanest of this C05 mini-batch because its business is closer to project management / construction management than a generic “Saudi theme” label. But the move was too large relative to immediately visible contract economics. This should not become pure Stage3-Green unless firm-level scope and margin/cash conversion are validated. Treat as **positive route, but 4B full-window watch**.

**C05 learning.** CM/PM exposure can matter, but only when the company’s actual signed scope, contract amount, project duration, margin, and revenue-recognition path are known. Otherwise the signal is price-responsive but fragile.

---

### Case 2 — Heerim / 희림 (037440): architecture/design label after Saudi/NEOM theme is a hard fade risk

```json
{
  "case_id": "C05_R1_L113_037440_2022-11-17_SAUDI_DESIGN_LABEL_FADE",
  "ticker": "037440",
  "name": "희림",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "NEOM_DESIGN_ARCHITECTURE_LABEL_FALSE_POSITIVE",
  "trigger_date": "2022-11-17",
  "entry_date": "2022-11-17",
  "entry_price": 11100,
  "peak_date": "2022-11-30",
  "peak_price": 12400,
  "local_low_date": "2022-12-29",
  "local_low_price": 8160,
  "mfe_pct": 11.71,
  "mae_pct": -26.49,
  "classification": "hard_counterexample",
  "calibration_usable": true,
  "source_quality": "price_rows_verified_external_project_spine_company_scope_repair_needed"
}
```

**Price path.** The stock-web row for 2022-11-17 gives close 11,100. The post-trigger high was 12,400 on 2022-11-30, giving MFE +11.71%. By 2022-12-29, the low reached 8,160, giving MAE -26.49%.

**Interpretation.** This is a C05 false positive. A design/architecture label can react to Saudi/NEOM project news, but that does not mean large EPC backlog, margin expansion, or working-capital quality. The price path had modest upside and large drawdown.

**C05 learning.** In C05, architecture/design exposure should be a **scope-discounted read-through**, not a primary mega-contract signal, unless exact contract amount and margin path are verified.

---

### Case 3 — Yushin / 유신 (054930): engineering-consulting label can blow off and then revert without contract economics

```json
{
  "case_id": "C05_R1_L113_054930_2022-11-17_SAUDI_ENGINEERING_LABEL_FADE",
  "ticker": "054930",
  "name": "유신",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "NEOM_ENGINEERING_CONSULTING_LABEL_FALSE_POSITIVE",
  "trigger_date": "2022-11-17",
  "entry_date": "2022-11-17",
  "entry_price": 43750,
  "peak_date": "2022-12-01",
  "peak_price": 46550,
  "local_low_date": "2022-12-29",
  "local_low_price": 31750,
  "mfe_pct": 6.40,
  "mae_pct": -27.43,
  "classification": "hard_counterexample",
  "calibration_usable": true,
  "source_quality": "price_rows_verified_external_project_spine_company_scope_repair_needed"
}
```

**Price path.** The stock-web row for 2022-11-17 gives close 43,750. The post-trigger high was 46,550 on 2022-12-01, giving MFE +6.40%. The low reached 31,750 on 2022-12-29, giving MAE -27.43%.

**Interpretation.** This is the sharper version of the same C05 problem. Engineering-consulting labels can join a giga-project narrative, but without visible signed scope, duration, billing schedule, cost structure, and cash conversion, the price path can become an air pocket.

**C05 learning.** A consulting / engineering label should be capped unless there is direct contract evidence. It should not inherit the full mega-project notional value.

## 6. Score Simulation

```json
{
  "score_simulation": {
    "current_profile_risk": "C05 may over-score project-size headlines and under-penalize non-EPC scope labels if evidence is only giga-project narrative.",
    "stage2_raw": {
      "project_label": "+",
      "sector_momentum": "+",
      "large_project_notional": "+"
    },
    "stage2_actionable_required_evidence": {
      "signed_contract_amount": "required",
      "company_level_scope": "required",
      "revenue_recognition_schedule": "required",
      "margin_visibility": "required",
      "working_capital_or_advance_payment_quality": "required",
      "direct_counterparty_or_prime_contract_role": "required"
    },
    "stage3_yellow_allowed_when": "firm-level scope and contract amount are verified, but margin/cash conversion remains partial",
    "stage3_green_allowed_when": "signed scope + margin bridge + cash conversion + backlog schedule are verified",
    "force_4b_when": "price route is strong but non-price evidence is only project label / sector read-through",
    "force_4c_when": "MFE is low or temporary and MAE exceeds 20% after project-label trigger"
  }
}
```

## 7. Residual Contribution

```json
{
  "residual_contribution": {
    "new_independent_case_count": 3,
    "reused_case_count": 0,
    "same_archetype_new_symbol_count": 3,
    "same_archetype_new_trigger_family_count": 2,
    "calibration_usable_case_count": 3,
    "calibration_usable_trigger_count": 3,
    "positive_case_count": 1,
    "counterexample_count": 2,
    "current_profile_error_count": 3,
    "verified_url_repair_needed_count": 3,
    "diversity_score_summary": "C05 Priority 1 보강 + HanmiGlobal NEOM CM/PM route positive 4B watch + Heerim design-label hard fade + Yushin engineering-consulting-label hard fade"
  }
}
```

## 8. Shadow Rule Candidate

```json
{
  "shadow_rule_candidate": {
    "rule_id": "c05_neom_giga_project_scope_margin_cash_bridge_required_v1",
    "scope": "canonical_archetype_specific",
    "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
    "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
    "proposal_type": "shadow_weight_only",
    "production_scoring_changed": false,
    "rule_text": "For C05, mega-project / NEOM / Saudi Vision labels must not inherit the project notional unless firm-level signed scope, contract amount, schedule, margin bridge, and working-capital or advance-payment evidence are verified. CM/PM/design/engineering-consulting labels receive a scope discount and default to 4B watch after strong price routes or 4C after low-MFE/high-MAE fades.",
    "positive_adjustment": {
      "condition": "direct signed scope + contract economics + margin/cash bridge verified",
      "stage_cap": "Stage3-Yellow or Stage3-Green depending on evidence quality"
    },
    "negative_adjustment": {
      "condition": "project label only, no firm-level signed scope, no margin bridge, no working-capital bridge",
      "stage_cap": "Stage2 or 4B watch",
      "hard_fade_condition": "MFE < 15% and MAE <= -20%",
      "hard_fade_bucket": "4C"
    }
  }
}
```

## 9. Machine-Readable Rows

```jsonl
{"row_type":"case","case_id":"C05_R1_L113_053690_2022-06-29_NEOM_CM_PM_ROUTE","ticker":"053690","name":"한미글로벌","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"NEOM_CM_PM_SCOPE_MARGIN_BRIDGE_POSITIVE_BUT_THEME_EXTENSION_4B_WATCH","trigger_date":"2022-06-29","entry_date":"2022-06-29","entry_price":11100,"peak_date":"2022-11-07","peak_price":48900,"low_date":"2022-07-15","low_price":10500,"mfe_pct":340.54,"mae_pct":-5.41,"classification":"positive_with_full_4B_watch","calibration_usable":true}
{"row_type":"case","case_id":"C05_R1_L113_037440_2022-11-17_SAUDI_DESIGN_LABEL_FADE","ticker":"037440","name":"희림","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"NEOM_DESIGN_ARCHITECTURE_LABEL_FALSE_POSITIVE","trigger_date":"2022-11-17","entry_date":"2022-11-17","entry_price":11100,"peak_date":"2022-11-30","peak_price":12400,"low_date":"2022-12-29","low_price":8160,"mfe_pct":11.71,"mae_pct":-26.49,"classification":"hard_counterexample","calibration_usable":true}
{"row_type":"case","case_id":"C05_R1_L113_054930_2022-11-17_SAUDI_ENGINEERING_LABEL_FADE","ticker":"054930","name":"유신","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"NEOM_ENGINEERING_CONSULTING_LABEL_FALSE_POSITIVE","trigger_date":"2022-11-17","entry_date":"2022-11-17","entry_price":43750,"peak_date":"2022-12-01","peak_price":46550,"low_date":"2022-12-29","low_price":31750,"mfe_pct":6.40,"mae_pct":-27.43,"classification":"hard_counterexample","calibration_usable":true}
{"row_type":"shadow_weight","rule_id":"c05_neom_giga_project_scope_margin_cash_bridge_required_v1","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"aggregate","selected_round":"R1","selected_loop":113,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":3,"positive_case_count":1,"counterexample_count":2,"verified_url_repair_needed_count":3}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent applying a batch of E2R v12 residual calibration research artifacts.

Do not use this single file as a production patch by itself. Ingest it with other v12 residual research MD files.

From this file, extract the following candidate rule only as shadow / candidate evidence until batch consensus is reached:

- canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
- rule_id: c05_neom_giga_project_scope_margin_cash_bridge_required_v1
- core idea: Mega-project / NEOM / Saudi Vision labels require company-level signed scope, contract amount, margin bridge, and working-capital bridge. CM/PM/design/engineering labels must be scope-discounted. Strong price route without non-price evidence goes to 4B watch; low-MFE/high-MAE theme fade goes to 4C.

Suggested ingestion:
1. Parse the JSONL rows.
2. Add the cases to the v12 research registry only if no duplicate canonical_archetype_id + ticker + trigger_date + entry_date exists.
3. Do not change production scoring from this file alone.
4. Aggregate with other C05 residual files.
5. Promote only if multiple independent C05 files support the same bridge requirement.
```

## 11. Final Run Summary

```yaml
selected_round: R1
selected_loop: 113
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: NEOM_GIGA_PROJECT_CM_DESIGN_ENGINEERING_SCOPE_MARGIN_BRIDGE_VS_PROJECT_LABEL_THEME_BLOWOFF
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 2
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
verified_url_repair_needed_count: 3
diversity_score_summary: C05 Priority 1 보강 + HanmiGlobal NEOM CM/PM route positive 4B watch + Heerim design-label hard fade + Yushin engineering-consulting-label hard fade
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C05 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c05_neom_giga_project_scope_margin_cash_bridge_required_v1
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C05 mega-project/NEOM/Saudi Vision CM-design-engineering labels
existing_axis_weakened: null
next_recommended_archetypes: C15_MATERIAL_SPREAD_SUPERCYCLE, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```
