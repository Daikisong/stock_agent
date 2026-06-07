# E2R Stock-Web V12 Residual Research
## C18_CONSUMER_EXPORT_CHANNEL_REORDER — gim/seafood/K-food export-channel route vs firm-specific reorder bridge

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R5
selected_loop: 112
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: GIM_SEAFOOD_AND_RAMEN_EXPORT_CHANNEL_REORDER_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE
output_format: one_standalone_markdown_file
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
stock_web_price_atlas_access_required: true
```

---

## 1. Execution boundary

This research file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.

This is not a coding task, not a repository patch, not a live scan, and not a current stock recommendation.
The only output is this standalone historical calibration Markdown file.

Allowed:
- read limited `stock_agent` research artifacts for coverage gap and duplicate avoidance;
- read `Songdaiki/stock-web` price atlas rows;
- verify historical trigger/evidence;
- compute entry, MFE, MAE, peak, drawdown from actual 1D OHLCV rows;
- propose shadow-only sector/archetype rules.

Forbidden:
- opening or inferring `stock_agent/src/e2r` code;
- writing a production scoring patch;
- live candidate discovery;
- auto-trading or brokerage integration;
- repeating the same case set with only a loop number change.

---

## 2. Coverage / no-repeat basis

`V12_Research_No_Repeat_Index.md` marks `C18_CONSUMER_EXPORT_CHANNEL_REORDER` as Priority 1 with 33 rows and 17 more rows needed to reach the 50-row practical calibration zone.

Already-used C18 cases avoided in this run:
- Samyang Foods
- Nongshim
- Orion
- Binggrae
- Lotte Wellfood
- Pulmuone
- CJ CheilJedang
- Daesang
- HiteJinro

This run adds a new C18 axis around Korean dried seaweed/gim and seafood/K-food export channel response, plus one ramen-export label boundary case.

---

## 3. Price source and caveats

Price source:
- repository: `Songdaiki/stock-web`
- shard root: `atlas/ohlcv_tradable_by_symbol_year`
- price basis: `tradable_raw`
- upstream source: `FinanceData/marcap`
- adjustment status: raw/unadjusted marcap
- atlas max date: 2026-02-20

Important caveat:
- corporate-action-contaminated windows are blocked by default;
- raw OHLC is not adjusted unless separately handled;
- all MFE/MAE figures below use the actual stock-web row values cited in this run.

---

## 4. External evidence spine

### 4.1 Gim / seaweed export demand

Korean dried seaweed/gim exports reached a record in 2023. The available source-proxy notes that dried seaweed exports in January–October 2023 rose more than 20% YoY to about US$670m, exports went to 124 countries, and the full-year 2023 total was about US$763m. Another source-proxy describes gim as a major Korean food export product with large global share and major markets including the United States, Japan, and China.

Interpretation for C18:
- the category-level export signal is real;
- however, category-level exports do not automatically prove a listed company’s reorder acceleration, sell-through, inventory normalization, or margin bridge;
- company-level channel and sales evidence is required before Stage2-Actionable or Stage3.

### 4.2 Ramen export label boundary

A 2024 report on Korean instant noodles described South Korean noodle exports reaching a record US$1bn in the prior year and highlighted overseas expansion by leading Korean ramen makers. This is useful as a broad K-food export label, but it is not enough to score every ramen-adjacent stock equally.

Interpretation for C18:
- export channel breadth can be a valid top-of-funnel trigger;
- firm-level SKU success, overseas mix, channel sell-through, repeat orders, ASP, and margin revision determine whether the equity path deserves Stage2/Stage3.

---

## 5. Case table

| case_id | symbol | company | trigger_date | entry_date | entry_price | peak_date | peak_high | MFE | MAE low | MAE | classification |
|---|---:|---|---|---|---:|---|---:|---:|---:|---:|---|
| C18_R5L112_001 | 003960 | Sajo Daerim | 2023-12-10 | 2023-12-11 | 31,900 | 2024-07-09 | 109,900 | +244.51% | 30,300 | -5.02% | positive_4B_watch |
| C18_R5L112_002 | 011150 | CJ Seafood | 2023-12-10 | 2023-12-11 | 2,950 | 2024-06-14 | 6,460 | +118.98% | 2,610 | -11.53% | high_MFE_high_MAE_source_repair_watch |
| C18_R5L112_003 | 007310 | Ottogi | 2024-05-27 | 2024-05-28 | 460,500 | 2024-06-13 | 513,000 | +11.40% | 393,500 | -14.55% | export_label_counterexample |

---

## 6. Case details

### 6.1 C18_R5L112_001 — Sajo Daerim / gim-seafood export route positive, but full 4B watch

```json
{
  "case_id": "C18_R5L112_001",
  "symbol": "003960",
  "company": "Sajo Daerim",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "trigger_date": "2023-12-10",
  "entry_date": "2023-12-11",
  "entry_price": 31900,
  "peak_date": "2024-07-09",
  "peak_high": 109900,
  "mfe_pct": 244.51,
  "mae_low": 30300,
  "mae_pct": -5.02,
  "classification": "positive_4B_watch",
  "source_status": "category_export_spine_plus_stock_web_price_rows",
  "source_repair_required": true
}
```

**Mechanism.**
The 2023 gim/seaweed export record made a real C18 top-of-funnel signal: overseas channel demand was not imaginary, and Korean processed seafood/gim names could act like a springboard. Sajo Daerim’s equity path was very strong after the category trigger.

**Why not automatic Green.**
The problem is not the price path. The problem is attribution. A category export record does not prove Sajo Daerim’s exact reorder loop, channel sell-through, product mix, inventory burden, or margin pass-through. The stock can be a valid positive route, but the model should require firm-specific proof before Stage3-Green.

**Score implication.**
- Stage2: yes, if category export strength plus listed-company product exposure is present.
- Stage2-Actionable: only with firm-level overseas order/sales/margin bridge.
- Stage3-Yellow: possible after confirming repeat demand and inventory control.
- Stage3-Green: blocked without firm-level sell-through/reorder/OPM revision evidence.
- 4B watch: yes, because the price route can outrun the fundamental bridge.

---

### 6.2 C18_R5L112_002 — CJ Seafood / high-MFE but high-MAE and weak firm-level bridge

```json
{
  "case_id": "C18_R5L112_002",
  "symbol": "011150",
  "company": "CJ Seafood",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "trigger_date": "2023-12-10",
  "entry_date": "2023-12-11",
  "entry_price": 2950,
  "peak_date": "2024-06-14",
  "peak_high": 6460,
  "mfe_pct": 118.98,
  "mae_low": 2610,
  "mae_pct": -11.53,
  "classification": "high_MFE_high_MAE_source_repair_watch",
  "source_status": "category_export_spine_plus_stock_web_price_rows",
  "source_repair_required": true
}
```

**Mechanism.**
CJ Seafood responded to the seafood/gim/K-food export channel theme with a large upside move. That means the theme is price-relevant and should not be ignored.

**Residual error.**
A high-MFE path with double-digit MAE is not the same as clean reorder compounding. This is the market saying, “there is a story,” while the model still needs to ask, “does this company actually own the repeat-order cash flow?” Without a firm-specific export channel and margin bridge, this case remains a 4B/Stage2 watch rather than Green.

**Score implication.**
- Positive evidence for theme sensitivity.
- Not enough for clean Green.
- Add a penalty when a seafood/K-food export label lacks company-level sell-through or margin evidence.

---

### 6.3 C18_R5L112_003 — Ottogi / ramen export label counterexample

```json
{
  "case_id": "C18_R5L112_003",
  "symbol": "007310",
  "company": "Ottogi",
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "trigger_date": "2024-05-27",
  "entry_date": "2024-05-28",
  "entry_price": 460500,
  "peak_date": "2024-06-13",
  "peak_high": 513000,
  "mfe_pct": 11.40,
  "mae_low": 393500,
  "mae_pct": -14.55,
  "classification": "export_label_counterexample",
  "source_status": "ramen_export_spine_plus_stock_web_price_rows",
  "source_repair_required": false
}
```

**Mechanism.**
Korean ramen exports and global K-food demand were real, but Ottogi’s equity path was much weaker than the category headline would imply. The company is a legitimate ramen/food player, but category export growth did not translate into a clean C18 equity signal in this window.

**Residual error.**
This is the key counterexample: “K-ramen export record” is not enough. The model must distinguish:
- category leader with confirmed overseas SKU acceleration;
- broad domestic food conglomerate with weaker export operating leverage;
- theme label without reorder/margin revision.

**Score implication.**
- Category headline only: Stage1/Stage2 at most.
- Need SKU-level export growth, overseas sales mix, distributor/channel confirmation, and OPM/revision bridge before Stage2-Actionable.
- Without those, keep it as 4B or reject as 4C-prone label.

---

## 7. Residual finding

C18 still has a systematic residual error:

> The model can over-score consumer exporters when it treats category export statistics as if they were company-specific repeat-order economics.

This is like hearing that a whole shopping street is crowded and assuming every store on the street is making money. Foot traffic is real, but cash registers differ by store. C18 needs the register-level evidence: reorder, sell-through, inventory, ASP, margin, and channel quality.

---

## 8. Proposed shadow rule

```json
{
  "shadow_rule_id": "c18_export_category_to_company_reorder_bridge_required_v2",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "status": "proposed_shadow_only",
  "rule": "For C18, category-level export records or global K-food headlines may open Stage2 watch, but Stage2-Actionable or Stage3 requires firm-level evidence of repeat orders, overseas sell-through, channel/distributor quality, inventory normalization, ASP or margin conversion, and preferably earnings revision.",
  "positive_components": [
    "firm_specific_export_sales_growth",
    "named overseas channel or distributor expansion",
    "repeat order / reorder evidence",
    "inventory burden not rising",
    "OPM or gross-margin bridge",
    "earnings revision or management guidance confirmation"
  ],
  "penalty_components": [
    "category export headline only",
    "generic K-food / seafood / ramen label",
    "one-off social media virality without replenishment proof",
    "inventory build or working-capital pressure",
    "low-purity conglomerate exposure",
    "high MFE followed by high MAE without revision confirmation"
  ],
  "stage_effect": {
    "stage2_watch": "allowed on category export + listed exposure",
    "stage2_actionable": "requires at least two firm-level bridge items",
    "stage3_yellow": "requires firm-level reorder/sell-through plus margin or revision bridge",
    "stage3_green": "blocked unless company-level channel and margin conversion are verified"
  }
}
```

---

## 9. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C18_R5L112_001","symbol":"003960","company":"Sajo Daerim","trigger_date":"2023-12-10","entry_date":"2023-12-11","entry_price":31900,"peak_date":"2024-07-09","peak_high":109900,"mfe_pct":244.51,"mae_low":30300,"mae_pct":-5.02,"classification":"positive_4B_watch","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GIM_SEAFOOD_AND_RAMEN_EXPORT_CHANNEL_REORDER_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE"}
{"row_type":"case","case_id":"C18_R5L112_002","symbol":"011150","company":"CJ Seafood","trigger_date":"2023-12-10","entry_date":"2023-12-11","entry_price":2950,"peak_date":"2024-06-14","peak_high":6460,"mfe_pct":118.98,"mae_low":2610,"mae_pct":-11.53,"classification":"high_MFE_high_MAE_source_repair_watch","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GIM_SEAFOOD_AND_RAMEN_EXPORT_CHANNEL_REORDER_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE"}
{"row_type":"case","case_id":"C18_R5L112_003","symbol":"007310","company":"Ottogi","trigger_date":"2024-05-27","entry_date":"2024-05-28","entry_price":460500,"peak_date":"2024-06-13","peak_high":513000,"mfe_pct":11.40,"mae_low":393500,"mae_pct":-14.55,"classification":"export_label_counterexample","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GIM_SEAFOOD_AND_RAMEN_EXPORT_CHANNEL_REORDER_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE"}
{"row_type":"shadow_weight","shadow_rule_id":"c18_export_category_to_company_reorder_bridge_required_v2","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","suggested_effect":"block_stage3_green_without_firm_specific_reorder_sellthrough_margin_bridge","production_scoring_changed":false}
{"row_type":"aggregate","selected_round":"R5","selected_loop":112,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"verified_url_repair_needed_count":2}
```

