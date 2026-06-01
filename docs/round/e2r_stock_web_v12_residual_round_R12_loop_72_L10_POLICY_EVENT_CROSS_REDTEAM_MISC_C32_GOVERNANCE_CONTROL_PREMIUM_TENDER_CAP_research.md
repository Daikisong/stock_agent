# E2R Stock-Web v12 Residual Research — R12 Loop 72 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 72,
  "computed_next_round": "R13",
  "computed_next_loop": 72,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE",
  "loop_objective": [
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "tender_cap_and_control_contest_lifecycle_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## Round / scope resolution

Previous completed state in this interactive run: R11 / loop 72.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 72
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R13
computed_next_loop = 72
```

R12 was routed to C32 because this is a governance/control premium/tender cap residual test.  
The accidental intermediate R11 file generated during this request is not the final artifact and should be ignored.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C32 has high concentration in Korea Zinc / SM style names.  
This run avoids the existing top-covered symbols and adds:

```text
008930 / 한미사이언스 / control contest and execution risk
036560 / 영풍정밀/KZ정밀 / tender battle and tender-cap fade
001750 / 한양증권 / control-stake sale process and closing/price-cap risk
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C32 is not simply “control premium.”

A governance event can light the fuse, but the rerating only survives if there is a closing bridge.

```text
C32 positive:
  explicit tender price / buyer certainty / sale-process closing path / shareholder approval
  + controlled MAE or clear post-event floor

C32 false positive:
  control-contest headline / family dispute / strategic rumor
  + no tender price or no clean closing bridge
  + post-peak drawdown

C32 local 4B:
  tender or control premium MFE
  + tender window closes or execution risk rises
  + price falls back toward pre-event range
```

Control premium is a bridge with a toll gate.  
If the gate price is real and cars can cross, the bridge matters.  
If the gate disappears, the traffic backs up into drawdown.

---

## Case 1 — Counterexample: 008930 / 한미사이언스 / control-contest execution risk

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is the OCI/Hanmi group integration, board/shareholder approval, family control contest, and execution risk path.

```text
evidence_family = OCI_HANMI_GROUP_CONTROL_CONTEST_EXECUTION_RISK_WITH_NO_TENDER_PRICE
case_role = counterexample
trigger_date = 2024-01-12
entry_date = 2024-01-15
entry_price = 46,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv`:

```text
2024-01-15,46350,47650,40450,43300
2024-01-16,42300,56200,42200,56200
2024-03-28,41350,47000,38000,44350
2024-09-05,31350,31400,30500,30950
```

### Backtest

```text
MFE_30D  = +21.25%
MAE_30D  = -16.50%
MFE_90D  = +21.25%
MAE_90D  = -24.70%
MFE_180D = +21.25%
MAE_180D = -34.20%
peak_180 = 56,200 on 2024-01-16
trough_180 = 30,500 on 2024-09-05
peak_to_later_drawdown = -45.73%
```

### Interpretation

This is the C32 control-contest trap.  
The first peak looked like a control-premium rerating, but without clean closing/tender certainty, the stock-web path became a drawdown.

The model should not promote this to durable Green without:

```text
tender price
shareholder approval
board execution certainty
legal/closing bridge
```

---

## Case 2 — Positive with later 4B-watch: 036560 / 영풍정밀/KZ정밀 / tender battle cap

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is the Korea Zinc-related tender battle, tender price, competing bid/tender window, and control-premium cap.

```text
evidence_family = KOREA_ZINC_RELATED_TENDER_BATTLE_CONTROL_PREMIUM_WITH_TENDER_CAP_RISK
case_role = positive_with_later_4b_watch
trigger_date = 2024-09-12
entry_date = 2024-09-13
entry_price = 12,180
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv` and `2025.csv`:

```text
2024-09-13,12180,12180,12180,12180
2024-09-20,20550,20550,20550,20550
2024-10-07,34200,36700,33300,34700
2024-11-29,15070,15070,14110,14150
2025-04-07,10410,11010,10260,10290
```

### Backtest

```text
MFE_30D  = +201.31%
MAE_30D  = +0.00%
MFE_90D  = +201.31%
MAE_90D  = +0.00%
MFE_180D = +201.31%
MAE_180D = -15.76%
peak_180 = 36,700 on 2024-10-07
trough_180 = 10,260 on 2025-04-07
peak_to_later_drawdown = -72.04%
```

### Interpretation

This is a powerful C32 positive path, but only inside the tender-battle lifecycle.  
The tender/control premium bridge can be Stage2 while the tender math is alive. After the tender window and control premium peak, the local 4B-watch must activate quickly.

The rule should be:

```text
explicit tender price / control battle bridge → Stage2 possible
post-tender fade or price falling back toward pre-event range → local 4B-watch
```

---

## Case 3 — Positive with execution cap: 001750 / 한양증권 / sale process

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is control-stake sale process, buyer certainty, closing path, and price-cap risk.

```text
evidence_family = SECURITIES_FIRM_CONTROL_STAKE_SALE_PROCESS_WITH_CLOSING_RISK_AND_PRICE_CAP
case_role = positive_with_execution_cap
trigger_date = 2024-07-10
entry_date = 2024-07-11
entry_price = 11,630
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv` and `2025.csv`:

```text
2024-07-11,11630,13000,11610,12790
2024-07-15,15000,17210,14330,15000
2024-08-05,19000,19410,15490,16160
2025-03-13,12060,12070,11300,11590
```

### Backtest

```text
MFE_30D  = +66.90%
MAE_30D  = -0.17%
MFE_90D  = +66.90%
MAE_90D  = -0.17%
MFE_180D = +66.90%
MAE_180D = -2.84%
peak_180 = 19,410 on 2024-08-05
trough_180 = 11,300 on 2025-03-13
peak_to_later_drawdown = -41.78%
```

### Interpretation

This is a sale-process positive with a cap.  
The early path is attractive, but the stock later returns close to pre-event levels. That means C32 needs a lifecycle stage:

```text
sale process live → Stage2 possible
closing/price certainty weakens or time passes → local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
full_4b_requires_non_price_evidence = keep
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C32_weight = true
do_not_treat_control_contest_as_Green_without_closing_bridge = true
do_not_convert_tender_fade_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE
```

This fine archetype covers:

```text
1. control-contest headline without tender/closing certainty → false Stage2 / local 4B
2. explicit tender battle/control premium → Stage2 possible, later local 4B after tender cap
3. control-stake sale process → Stage2 possible, later local 4B if closing/price certainty fades
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B-Local-ControlContestExecutionRisk", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy row; stock-web path usable, but non-proxy governance/tender/sale-process evidence must be attached before promotion."}
{"row_type": "case", "case_id": "R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-TenderBattleWithLater4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy row; stock-web path usable, but non-proxy governance/tender/sale-process evidence must be attached before promotion."}
{"row_type": "case", "case_id": "R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP", "symbol": "001750", "company_name": "한양증권", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-SaleProcessTenderCap", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy row; stock-web path usable, but non-proxy governance/tender/sale-process evidence must be attached before promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF", "case_id": "R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "loop_objective": "tender_cap_and_control_contest_lifecycle_test", "trigger_type": "Stage4B-Local-ControlContestExecutionRisk", "trigger_date": "2024-01-12", "entry_date": "2024-01-15", "entry_price": 46350.0, "evidence_available_at_that_date": "OCI_HANMI_GROUP_CONTROL_CONTEST_EXECUTION_RISK_WITH_NO_TENDER_PRICE", "evidence_source": "source_proxy_manual_verification_required:HANMI_SCIENCE_OCI_GROUP_INTEGRATION_CONTROL_CONTEST_BOARD_SHAREHOLDER_EXECUTION_RISK_2024", "stage2_evidence_fields": ["governance_event", "control_premium_or_sale_process_attention"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tender_cap_or_execution_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.25, "MFE_90D_pct": 21.25, "MFE_180D_pct": 21.25, "MAE_30D_pct": -16.5, "MAE_90D_pct": -24.7, "MAE_180D_pct": -34.2, "peak_date": "2024-01-16", "peak_price": 56200.0, "drawdown_after_peak_pct": -45.73, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_should_fire_after_tender_or_control_peak", "four_b_full_window_peak_proximity": "full_4b_requires_execution_failure_or_non_price_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_008930_2024-01-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "case_id": "R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "loop_objective": "tender_cap_and_control_contest_lifecycle_test", "trigger_type": "Stage2-Actionable-TenderBattleWithLater4B", "trigger_date": "2024-09-12", "entry_date": "2024-09-13", "entry_price": 12180.0, "evidence_available_at_that_date": "KOREA_ZINC_RELATED_TENDER_BATTLE_CONTROL_PREMIUM_WITH_TENDER_CAP_RISK", "evidence_source": "source_proxy_manual_verification_required:YOUNGPOONG_PRECISION_KOREA_ZINC_TENDER_BATTLE_CONTROL_PREMIUM_TENDER_CAP_2024", "stage2_evidence_fields": ["governance_event", "control_premium_or_sale_process_attention"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tender_cap_or_execution_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv", "profile_path": "atlas/symbol_profiles/036/036560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 201.31, "MFE_90D_pct": 201.31, "MFE_180D_pct": 201.31, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -15.76, "peak_date": "2024-10-07", "peak_price": 36700.0, "drawdown_after_peak_pct": -72.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_should_fire_after_tender_or_control_peak", "four_b_full_window_peak_proximity": "full_4b_requires_execution_failure_or_non_price_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_036560_2024-09-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP", "case_id": "R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP", "symbol": "001750", "company_name": "한양증권", "round": "R12", "loop": "72", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "loop_objective": "tender_cap_and_control_contest_lifecycle_test", "trigger_type": "Stage2-Actionable-SaleProcessTenderCap", "trigger_date": "2024-07-10", "entry_date": "2024-07-11", "entry_price": 11630.0, "evidence_available_at_that_date": "SECURITIES_FIRM_CONTROL_STAKE_SALE_PROCESS_WITH_CLOSING_RISK_AND_PRICE_CAP", "evidence_source": "source_proxy_manual_verification_required:HANYANG_SECURITIES_CONTROL_STAKE_SALE_PROCESS_BUYER_CLOSING_PRICE_CAP_2024", "stage2_evidence_fields": ["governance_event", "control_premium_or_sale_process_attention"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tender_cap_or_execution_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv", "profile_path": "atlas/symbol_profiles/001/001750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 66.9, "MFE_90D_pct": 66.9, "MFE_180D_pct": 66.9, "MAE_30D_pct": -0.17, "MAE_90D_pct": -0.17, "MAE_180D_pct": -2.84, "peak_date": "2024-08-05", "peak_price": 19410.0, "drawdown_after_peak_pct": -41.78, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_should_fire_after_tender_or_control_peak", "four_b_full_window_peak_proximity": "full_4b_requires_execution_failure_or_non_price_break", "trigger_outcome_label": "positive_with_execution_cap", "current_profile_verdict": "C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C32_001750_2024-07-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF", "trigger_id": "TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"policy_or_regulatory_score": 4, "valuation_repricing_score": 15, "relative_strength_score": 15, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch / governance control premium beta", "raw_component_scores_after": {"policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "relative_strength_score": 8, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 16, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-local-watch after peak / source repair required", "changed_components": ["valuation_repricing_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Governance/control premium should be capped unless tender price, closing path, shareholder approval and execution certainty are verified.", "MFE_90D_pct": 21.25, "MAE_90D_pct": -24.7, "score_return_alignment_label": "large_MFE_with_tender_or_control_peak_then_drawdown", "current_profile_verdict": "C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "trigger_id": "TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "symbol": "036560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"policy_or_regulatory_score": 4, "valuation_repricing_score": 15, "relative_strength_score": 15, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch / governance control premium beta", "raw_component_scores_after": {"policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "relative_strength_score": 8, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 16, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage4B-local-watch after peak / source repair required", "changed_components": ["valuation_repricing_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Governance/control premium should be capped unless tender price, closing path, shareholder approval and execution certainty are verified.", "MFE_90D_pct": 201.31, "MAE_90D_pct": 0.0, "score_return_alignment_label": "large_MFE_with_tender_or_control_peak_then_drawdown", "current_profile_verdict": "C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP", "trigger_id": "TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP", "symbol": "001750", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"policy_or_regulatory_score": 4, "valuation_repricing_score": 15, "relative_strength_score": 15, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch / governance control premium beta", "raw_component_scores_after": {"policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "relative_strength_score": 8, "contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "customer_quality_score": 0, "execution_risk_score": 16, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage4B-local-watch after peak / source repair required", "changed_components": ["valuation_repricing_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Governance/control premium should be capped unless tender price, closing path, shareholder approval and execution certainty are verified.", "MFE_90D_pct": 66.9, "MAE_90D_pct": -0.17, "score_return_alignment_label": "large_MFE_with_tender_or_control_peak_then_drawdown", "current_profile_verdict": "C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 3, "diversity_score_summary": "+3 underused C32 symbols, +3 governance/tender/sale-process families, +2 positive-with-later-4B paths, +1 control-contest false-positive path, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "control_contest_tender_cap_sale_process_vs_execution_and_closing_bridge", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C32 should split control contest, tender battle and sale-process cases by execution bridge. Stage2 requires explicit tender price or closing path; local 4B-watch should fire after the governance peak when tender window closes, shareholder approval fails, buyer certainty weakens, or price falls back toward pre-event range.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["008930", "036560", "001750"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 needs a lifecycle guard. Hanmi Science shows control-contest execution risk; Youngpoong Precision shows tender battle MFE followed by tender-cap fade; Hanyang Securities shows sale-process MFE followed by closing/price-cap fade. All require source repair before runtime promotion."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
008930:
  corporate_action_candidate_dates = 1999-04-19, 2010-07-30, 2010-10-21, 2012-05-14
  selected window = 2024-01-15~D+180
  contamination = false

036560:
  corporate_action_candidate_dates = 2008-04-14
  selected window = 2024-09-13~D+180
  contamination = false

001750:
  corporate_action_candidate_dates = none
  selected window = 2024-07-11~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C32 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C32 lifecycle rule-shape discovery,
but coding-agent promotion requires non-proxy governance/tender/sale-process evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C32 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
control_contest_tender_cap_sale_process_vs_execution_and_closing_bridge

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 008930, 036560 and 001750.
4. Keep generic C32 governance weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - explicit tender price or control-stake sale price is known,
   - buyer/tender/closing path is credible,
   - shareholder or board approval risk is understood,
   - execution/legal risk is not dominant.
6. Consider local 4B-watch when:
   - the event has already reached tender/control premium peak,
   - tender window closes or competing bid uncertainty fades,
   - price falls back toward pre-event range,
   - closing evidence weakens.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C32 overblocks verified tender positives or underflags execution-risk fades.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 72
next_round = R13
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

