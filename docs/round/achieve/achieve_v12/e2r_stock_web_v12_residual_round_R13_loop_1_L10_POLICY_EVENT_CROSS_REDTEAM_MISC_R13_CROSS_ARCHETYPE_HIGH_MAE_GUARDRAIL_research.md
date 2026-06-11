# E2R Stock-Web v12 Residual Research — R13 Cross-Archetype High-MAE Guardrail

```text
schema_family = v12_sector_archetype_residual
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research

selected_round = R13
selected_loop = 1
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id = CROSS_ARCHETYPE_VERTICAL_MFE_HIGH_MAE_AND_LOW_MFE_HIGH_MAE_GUARDRAIL

selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
handoff_prompt_executed_now = false
```

## 1. Selection rationale

`R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` is selected because the latest No-Repeat Index shows all R13 cross-archetype scopes at zero representative rows. R13 is not a sector discovery round. It is a checkpoint comparing false positive, high-MAE, 4B timing, 4C lateness, and evidence-trust issues already observed across R1~R12.

This run therefore avoids creating a new sector-specific thesis. It stress-tests the common failure pattern:

> A case can show large early MFE, but if it also produces deep 90D/180D MAE without refreshed non-price evidence, the profile should not treat the price route as clean Stage3 persistence. It should receive high-MAE watch, local 4B cap, or Stage2 false-positive blocking depending on evidence quality.

## 2. Price source validation

The run uses `Songdaiki/stock-web` 1D OHLCV shards only.

```text
manifest = atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
```

All four rows below include complete 30D / 90D / 180D MFE and MAE fields.

## 3. Cross-case comparison table

| symbol | name | source canonical | trigger_type | entry_date | entry_price | MFE 30/90/180 | MAE 30/90/180 | R13 classification |
|---|---|---|---|---:|---:|---:|---:|---|
| 079550 | LIG넥스원 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Stage2-Actionable | 2024-09-19 | 206,500 | 28.33%/31.48%/57.14% | -0.48%/-18.26%/-18.26% | positive_with_high_MAE_watch |
| 006260 | LS | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | Stage2-Actionable | 2024-04-26 | 127,800 | 52.43%/52.43%/52.43% | -6.10%/-26.45%/-33.88% | positive_price_path_but_local_4B_watch |
| 010950 | S-Oil | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Stage2-Actionable | 2024-02-13 | 71,500 | 11.47%/18.18%/18.18% | -0.14%/-6.57%/-25.31% | positive_rebound_but_later_4B_watch |
| 051910 | LG화학 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Stage2-FalsePositive | 2024-05-20 | 391,500 | 2.04%/2.04%/2.04% | -14.05%/-32.69%/-46.87% | counterexample_high_MAE |

## 4. Case notes

### 4.1 LIG넥스원 — signed export positive, but drawdown bridge is not free

LIG Nex1 has a real defense-export/backlog bridge, not a pure theme label. However, the stock path still shows that a confirmed export framework can suffer a deep drawdown before the next confirmation leg. Entry is `2024-09-19 close 206,500`. The path reached `271,500` on `2024-11-08` and later `324,500` on `2025-03-06`, but also printed `168,800` on `2024-12-10`.

R13 interpretation: signed export can keep the case eligible, but high-MAE watch should require refreshed delivery/backlog/revision evidence before persistent Stage3-Green-style treatment.

### 4.2 LS — vertical MFE from strategic-resource/electrification bridge, then local 4B risk

LS had a stronger company-level supply-chain bridge than a simple resource label. Still, entry at `2024-04-26 close 127,800` was followed by `194,800` on `2024-05-21`, then a deep path to `94,000` on `2024-08-05` and `84,500` on `2024-11-18`.

R13 interpretation: vertical MFE above +50% should not mechanically validate persistence. Without renewed margin/revision/cash-flow confirmation, this path is a local 4B watch pattern.

### 4.3 S-Oil — refining-margin rebound can be real and still fade

S-Oil shows the softer variant of the same problem. Entry at `2024-02-13 close 71,500` reached `79,700` on `2024-03-15` and `84,500` on `2024-04-08`, but later printed `53,400` on `2024-12-09`.

R13 interpretation: a commodity-margin rebound can deserve Stage2, but if the margin bridge fades and 180D MAE crosses roughly -25%, the rule should downgrade persistence and shift the case into local 4B watch.

### 4.4 LG화학 — low-MFE/high-MAE false Stage2 prototype

LG Chem is the clearest high-MAE block case. Entry at `2024-05-20 close 391,500` had only `399,500` as the relevant high in the early window, while the path fell to `263,500` on `2024-08-05` and `208,000` on `2025-02-10`.