---

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this section in the current research session.

```text
You are a coding agent working on Songdaiki/stock_agent.

Input research artifact:
- e2r_stock_web_v12_residual_round_R5_loop_112_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Task:
1. Ingest the machine-readable rows only after validating the cited OHLCV rows from Songdaiki/stock-web.
2. Do not treat category export headlines as company-level evidence.
3. Add or strengthen a C18 shadow rule:
   c18_export_category_to_company_reorder_bridge_required_v2
4. Rule intent:
   - category export records open Stage2 watch only;
   - Stage2-Actionable requires firm-level repeat order / sell-through / overseas channel / inventory / margin bridge;
   - Stage3-Green is blocked without company-level evidence.
5. Preserve production_scoring_changed=false unless explicitly instructed in a separate coding session.
```

---

## 11. Final execution metadata

```text
이번 라운드: R5 / Loop 112 / L5_CONSUMER_BRAND_DISTRIBUTION
selected_round: R5
selected_loop: 112
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: GIM_SEAFOOD_AND_RAMEN_EXPORT_CHANNEL_REORDER_BRIDGE_VS_EXPORT_LABEL_HIGH_MAE_FADE

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 2
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
verified_url_repair_needed_count: 2

diversity_score_summary: C18 Priority 1 보강 + Sajo Daerim gim/seafood export-channel positive 4B watch + CJ Seafood high-MFE/high-MAE export-label watch + Ottogi ramen export label counterexample
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C18 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c18_export_category_to_company_reorder_bridge_required_v2
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C18 K-food/gim/seafood/ramen export-label rallies
existing_axis_weakened: null
next_recommended_archetypes: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
