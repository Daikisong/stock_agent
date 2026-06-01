# E2R Stock-Web v12 Residual Research — R12 Loop 71 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R12",
  "scheduled_loop": 71,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R12",
  "completed_loop": 71,
  "computed_next_round": "R13",
  "computed_next_loop": 71,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "residual_false_positive_mining"
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

Previous completed state in this interactive run: R11 / loop 71.

Therefore:

```text
scheduled_round = R12
scheduled_loop = 71
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant under-covered service/agri sector
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R13
computed_next_loop = 71
```

R12 was routed to L10 because this is not a live sector scan. It is a governance/control-premium residual check: control-transfer, overhang release, tender cap, shareholder-vote blowoff, and execution/litigation risk.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C32 has meaningful existing coverage, but high-repeat symbols such as Korea Zinc / SM / Korea & Company style cases are intentionally avoided.  
This run adds a different symbol set:

```text
042660 / Hanwha Ocean / KDB overhang sale after Hanwha control transfer
003920 / Namyang Dairy / control stake sale headline with execution/litigation decay
180640 / Hanjin KAL / shareholder-vote control battle blowoff
```

Important data-quality note:

```text
003920 and 180640 are calibration-usable on stock-web OHLC,
but evidence rows are marked source_proxy_only=true / evidence_url_pending=true.
They should be treated as source-repair candidates before any runtime weight change.
```

## Research thesis

C32 governance events are not one animal.

A control event can be a drawbridge lowering, or it can be a crowd chasing smoke.  
The price path only tells us that the crowd moved. The rule needs to know whether the bridge actually touched the ground.

```text
Positive bridge:
confirmed control transfer / overhang release / tender or block sale with separate operating or ownership-structure improvement

Counterexample:
shareholder-vote scarcity / legal execution risk / pure tender cap / no durable operating or cash-flow bridge
```

The residual rule candidate is therefore:

```text
C32 should split governance events into:
1. execution-bridge / overhang-release positives
2. tender-cap or price-only governance blowoff local 4B-watch
```

Because two of three rows need source repair, this file intentionally sets:

```text
do_not_propose_new_weight_delta = true
decision = hold_for_source_repair_and_more_evidence
```

---

## Case 1 — Positive bridge: 042660 / 한화오션 / KDB overhang sale after control transfer

### Evidence

Reuters reported on 2025-04-28 that Korea Development Bank planned to sell shares in Hanwha Ocean through block sales. The same Reuters report states that KDB had become the second-largest shareholder after Hanwha Aerospace acquired a 30.4% stake in the former Daewoo Shipbuilding during the 2022 takeover. This gives the event a governance bridge rather than a pure rumor: control had already transferred, and the KDB stake sale reduced an ownership overhang.

```text
evidence_family = KDB_BLOCK_SALE_OVERHANG_RELEASE_AFTER_HANWHA_CONTROL_TRANSFER
case_role = positive
trigger_date = 2025-04-28
entry_date = 2025-04-29
entry_price = 82,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/042/042660/2025.csv`:

```text
2025-04-29,82400,82400,78000,78500
2025-07-04,76800,76900,72300,73100
2025-10-30,149600,151600,137500,141000
```

### Backtest

```text
MFE_30D  = +5.10%
MAE_30D  = -11.17%
MFE_90D  = +50.12%
MAE_90D  = -12.26%
MFE_180D = +83.98%
MAE_180D = -12.26%
peak_180 = 151,600 on 2025-10-30
trough_180 = 72,300 on 2025-07-04
peak_to_later_drawdown = -31.73%
```

### Interpretation

This is the positive governance pattern.  
The event is not just “someone may buy shares.” It is an overhang-release event after an already completed control transfer, and it rides on an external shipbuilding/defense demand bridge.

C32 should allow Stage2-Actionable only when this extra bridge exists.

---

## Case 2 — Counterexample: 003920 / 남양유업 / control stake sale headline with execution risk

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row is included as a data-quality repair candidate because the stock-web price path is strong and the event family is known, but the non-proxy evidence URL should be verified before coding-agent ingestion.

```text
evidence_family = OWNER_STAKE_SALE_CONTROL_PREMIUM_WITH_EXECUTION_LITIGATION_RISK
case_role = counterexample
trigger_date = 2021-05-27
entry_date = 2021-05-28
entry_price = 570,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv` and `2022.csv`:

```text
2021-05-28,570000,570000,540000,570000
2021-07-01,757000,813000,750000,760000
2022-01-26,380000,385000,371000,374000
```

### Backtest

```text
MFE_30D  = +42.63%
MAE_30D  = -5.26%
MFE_90D  = +42.63%
MAE_90D  = -20.18%
MFE_180D = +42.63%
MAE_180D = -34.91%
peak_180 = 813,000 on 2021-07-01
trough_180 = 371,000 on 2022-01-26
peak_to_later_drawdown = -54.37%
```

### Interpretation

This is the C32 trap: control-premium headlines can create enormous MFE, but if closing/execution/litigation risk is unresolved, the initial premium becomes a cap and then a cliff.

The rule is not “control sale is bullish.”  
The rule is:

