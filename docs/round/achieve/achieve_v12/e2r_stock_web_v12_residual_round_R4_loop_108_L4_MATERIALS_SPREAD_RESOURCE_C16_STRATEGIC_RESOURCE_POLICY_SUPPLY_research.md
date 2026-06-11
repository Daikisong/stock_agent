# stock-web v12 residual research — R4 / Loop 108 / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R4
selected_loop = 108
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = CRITICAL_MINERAL_GRAPHITE_CATHODE_ANODE_SUPPLY_CHAIN_OFFTAKE_VS_EV_DEMAND_AND_RESOURCE_LABEL_FADE
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution boundary

This file is a standalone historical calibration / sector-archetype residual research artifact. It does **not** patch `stock_agent`, does **not** run live discovery, and does **not** change production scoring.

The only repository used as a price source is:

```text
price_repo = Songdaiki/stock-web
price_basis = tradable_raw
ohlcv_root = atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status = raw_unadjusted_marcap
```

The only `stock_agent` artifact consulted is the No-Repeat / coverage index, for duplicate avoidance and coverage-gap selection.

---

## 2. Why this archetype was selected

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` remains a Priority 1 underfilled archetype in the No-Repeat Index:

```text
C16 rows = 30
need_to_50 = 20
research_focus = 전략자원 정책과 실제 offtake/margin/공급망 실행
```

Prior C16 runs already used:

```text
005490 POSCO홀딩스
006260 LS
001570 금양
047050 포스코인터내셔널
365340 성일하이텍
005420 코스모화학
011810 STX blocked comparator
```

This run therefore avoids that set and focuses on a new C16 slice:

```text
003670 포스코퓨처엠
051910 LG화학
078600 대주전자재료
```

The question being calibrated is not “does the company have a battery-material / critical-mineral label?”
The calibration question is narrower:

> Did the event create a company-specific raw-material / offtake / processing / margin bridge, or was it merely a resource-policy label riding a sector tape?

---

## 3. External evidence spine

### 3.1 POSCO Future M / Syrah graphite offtake

Reuters reported that Syrah Resources agreed to supply natural graphite from Balama, Mozambique, to POSCO Future M under a six-year deal. The supply starts at up to 2 kt per month after commissioning and can rise to 5 kt per month from the second year, with quarterly price negotiation.

```text
external_trigger_url = https://www.reuters.com/markets/commodities/australias-syrah-resources-inks-offtake-deal-with-s-koreas-posco-future-m-2024-02-29/
event_date_utc = 2024-02-29
korea_next_trading_entry = 2024-03-04
```

This is a real offtake bridge, but the price path tests whether “offtake exists” is enough when the broader EV/battery-material cycle is weakening.

### 3.2 LG Chem / GM cathode-material supply deal

GM announced a long-dated LG Chem cathode-material supply agreement, reported as an $18.8bn / 25tn won deal covering more than 500,000 tons of cathode materials from 2026 to 2035.

```text
external_trigger_url = https://www.investopedia.com/gm-strikes-deal-with-lg-chem-securing-enough-materials-to-produce-5-million-evs-8563811
event_date = 2024-02-07
korea_entry_date = 2024-02-08
```

This is contract-scale positive evidence. The stress test is whether a large parent chemical stock rerates durably when the downstream battery cycle remains under pressure.

### 3.3 China graphite export controls / anode substitution label

China’s October 2023 graphite export controls created a strategic-resource policy shock around graphite and anode supply. This can help true anode substitution stories, but it can also create a resource-label rally without firm-specific offtake or margin evidence.

```text
external_trigger_url = https://www.investopedia.com/china-restricts-exports-of-graphite-a-key-mineral-used-for-making-ev-batteries-8364318
event_date = 2023-10-20
korea_entry_date = 2023-10-20
```

For `078600 대주전자재료`, the company-specific source is treated as **source_proxy_only_url_repair_required** in this run. The price path is still useful for C16 as an anode-material / graphite-substitution label stress case.

---

## 4. Price path calculations

### Calculation convention

```text
entry_price = close on trigger trading date or next Korea trading date if event landed after local close/holiday
MFE = (forward_high - entry_price) / entry_price
MAE = (forward_low - entry_price) / entry_price
window = trigger to 2024 year-end unless otherwise noted
```

### 4.1 003670 포스코퓨처엠 — graphite offtake did not offset EV-cycle pressure

```text
case_id = C16_003670_2024-03-04_GRAPHITE_OFFTAKE_SYRAH_POSCO_FUTURE_M
symbol = 003670
company = 포스코퓨처엠
trigger_type = graphite_offtake_supply_contract
external_trigger_date = 2024-02-29 UTC
entry_date = 2024-03-04
entry_price = 334500
forward_peak_date = 2024-03-13
forward_peak_price = 341000
forward_low_date = 2024-12-27
forward_low_price = 139500

