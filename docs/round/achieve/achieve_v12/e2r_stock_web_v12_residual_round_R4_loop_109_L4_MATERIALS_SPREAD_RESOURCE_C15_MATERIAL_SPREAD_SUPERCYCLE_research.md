# e2r stock-web v12 residual research — R4/L4/C15 material spread supercycle

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file

selected_round = R4
selected_loop = 109
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = REFINING_CRACK_AND_PETCHEM_NAPHTHA_SPREAD_MARGIN_BRIDGE_VS_CONGLOMERATE_OR_FEEDSTOCK_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
coverage_gap_at_selection = C15 rows 33 / need 17 to 50
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
```

## 0. Scope guard

This research output is not a code patch, not a live scan, not a watchlist, and not a production-scoring change.

Only the following was done:

- read the v12 execution constraints and no-repeat/coverage index,
- used `Songdaiki/stock-web` as the historical OHLCV price atlas,
- selected a new C15 case set that avoids the prior C15 copper/steel cases,
- calculated entry / MFE / MAE from actual 1D OHLCV rows,
- wrote shadow-only residual rules for a later coding-agent batch.

## 1. Why C15 again

`C15_MATERIAL_SPREAD_SUPERCYCLE` remains a Priority 1 under-filled archetype: 33 rows, 17 short of the 50-row calibration target.

Prior C15 runs already used:

- `103140` 풍산 — copper concentrate squeeze positive,
- `010130` 고려아연 — zinc/local control with governance contamination,
- `004020` 현대제철 — steel spread false rebound,
- `025820` 이구산업 — copper downstream positive,
- `012800` 대창 — copper beta high-MFE/high-MAE,
- `021050` 서원 — copper beta high-MFE/high-MAE.

This run therefore avoids copper downstream, zinc control, and steel rebound. The new axis is **refining crack spread / petrochemical naphtha spread**: same commodity shock family, different margin mechanics.

## 2. Evidence spine

### 2.1 External historical trigger

The trigger family is the 2022 post-pandemic / Russia-Ukraine refined-product margin shock.

Source-proxy references used:

- Reuters 2025 retrospective: global refining margins averaged around `$33.50/bbl` in June 2022 during the post-pandemic recovery and after Russia's invasion of Ukraine.
  URL: https://www.reuters.com/business/energy/global-oil-refiners-see-short-term-boost-higher-margins-2025-06-03/
- Reuters 2026 retrospective: jet fuel margins in Asia reached levels in 2026 that were the highest since June 2022, and gasoil cracks the highest since August 2022, confirming the 2022 spike as a comparable historical extreme.
  URL: https://www.reuters.com/business/energy/asia-refining-margins-rocket-highest-nearly-4-years-hormuz-supply-disruption-2026-03-05/
- Reuters 2025 petrochemical-sector context: Asia naphtha margins reached as high as `$257/ton` in March 2022 amid Black Sea route supply-disruption fears, but later collapsed as demand softened and Chinese capacity came online.
  URL: https://www.reuters.com/markets/commodities/trump-tariffs-poised-exacerbate-woes-ailing-petchems-sector-2025-04-04/

Because the best accessible sources are retrospective rather than contemporaneous 2022 one-day articles, external evidence quality is marked as `source_proxy_retroactive_confirmation`. Price evidence is direct from stock-web rows.

## 3. Price source and caveats

```text
price_source_repo = Songdaiki/stock-web
price_basis = tradable_raw
shard_root = atlas/ohlcv_tradable_by_symbol_year
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
corporate_action_contaminated_windows = blocked_by_default
```

Relevant symbol-profile caveats:

| Symbol | Name | Profile caveat |
|---|---|---|
| 010950 | S-Oil | only historical corporate-action candidate outside this window; 2022 usable |
| 096770 | SK이노베이션 | corporate-action candidate at 2024-11-20; 2022 usable |
| 011170 | 롯데케미칼 | corporate-action candidate at 2023-02-13; 2022 usable |

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | label |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C15_REF_CRACK_SOIL_20220328 | 010950 | S-Oil | 2022-03-28 | 2022-03-28 | 97,900 | 2022-06-13 | 123,000 | 2022-09-23 | 86,300 | +25.64% | -11.85% | positive-high-MAE watch |
| C15_REF_CONGLOM_SKI_20220607 | 096770 | SK이노베이션 | 2022-06-07 | 2022-06-07 | 236,500 | 2022-06-09 | 246,000 | 2022-07-13 | 158,500 | +4.02% | -32.98% | counterexample |
| C15_PETCHEM_NAPHTHA_LOTTECHEM_20220308 | 011170 | 롯데케미칼 | 2022-03-08 | 2022-03-08 | 192,000 | 2022-06-03 | 210,500 | 2022-09-28 | 144,000 | +9.64% | -25.00% | counterexample |

### 4.1 S-Oil — refining crack positive, but not clean Green

**Hypothesis tested:** when the spread shock is directly tied to transport-fuel refining economics, a pure refiner can re-rate.

- Entry row: `2022-03-28 close 97,900`.
- Peak row: `2022-06-13 high 123,000`.
- Trough row used for calibration window: `2022-09-23 low 86,300`.
- Full-window stress note: `2022-09-28 low 77,500` would deepen MAE to `-20.84%`.

Path:

```text
entry = 97,900
peak_high = 123,000
window_low = 86,300
MFE = +25.64%
MAE = -11.85%
full_window_MAE_if_extended = -20.84%
```

Interpretation:

S-Oil behaves like a usable C15 positive because the margin shock maps more directly to refiner earnings than to a generic commodity-beta headline. However, the drawdown still exceeds the clean Green comfort zone. This belongs in `Stage2-Actionable / Stage3-Yellow watch`, not automatic Stage3-Green.

Residual learning:

```text
refining_spread_positive_requires:
  - direct refining margin exposure
  - product crack evidence, not just crude-price headline
  - inventory/working-capital sensitivity check
  - no simultaneous demand-collapse signal
