# E2R Stock-Web v12 Residual Research — R11 Loop 71

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R11
completed_loop: 71
next_round: R12
next_loop: 71
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_EAST_SEA_GASFIELD_POLICY_EVENT_CASHFLOW_CONVERSION
output_file: e2r_stock_web_v12_residual_round_R11_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This file follows the v12 historical calibration prompt as the execution procedure and uses `V12_Research_No_Repeat_Index.md` only as the duplicate-avoidance ledger.

This is not a live stock discovery run, not a trading recommendation, and not a `stock_agent` code patch. The only deliverable is a standalone Markdown research file for later batch ingestion.

### Round resolution

The immediately preceding completed file in this automation chain was:

```text
R10 / loop 71 / L9_CONSTRUCTION_REALESTATE_HOUSING / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Therefore the next scheduled round is:

```text
scheduled_round = R11
scheduled_loop  = 71
```

R11 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or, where appropriate, policy-defense/infrastructure-linked L1. This run uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`, which is a valid R11 pairing.

---

## 1. Source and price atlas validation

### Stock-Web manifest

```json
{
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "research_pack_default_price_basis": "tradable_raw"
}
```

Stock-Web manifest notes state that OHLC is raw/unadjusted, zero-volume and zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default.

### Candidate symbol profiles

| symbol | name at event window | profile status | corporate-action contamination in 2024-06-04~D+180 window | calibration usable |
|---|---|---|---|---|
| `036460` | 한국가스공사 | active_like | none listed | true |
| `008970` | 동양철관 / later KBI동양철관 | active_like | none in 2024 window; later name event in 2025 only | true for 30/90/180D |
| `039610` | 화성밸브 | active_like | none in 2024 window | true |

Profile caveat: all three are raw/unadjusted marcap rows. `008970` and `039610` have older corporate-action candidates outside the 2024 window, so 30/90/180D windows are usable for this event. `036460` has no listed corporate-action candidates.

---

## 2. No-repeat and novelty check

`V12_Research_No_Repeat_Index.md` defines the hard duplicate key as:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The current ledger snapshot shows high C31 coverage overall but still useful room for new symbol / trigger-family / failure-mode examples. C31 had 155 rows and 63 symbols in the ledger snapshot, with 38/32 good/bad Stage2 balance and 35 4B cases.

Targeted repository searches for the exact hard-duplicate combinations returned no direct match for this run:

```text
036460 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT + 2024-06-04 -> no direct match found
008970 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT + 2024-06-04 -> no direct match found
039610 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT + 2024-06-04 -> no direct match found
```

Novelty contribution:

```text
new_symbol_count = 3
minimum_new_symbol_count = 2
minimum_counterexample_count = 1
minimum_positive_case_count = 1
minimum_new_independent_case_ratio = 1.00
duplicate_status = pass
```

---

## 3. Evidence event

### Event family

```text
event_family = Korea East Sea offshore oil/gas exploration policy announcement
trigger_date = 2024-06-03
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-06-04
```

### External evidence summary

On 2024-06-03, South Korea announced that it had approved offshore drilling/exploration for potential oil and gas prospects off the east coast near Pohang. Reuters described the resource estimate as up to 14 billion barrels of oil and gas and noted that the government expected drilling to begin later in 2024, with preliminary results in 2025. Reuters also reported the event had an estimated success probability around 20% and per-well drilling costs around KRW 100 billion in follow-up coverage. The Wall Street Journal reported that Korea Gas shares surged as much as 30% on the announcement and that economic viability had not yet been determined.

Interpretation for E2R:

```text
This was a high-signal policy/event shock, but not yet a cash-flow-confirmed rerating.
```

The correct E2R behavior should be:

```text
- permit direct-operator Stage2-Actionable / 4B-watch classification only with bridge language
- block Stage3-Green without drilling confirmation, reserve confirmation, project economics, or cash-flow bridge
- treat indirect supplier rallies as price-only blowoff unless contract/order evidence arrives
```

---

## 4. Case design

This run intentionally uses one direct policy-linked operator and two indirect theme beneficiaries.

| case_id | symbol | role | expected calibration role |
|---|---|---|---|
| `R11L71_C31_036460_20240604` | `036460` 한국가스공사 | direct state-linked gas utility / resource-policy channel | positive-but-guarded Stage2/4B watch |
| `R11L71_C31_008970_20240604` | `008970` 동양철관 | indirect pipe-theme beneficiary | counterexample / price-only blowoff guard |
| `R11L71_C31_039610_20240604` | `039610` 화성밸브 | indirect valve-theme beneficiary | counterexample / local 4B watch |

The point is not to prove again that “price-only blowoff should be blocked.” That is already global policy. The residual tested here is narrower:

```text
For C31 policy/subsidy/legislation events, the scoring model should distinguish:
1. direct project/entity linkage, where Stage2 watch can be allowed but Green blocked; and
2. indirect theme linkage, where even very large MFE should not become Stage2/Green unless order/capex/cash-flow bridge appears.
```

---

## 5. Stock-Web OHLC excerpts and trigger rows

### 5.1 `036460` 한국가스공사

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,29800.0,38700.0,29700.0,38700.0,13412864.0,498113399650.0,3572513100000.0,92313000,KOSPI
2024-06-04,40800.0,49350.0,38750.0,39400.0,33946477.0,1494925644300.0,3637132200000.0,92313000,KOSPI
2024-06-05,39000.0,44650.0,37350.0,43700.0,23475149.0,968111636450.0,4034078100000.0,92313000,KOSPI
2024-06-20,59200.0,64500.0,56500.0,63500.0,12497795.0,748090305700.0,5861875500000.0,92313000,KOSPI
2024-08-05,40350.0,40950.0,36500.0,37950.0,2254302.0,87875721600.0,3503278350000.0,92313000,KOSPI
2024-09-03,51700.0,53800.0,51400.0,53300.0,3230801.0,170852829300.0,4920282900000.0,92313000,KOSPI
2024-12-02,42950.0,43500.0,39800.0,40050.0,2511076.0,102755779250.0,3697135650000.0,92313000,KOSPI
```

Backtest convention:

```text
entry_date = 2024-06-04
entry_price = 40800.0
entry_price_type = next_tradable_open
```

MFE/MAE:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 64500 | 2024-06-20 | 37350 | 2024-06-05 | +58.09% | -8.46% |
| 90D | 64500 | 2024-06-20 | 36500 | 2024-08-05 | +58.09% | -10.54% |
| 180D | 64500 | 2024-06-20 | 36500 | 2024-08-05 | +58.09% | -10.54% |

Interpretation:

```text
036460 is a real policy-linked operator/channel case, not a pure ticker-theme echo.
However, the price peak came before reserve confirmation or cash-flow confirmation.
Thus the proper E2R state is Stage2-Actionable / local 4B watch, not Stage3-Green.
```

### 5.2 `008970` 동양철관

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,697.0,904.0,697.0,904.0,8309103.0,7280138824.0,107472302160.0,118885290,KOSPI
2024-06-04,1175.0,1175.0,1175.0,1175.0,7102951.0,8345967154.0,139690215750.0,118885290,KOSPI
2024-06-05,1414.0,1527.0,1351.0,1527.0,146881334.0,214380321675.0,181537837830.0,118885290,KOSPI
2024-06-07,1610.0,1678.0,1285.0,1411.0,142968215.0,211189736927.0,167747144190.0,118885290,KOSPI
2024-07-12,950.0,954.0,921.0,926.0,2546178.0,2372502019.0,133016078398.0,143645873,KOSPI
2024-08-05,985.0,987.0,826.0,890.0,6103922.0,5607437467.0,129945030280.0,146005652,KOSPI
```

Backtest convention:

```text
entry_date = 2024-06-04
entry_price = 1175.0
entry_price_type = next_tradable_open
```

MFE/MAE:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 1678 | 2024-06-07 | 921 | 2024-07-12 | +42.81% | -21.62% |
| 90D | 1678 | 2024-06-07 | 826 | 2024-08-05 | +42.81% | -29.70% |
| 180D | 1678 | 2024-06-07 | 826 | 2024-08-05 | +42.81% | -29.70% |

Interpretation:

```text
This is a textbook C31 indirect-theme blowoff. 
MFE was large, but the path had rapid drawdown and no confirmed policy-to-order bridge in the trigger window.
```