R13 interpretation: when MFE is weak and MAE is deep, the case should not be rescued by sector vocabulary. For integrated large-cap chemical names, segment-level margin/revision/cash bridge is mandatory.

## 5. Trigger rows JSONL

```jsonl
{"MAE_180D_pct": -18.26, "MAE_30D_pct": -0.48, "MAE_90D_pct": -18.26, "MFE_180D_pct": 57.14, "MFE_30D_pct": 28.33, "MFE_90D_pct": 31.48, "as_of_date": "2024-09-19", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "classification": "positive_with_high_MAE_watch", "corporate_action_contamination": "none_in_selected_window_based_on_profile_caveat_check_or_not_near_candidate", "entry_date": "2024-09-19", "entry_price": 206500, "evidence_family": "signed_export_framework_repeat_government_customer_but_drawdown_before_next_confirmation", "fine": "SIGNED_DEFENSE_EXPORT_BACKLOG_WITH_HIGH_MAE_WATCH", "guardrail": "confirmed export/backlog can remain Stage2/3 candidate, but 90D MAE near -18% requires high-MAE watch and confirmation refresh before any Green-like persistence credit", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": "1", "name": "LIG넥스원", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "round": "R13", "source_canonical": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "source_lines": "079550/2024.csv: 2024-09-19 entry, 2024-10-22 265000 high, 2024-11-08 271500 high, 2024-12-10 168800 low; 079550/2025.csv: 2025-03-06 324500 high", "symbol": "079550", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -33.88, "MAE_30D_pct": -6.1, "MAE_90D_pct": -26.45, "MFE_180D_pct": 52.43, "MFE_30D_pct": 52.43, "MFE_90D_pct": 52.43, "as_of_date": "2024-04-26", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "classification": "positive_price_path_but_local_4B_watch", "corporate_action_contamination": "none_in_selected_window_based_on_profile_caveat_check_or_not_near_candidate", "entry_date": "2024-04-26", "entry_price": 127800, "evidence_family": "strategic_resource_supply_chain_bridge_with_vertical_MFE_and_deep_followthrough_MAE", "fine": "COPPER_ELECTRIFICATION_SUPPLY_CHAIN_VERTICAL_MFE_HIGH_MAE", "guardrail": "vertical MFE above +50% is not enough; if later 90D/180D MAE exceeds -25% without renewed margin/revision evidence, local 4B watch should cap persistence", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": "1", "name": "LS", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "round": "R13", "source_canonical": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "source_lines": "006260/2024.csv: 2024-04-26 entry 127800, 2024-05-21 high 194800, 2024-08-05 low 94000, 2024-11-18 low 84500", "symbol": "006260", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -25.31, "MAE_30D_pct": -0.14, "MAE_90D_pct": -6.57, "MFE_180D_pct": 18.18, "MFE_30D_pct": 11.47, "MFE_90D_pct": 18.18, "as_of_date": "2024-02-13", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "classification": "positive_rebound_but_later_4B_watch", "corporate_action_contamination": "none_in_selected_window_based_on_profile_caveat_check_or_not_near_candidate", "entry_date": "2024-02-13", "entry_price": 71500, "evidence_family": "refining_margin_rebound_without_durable_margin_confirmation", "fine": "REFINING_MARGIN_REBOUND_THEN_MARGIN_FADE", "guardrail": "commodity margin rebound can create early MFE, but if margin evidence fades and 180D MAE crosses -25%, residual guard should shift from Stage2 persistence to local 4B watch", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": "1", "name": "S-Oil", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "round": "R13", "source_canonical": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "source_lines": "010950/2024.csv: 2024-02-13 entry 71500, 2024-03-15 high 79700, 2024-04-08 high 84500, 2024-12-09 low 53400", "symbol": "010950", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -46.87, "MAE_30D_pct": -14.05, "MAE_90D_pct": -32.69, "MFE_180D_pct": 2.04, "MFE_30D_pct": 2.04, "MFE_90D_pct": 2.04, "as_of_date": "2024-05-20", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "classification": "counterexample_high_MAE", "corporate_action_contamination": "none_in_selected_window_based_on_profile_caveat_check_or_not_near_candidate", "entry_date": "2024-05-20", "entry_price": 391500, "evidence_family": "integrated_largecap_petchem_headline_without_segment_margin_revision_cash_bridge", "fine": "PETCHEM_FEEDSTOCK_HEADLINE_AND_MIX_DILUTION_HIGH_MAE_FALSE_STAGE2", "guardrail": "low-MFE/high-MAE profile should be hard-blocked as Stage2 false positive unless company-specific segment margin and cash-flow bridge appears", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": "1", "name": "LG화학", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "round": "R13", "source_canonical": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "source_lines": "051910/2024.csv: 2024-05-20 entry 391500, 2024-05-28 high 399500, 2024-08-05 low 263500; 051910/2025.csv: 2025-02-10 low 208000", "symbol": "051910", "trigger_type": "Stage2-FalsePositive"}
```

