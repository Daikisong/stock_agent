# E2R v12 Residual Research — R1 / L1 / C05 EPC Mega Contract Margin Gap

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 92
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_MEGA_CONTRACT_MARGIN_BRIDGE_VS_ORDER_HEADLINE_AND_WORKING_CAPITAL_GAP
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: undercovered_canonical_rows_and_current_index_gap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_atlas_repo: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
source_proxy_only: true
evidence_url_pending: true
```

## 1. Selection and novelty check

Latest No-Repeat Index shows C05_EPC_MEGA_CONTRACT_MARGIN_GAP as one of the thinnest C01-C32 canonical scopes in the current corpus. The goal of this run is not to restate the already-applied global rule that price-only blowoff needs non-price evidence. The useful residual question is narrower:

> In EPC/plant/mega-contract names, when does order backlog actually become margin/FCF/revision evidence, and when is it only contract-value vocabulary?

Hard duplicate gate used:

```text
duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
selected symbols = 028050, 034020, 047040, 000720
```

These are used as a C05 margin-bridge stress set. All non-price evidence is kept as source_proxy_only / evidence_url_pending, so this file is a shadow ledger item, not a production patch.

## 2. Price source validation

```json
{
  "row_type": "price_source_validation",
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "manifest_max_date": "2026-02-20",
  "calculation_rule": "MFE_N_pct=(max high from entry_date through N tradable rows / entry_price - 1)*100; MAE_N_pct=(min low from entry_date through N tradable rows / entry_price - 1)*100",
  "corporate_action_window_block": true,
  "data_quality_label": "usable_with_caveat",
  "evidence_url_pending": true,
  "source_proxy_only": true
}
```

## 3. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "C05_L92_028050_20240228_margin_recovery_stress", "symbol": "028050", "company_name": "Samsung E&A", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_SELECTIVE_ORDER_MARGIN_RECOVERY_BRIDGE_VS_MEGA_CONTRACT_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "round": "R1", "loop": 92, "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 26000, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 8.27, "MAE_30D_pct": -8.08, "MFE_90D_pct": 8.27, "MAE_90D_pct": -16.92, "MFE_180D_pct": 12.69, "MAE_180D_pct": -18.85, "stage_path_observed": "Stage2 -> Yellow watch -> failed Green unless margin/revision bridge arrives", "evidence_family": "EPC_order_margin_bridge_proxy", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_to_production": true, "notes": "Price spike around 2024-02-28 produced only modest 30D MFE and later drawdown; C05 should require contract-margin bridge not headline order vocabulary."}
{"row_type": "trigger", "case_id": "C05_L92_034020_20240311_plant_project_beta", "symbol": "034020", "company_name": "Doosan Enerbility", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EQUIPMENT_PROJECT_ORDER_MARGIN_BRIDGE_VS_POLICY_EPC_THEME_BETA", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "round": "R1", "loop": 92, "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-11", "entry_date": "2024-03-11", "entry_price": 16720, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 13.16, "MAE_30D_pct": -14.35, "MFE_90D_pct": 34.57, "MAE_90D_pct": -14.35, "MFE_180D_pct": 49.52, "MAE_180D_pct": -14.35, "stage_path_observed": "Stage2 -> volatile Yellow/Green candidate but high-MAE guard required", "evidence_family": "large_project_equipment_backlog_proxy", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_to_production": true, "notes": "Strong later MFE exists, but entry path carries deep MAE. C05 profile should not Green this without delivery/margin visibility and position-risk haircut."}
{"row_type": "trigger", "case_id": "C05_L92_047040_20240110_contract_theme_decay", "symbol": "047040", "company_name": "Daewoo E&C", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_CONTRACT_HEADLINE_VS_WORKING_CAPITAL_MARGIN_GAP", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "round": "R1", "loop": 92, "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 4260, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 1.88, "MAE_30D_pct": -9.15, "MFE_90D_pct": 1.88, "MAE_90D_pct": -14.91, "MFE_180D_pct": 16.55, "MAE_180D_pct": -14.91, "stage_path_observed": "Stage2 label -> drawdown/sideways -> only late event MFE", "evidence_family": "contract_headline_no_margin_bridge_proxy", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_to_production": true, "notes": "Classic C05 counterexample: mega-contract/EPC label without margin and working-capital evidence should remain Yellow/Red, not Green."}
{"row_type": "trigger", "case_id": "C05_L92_000720_20240422_backlog_not_margin", "symbol": "000720", "company_name": "Hyundai Engineering & Construction", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "INFRA_CONSTRUCTION_BACKLOG_BRIDGE_VS_CONTRACT_VALUE_LABEL", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "round": "R1", "loop": 92, "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 34000, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 5.88, "MAE_30D_pct": -2.79, "MFE_90D_pct": 5.88, "MAE_90D_pct": -7.5, "MFE_180D_pct": 5.88, "MAE_180D_pct": -7.5, "stage_path_observed": "Stage2 -> low-MFE plateau; no Green unless margin bridge appears", "evidence_family": "backlog_value_vs_margin_conversion_proxy", "source_proxy_only": true, "evidence_url_pending": true, "do_not_promote_to_production": true, "notes": "Backlog can support Stage2 observation, but low MFE without margin revision argues for C05 bridge requirement."}
```

