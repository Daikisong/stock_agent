# E2R Stock-Web v12 Residual Research — R10 Loop 72 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 72,
  "computed_next_round": "R11",
  "computed_next_loop": 72,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": false
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

Previous completed state in this interactive run: R9 / loop 72.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 72
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 72
```

R10 was routed to C30 because R10 is the construction/PF balance-sheet break round.  
This file avoids the existing high-repeat C30 symbols and adds mid/small builder risk paths.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C30 coverage is concentrated in `006360`, `294870`, `375500`, `UNKNOWN_SYMBOL`, and `000720`.  
This run uses:

```text
001470 / 삼부토건 / hard balance-sheet/control-liquidity break
005960 / 동부건설 / PF/local liquidity risk
013580 / 계룡건설 / PF risk with bounded drawdown / no full 4B
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
001470 and 005960 also have share-count changes inside the selected window and need coding-agent validation before promotion.
```

## Research thesis

C30 is not “construction stock fell.”

The mechanism must be evidence-severity based:

```text
PF exposure / housing slowdown / liquidity pressure
→ refinancing or impairment stress
→ covenant, cash, control, auditor, default, or court-rehabilitation evidence
→ hard 4C
```

But there are two softer paths:

```text
local 4B:
  PF/liquidity/orderbook risk plus widening MAE, but no explicit default or control break

RiskWatch / no full 4B:
  PF fear exists, but orderbook/capital buffer keeps drawdown bounded
```

A construction balance sheet is a dam.  
Hairline cracks can justify watch. Water through the wall is local 4B.  
The dam breaking is 4C.

---

## Case 1 — Hard 4C after source repair: 001470 / 삼부토건

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
share_count_change_inside_window = true
```

This row is used as a hard-break price-path guardrail.  
The coding-agent must verify non-proxy balance-sheet/control/liquidity evidence and check the share-count change before promotion.

```text
evidence_family = MID_SMALL_BUILDER_LIQUIDITY_SOLVENCY_CONTROL_BREAK
case_role = hard_4c
trigger_date = 2024-01-04
entry_date = 2024-01-05
entry_price = 2,205
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv`:

```text
2024-01-05,2205,2235,2170,2210
2024-02-16,2545,2780,2500,2735
2024-03-15,2565,2865,2430,2690
2024-08-05,1369,1369,1150,1259
2024-09-09,456,530,440,498
```

### Backtest

```text
MFE_30D  = +26.08%
MAE_30D  = -15.56%
MFE_90D  = +29.93%
MAE_90D  = -31.52%
MFE_180D = +29.93%
MAE_180D = -80.05%
peak_180 = 2,865 on 2024-03-15
trough_180 = 440 on 2024-09-09
peak_to_later_drawdown = -84.64%
```

### Interpretation

This is the hard 4C shape.  
The early MFE is a trap: a short squeeze or rescue hope can appear before the balance-sheet reality overwhelms it.

For C30, a price collapse this large is not enough by itself.  
The rule should require non-price evidence:

```text
default / court rehabilitation / refinancing failure / auditor issue / control break / insolvency signal
```

After that evidence is verified, this becomes a hard 4C exemplar.

---

