---
research_version: e2r_stock_web_v12_residual
selected_round: R1
selected_loop: 112
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_AND_SERVICE_SCOPE_BRIDGE_VS_SMALL_SUPPLIER_THEME_FALSE_POSITIVE
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
created_at_kst: 2026-06-07
stock_agent_code_accessed: false
stock_agent_code_patched: false
handoff_prompt_executed_now: false
---

# C04 Nuclear Policy / Project Legal Delay — residual calibration research

## 0. Execution boundary

This file is a standalone historical calibration / sector-archetype residual research artifact.

It is not a live scan, not a current recommendation list, not a trading signal, not a code patch, and not a production-scoring change.
The only price source used for OHLCV calculation is `Songdaiki/stock-web` tradable raw shard data.

Allowed work performed:

- checked `docs/core/V12_Research_No_Repeat_Index.md` only for coverage/duplicate avoidance;
- checked `Songdaiki/stock-web/atlas/manifest.json`;
- checked actual 1D OHLCV rows for selected historical cases;
- computed entry, MFE, MAE, local peak, and drawdown from row values;
- produced C04-specific shadow-rule candidates only.

Forbidden work not performed:

- no `stock_agent` source-code inspection;
- no production scoring patch;
- no live watchlist;
- no current candidate discovery;
- no brokerage/API action.