### 5.3 `039610` 화성밸브

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,5150.0,6640.0,5140.0,6640.0,3557446.0,22292106990.0,69125056000.0,10410400,KOSDAQ
2024-06-04,8630.0,8630.0,8310.0,8630.0,3942431.0,33930835030.0,89841752000.0,10410400,KOSDAQ
2024-06-05,8330.0,11080.0,7800.0,9870.0,50911410.0,487972385270.0,102750648000.0,10410400,KOSDAQ
2024-07-02,7220.0,7380.0,6820.0,7020.0,471396.0,3320461860.0,73081008000.0,10410400,KOSDAQ
2024-07-18,7600.0,9540.0,7240.0,9180.0,19473141.0,174372050900.0,95567472000.0,10410400,KOSDAQ
2024-07-29,11250.0,12470.0,10830.0,11950.0,13762616.0,164118955540.0,124404280000.0,10410400,KOSDAQ
2024-08-20,12200.0,13470.0,11640.0,11790.0,13989254.0,179128302580.0,122738616000.0,10410400,KOSDAQ
```

Backtest convention:

```text
entry_date = 2024-06-04
entry_price = 8630.0
entry_price_type = next_tradable_open
```

MFE/MAE:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 11080 | 2024-06-05 | 6820 | 2024-07-02 | +28.39% | -20.97% |
| 90D | 13470 | 2024-08-20 | 6820 | 2024-07-02 | +56.08% | -20.97% |
| 180D | 13470 | 2024-08-20 | 6820 | 2024-07-02 | +56.08% | -20.97% |

Interpretation:

```text
039610 had a second 4B-like momentum wave after the initial policy shock.
But without a confirmed order/backlog/cash-flow bridge tied to the East Sea drilling project, the proper label is not Stage3-Green.
It is a local 4B watch / indirect-theme residual counterexample.
```

---

## 6. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R11L71_C31_POLICY_EVENT_GASFIELD","round":"R11","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_EAST_SEA_GASFIELD_POLICY_EVENT_CASHFLOW_CONVERSION","symbol":"036460","name":"한국가스공사","trigger_type":"Stage2-Actionable","trigger_family":"policy_resource_exploration_approval_direct_operator","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":40800.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":58.09,"mae_30d_pct":-8.46,"mfe_90d_pct":58.09,"mae_90d_pct":-10.54,"mfe_180d_pct":58.09,"mae_180d_pct":-10.54,"peak_price_180d":64500.0,"peak_date_180d":"2024-06-20","trough_price_180d":36500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"guarded_positive","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"medium","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_or_4B_watch","residual_error_type":"green_should_be_blocked_until_reserve_or_cashflow_confirmation"}
{"row_type":"trigger","research_id":"R11L71_C31_POLICY_EVENT_GASFIELD","round":"R11","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_EAST_SEA_GASFIELD_POLICY_EVENT_CASHFLOW_CONVERSION","symbol":"008970","name":"동양철관","trigger_type":"4B-local-watch","trigger_family":"policy_resource_exploration_indirect_pipe_theme","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":1175.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":42.81,"mae_30d_pct":-21.62,"mfe_90d_pct":42.81,"mae_90d_pct":-29.70,"mfe_180d_pct":42.81,"mae_180d_pct":-29.70,"peak_price_180d":1678.0,"peak_date_180d":"2024-06-07","trough_price_180d":826.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"low","price_only_blowoff":true,"expected_stage_current_profile":"4B-local-watch_or_blocked_positive_stage","residual_error_type":"indirect_theme_large_mfe_should_not_create_stage2_green"}
{"row_type":"trigger","research_id":"R11L71_C31_POLICY_EVENT_GASFIELD","round":"R11","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_EAST_SEA_GASFIELD_POLICY_EVENT_CASHFLOW_CONVERSION","symbol":"039610","name":"화성밸브","trigger_type":"4B-local-watch","trigger_family":"policy_resource_exploration_indirect_valve_theme","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":8630.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":28.39,"mae_30d_pct":-20.97,"mfe_90d_pct":56.08,"mae_90d_pct":-20.97,"mfe_180d_pct":56.08,"mae_180d_pct":-20.97,"peak_price_180d":13470.0,"peak_date_180d":"2024-08-20","trough_price_180d":6820.0,"trough_date_180d":"2024-07-02","calibration_usable":true,"case_polarity":"counterexample","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"low","price_only_blowoff":true,"expected_stage_current_profile":"4B-local-watch_or_blocked_positive_stage","residual_error_type":"second_wave_theme_momentum_still_needs_contract_bridge"}
```

---

## 7. Score simulation and raw component breakdown

The following score simulation is a shadow stress test only. It does not change production scoring.

### Component scale

```text
components:
- eps_fcf_explosion
- earnings_visibility
- bottleneck_pricing
- market_mispricing
- valuation_rerating
- capital_allocation
- information_confidence
```

### Simulated current calibrated profile behavior

| symbol | EPS/FCF | visibility | bottleneck/pricing | mispricing | valuation | cap allocation | info confidence | total shadow | expected current-stage behavior |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `036460` | 7 | 11 | 12 | 10 | 8 | 4 | 14 | 66 | Stage2-Actionable only if direct-policy bridge is recognized; Green blocked |
| `008970` | 1 | 2 | 5 | 6 | 2 | 1 | 5 | 22 | blocked positive stage; local 4B watch only |
| `039610` | 1 | 2 | 5 | 7 | 2 | 1 | 5 | 23 | blocked positive stage; local 4B watch only |

### Residual stress result

The current global rules already block price-only positive stages. The remaining C31-specific residual is subtler:

```text
Direct policy-linked project operator should receive limited Stage2-Actionable credit,
but indirect suppliers should require a named contract/order/backlog/capex bridge before receiving any Stage2 bonus.
```

Without this distinction, C31 creates two errors at once:

```text
false_negative_risk:
  direct policy-linked operator ignored even when state project channel is clear

false_positive_risk:
  indirect theme stocks promoted because MFE was large despite no cash-flow bridge
```

