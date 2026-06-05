# E2R Stock-Web v12 Residual Research — R8 / Loop 94

```yaml
scheduled_round: R8
scheduled_loop: 94
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 94
next_round: R9
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_94_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 94
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 hard gate requires:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

Recent R8 branch usage:

```text
loop91: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop92: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop93: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

This run selects the content/IP branch:

```text
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

The selected fine branch is:

```text
game / K-pop / drama IP global monetization and margin bridge
vs generic content label beta
```

The purpose is to distinguish:

```text
real IP monetization engines with new release or global user monetization
```

from:

```text
content brand labels where fanbase, catalog quality, or global relevance does not convert into margin and price survival.
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
rows: 39
symbols: 15
date_range: 2021-01-22~2024-09-26
good/bad S2: 20/6
4B/4C: 3/1
URL pending/proxy: 6/6
top covered symbols:
  263750(5), 112040(4), 122870(4), 293490(4), 259960(3), 376300(3)
```

Selected symbols:

```text
251270 넷마블
035900 JYP Ent.
253450 스튜디오드래곤
```

They avoid the C27 top-covered symbols and avoid recent R8 loop91~93 names:

```text
loop91 avoid: 067160, 273060, 236810
loop92 avoid: 136540, 053800, 356680
loop93 avoid: 230360, 214320, 089600
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
251270: same archetype, new symbol, game IP / release monetization positive with capped Green
035900: same archetype, new symbol, K-pop IP label hard-4C without current monetization and margin bridge
253450: same archetype, new symbol, drama/OTT production IP Watch cap without new global sell-through margin bridge
```

---

## 3. Price-atlas validation

Manifest fields checked from stock-web:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
inactive_or_delisted_like_symbol_count: 2,546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
251270 넷마블
  profile: atlas/symbol_profiles/251/251270.json
  name history:
    넷마블게임즈 until 2018-04-13
    넷마블 from 2018-04-16
  first_date: 2017-05-12
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,152
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

035900 JYP Ent.
  profile: atlas/symbol_profiles/035/035900.json
  name history includes:
    아라리온, 세이텍, 제이튠엔터, 제이와이피엔터, JYP Ent.
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  first_date: 2001-08-30
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,935
  non_tradable_zero_volume rows: 103
  corporate_action_candidate_dates:
    historical only; latest candidate 2013-10-31
  2024 entry~D+180 contamination: none

253450 스튜디오드래곤
  profile: atlas/symbol_profiles/253/253450.json
  first_date: 2017-11-24
  last_date: 2026-02-20
  market:
    KOSDAQ until 2024-06-13
    KOSDAQ GLOBAL from 2024-06-14
  tradable_ohlcv rows: 2,020
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C27 is about content/IP global monetization. It is not a generic "content stock" or "K-pop/K-drama/game label" archetype.

The model can over-score:

```text
global game IP label
K-pop fandom label
drama studio / OTT distribution label
global content sentiment
fanbase / catalog quality
one-week content-stock volume spike
```

The C27 bridge must be stricter:

```text
content / IP event
  -> active user or audience growth
  -> paid conversion, ARPU, touring, merch, publishing, licensing, or platform revenue
  -> release cadence and IP lifecycle
  -> overseas distribution / localization
  -> production or marketing-cost control
  -> margin / OP conversion
  -> price survival after the first content-theme spike
```

A content IP thesis is like a stage with bright lights. The crowd matters, but C27 asks whether the crowd buys tickets, streams, spends in-game, renews subscriptions, buys merchandise, or licenses the IP at margins that survive production and marketing cost.

---

## 5. Case 1 — 251270 넷마블

```yaml
case_id: C27_R8L94_251270_2024_02_01
symbol: "251270"
name: "넷마블"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 56500
classification: positive_game_ip_release_monetization_with_capped_green
calibration_usable: true
```

### Evidence interpretation

넷마블 is the constructive C27 control.

The useful C27 read is not simply:

```text
game company / content IP label
```

It is:

```text
game IP and release pipeline
  -> user monetization / launch cadence
  -> global publishing leverage
  -> price confirmation
  -> controlled drawdown after the entry
```

The forward path delivered a meaningful MFE and held its entry range even through later market volatility. This is a C27 positive, but Green still needs fresh game-performance and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 58,300 / close 56,500
2024-02-13: high 65,100 / close 62,200
2024-02-27: high 67,000 / close 66,800
2024-04-25: low 52,100 / close 53,100
2024-05-08: high 62,600 / close 60,700
2024-07-24: high 62,800 / close 62,700
2024-08-09: high 72,100 / close 61,900
2024-09-12: high 61,700 / close 61,700
```

Approximate path from entry close:

```text
entry_close: 56,500
peak_high: 72,100
MFE: +27.6%
worst_low_after_entry: 52,100
MAE: -7.8%
```

### Interpretation

This is a C27 positive, but capped:

```text
Stage2-Actionable: valid if launch, user monetization, and margin bridge are explicit.
Stage3-Green: possible only with active user, ARPU, publishing, and OP evidence.
Local 4B: monitor after +25% MFE; not mandatory from initial path alone.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  game_ip_relevance: high
  release_pipeline_bridge: medium_high
  global_publishing_bridge: medium
  monetization_margin_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 035900 JYP Ent.

```yaml
case_id: C27_R8L94_035900_2024_02_01
symbol: "035900"
name: "JYP Ent."
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 76000
classification: hard_4c_candidate_kpop_ip_label_without_current_monetization_margin_bridge
calibration_usable: true
```

### Evidence interpretation

JYP Ent. is the K-pop IP hard guardrail.

The model can be tempted by:

```text
K-pop global fandom
touring / album / merch / platform monetization
global entertainment label
```

But from this entry, the forward price path did not validate active monetization or margin survival. The initial MFE was shallow and the later MAE crossed the hard-4C threshold.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 76,300 / close 76,000
2024-02-21: high 79,400 / close 77,100
2024-03-07: low 66,300 / close 66,600
2024-04-17: low 62,600 / close 62,600
2024-08-05: low 48,300 / close 50,900
2024-09-09: low 43,100 / close 44,150
2024-11-04: high 54,500 / close 53,900
```

Approximate path from entry close:

```text
entry_close: 76,000
peak_high: 79,400
MFE: +4.5%
worst_low_after_entry: 43,100
MAE: -43.3%
```

### Interpretation

This is a hard C27 false-positive:

```text
Stage2-Watch: possible from K-pop IP and global fandom relevance.
Stage2-Actionable: blocked unless touring, album, merch, platform, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and large MAE.
```

The lesson is that global fandom is not always current monetization.

### Stress-test components

```text
raw_component_score_proxy:
  kpop_ip_label: high
  fandom_global_relevance: high
  current_monetization_bridge: weak
  margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 253450 스튜디오드래곤

```yaml
case_id: C27_R8L94_253450_2024_02_01
symbol: "253450"
name: "스튜디오드래곤"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 46500
classification: watch_cap_kdrama_ott_ip_label_without_new_sellthrough_margin_bridge
calibration_usable: true
```

### Evidence interpretation

스튜디오드래곤 is the drama/OTT Watch cap.

The company has clear content IP relevance:

```text
K-drama catalog
OTT distribution
production studio / global licensing
```

But C27 should not promote the label into Actionable/Green unless new global sell-through, licensing economics, production-cost control, and margin evidence are visible. The forward price path had shallow MFE and a material drawdown, but did not cross the hard-4C threshold from this entry.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 46,850 / close 46,500
2024-02-08: high 48,100 / close 47,800
2024-03-06: low 42,700 / close 42,900
2024-04-17: low 40,200 / close 40,350
2024-08-05: low 33,000 / close 35,350
2024-09-04: low 33,800 / close 34,100
2024-11-04: high 42,550 / close 42,300
```

Approximate path from entry close:

```text
entry_close: 46,500
peak_high: 48,100
MFE: +3.4%
worst_low_after_entry: 33,000
MAE: -29.0%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from K-drama/OTT IP relevance.
Stage2-Actionable: blocked unless global licensing, new slate monetization, and production-cost/margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: borderline, but Watch/Yellow cap is more appropriate because MAE is just below hard threshold and price later recovered partially.
```

### Stress-test components

```text
raw_component_score_proxy:
  drama_ip_relevance: high
  ott_distribution_label: medium_high
  new_slate_sellthrough_bridge: weak
  licensing_margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium_high
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C27 content/IP grid:

```text
251270 넷마블:
  game IP / release monetization positive;
  useful MFE and controlled MAE, but Green requires user monetization and OP bridge.

035900 JYP Ent.:
  K-pop IP label failed from the entry;
  shallow MFE and high MAE, hard 4C.

253450 스튜디오드래곤:
  K-drama/OTT IP label did not validate Actionable;
  shallow MFE and material MAE, Watch/Yellow cap.