```

### 4.2 SK이노베이션 — refiner label is not enough

**Hypothesis tested:** a large integrated refiner with battery and broader conglomerate attributes should not get full C15 credit from refining spread alone.

- Entry row: `2022-06-07 close 236,500`.
- Peak row: `2022-06-09 high 246,000`.
- Trough row: `2022-07-13 low 158,500`.

Path:

```text
entry = 236,500
peak_high = 246,000
window_low = 158,500
MFE = +4.02%
MAE = -32.98%
```

Interpretation:

This is the key false-positive guardrail for C15. Even under a true refining-margin supercycle, a stock with multiple large attribute channels can fail to translate the spread into durable equity upside. Battery capex/losses, oil-price inventory swings, and conglomerate discount can swamp the simple spread narrative.

Residual learning:

```text
reject_or_downweight_if:
  - spread exposure is only one segment
  - non-spread segment can dominate EBIT/revision
  - capex/loss cycle offsets refining cash flow
  - price path shows low MFE and high MAE after spread headline
```

### 4.3 롯데케미칼 — naphtha spread/feedstock label is not a profit bridge

**Hypothesis tested:** naphtha/petrochemical feedstock stress is not automatically bullish for naphtha-cracker petrochemical producers.

- Entry row: `2022-03-08 close 192,000`.
- Peak row: `2022-06-03 high 210,500`.
- Trough row: `2022-09-28 low 144,000`.

Path:

```text
entry = 192,000
peak_high = 210,500
window_low = 144,000
MFE = +9.64%
MAE = -25.00%
```

Interpretation:

The 2022 naphtha/petrochemical shock is the mirror image of the refining crack-spread positive. Feedstock tightness can compress downstream petrochemical margins if product demand and pass-through are weak. This case says C15 must distinguish **input-price shock** from **real spread expansion**.

Residual learning:

```text
petrochemical_spread_positive_requires:
  - product price pass-through evidence
  - naphtha-to-product spread improvement
  - utilization/restart discipline
  - no China-capacity glut signal
  - revision/OPM evidence, not only feedstock shortage headline