## 6. Aggregate residual summary

```text
case_count = 4
calibration_usable_case_count = 4
source_canonical_count = 3
positive_with_high_MAE_watch_count = 2
positive_rebound_but_later_4B_watch_count = 1
counterexample_high_MAE_count = 1

mean_MFE_180D_pct = 32.45
mean_MAE_180D_pct = -31.08
high_MAE_threshold_suggested = MAE_90D <= -18% or MAE_180D <= -25%
low_MFE_high_MAE_block_suggested = MFE_90D < +10% and MAE_90D <= -25%
vertical_MFE_local_4B_watch_suggested = MFE_30D >= +30% and MAE_90D <= -25%
```

## 7. Score-return alignment stress test

The common error is not that all high-MAE cases are bad. The common error is that the score can confuse **MFE availability** with **clean persistence**.

```text
if non_price_bridge_is_strong and MFE_30D >= +20% and MAE_90D > -15%:
    keep Stage2/Stage3 persistence path open

if non_price_bridge_is_strong and MFE_30D >= +30% and MAE_90D <= -25%:
    keep case usable but add local_4B_high_MAE_watch
    require refreshed non-price evidence before persistent Stage3-Green credit

if MFE_90D < +10% and MAE_90D <= -25%:
    classify as Stage2-FalsePositive unless fresh company-specific bridge appears

if MAE_180D <= -25% and no refreshed margin/revision/cash evidence:
    cap positive contribution; do not allow price-only success narrative
```

## 8. Shadow rule candidate

```text
rule_candidate_id = R13_HIGH_MAE_GUARDRAIL_CROSS_ARCHETYPE_V1
rule_type = cross_archetype_guardrail
applies_to = all canonical_archetype_id
shadow_only = true
production_scoring_changed = false

condition_A_vertical_mfe_watch:
    MFE_30D_pct >= +30
    and MAE_90D_pct <= -25
    and refreshed_non_price_bridge == false

action_A:
    add local_4B_watch
    reduce persistence confidence
    block Stage3-Green persistence credit until new non-price evidence appears

condition_B_low_mfe_high_mae_block:
    MFE_90D_pct < +10
    and MAE_90D_pct <= -25

action_B:
    classify as Stage2-FalsePositive or counterexample
    block sector-vocabulary-only Stage2 promotion

condition_C_late_fade:
    MAE_180D_pct <= -25
    and no refreshed margin/revision/cash bridge

action_C:
    cap positive contribution
    add high_MAE_guardrail tag
```

## 9. Residual contribution summary

```text
sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = false
cross_archetype_guardrail_candidate = true
loop_contribution_label = cross_archetype_high_MAE_guardrail_candidate

new_axis_proposed = R13_cross_archetype_high_MAE_watch_and_low_MFE_block
existing_axis_strengthened = high_MAE_guard; local_4B_watch_guard; price_only_success_block
existing_axis_weakened = null

do_not_propose_new_weight_delta = false
shadow_weight_only = true
```

## 10. Novelty and no-repeat check

```text
NO_REPEAT_INDEX_USED = docs/core/V12_Research_No_Repeat_Index.md
R13 prior rows in index = 0
selected_canonical_scope = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
selected_loop = 1

dedupe_basis:
- this is a cross-archetype checkpoint, not a same canonical sector rerun
- selected rows intentionally come from different source canonical archetypes
- the output canonical is R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
- same source-sector examples may have appeared in previous R1~R12 loops, but R13 uses them for cross-case guardrail validation, not as new sector positives
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the current research run.

```text
You are the later coding agent for stock_agent. Read this MD together with the v12 batch corpus.

Task:
- Treat this file as a cross-archetype high-MAE guardrail research artifact.
- Do not change production scoring automatically.
- Add or test only shadow logic if the batch aggregation supports it.
- Candidate guardrail:
  - vertical MFE with MAE_90D <= -25% requires local_4B_watch unless refreshed non-price evidence appears.
  - low MFE / high MAE blocks Stage2 promotion when sector vocabulary is the main evidence.
  - MAE_180D <= -25% without renewed margin/revision/cash bridge caps positive contribution.
- Validate the rule across all canonical archetypes before applying.
```

## 12. Next research state

```text
completed_round = R13
completed_loop = 1
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