```text
control sale + confirmed closing path + no litigation cloud = possible positive bridge
control sale + execution/legal dispute = local 4B-watch / tender-cap decay
```

---

## Case 3 — Counterexample: 180640 / 한진칼 / control battle shareholder-vote blowoff

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row is included because it supplies a clean stock-web control-battle price path, but non-proxy source verification should be completed before scoring profile changes.

```text
evidence_family = CONTROL_BATTLE_SHAREHOLDER_VOTE_PRICE_ONLY_BLOWOFF
case_role = counterexample
trigger_date = 2020-03-27
entry_date = 2020-03-27
entry_price = 45,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv`:

```text
2020-03-27,45000,57200,44850,57200
2020-04-20,109500,111000,77400,81000
2020-12-15,63000,63100,60200,60300
```

### Backtest

```text
MFE_30D  = +146.67%
MAE_30D  = -0.33%
MFE_90D  = +146.67%
MAE_90D  = -0.33%
MFE_180D = +146.67%
MAE_180D = -0.33%
peak_180 = 111,000 on 2020-04-20
trough_180 = 44,850 on 2020-03-27
peak_to_later_drawdown = -45.77%
```

### Interpretation

This is the scarcity-blowoff version of C32.  
The price path is spectacular, but a shareholder-vote control fight is not the same as a cash tender offer or a completed control transfer.

This case argues for a local 4B-watch rule:

```text
if governance-control MFE is extreme
and there is no explicit tender price, no completed ownership transfer, and no operating bridge,
then the signal should be local 4B-watch rather than durable Stage2/Green.
```

---

## Cross-case residual finding

### What repeated global rules already get right

```text
price_only_blowoff_blocks_positive_stage = useful
full_4b_requires_non_price_evidence = useful for full 4B
hard_4c_thesis_break_routes_to_4c = not directly tested here
```

### What remains unresolved

C32 has a special timing problem.

Governance events can create MFE before fundamentals appear. If we wait for a full non-price 4B break, the peak is often already gone. But if we treat every control event as positive, we overfit to tender headlines and shareholder-vote scarcity.

The residual rule candidate is:

```text
C32 local 4B-watch should trigger earlier when:
- MFE_30D is very large,
- event evidence is governance/control related,
- explicit tender price or completed control transfer is absent,
- litigation/execution risk is visible,
- no EPS/order/cash-flow bridge exists.
```

### Candidate canonical compression

Fine labels can compress into:

```text
CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF
```

This fine archetype covers:

```text
1. control-transfer + overhang release + operating bridge → Stage2-Actionable possible
2. control stake sale but closing/litigation risk → tender-cap / local 4B-watch
3. shareholder vote / control scarcity blowoff → price-only local 4B-watch
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R12", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF", "case_id": "R12L71-C32-042660-KDB-OVERHANG-BLOCK-SALE-CONTROL-TRANSFER", "symbol": "042660", "company": "한화오션", "trigger_type": "Stage2-Actionable-GovernanceOverhangRelease", "trigger_date": "2025-04-28", "entry_date": "2025-04-29", "entry_price": 82400.0, "mfe_30_pct": 5.1, "mae_30_pct": -11.17, "mfe_90_pct": 50.12, "mae_90_pct": -12.26, "mfe_180_pct": 83.98, "mae_180_pct": -12.26, "peak_price_180": 151600.0, "peak_date_180": "2025-10-30", "trough_price_180": 72300.0, "trough_date_180": "2025-07-04", "peak_to_later_drawdown_pct": -31.73, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "KDB_BLOCK_SALE_OVERHANG_RELEASE_AFTER_HANWHA_CONTROL_TRANSFER", "evidence_url": "https://www.reuters.com/markets/europe/korea-development-bank-sell-shares-hanwha-ocean-paper-reports-2025-04-28/", "source_proxy_only": false, "evidence_url_pending": false}
{"row_type": "trigger", "round": "R12", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF", "case_id": "R12L71-C32-003920-NAMYANG-HAHNCONTROL-EXECUTION-LITIGATION-CAP", "symbol": "003920", "company": "남양유업", "trigger_type": "Stage4B-GovernanceExecutionRisk", "trigger_date": "2021-05-27", "entry_date": "2021-05-28", "entry_price": 570000.0, "mfe_30_pct": 42.63, "mae_30_pct": -5.26, "mfe_90_pct": 42.63, "mae_90_pct": -20.18, "mfe_180_pct": 42.63, "mae_180_pct": -34.91, "peak_price_180": 813000.0, "peak_date_180": "2021-07-01", "trough_price_180": 371000.0, "trough_date_180": "2022-01-26", "peak_to_later_drawdown_pct": -54.37, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "OWNER_STAKE_SALE_CONTROL_PREMIUM_WITH_EXECUTION_LITIGATION_RISK", "evidence_url": "source_proxy_manual_verification_required:NAMYANG_DAIRY_HAHN_AND_COMPANY_CONTROL_STAKE_SALE_2021", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R12", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF", "case_id": "R12L71-C32-180640-HANJINKAL-CONTROL-BATTLE-BLOWOFF", "symbol": "180640", "company": "한진칼", "trigger_type": "Stage4B-Local-PriceOnly-GovernanceBlowoff", "trigger_date": "2020-03-27", "entry_date": "2020-03-27", "entry_price": 45000.0, "mfe_30_pct": 146.67, "mae_30_pct": -0.33, "mfe_90_pct": 146.67, "mae_90_pct": -0.33, "mfe_180_pct": 146.67, "mae_180_pct": -0.33, "peak_price_180": 111000.0, "peak_date_180": "2020-04-20", "trough_price_180": 44850.0, "trough_date_180": "2020-03-27", "peak_to_later_drawdown_pct": -45.77, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CONTROL_BATTLE_SHAREHOLDER_VOTE_PRICE_ONLY_BLOWOFF", "evidence_url": "source_proxy_manual_verification_required:HANJIN_KAL_2020_CONTROL_BATTLE_SHAREHOLDER_VOTE", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R12L71-C32-042660-KDB-OVERHANG-BLOCK-SALE-CONTROL-TRANSFER", "symbol": "042660", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 12, "bottleneck_pricing_power": 10, "market_mispricing": 15, "valuation_rerating": 14, "capital_allocation": 4, "information_confidence": 4}, "diagnostic_flags": ["governance_event", "control_premium_or_overhang", "execution_bridge_present", "verified_evidence_url"], "expected_current_profile_stage": "Stage2-Actionable", "profile_stress_result": "control transfer / overhang release can become actionable only when ownership overhang is explicitly reduced and operating-defense/shipbuilding thesis already has external demand bridge"}
{"row_type": "score_simulation", "case_id": "R12L71-C32-003920-NAMYANG-HAHNCONTROL-EXECUTION-LITIGATION-CAP", "symbol": "003920", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 6, "bottleneck_pricing_power": 3, "market_mispricing": 15, "valuation_rerating": 12, "capital_allocation": 3, "information_confidence": 2}, "diagnostic_flags": ["governance_event", "control_premium_or_overhang", "execution_bridge_uncertain_or_absent", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "a control-premium headline can produce immediate MFE but should be capped if execution/litigation risk appears; tender/control premium without clean closing is not durable Green"}
{"row_type": "score_simulation", "case_id": "R12L71-C32-180640-HANJINKAL-CONTROL-BATTLE-BLOWOFF", "symbol": "180640", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 6, "bottleneck_pricing_power": 3, "market_mispricing": 15, "valuation_rerating": 12, "capital_allocation": 3, "information_confidence": 2}, "diagnostic_flags": ["governance_event", "control_premium_or_overhang", "execution_bridge_uncertain_or_absent", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "control contest scarcity can generate explosive price MFE, but absent a confirmed tender price or cash-flow bridge it should trigger local 4B-watch rather than a positive control-premium weight"}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 2, "evidence_url_pending_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "+3 new symbols, +3 trigger families, +1 overhang-release positive, +2 governance blowoff/tender-cap counterexamples, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R12", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "control_transfer_overhang_release_vs_tender_cap_price_only_blowoff", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "Do not raise generic C32 governance weight yet. Split C32 into execution-bridge positive and price-only/local-4B guard: overhang-release/control-transfer with external earnings bridge can be Stage2-Actionable, but tender/control headlines with litigation, shareholder-vote scarcity, or no cash-flow bridge should be local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["003920", "180640"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 governance events need a split between confirmed control-transfer/overhang-release bridges and pure control-premium scarcity spikes. The former can act like Stage2-Actionable when a separate operating bridge exists; the latter should be local 4B-watch or tender-cap, especially when litigation/execution risk is visible."}
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
042660:
  corporate_action_candidate_dates = 2016-01-11, 2017-10-30, 2023-06-13, 2023-11-28
  selected window = 2025-04-29~D+180
  contamination = false

003920:
  corporate_action_candidate_dates = 2024-11-20
  selected window = 2021-05-28~D+180
  contamination = false

180640:
  corporate_action_candidate_dates = 2014-11-20
  selected window = 2020-03-27~D+180
  contamination = false
```

Data-quality caveat:

```text
003920 and 180640 source URLs are proxy/pending.
They should be treated as source-repair candidates before any coding agent promotes a runtime rule.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R12/C32 artifact is marked do_not_propose_new_weight_delta=true because two rows need source repair.

Candidate axis:
control_transfer_overhang_release_vs_tender_cap_price_only_blowoff

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 003920 and 180640.
4. Keep generic C32 positive governance weight unchanged until source repair is complete.
5. Consider a scoped local-4B-watch diagnostic:
   if governance/control MFE_30D is extreme
   and explicit tender price / completed control transfer / overhang-release bridge is absent
   and no operating bridge exists
   then label Stage4B-local-watch, not Stage2/Green.
6. Allow Stage2-Actionable only when governance event has:
   completed or high-confidence execution bridge
   plus ownership overhang reduction or tender clarity
   plus separate earnings/cash-flow/operating bridge.
7. Emit before/after diagnostics and reject if C32 false positives increase.
```

---

## Final round state

```text
completed_round = R12
completed_loop = 71
next_round = R13
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