## Case 2 — Local 4B risk: 005960 / 동부건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
share_count_change_inside_window = true
```

This row tests PF/orderbook/liquidity stress that opens MAE but does not yet reach hard 4C.

```text
evidence_family = PF_EXPOSURE_ORDERBOOK_MARGIN_LIQUIDITY_RISK_WITH_NO_HARD_DEFAULT
case_role = risk_positive
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv`:

```text
2024-02-01,5350,5470,5330,5430
2024-02-19,5400,5500,5360,5430
2024-04-05,4995,5010,4990,4990
2024-08-05,4840,4845,4365,4435
2024-09-09,4200,4400,4175,4330
```

### Backtest

```text
MFE_30D  = +2.80%
MAE_30D  = -6.64%
MFE_90D  = +2.80%
MAE_90D  = -10.84%
MFE_180D = +2.80%
MAE_180D = -21.96%
peak_180 = 5,500 on 2024-02-19
trough_180 = 4,175 on 2024-09-09
peak_to_later_drawdown = -24.09%
```

### Interpretation

This is not hard 4C.  
It is a local 4B / risk-positive row. The stock never produced meaningful MFE and the 180D drawdown widened, but the row still needs explicit non-price deterioration before full 4B or 4C.

The rule should be:

```text
PF/liquidity risk + widening MAE = local 4B-watch
explicit default/refinancing failure/control break = full 4B/4C
```

---

## Case 3 — Overbearish counterexample: 013580 / 계룡건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests the opposite error: turning every construction/PF risk headline into full 4B.

```text
evidence_family = REGIONAL_BUILDER_PF_RISK_WITH_ORDERBOOK_AND_CAPITAL_BUFFER
case_role = overbearish_counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 14,460
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv`:

```text
2024-02-01,14460,14990,14300,14900
2024-02-19,15190,15430,15110,15330
2024-04-15,12930,13040,12800,12830
2024-07-17,14210,15490,14210,15220
2024-08-21,15140,15580,14980,15470
```

### Backtest

```text
MFE_30D  = +6.71%
MAE_30D  = -5.60%
MFE_90D  = +6.71%
MAE_90D  = -11.48%
MFE_180D = +7.75%
MAE_180D = -11.48%
peak_180 = 15,580 on 2024-08-21
trough_180 = 12,800 on 2024-04-15
peak_to_later_drawdown = -12.64%
```

### Interpretation

This is the C30 overbearish guardrail.  
The sector risk existed, but the stock-web path did not confirm a balance-sheet break.

C30 should not punish every builder equally.  
If orderbook, regional public-project mix, capital buffer, or refinancing access keeps MAE bounded, the correct label is:

```text
RiskWatch / no full 4B
```

not hard deterioration.

---

## Cross-case residual finding

### What this strengthens

```text
hard_4c_confirmation = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
```

### What this does not justify

```text
do_not_treat_all_construction_pf_risk_as_4C = true
do_not_call_price_drawdown_hard_4C_without_non_price_break = true
do_not_ignore_share_count_or_recapitalization_when reading collapse paths = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER
```

This fine archetype covers:

```text
1. liquidity/solvency/control break → hard 4C after source repair
2. PF/orderbook/margin stress without explicit default → local 4B-watch
3. PF fear but bounded MAE / orderbook-capital buffer → RiskWatch / no full 4B
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R10", "loop": 72, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER", "case_id": "R10L72-C30-001470-SAMBU-HARD-BALANCE-SHEET-BREAK", "symbol": "001470", "company": "삼부토건", "trigger_type": "Stage4C-HardBalanceSheetBreak", "trigger_date": "2024-01-04", "entry_date": "2024-01-05", "entry_price": 2205.0, "mfe_30_pct": 26.08, "mae_30_pct": -15.56, "mfe_90_pct": 29.93, "mae_90_pct": -31.52, "mfe_180_pct": 29.93, "mae_180_pct": -80.05, "peak_price_180": 2865.0, "peak_date_180": "2024-03-15", "trough_price_180": 440.0, "trough_date_180": "2024-09-09", "peak_to_later_drawdown_pct": -84.64, "case_role": "hard_4c", "calibration_usable": true, "corporate_action_contaminated_180d": false, "share_count_change_inside_window": true, "evidence_family": "MID_SMALL_BUILDER_LIQUIDITY_SOLVENCY_CONTROL_BREAK", "evidence_url": "source_proxy_manual_verification_required:SAMBU_ENGINEERING_2024_CONSTRUCTION_PF_LIQUIDITY_SOLVENCY_CONTROL_BREAK", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R10", "loop": 72, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER", "case_id": "R10L72-C30-005960-DONGBU-CONSTRUCTION-PF-RISK-LOCAL4B", "symbol": "005960", "company": "동부건설", "trigger_type": "Stage4B-Local-PFRisk", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5350.0, "mfe_30_pct": 2.8, "mae_30_pct": -6.64, "mfe_90_pct": 2.8, "mae_90_pct": -10.84, "mfe_180_pct": 2.8, "mae_180_pct": -21.96, "peak_price_180": 5500.0, "peak_date_180": "2024-02-19", "trough_price_180": 4175.0, "trough_date_180": "2024-09-09", "peak_to_later_drawdown_pct": -24.09, "case_role": "risk_positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "share_count_change_inside_window": true, "evidence_family": "PF_EXPOSURE_ORDERBOOK_MARGIN_LIQUIDITY_RISK_WITH_NO_HARD_DEFAULT", "evidence_url": "source_proxy_manual_verification_required:DONGBU_CONSTRUCTION_2024_PF_LIQUIDITY_ORDERBOOK_MARGIN_RISK", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R10", "loop": 72, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER", "case_id": "R10L72-C30-013580-KYERYONG-ORDERBOOK-BUFFER-OVERBEARISH", "symbol": "013580", "company": "계룡건설", "trigger_type": "Stage2-RiskWatch / NoFull4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 14460.0, "mfe_30_pct": 6.71, "mae_30_pct": -5.6, "mfe_90_pct": 6.71, "mae_90_pct": -11.48, "mfe_180_pct": 7.75, "mae_180_pct": -11.48, "peak_price_180": 15580.0, "peak_date_180": "2024-08-21", "trough_price_180": 12800.0, "trough_date_180": "2024-04-15", "peak_to_later_drawdown_pct": -12.64, "case_role": "overbearish_counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "share_count_change_inside_window": false, "evidence_family": "REGIONAL_BUILDER_PF_RISK_WITH_ORDERBOOK_AND_CAPITAL_BUFFER", "evidence_url": "source_proxy_manual_verification_required:KYERYONG_CONSTRUCTION_2024_REGIONAL_BUILDER_PF_ORDERBOOK_CAPITAL_BUFFER", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R10L72-C30-001470-SAMBU-HARD-BALANCE-SHEET-BREAK", "symbol": "001470", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 1, "earnings_visibility": 1, "bottleneck_pricing_power": 1, "market_mispricing": 13, "valuation_rerating": 2, "capital_allocation": 0, "information_confidence": 2}, "diagnostic_flags": ["construction_pf_balance_sheet_break", "hard_4c_balance_sheet_break", "source_proxy_only", "share_count_change_inside_window"], "expected_current_profile_stage": "Stage4C-hard-break after source repair", "profile_stress_result": "C30 hard 4C should require non-price balance-sheet/control/liquidity break evidence, not price alone. The stock-web path shows a hard collapse after a short squeeze-like MFE; it is useful as a hard-break guardrail but should be source-repaired and share-count-checked before runtime promotion."}
{"row_type": "score_simulation", "case_id": "R10L72-C30-005960-DONGBU-CONSTRUCTION-PF-RISK-LOCAL4B", "symbol": "005960", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 5, "bottleneck_pricing_power": 1, "market_mispricing": 13, "valuation_rerating": 5, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["construction_pf_balance_sheet_break", "local_4b_or_riskwatch", "source_proxy_only", "share_count_change_inside_window"], "expected_current_profile_stage": "Stage4B-local-watch", "profile_stress_result": "C30 local 4B should fire when PF/orderbook/margin/liquidity risk opens 180D MAE, but full 4B/4C should wait for non-price deterioration such as covenant stress, refinancing failure, impairment, default, or control break."}
{"row_type": "score_simulation", "case_id": "R10L72-C30-013580-KYERYONG-ORDERBOOK-BUFFER-OVERBEARISH", "symbol": "013580", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 5, "bottleneck_pricing_power": 1, "market_mispricing": 8, "valuation_rerating": 5, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["construction_pf_balance_sheet_break", "local_4b_or_riskwatch", "source_proxy_only", "clean_share_count_window"], "expected_current_profile_stage": "RiskWatch / no full 4B", "profile_stress_result": "C30 should not convert every construction/PF risk headline into full 4B or 4C. When orderbook/capital buffer prevents severe MAE and price path remains bounded, the correct label is RiskWatch or no-full-4B, not balance-sheet break."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 72, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "hard_4c_case_count": 1, "risk_positive_case_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 1, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C30 symbols, +3 PF/BS trigger families, +1 hard 4C path, +1 local-4B risk path, +1 overbearish no-full-4B path, no hard duplicate", "residual_contribution_label": "canonical_archetype_rule_candidate_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 72, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "mid_small_builder_pf_liquidity_break_vs_recapitalization_and_orderbook_buffer", "decision": "candidate_observe_more", "proposed_runtime_effect": "C30 should split hard balance-sheet/control/liquidity break from local PF risk and overbearish construction fear. Hard 4C requires explicit default, court rehabilitation, refinancing failure, auditor/control break, or insolvency evidence. Local 4B can fire on PF/liquidity/orderbook risk with widening MAE. RiskWatch/no-full-4B applies when orderbook or capital buffer limits MAE.", "do_not_propose_new_weight_delta": false, "needs_more_evidence": true, "source_repair_required": ["001470", "005960", "013580"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 72, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 must classify construction/PF risk by evidence severity: 삼부토건-like collapse is hard 4C after balance-sheet/control/liquidity source repair; 동부건설-like widening MAE is local 4B; 계룡건설-like bounded drawdown is RiskWatch/no-full-4B. Price alone is insufficient."}
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
001470:
  corporate_action_candidate_dates = 1996-01-03, 2016-05-13, 2016-12-23, 2017-10-31, 2018-09-18, 2019-05-02
  selected window = 2024-01-05~D+180
  contamination = false by stock-web profile
  share_count_change_inside_window = true → coding-agent validation required