The target rule should be a routing rule, not a broad score boost.

---

## 8. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R11L71_C31_POLICY_EVENT_GASFIELD",
  "round": "R11",
  "loop": 71,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "KOREA_EAST_SEA_GASFIELD_POLICY_EVENT_CASHFLOW_CONVERSION",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "guarded_positive_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "price_only_blowoff_count": 2,
  "direct_policy_bridge_count": 1,
  "indirect_theme_no_bridge_count": 2,
  "avg_mfe_90d_pct": 52.33,
  "avg_mae_90d_pct": -20.40,
  "max_mfe_90d_pct": 58.09,
  "worst_mae_90d_pct": -29.70
}
```

---

## 9. Shadow rule candidate

### Proposed rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_EAST_SEA_GASFIELD_POLICY_EVENT_CASHFLOW_CONVERSION
rule_name: C31_policy_event_bridge_tier_router
production_scoring_changed: false
shadow_weight_only: true
```

### Rule logic

```text
For C31 policy/subsidy/legislation events:

Tier A: direct policy/project entity
  Conditions:
    - named government approval / budget / drilling / subsidy / legislation event
    - symbol has direct state-owned, concession, operator, asset-owner, or explicit project role
    - project economics still uncertain
  Routing:
    - allow Stage2-Actionable bridge bonus
    - block Stage3-Green until reserve confirmation, order/backlog, margin bridge, or cash-flow confirmation
    - allow local 4B watch if price peak arrives before non-price confirmation

Tier B: indirect supplier/theme beneficiary
  Conditions:
    - price reacts to policy event
    - no named order, contract, tender, backlog, subsidy award, or capex conversion evidence
  Routing:
    - no Stage2 bonus
    - no Stage3-Green
    - classify as price-only blowoff / local 4B watch
    - keep as counterexample if MFE is large but MAE or reversal is severe
```

### Suggested weight delta

```json
{
  "row_type": "shadow_weight",
  "axis": "stage2_required_bridge",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "direct_policy_entity_stage2_bridge_bonus": 1.0,
    "indirect_theme_no_contract_stage2_bonus_cap": 0.0,
    "indirect_theme_no_contract_green_allowed": false,
    "policy_event_local_4b_watch_guard": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "One direct operator and two indirect supplier/theme cases show high MFE but different evidence quality. The rule should route by policy-to-cashflow bridge tier rather than by event magnitude."
}
```

---

## 10. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R11L71_C31_POLICY_EVENT_GASFIELD",
  "residual_type": "policy_event_bridge_tiering",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds a C31-specific distinction between direct policy-linked project entities and indirect event-theme suppliers. This prevents large-MFE indirect-theme cases from contaminating Stage2/Green calibration while preserving limited Stage2-Actionable credit for directly exposed project entities.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "guardrail_added": "Indirect policy-event beneficiaries require named contract/order/backlog/subsidy-award bridge before Stage2 bonus.",
  "4b_split": {
    "local_4b_watch": ["008970", "039610"],
    "full_4b_requires_non_price_evidence": ["036460 if project economics/reserve confirmation fails to arrive after price peak"]
  }
}
```

---

## 11. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  price_basis: tradable_raw
  price_adjustment_status: raw_unadjusted_marcap
  manifest_max_date: 2026-02-20
  forward_window_required: 180D
  forward_window_available: true
  raw_shard_used_for_weight_calibration: false
  corporate_action_contaminated_180D_window:
    036460: false
    008970: false
    039610: false
  evidence_url_pending:
    036460: false
    008970: false
    039610: false
  source_proxy_only:
    036460: false
    008970: false
    039610: false
```

Limitations:

```text
- This run uses public event evidence plus Stock-Web price rows.
- It does not verify later drilling results or later company-level contract conversion.
- It should not be used as investment advice.
- It should not trigger production profile changes by itself.
```

---

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact. Do not treat it as production-ready by itself.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve the R11/loop 71 metadata.
3. Add the cases to the C31_POLICY_SUBSIDY_LEGISLATION_EVENT evidence corpus if they pass parser validation.
4. Add or update a shadow-only rule candidate named C31_policy_event_bridge_tier_router.
5. Do not loosen Stage3-Green.
6. Do not allow price-only indirect policy-event beneficiaries to receive Stage2/Green promotion without named non-price bridge evidence.
7. If enough future C31 artifacts confirm the same pattern, consider a canonical-archetype-scoped bridge-tier router:
   - direct policy/project entity: allow limited Stage2-Actionable bridge credit
   - indirect theme beneficiary: require contract/order/backlog/subsidy-award evidence
8. Keep production scoring unchanged unless batch promotion logic independently marks this axis as safe.
```

---

## 13. Next round state

```text
completed_round = R11
completed_loop = 71
next_round = R12
next_loop = 71
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri sector
```