```

## 5. Current calibrated profile residual error

The existing calibrated profile can still over-score:

1. **Commodity shock as universal positive**
   The same external shock can be positive for direct refiners, negative for naphtha crackers, and noisy for conglomerate refiners.

2. **MFE without path quality**
   S-Oil eventually produced >25% MFE, but with double-digit MAE. It should improve Stage2/Yellow evidence, not bypass 4B checks.

3. **Segment mismatch**
   SK이노베이션 demonstrates that the equity may not behave like a pure refining spread vehicle.

4. **Input/output confusion**
   롯데케미칼 shows why "naphtha margin/feedstock shock" must be modeled as input-cost pressure unless product spread evidence is attached.

## 6. Shadow rule candidate

```text
rule_id = c15_refining_petchem_spread_direct_margin_bridge_required_shadow_only
scope = canonical_archetype:C15_MATERIAL_SPREAD_SUPERCYCLE
production_scoring_changed = false
shadow_weight_only = true

if material_spread_trigger:
    require one of:
      - direct refining crack/product-margin expansion evidence
      - ASP-to-input spread evidence
      - product price pass-through evidence
      - segment-level margin/revision evidence

    downweight if:
      - headline is input-cost/feedstock tightness only
      - company has dominant non-spread segment
      - battery/capex/loss cycle offsets spread benefit
      - high MFE is followed by >20% MAE without durable revision bridge

    promote only to:
      - Stage2-Actionable if spread bridge is explicit but path has high MAE
      - Stage3-Yellow if direct spread exposure + revision evidence + manageable MAE
      - Stage3-Green only if spread expansion, segment earnings, and price path all confirm