MFE = +1.94%
MAE = -58.30%
classification = counterexample
```

Interpretation:

The event had real C16 content because it was an actual graphite offtake arrangement, not just a press headline. However, the stock path says that **raw-material offtake alone was not enough** when cathode/anode demand revision, EV inventory, and material-price pressure dominated the equity tape.

This is a useful residual case because a naive rule could over-score “graphite offtake” as Stage2-Actionable. The v12 profile should instead require:

```text
offtake + customer demand pull + margin visibility + inventory/ASP stabilization
```

before allowing Stage2-Actionable / Stage3 escalation.

---

### 4.2 051910 LG화학 — very large GM cathode contract, but parent-stock rerating failed

```text
case_id = C16_051910_2024-02-08_GM_LG_CHEM_CATHODE_SUPPLY_PARENT_STOCK_FADE
symbol = 051910
company = LG화학
trigger_type = cathode_material_supply_contract
external_trigger_date = 2024-02-07
entry_date = 2024-02-08
entry_price = 470500
forward_peak_date = 2024-02-19
forward_peak_price = 520000
forward_low_date = 2024-12-27
forward_low_price = 242000

MFE = +10.52%
MAE = -48.57%
classification = counterexample
```

Interpretation:

The contract was large and long-duration, but the stock did not become a durable C16 winner. This case is not “contract news does not matter.” The sharper conclusion is:

```text
large downstream cathode contract is insufficient when
- parent-company earnings are exposed to broader chemical/battery spread pressure
- cash conversion starts far in the future
- sector-wide EV demand revision overwhelms the single contract
```

For C16, this becomes a parent-conglomerate / future-dated contract haircut rule.

---

### 4.3 078600 대주전자재료 — graphite-control / silicon-anode label produced a local positive path, but source repair is required

```text
case_id = C16_078600_2023-10-20_CHINA_GRAPHITE_CONTROL_SILICON_ANODE_LABEL
symbol = 078600
company = 대주전자재료
trigger_type = graphite_export_control_anode_substitution_label
external_trigger_date = 2023-10-20
entry_date = 2023-10-20
entry_price = 74500
forward_peak_date = 2023-12-18
forward_peak_price = 93300
forward_low_date = 2023-11-01
forward_low_price = 67500

MFE = +25.23%
MAE = -9.40%
classification = positive_with_source_repair_required
```

Interpretation:

This case shows that a graphite-control shock can create a local positive path for anode-substitution labels. However, the present run does **not** verify a firm-specific supply contract, customer offtake, or margin bridge for `078600`; therefore this is not a clean Green case. It is best used as:

```text
Stage2 watch / source-repair-required positive
not Stage3-Green evidence
```

The important distinction is the same mechanical distinction seen in earlier C16 runs:

```text
resource policy label = optional narrative
resource policy + company-specific offtake/processing/margin bridge = usable calibration evidence
```

---

## 5. Cross-case findings

### 5.1 C16 false-positive pattern strengthened

Two cases show that a contract/offtake headline can still fail:

```text
003670: real graphite offtake, but MFE only +1.94%, MAE -58.30%
051910: large GM cathode contract, but MFE +10.52%, MAE -48.57%
```

The cause is not that the events were fake. The cause is that the **equity bridge was incomplete**. In C16, a supply contract becomes investable only when it turns into a visible path through:

```text
feedstock security
processing ramp
customer demand pull
ASP / spread stabilization
margin conversion
working-capital discipline
revision support
```

Without that, the event becomes a bridge drawn on fog: it looks like a road, but the tires never find asphalt.

### 5.2 C16 false-negative / watchlist pattern

`078600` shows that policy shocks around strategic materials can create a tradable local path, but without direct source repair the signal cannot become production weight evidence. It should remain a watchlist / Stage2 candidate until firm-specific evidence is repaired.

### 5.3 Shadow rule candidate

```text
C16_SHADOW_RULE_2026_06_06:
For strategic-resource / critical-mineral events, do not promote to Stage2-Actionable solely from
policy restriction, offtake headline, or contract-size headline.