005960:
  corporate_action_candidate_dates = 1997-01-31, 1999-06-16, 2000-02-22, 2012-09-10, 2014-05-16, 2015-09-04, 2016-11-04
  selected window = 2024-02-01~D+180
  contamination = false by stock-web profile
  share_count_change_inside_window = true → coding-agent validation required

013580:
  corporate_action_candidate_dates = 1999-07-16
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
001470 and 005960 also require share-count / recapitalization validation.
This MD is useful for stock-web path calibration and C30 rule-shape discovery,
but coding-agent promotion requires non-proxy balance-sheet/PF evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.

Candidate axis:
mid_small_builder_pf_liquidity_break_vs_recapitalization_and_orderbook_buffer

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 001470, 005960 and 013580.
4. Validate share-count changes for 001470 and 005960 before using them as runtime weight evidence.
5. Keep hard 4C evidence-based:
   - default,
   - court rehabilitation,
   - refinancing failure,
   - auditor/control break,
   - covenant or insolvency signal.
6. Use local 4B-watch when:
   - PF/liquidity/orderbook risk is present,
   - MFE remains small or temporary,
   - MAE_180D <= -20% or post-peak drawdown widens,
   - but hard-break evidence is not confirmed.
7. Keep RiskWatch/no-full-4B when:
   - construction/PF fear exists,
   - but MAE is bounded,
   - orderbook/capital/refinancing buffer is credible.
8. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags hard break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 72
next_round = R11
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