```

Shared rule:

```text
C27 is not "content IP is globally known."
C27 is "audience becomes paid conversion, licensing, touring, in-game spending, merch, reorder, platform revenue, and margin for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C27_R8L94_251270_2024_02_01","scheduled_round":"R8","scheduled_loop":94,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA","symbol":"251270","name":"넷마블","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":56500,"peak_high":72100,"peak_date":"2024-08-09","worst_low_after_entry":52100,"worst_low_after_entry_date":"2024-04-25","mfe_pct":27.6,"mae_pct":-7.8,"classification":"positive_game_ip_release_monetization_with_capped_green","calibration_usable":true,"evidence_family":"game_ip_release_pipeline_user_monetization_publishing_margin_bridge","residual_error":"positive_game_ip_path_still_requires_active_user_arpu_and_op_bridge_before_green","shadow_rule_candidate":"preserve_content_ip_positive_when_release_monetization_and_price_survival_confirm_but_cap_green_without_margin_evidence"}
{"row_type":"case","case_id":"C27_R8L94_035900_2024_02_01","scheduled_round":"R8","scheduled_loop":94,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA","symbol":"035900","name":"JYP Ent.","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76000,"peak_high":79400,"peak_date":"2024-02-21","worst_low_after_entry":43100,"worst_low_after_entry_date":"2024-09-09","mfe_pct":4.5,"mae_pct":-43.3,"classification":"hard_4c_candidate_kpop_ip_label_without_current_monetization_margin_bridge","calibration_usable":true,"evidence_family":"kpop_global_fandom_ip_label_without_current_touring_merch_platform_margin_bridge","residual_error":"global_fandom_label_can_overpromote_without_current_monetization_and_margin_survival","shadow_rule_candidate":"route_kpop_ip_label_to_hard_4c_if_mfe_shallow_mae_large_and_monetization_bridge_missing"}
{"row_type":"case","case_id":"C27_R8L94_253450_2024_02_01","scheduled_round":"R8","scheduled_loop":94,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA","symbol":"253450","name":"스튜디오드래곤","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":46500,"peak_high":48100,"peak_date":"2024-02-08","worst_low_after_entry":33000,"worst_low_after_entry_date":"2024-08-05","mfe_pct":3.4,"mae_pct":-29.0,"classification":"watch_cap_kdrama_ott_ip_label_without_new_sellthrough_margin_bridge","calibration_usable":true,"evidence_family":"kdrama_ott_distribution_label_without_new_slate_sellthrough_licensing_margin_bridge","residual_error":"content_catalog_quality_can_overpromote_without_fresh_global_licensing_and_margin_conversion","shadow_rule_candidate":"cap_kdrama_ott_ip_label_at_watch_yellow_if_mfe_shallow_and_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":94,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_KPOP_DRAMA_IP_GLOBAL_MONETIZATION_REORDER_MARGIN_BRIDGE_VS_CONTENT_LABEL_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":94,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","rule_id":"C27_IP_MONETIZATION_AUDIENCE_TO_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C27, do not open Stage2-Actionable or Stage3-Green from game, K-pop, drama, OTT, fanbase, catalog, global IP, or one-week content-stock volume spike labels alone. Require active user or audience growth, paid conversion, ARPU, touring, merch, publishing, licensing, global distribution/localization, production and marketing-cost control, margin/OP conversion, and post-trigger price survival. Game IP positives may be Actionable when launch and user monetization bridge are explicit. K-pop labels with shallow MFE and high MAE should route to hard-4C when current monetization and margin bridge are missing. Drama/OTT labels with shallow MFE and material MAE should cap at Watch/Yellow without fresh slate sell-through and licensing evidence.","expected_effect":"Reduce content-label and global-fandom false positives while preserving true IP monetization positives with audience-to-margin conversion evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":94,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","residual_type":"content_ip_audience_to_margin_guard","contribution":"Adds one game IP positive, one K-pop hard-4C, and one K-drama/OTT Watch cap to calibrate C27 global IP monetization and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C27_IP_MONETIZATION_AUDIENCE_TO_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C27_CONTENT_IP_GLOBAL_MONETIZATION:

  Do not open Stage3-Green from:
    - game IP label alone
    - K-pop fandom label alone
    - drama / OTT catalog label alone
    - global content sentiment alone
    - fanbase size alone
    - one-week content-stock volume spike alone

  Require at least two of:
    - active user / audience growth
    - paid conversion or ARPU
    - touring / merch / platform revenue
    - publishing / licensing economics
    - global distribution / localization
    - release cadence or new slate monetization
    - production / marketing-cost containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the IP headline

  If MFE < 10% and MAE < -35%:
    route to C27 hard-4C candidate.

  If MFE is shallow and the bridge is catalog/fanbase label only:
    cap at Watch/Yellow.

  If MFE > 25% and MAE remains controlled:
    allow capped Actionable only if monetization and margin bridge are explicit.

  Distinguish:
    - game IP names where launch/user monetization reaches OP
    - from K-pop/drama labels where global relevance does not convert into current margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_94_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C27 content/IP global-monetization cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C27_IP_MONETIZATION_AUDIENCE_TO_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C27 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C27 cases agree, consider implementing a canonical guard that:
   - blocks content-label Green without audience-to-paid-monetization and margin bridge,
   - preserves game-IP positives only with price survival and user monetization evidence,
   - caps drama/OTT catalog labels at Watch/Yellow without licensing/margin evidence,
   - routes shallow-MFE/high-MAE K-pop IP labels to hard-4C.

Expected next schedule:
completed_round = R8
completed_loop = 94
next_round = R9
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 94
next_round = R9
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