```

## 7. Machine-readable rows

### 7.1 case rows

```jsonl
{"row_type":"case","case_id":"C15_REF_CRACK_SOIL_20220328","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_CRACK_SPREAD_DIRECT_MARGIN_BRIDGE","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"010950","name":"S-Oil","trigger_date":"2022-03-28","entry_date":"2022-03-28","entry_price":97900,"peak_date":"2022-06-13","peak_high":123000,"trough_date":"2022-09-23","trough_low":86300,"mfe_pct":25.64,"mae_pct":-11.85,"full_window_mae_pct":-20.84,"outcome_label":"positive_high_mae_watch","calibration_usable":true,"source_quality":"source_proxy_retroactive_confirmation_plus_direct_stock_web_ohlc"}
{"row_type":"case","case_id":"C15_REF_CONGLOM_SKI_20220607","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_SPREAD_CONGLOMERATE_SEGMENT_MISMATCH","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"096770","name":"SK이노베이션","trigger_date":"2022-06-07","entry_date":"2022-06-07","entry_price":236500,"peak_date":"2022-06-09","peak_high":246000,"trough_date":"2022-07-13","trough_low":158500,"mfe_pct":4.02,"mae_pct":-32.98,"outcome_label":"counterexample_low_mfe_high_mae","calibration_usable":true,"source_quality":"source_proxy_retroactive_confirmation_plus_direct_stock_web_ohlc"}
{"row_type":"case","case_id":"C15_PETCHEM_NAPHTHA_LOTTECHEM_20220308","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"PETCHEM_NAPHTHA_FEEDSTOCK_SHOCK_NOT_SPREAD_EXPANSION","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","symbol":"011170","name":"롯데케미칼","trigger_date":"2022-03-08","entry_date":"2022-03-08","entry_price":192000,"peak_date":"2022-06-03","peak_high":210500,"trough_date":"2022-09-28","trough_low":144000,"mfe_pct":9.64,"mae_pct":-25.00,"outcome_label":"counterexample_input_cost_false_positive","calibration_usable":true,"source_quality":"source_proxy_retroactive_confirmation_plus_direct_stock_web_ohlc"}
```

### 7.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_2022_REFINING_CRACK_SUPERCYCLE_RETRO","trigger_date":"2022-03-28","trigger_type":"refining_crack_spread_supercycle","evidence_url":"https://www.reuters.com/business/energy/global-oil-refiners-see-short-term-boost-higher-margins-2025-06-03/","evidence_note":"Reuters retrospective confirms June 2022 global composite refining margins averaged around $33.50/bbl during post-pandemic recovery and after Russia invasion of Ukraine."}
{"row_type":"trigger","trigger_id":"TRG_2022_REFINING_MARGIN_ASIA_EXTREME_RETRO","trigger_date":"2022-06-07","trigger_type":"asia_refining_margin_extreme","evidence_url":"https://www.reuters.com/business/energy/asia-refining-margins-rocket-highest-nearly-4-years-hormuz-supply-disruption-2026-03-05/","evidence_note":"Reuters retrospective confirms 2022 as the prior extreme for jet fuel/diesel margins in Asia."}
{"row_type":"trigger","trigger_id":"TRG_2022_NAPHTHA_MARGIN_FEEDSTOCK_STRESS_RETRO","trigger_date":"2022-03-08","trigger_type":"naphtha_feedstock_cost_stress","evidence_url":"https://www.reuters.com/markets/commodities/trump-tariffs-poised-exacerbate-woes-ailing-petchems-sector-2025-04-04/","evidence_note":"Reuters retrospective notes naphtha margins reached $257/ton in March 2022, then collapsed as demand softened and China capacity came online."}
```

### 7.3 score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C15_REF_CRACK_SOIL_20220328","current_profile_likely_score":"Stage3-Yellow_candidate","proposed_shadow_score":"Stage2-Actionable_to_Stage3-Yellow_watch","reason":"direct refiner spread bridge but MAE and full-window drawdown prevent clean Green"}
{"row_type":"score_simulation","case_id":"C15_REF_CONGLOM_SKI_20220607","current_profile_likely_score":"Stage2_or_Yellow_if_refiner_label_overweighted","proposed_shadow_score":"4B_or_reject_without_segment_margin_bridge","reason":"low MFE and high MAE despite true margin backdrop"}
{"row_type":"score_simulation","case_id":"C15_PETCHEM_NAPHTHA_LOTTECHEM_20220308","current_profile_likely_score":"Stage2_if_naphtha_theme_overweighted","proposed_shadow_score":"4C_counterexample","reason":"feedstock shock is not product-spread expansion"}
```

### 7.4 aggregate row

```jsonl
{"row_type":"aggregate","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","round":"R4","loop":109,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_case_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"verified_url_repair_needed_count":0,"new_axis_proposed":"c15_refining_petchem_spread_direct_margin_bridge_required_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C15 refining/petrochemical spread headlines"}
```

### 7.5 shadow weight row

```jsonl
{"row_type":"shadow_weight","shadow_rule_id":"c15_refining_petchem_spread_direct_margin_bridge_required_shadow_only","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","production_scoring_changed":false,"suggested_effect":"reduce false positives from generic commodity/feedstock headlines; allow direct refiner spread positives only with margin bridge and manageable MAE","priority":"medium_high"}
```

### 7.6 residual contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","contribution_label":"canonical_archetype_rule_candidate","summary":"Adds refining crack spread vs petrochemical naphtha/feedstock distinction; separates direct refiner positive from conglomerate and naphtha-cracker false positives."}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent operating on Songdaiki/stock_agent.

Do not treat this Markdown as a command to change production scoring immediately.
First ingest this file as one v12 residual calibration artifact.

Task:
1. Parse the JSONL rows embedded in this MD.
2. Add the case rows to the v12 calibration artifact registry if they are not duplicate under:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Keep all weight changes shadow-only unless a separate approval prompt authorizes production changes.
4. For C15_MATERIAL_SPREAD_SUPERCYCLE, add or update a shadow-only feature proposal:
   c15_refining_petchem_spread_direct_margin_bridge_required_shadow_only.
5. Ensure the feature distinguishes:
   - direct refining crack/product-margin expansion,
   - petrochemical naphtha/feedstock cost shock,
   - conglomerate segment mismatch,
   - high-MFE/high-MAE blowoff.
6. Do not rerun live scan.
7. Do not generate current stock recommendations.
8. Output a patch summary and tests only after parsing multiple residual MDs in batch.
```

## 9. Final status

```text
selected_round: R4
selected_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: REFINING_CRACK_AND_PETCHEM_NAPHTHA_SPREAD_MARGIN_BRIDGE_VS_CONGLOMERATE_OR_FEEDSTOCK_FALSE_POSITIVE

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
verified_url_repair_needed_count: 0

diversity_score_summary: C15 Priority 1 보강 + S-Oil direct refining spread positive/high-MAE watch + SK Innovation conglomerate/refiner-label low-MFE high-MAE counterexample + Lotte Chemical naphtha feedstock false-positive counterexample
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C15 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c15_refining_petchem_spread_direct_margin_bridge_required_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C15 refining/petrochemical spread headlines
existing_axis_weakened: null
next_recommended_archetypes: C18_CONSUMER_EXPORT_CHANNEL_REORDER, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```