## 4. Case notes

### 4.1 028050 Samsung E&A — order vocabulary without immediate margin confirmation

Entry uses 2024-02-28 close 26,000. The stock showed a short-term high of 28,150 around mid-March, but later drifted toward the low 21,000s by early October. That is exactly the C05 trap: the market can briefly pay for order/contract language, then withdraw that premium if margin conversion and revision do not follow.

Score interpretation:

```text
current_profile_candidate_stage = Stage2-Actionable / Yellow
green_block_reason = missing_verified_contract_margin_revision_bridge
4B_status = local_4B_not_full_4B
residual_error = possible Stage2 over-credit if contract headline is counted as backlog-quality evidence
```

### 4.2 034020 Doosan Enerbility — high MFE but also high MAE

Entry uses 2024-03-11 close 16,720. Later MFE is strong, but the early path included a drawdown into the mid-14,000s before the move recovered. This is not a clean Green; it is a position-risk-heavy Yellow/Green candidate.

Score interpretation:

```text
current_profile_candidate_stage = Stage2-Actionable -> Stage3-Yellow
green_requires = project delivery acceptance + margin/revision evidence
guardrail = high_MAE_guardrail
```

### 4.3 047040 Daewoo E&C — contract headline decay

Entry uses 2024-01-10 close 4,260. The 30D and 90D MFE were weak while MAE deepened. Later July rebound exists, but it behaves more like sector beta / delayed event MFE than a clean margin-bridge rerating.

Score interpretation:

```text
current_profile_candidate_stage = Stage2-FalsePositive
green_block_reason = working_capital_margin_gap
4B_status = no full 4B; no durable non-price bridge
```

### 4.4 000720 Hyundai E&C — backlog is not yet margin

Entry uses 2024-04-22 close 34,000. 30D MFE reached about 5.88%, but 90D/180D did not expand into a structural rerating. This supports a C05 rule: backlog value can justify observation, but not Green unless margin quality, cash conversion, or revision evidence is verified.

## 5. Aggregate metric

```json
{
  "row_type": "aggregate_metric",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "round": "R1",
  "loop": 92,
  "sample_trigger_rows": 4,
  "positive_or_partial_positive": 1,
  "counterexample_rows": 3,
  "median_MFE_90D_pct": 7.08,
  "median_MAE_90D_pct": -12.21,
  "dominant_residual_error": "contract/backlog vocabulary receives too much Stage2/Green credit without margin bridge",
  "production_patch_ready": false,
  "blocked_reason": "evidence_url_pending_and_source_proxy_only"
}
```

## 6. Shadow weight candidate

```json
{
  "row_type": "shadow_weight",
  "scope": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "axis": "stage2_required_bridge",
  "proposal": "For C05, Stage2 can be observed on contract/backlog vocabulary, but Stage3-Green requires at least one verified bridge: margin guidance/revision, delivery acceptance, cash conversion, or working-capital improvement.",
  "suggested_delta": {
    "industrial_subscore.order_backlog": -0.5,
    "revision_score.forward_margin_bridge": 1.0,
    "financial_actual.cash_conversion": 0.5,
    "risk_penalty.working_capital_gap": 1.0
  },
  "promotion_ready": false,
  "why_not_ready": "Exact non-price URL validation is pending."
}
```

```json
{
  "row_type": "shadow_weight",
  "scope": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "axis": "local_4b_watch_guard",
  "proposal": "If C05 price has already moved >40% within the prior 90 trading days but no fresh margin/revision bridge appears, classify as local 4B watch rather than Green.",
  "promotion_ready": false,
  "why_not_ready": "Needs exact evidence URLs and more clean cases."
}
```

## 7. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "contribution_label": "bridge_required_counterexample_set",
  "new_symbol_count": 4,
  "new_trigger_family": "EPC mega-contract headline vs margin/FCF/revision bridge",
  "positive_counterexample_balance": "1 partial positive / 3 counterexamples",
  "recommended_next": [
    "Add exact 공시/IR/report URLs for contract margin and working-capital bridge.",
    "Add overseas plant/EPC cases where backlog converted into clean margin revision.",
    "Separate C05 EPC margin gap from C30 construction PF balance-sheet repair."
  ]
}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff during research generation.

When batch-applying v12 residual research files, ingest this MD as a shadow-only C05 candidate. Do not change production scoring from this file alone. First verify non-price evidence URLs for each row. If evidence is verified, consider a C05-specific stage2_required_bridge rule: contract/backlog vocabulary alone may support Stage2 observation but cannot support Stage3-Green unless margin guidance, delivery acceptance, FCF/cash conversion, or working-capital improvement is present. Also consider local_4b_watch_guard for C05 when price has already rerated without fresh margin bridge.
```

## 9. Next research state

```text
completed_round = R1
completed_loop = 92
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = undercovered_canonical_rows_and_current_index_gap
next_recommended_archetypes = C05 exact URL repair, C03/C07/C13/C17/C19/C20/C23/C26 blocked_by_data_quality URL verification, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW non-overlapping cases
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