Require at least two of:
1. company-specific offtake or supply contract with named counterparties,
2. processing/refining/ramp schedule,
3. ASP/spread or cost-pass-through visibility,
4. customer demand pull or volume commitment,
5. margin/revision bridge within a measurable window,
6. low-MAE confirmation in the first 20-40 trading days.

If contract is future-dated or parent-company exposure is diluted, apply parent-conglomerate / time-to-cash haircut.
```

---

## 6. Stage interpretation

| case | Stage2? | Stage2-Actionable? | Stage3-Yellow? | Stage3-Green? | 4B/4C |
|---|---:|---:|---:|---:|---|
| 003670 POSCO Future M / Syrah graphite | yes | no | no | no | 4C after failed bridge |
| 051910 LG Chem / GM cathode | yes | no | no | no | 4C parent/future-dated contract fade |
| 078600 Daejoo / graphite-control anode label | yes | watch only | no | no | 4B watch until source repair |

---

## 7. Machine-readable rows

### 7.1 case rows

```jsonl
{"row_type":"case","round":"R4","loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"CRITICAL_MINERAL_GRAPHITE_CATHODE_ANODE_SUPPLY_CHAIN_OFFTAKE_VS_EV_DEMAND_AND_RESOURCE_LABEL_FADE","symbol":"003670","company":"포스코퓨처엠","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":334500,"peak_date":"2024-03-13","peak_price":341000,"low_date":"2024-12-27","low_price":139500,"mfe_pct":1.94,"mae_pct":-58.30,"classification":"counterexample","calibration_usable":true,"source_quality":"verified_external_event_plus_stock_web_price","notes":"Real graphite offtake but no durable equity bridge; EV demand/material spread pressure dominated."}
{"row_type":"case","round":"R4","loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"CRITICAL_MINERAL_GRAPHITE_CATHODE_ANODE_SUPPLY_CHAIN_OFFTAKE_VS_EV_DEMAND_AND_RESOURCE_LABEL_FADE","symbol":"051910","company":"LG화학","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":470500,"peak_date":"2024-02-19","peak_price":520000,"low_date":"2024-12-27","low_price":242000,"mfe_pct":10.52,"mae_pct":-48.57,"classification":"counterexample","calibration_usable":true,"source_quality":"verified_external_event_plus_stock_web_price","notes":"Large GM cathode contract but future-dated and parent-company exposure diluted by EV/material cycle."}
{"row_type":"case","round":"R4","loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"CRITICAL_MINERAL_GRAPHITE_CATHODE_ANODE_SUPPLY_CHAIN_OFFTAKE_VS_EV_DEMAND_AND_RESOURCE_LABEL_FADE","symbol":"078600","company":"대주전자재료","trigger_date":"2023-10-20","entry_date":"2023-10-20","entry_price":74500,"peak_date":"2023-12-18","peak_price":93300,"low_date":"2023-11-01","low_price":67500,"mfe_pct":25.23,"mae_pct":-9.40,"classification":"positive_with_source_repair_required","calibration_usable":true,"source_quality":"policy_event_verified_company_specific_url_repair_required","notes":"Graphite-control/anode substitution label worked locally, but company-specific offtake/margin bridge needs URL repair before production weight."}
```

### 7.2 trigger rows

```jsonl
{"row_type":"trigger","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"003670","trigger_type":"graphite_offtake_supply_contract","trigger_date":"2024-02-29","entry_date":"2024-03-04","evidence_url":"https://www.reuters.com/markets/commodities/australias-syrah-resources-inks-offtake-deal-with-s-koreas-posco-future-m-2024-02-29/","direct_company_bridge":true,"needs_url_repair":false}
{"row_type":"trigger","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"051910","trigger_type":"large_cathode_material_supply_contract","trigger_date":"2024-02-07","entry_date":"2024-02-08","evidence_url":"https://www.investopedia.com/gm-strikes-deal-with-lg-chem-securing-enough-materials-to-produce-5-million-evs-8563811","direct_company_bridge":true,"needs_url_repair":false}
{"row_type":"trigger","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"078600","trigger_type":"graphite_export_control_anode_substitution_policy","trigger_date":"2023-10-20","entry_date":"2023-10-20","evidence_url":"https://www.investopedia.com/china-restricts-exports-of-graphite-a-key-mineral-used-for-making-ev-batteries-8364318","direct_company_bridge":false,"needs_url_repair":true}
```

### 7.3 score simulation rows

```jsonl
{"row_type":"score_simulation","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"003670","old_profile_likely_score":"Stage2-Actionable possible due to real offtake","proposed_shadow_score":"Stage2 only / 4C watch","reason":"MFE below +2% and full-window MAE below -50% despite real offtake."}
{"row_type":"score_simulation","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"051910","old_profile_likely_score":"Stage2-Actionable possible due to large contract size","proposed_shadow_score":"Stage2 only / parent-conglomerate haircut / 4C watch","reason":"Future-dated contract and broad parent exposure failed durable rerating."}
{"row_type":"score_simulation","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"078600","old_profile_likely_score":"May reject as policy-only label","proposed_shadow_score":"Stage2 watch only until source repair","reason":"Local MFE +25.23% with MAE under -10%, but company-specific offtake/margin bridge not verified."}
```

### 7.4 aggregate row

```jsonl
{"row_type":"aggregate","round":"R4","loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":3,"positive_case_count":1,"counterexample_count":2,"calibration_usable_case_count":3,"current_profile_error_count":3,"verified_url_repair_needed_count":1,"residual_contribution":"Strengthens C16 bridge requirement: critical-mineral events need offtake + processing/ramp + margin/revision evidence; policy/resource labels alone remain 4B/4C-prone."}
```

### 7.5 shadow weight row

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","proposed_axis":"c16_critical_mineral_supply_offtake_processing_margin_bridge_required","direction":"add_shadow_gate","production_change_now":false,"stage2_actionable_gate":"Require direct bridge and early MAE control; haircut future-dated or parent-diluted contracts.","stage3_green_gate":"Require confirmed cash/margin/revision conversion and non-price evidence beyond headline contract size."}
```

### 7.6 residual contribution row

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","loop":108,"new_axis_proposed":"c16_critical_mineral_supply_offtake_processing_margin_bridge_required_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to strategic-resource/cathode/anode/graphite rallies","existing_axis_weakened":null,"next_recommended_archetypes":["C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","C05_EPC_MEGA_CONTRACT_MARGIN_GAP","C15_MATERIAL_SPREAD_SUPERCYCLE"]}
```

### 7.7 narrative-only row

```jsonl
{"row_type":"narrative_only","symbol":"078600","reason":"Company-specific anode/offtake source not fully repaired in this run. Keep as price-path stress case and Stage2 watch until external firm-specific source is verified."}
```

---

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not use this MD as a direct production-scoring patch. Use it as one C16 residual calibration input among many.

Read this file and extract:
- case rows
- trigger rows
- score_simulation rows
- aggregate row
- shadow_weight row
- residual_contribution row
- narrative_only row

Candidate implementation after batch review only:
1. Add a C16-specific shadow gate:
   c16_critical_mineral_supply_offtake_processing_margin_bridge_required
2. Apply it only to C16 strategic-resource / critical-mineral / cathode / anode / graphite labels.
3. Require at least two bridge evidences before Stage2-Actionable:
   - direct offtake/supply contract with named counterparty
   - processing/refining/ramp schedule
   - customer demand pull or committed volume
   - ASP/spread/margin/revision bridge
   - early MAE control
4. Add parent-conglomerate / future-dated-contract haircut for cases like LG Chem where the contract is large but cash conversion is remote and parent exposure is diluted.
5. Do not promote source_proxy_only rows until URL repair is complete.
6. Do not change production weights unless multiple C16 residual MDs agree.
```

---

## 9. Final run summary

```text
selected_round = R4
selected_loop = 108
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = CRITICAL_MINERAL_GRAPHITE_CATHODE_ANODE_SUPPLY_CHAIN_OFFTAKE_VS_EV_DEMAND_AND_RESOURCE_LABEL_FADE

new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 3
verified_url_repair_needed_count = 1

new_axis_proposed = c16_critical_mineral_supply_offtake_processing_margin_bridge_required_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C16 critical-mineral/cathode/anode/graphite rallies
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
production_scoring_changed = false
shadow_weight_only = true

next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C15_MATERIAL_SPREAD_SUPERCYCLE
```