## 1. Coverage selection

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` remains a Priority 1 archetype in the no-repeat index, with 31 rows and 19 rows still needed to reach the 50-row practical calibration target.

Previously used C04 examples avoided in this execution:

- Doosan Enerbility
- KEPCO E&C / 한전기술
- BHI / 비에이치아이
- KEPCO KPS / 한전KPS
- Woojin / 우진
- Iljin Power / 일진파워
- KEPCO / 한국전력
- KEPCO Industrial Development / 한전산업
- Bosung Powertec / 보성파워텍
- Woori Technology / 우리기술

This execution adds three new symbols:

1. `126720` 수산인더스트리
2. `019990` 에너토크
3. `046120` 오르비텍

## 2. Source spine

### 2.1 Czech nuclear project legal sequence

C04 is not simply “nuclear headline.” It is a project-timing archetype. The same story passes through several gates:

1. preferred bidder / policy headline;
2. appeals and legal/procedural challenges;
3. competition-authority or court clearance;
4. final contract signing;
5. company-specific scope/backlog/O&M conversion.

The Czech/KHNP Dukovany sequence is useful because it clearly separates those gates:

- 2024-07-17: KHNP selected as preferred bidder for two new Dukovany units, with final contract still to be agreed later.
- 2024-08-27: EDF/Westinghouse appeals highlighted unresolved legal risk.
- 2025-04-24: Czech competition-authority clearance/rejection of EDF appeals reopened signing path.
- 2025-05: a court temporarily blocked signing.
- 2025-06-04: final contract was signed after the legal block was lifted.

### 2.2 Price source

`Songdaiki/stock-web` manifest checked:

- source: `FinanceData/marcap`
- price adjustment: `raw_unadjusted_marcap`
- max date: `2026-02-20`
- calibration shard root: `atlas/ohlcv_tradable_by_symbol_year`
- corporate-action-contaminated windows are blocked by default.

## 3. Case rows

### CASE 1 — 126720 수산인더스트리 — final-contract/legal-clearance service-scope positive watch

```json
{
  "case_id": "C04_R1_L112_126720_2025_04_24_CZECH_LEGAL_CLEARANCE_SERVICE_SCOPE_POSITIVE_WATCH",
  "symbol": "126720",
  "name": "수산인더스트리",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_SERVICE_SCOPE_BRIDGE",
  "trigger_date": "2025-04-24",
  "trigger_type": "czech_khnp_legal_clearance_after_edf_appeals",
  "entry_date": "2025-04-24",
  "entry_price": 19420,
  "peak_date": "2025-06-20",
  "peak_price": 30350,
  "trough_date": "2025-05-07",
  "trough_price": 19100,
  "mfe_pct": 56.28,
  "mae_pct": -1.65,
  "classification": "positive_with_service_scope_4B_watch",
  "calibration_usable": true,
  "source_repair_needed": true
}
```

#### Interpretation

This is the strongest new C04-positive in this run.

The 2025-04-24 legal-clearance gate is much higher quality than the 2024-07 preferred-bidder headline because it comes after legal/procedural challenges. The equity route is also cleaner than the 2024 small-theme cases: entry at 19,420, later high at 30,350, with only shallow early MAE.

However, 수산인더스트리 is still not the prime nuclear-construction contractor in the evidence collected here. It is best treated as **service/O&M-scope positive with 4B watch**, not automatic Stage3-Green.

#### Price row support

- profile: active-like, no corporate-action candidate in this window;
- entry: 2025-04-24 close 19,420;
- MFE: 2025-06-20 high 30,350;
- MAE: 2025-05-07 low 19,100.

#### Score simulation

| model layer | likely old profile behavior | corrected C04 behavior |
|---|---|---|
| headline | nuclear/Czech/legal-clearance positive | positive |
| scope | likely over-credits broad nuclear service label | require company-specific O&M/service scope |
| risk | may miss 4B watch | keep Stage2/Stage2-Actionable shadow only unless scope/backlog is confirmed |
| final | potential Yellow | positive, but Green blocked pending scope evidence |

---

### CASE 2 — 019990 에너토크 — preferred-bidder actuator/theme high-MFE/high-MAE false positive

```json
{
  "case_id": "C04_R1_L112_019990_2024_07_17_CZECH_PREFERRED_BIDDER_ACTUATOR_THEME_FALSE_POSITIVE",
  "symbol": "019990",
  "name": "에너토크",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "PREFERRED_BIDDER_SMALL_SUPPLIER_ACTUATOR_THEME_FALSE_POSITIVE",
  "trigger_date": "2024-07-17",
  "trigger_type": "czech_khnp_preferred_bidder_before_legal_resolution",
  "entry_date": "2024-07-17",
  "entry_price": 7880,
  "peak_date": "2024-07-18",
  "peak_price": 9830,
  "trough_date": "2024-08-05",
  "trough_price": 5240,
  "mfe_pct": 24.75,
  "mae_pct": -33.50,
  "classification": "counterexample_high_MFE_high_MAE_preferred_bidder_theme",
  "calibration_usable": true,
  "source_repair_needed": true
}
```

#### Interpretation

에너토크 shows why C04 needs a **legal gate** and a **scope gate**.

The 2024-07-17 KHNP preferred-bidder headline created immediate upside, but this was not the same as final contract, legal clearance, or company-specific backlog. The next-day spike was tradable in hindsight, but the drawdown that followed was much larger than the MFE.

This should not be scored as Stage3-Green. It is a classic 4B/4C boundary case: price reacted, but the evidence bridge was too thin.

#### Price row support

- profile: active-like; old 2016 corporate-action caveat only, no window block;
- entry: 2024-07-17 close 7,880;
- MFE: 2024-07-18 high 9,830;
- MAE: 2024-08-05 low 5,240.

#### Score simulation

| model layer | likely old profile behavior | corrected C04 behavior |
|---|---|---|
| headline | Czech nuclear win → supplier positive | preferred-bidder only |
| legal gate | likely underweighted | unresolved appeals risk remains |
| scope gate | likely weak | no confirmed company-specific nuclear backlog |
| final | possible false Yellow | 4B/4C watch, no Green |

---

### CASE 3 — 046120 오르비텍 — inspection/radiation-service theme false positive

```json
{
  "case_id": "C04_R1_L112_046120_2024_07_17_CZECH_PREFERRED_BIDDER_INSPECTION_THEME_FALSE_POSITIVE",
  "symbol": "046120",
  "name": "오르비텍",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "PREFERRED_BIDDER_INSPECTION_RADIATION_SERVICE_THEME_FALSE_POSITIVE",
  "trigger_date": "2024-07-17",
  "trigger_type": "czech_khnp_preferred_bidder_before_legal_resolution",
  "entry_date": "2024-07-17",
  "entry_price": 2810,
  "peak_date": "2024-07-18",
  "peak_price": 3200,
  "trough_date": "2024-08-05",
  "trough_price": 2040,
  "mfe_pct": 13.88,
  "mae_pct": -27.40,
  "classification": "counterexample_preferred_bidder_small_service_theme",
  "calibration_usable": true,
  "source_repair_needed": true
}
```

#### Interpretation

오르비텍 has a nuclear-related label, but the 2024 Czech preferred-bidder headline did not provide a clear company-specific scope bridge. The price path validates this: short-lived MFE followed by much larger downside.

For C04, “nuclear inspection / radiation service” is not enough. The model should require:

- final contract or legal clearance,
- defined scope,
- customer or project linkage,
- backlog/order/earnings conversion path.

Without that, it belongs in 4B/4C, not Stage3.

#### Price row support

- profile: active-like; old 2017 corporate-action caveat only, no window block;
- entry: 2024-07-17 close 2,810;
- MFE: 2024-07-18 high 3,200;
- MAE: 2024-08-05 low 2,040.

#### Score simulation

| model layer | likely old profile behavior | corrected C04 behavior |
|---|---|---|
| headline | Czech nuclear win → nuclear service positive | preferred-bidder headline only |
| legal gate | underweighted | appeals/legal risk still unresolved |
| scope gate | weak | inspection label not equal project backlog |
| final | false positive risk | 4B/4C watch |

---

## 4. Aggregate calibration row

```json
{
  "aggregate_id": "C04_R1_L112_AGGREGATE",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "case_count": 3,
  "trigger_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "reused_case_count": 0,
  "full_window_blocked_count": 0,
  "avg_positive_mfe_pct": 56.28,
  "avg_positive_mae_pct": -1.65,
  "avg_counterexample_mfe_pct": 19.31,
  "avg_counterexample_mae_pct": -30.45,
  "residual_error_type": "preferred_bidder_small_supplier_theme_overcredit_without_legal_scope_backlog_bridge"
}
```

## 5. Shadow-rule candidate

```json
{
  "shadow_rule_id": "c04_final_contract_legal_clearance_scope_bridge_required_v2",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "rule_type": "sector_archetype_specific_shadow_rule",
  "production_scoring_changed": false,
  "condition": [
    "If nuclear trigger is only preferred-bidder or policy headline",
    "and company is small supplier/service/theme read-through",
    "and no company-specific project scope/backlog/O&M contract evidence is confirmed"
  ],
  "action": [
    "do_not_score_stage3_green",
    "cap_at_stage2_or_4B_watch",
    "require final contract or legal clearance plus company-specific scope bridge for Stage2-Actionable",
    "require backlog/order/margin/O&M conversion evidence for Stage3-Yellow/Green"
  ],
  "evidence_cases": [
    "019990_2024_07_17",
    "046120_2024_07_17",
    "126720_2025_04_24"
  ],
  "expected_error_reduction": "reduces false-positive nuclear-theme rallies around preferred-bidder headlines while preserving post-legal-clearance service-scope positives"
}
```

## 6. Machine-readable trigger rows

```jsonl
{"canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"126720","name":"수산인더스트리","trigger_date":"2025-04-24","entry_date":"2025-04-24","entry_price":19420,"peak_date":"2025-06-20","peak_price":30350,"trough_date":"2025-05-07","trough_price":19100,"mfe_pct":56.28,"mae_pct":-1.65,"label":"positive_with_service_scope_4B_watch","calibration_usable":true}
{"canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"019990","name":"에너토크","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":7880,"peak_date":"2024-07-18","peak_price":9830,"trough_date":"2024-08-05","trough_price":5240,"mfe_pct":24.75,"mae_pct":-33.50,"label":"counterexample_high_MFE_high_MAE_preferred_bidder_theme","calibration_usable":true}
{"canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"046120","name":"오르비텍","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":2810,"peak_date":"2024-07-18","peak_price":3200,"trough_date":"2024-08-05","trough_price":2040,"mfe_pct":13.88,"mae_pct":-27.40,"label":"counterexample_preferred_bidder_small_service_theme","calibration_usable":true}
```

## 7. Residual contribution

```json
{
  "residual_contribution_id": "C04_R1_L112_RESIDUAL",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": "c04_final_contract_legal_clearance_scope_bridge_required_v2",
  "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C04 nuclear preferred-bidder and small-supplier theme rallies",
  "existing_axis_weakened": null,
  "do_not_propose_new_weight_delta": false,
  "next_recommended_archetypes": [
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C18_CONSUMER_EXPORT_CHANNEL_REORDER"
  ]
}
```

## 8. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the current research session.

```text
You are a coding agent updating stock_agent calibration artifacts after batch review.

Input MD:
e2r_stock_web_v12_residual_round_R1_loop_112_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md

Task:
1. Ingest only machine-readable rows from this MD after human approval.
2. Do not alter production scoring directly.
3. Register the shadow rule candidate:
   c04_final_contract_legal_clearance_scope_bridge_required_v2
4. Add trigger rows only if no duplicate exists for:
   canonical_archetype_id + symbol + trigger_type + entry_date.
5. Preserve these labels:
   - positive_with_service_scope_4B_watch
   - counterexample_high_MFE_high_MAE_preferred_bidder_theme
   - counterexample_preferred_bidder_small_service_theme
6. Keep all C04 changes shadow-only until aggregate validation.
7. Do not run live scans.
```

## 9. Batch Ingest Repair Trigger Rows

The original research body used compact JSON case objects. The following JSONL rows preserve the same cases but add 30D / 90D / 180D MFE and MAE fields recalculated from the local `Songdaiki/stock-web` tradable OHLCV shards so this MD is usable by the v12 batch ingest.

```jsonl
{"MAE_180D_pct": -1.65, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MFE_180D_pct": 56.28, "MFE_30D_pct": 46.24, "MFE_90D_pct": 56.28, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_R1_L112_126720_2025_04_24_CZECH_LEGAL_CLEARANCE_SERVICE_SCOPE_POSITIVE_WATCH", "company_name": "수산인더스트리", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.7, "entry_date": "2025-04-24", "entry_price": 19420, "evidence_available_at_that_date": "Czech nuclear legal clearance/final contract path with service scope bridge, Green blocked until company scope/backlog is confirmed", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "NUCLEAR_FINAL_CONTRACT_LEGAL_CLEARANCE_SERVICE_SCOPE_BRIDGE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "112", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 19820.0, "max_drawdown_low_date": "2025-11-07", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2025-06-20", "peak_price": 30350.0, "positive_or_counterexample": "positive_control_or_positive_watch", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/126/126720/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/126/126720.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C04_R1_L112_126720_2025_04_24_CZECH_LEGAL_CLEARANCE_SERVICE_SCOPE_POSITIVE_WATCH", "source_proxy_only": true, "stage2_evidence_fields": ["Czech nuclear legal clearance/final contract path with service scope bridge, Green blocked until company scope/backlog is confirmed"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "126720", "trigger_date": "2025-04-24", "trigger_id": "C04_R1_L112_126720_2025_04_24_CZECH_LEGAL_CLEARANCE_SERVICE_SCOPE_POSITIVE_WATCH_TRIGGER", "trigger_outcome_label": "final_contract_legal_clearance_service_scope_positive_watch", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -48.86, "MAE_30D_pct": -33.5, "MAE_90D_pct": -33.5, "MFE_180D_pct": 24.75, "MFE_30D_pct": 24.75, "MFE_90D_pct": 24.75, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_R1_L112_019990_2024_07_17_CZECH_PREFERRED_BIDDER_ACTUATOR_THEME_FALSE_POSITIVE", "company_name": "에너토크", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -59.0, "entry_date": "2024-07-17", "entry_price": 7880, "evidence_available_at_that_date": "preferred bidder headline before legal resolution without company-specific actuator backlog bridge", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "PREFERRED_BIDDER_SMALL_SUPPLIER_ACTUATOR_THEME_FALSE_POSITIVE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "112", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 4030.0, "max_drawdown_low_date": "2024-12-09", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2024-07-18", "peak_price": 9830.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/019/019990/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/019/019990.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C04_R1_L112_019990_2024_07_17_CZECH_PREFERRED_BIDDER_ACTUATOR_THEME_FALSE_POSITIVE", "source_proxy_only": true, "stage2_evidence_fields": ["preferred bidder headline before legal resolution without company-specific actuator backlog bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "019990", "trigger_date": "2024-07-17", "trigger_id": "C04_R1_L112_019990_2024_07_17_CZECH_PREFERRED_BIDDER_ACTUATOR_THEME_FALSE_POSITIVE_TRIGGER", "trigger_outcome_label": "preferred_bidder_supplier_theme_high_mfe_high_mae_false_positive", "trigger_type": "Stage2"}
{"MAE_180D_pct": -36.26, "MAE_30D_pct": -27.4, "MAE_90D_pct": -27.4, "MFE_180D_pct": 13.88, "MFE_30D_pct": 13.88, "MFE_90D_pct": 13.88, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_R1_L112_046120_2024_07_17_CZECH_PREFERRED_BIDDER_INSPECTION_THEME_FALSE_POSITIVE", "company_name": "오르비텍", "corporate_action_window_status": "clean_180D_window_from_research_profile_check", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.03, "entry_date": "2024-07-17", "entry_price": 2810, "evidence_available_at_that_date": "preferred bidder headline before legal resolution without company-specific inspection/radiation service backlog bridge", "evidence_source": "source_proxy_from_research_text; URL verification pending", "evidence_url_pending": true, "fine_archetype_id": "PREFERRED_BIDDER_INSPECTION_RADIATION_SERVICE_THEME_FALSE_POSITIVE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "112", "loop_objective": "zero_trigger_doc_batch_ingest_repair", "max_drawdown_low": 1791.0, "max_drawdown_low_date": "2024-12-09", "parse_repair_note": "added to convert zero-trigger research MD into batch-ingestable v12 trigger rows using local stock-web OHLCV", "peak_date": "2024-07-18", "peak_price": 3200.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/046/046120.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C04_R1_L112_046120_2024_07_17_CZECH_PREFERRED_BIDDER_INSPECTION_THEME_FALSE_POSITIVE", "source_proxy_only": true, "stage2_evidence_fields": ["preferred bidder headline before legal resolution without company-specific inspection/radiation service backlog bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["4B watch if price premium expands without fresh company-specific bridge"], "stage4c_evidence_fields": ["4C watch if thesis bridge fails or high-MAE drawdown confirms"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "046120", "trigger_date": "2024-07-17", "trigger_id": "C04_R1_L112_046120_2024_07_17_CZECH_PREFERRED_BIDDER_INSPECTION_THEME_FALSE_POSITIVE_TRIGGER", "trigger_outcome_label": "preferred_bidder_small_service_theme_false_positive", "trigger_type": "Stage2"}
```
