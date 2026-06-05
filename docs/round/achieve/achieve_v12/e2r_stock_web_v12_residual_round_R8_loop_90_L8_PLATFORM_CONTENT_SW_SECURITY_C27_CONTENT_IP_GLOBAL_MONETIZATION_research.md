# E2R Stock-Web v12 Residual Research — R8 / Loop 90

```yaml
scheduled_round: R8
scheduled_loop: 90
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 90
next_round: R9
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 90
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 hard gate allows ordinary platform / content / software / security research. Recent R8 work already covered:

```text
loop88: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop89: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

This file therefore uses:

```text
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
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
225570 넥슨게임즈
251270 넷마블
194480 데브시스터즈
```

These are not in the C27 top-covered list. They also avoid the recent R8 C26/C28 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
225570: same archetype, new symbol, global PC/console game launch + retention bridge family
251270: same archetype, new symbol, external IP game launch + monetization bridge family
194480: same archetype, new symbol, China/IP franchise launch + live-service retention bridge family
```

---

## 3. Price-atlas validation

Manifest fields checked:

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
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
225570 넥슨게임즈
  profile: atlas/symbol_profiles/225/225570.json
  first_date: 2015-09-25
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,432
  corporate_action_candidate_dates:
    2017-06-12, 2018-05-09, 2022-04-15
  2024 entry~D+180 contamination: none

251270 넷마블
  profile: atlas/symbol_profiles/251/251270.json
  first_date: 2017-05-12
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,152
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

194480 데브시스터즈
  profile: atlas/symbol_profiles/194/194480.json
  first_date: 2014-10-06
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,793
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

C27 is about global monetization of content IP, not merely content visibility.

The danger is that the model may read:

```text
global launch
Steam / app-store ranking
large player downloads
known IP
webtoon / game / drama / anime cross-media fanbase
China release
```

as if those were enough for Stage3-Green.

They are not. The bridge has to be:

```text
global IP launch
  -> user acquisition
  -> retention / DAU survival
  -> payer conversion / ARPPU
  -> live-service cadence
  -> revenue and margin conversion
  -> sustainable revision
```

A launch spike is a match flare; C27 Green needs a furnace.

---

## 5. Case 1 — 225570 넥슨게임즈

```yaml
case_id: C27_R8L90_225570_2024_07_02
symbol: "225570"
name: "넥슨게임즈"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE
trigger_date: 2024-07-02
entry_date: 2024-07-02
entry_price_basis: close
entry_price: 15650
classification: positive_with_local_4b_watch
calibration_usable: true
```

### Evidence interpretation

The event frame is the global release and early traction of **The First Descendant**.

This case is a positive because the market gave a large MFE after the global launch. However, it is not a clean “global launch = durable Green” example. The same path later became a retention/4B lesson: the stock gave strong upside first, then a sharp drawdown after the initial launch-window excitement.

### Price path

Key Stock-Web rows:

```text
2024-07-02: close 15,650
2024-07-03: high 18,950 / close 17,900
2024-07-08: high 22,400 / close 21,500
2024-07-29: high 24,650 / close 23,800
2024-08-01: high 30,200 / close 28,800
2024-08-09: high 30,950 / close 28,850
2024-09-06: low 15,200 / close 15,270
2024-09-10: low 14,760 / close 14,860
```

Approximate path from entry close:

```text
entry_close: 15,650
peak_high: 30,950
MFE: +97.8%
worst_low_after_entry: 14,760
MAE: -5.7%
peak_to_later_low_drawdown: -52.3%
```

### Interpretation

This is the C27 positive control, but with an explicit local-4B overlay:

```text
Stage2-Actionable: valid after launch traction.
Stage3-Green: only if retention / monetization / live-service bridge confirms.
Local 4B: required after near +100% MFE and later drawdown.
Hard 4C: no for initial entry, but later retention failure risk must be guarded.
```

### Stress-test components

```text
raw_component_score_proxy:
  global_launch_evidence: high
  user_acquisition_signal: high
  revenue_visibility: medium
  retention_bridge: initially uncertain
  price_confirmation: very_high
  post_peak_drawdown_risk: high
  local_4b_watch: yes
```

---

## 6. Case 2 — 251270 넷마블

```yaml
case_id: C27_R8L90_251270_2024_05_09
symbol: "251270"
name: "넷마블"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE
trigger_date: 2024-05-08
entry_date: 2024-05-09
entry_price_basis: close
entry_price: 64800
classification: counterexample_external_ip_launch_without_sustained_revision_bridge
calibration_usable: true
```

### Evidence interpretation

The event frame is **Solo Leveling: Arise** global launch / anime-webtoon IP monetization.

The IP was real. The launch-window response was real. But C27 cannot treat a famous IP launch as equivalent to durable global monetization. The price path gave a short burst and then rolled over.

### Price path

Key Stock-Web rows:

```text
2024-05-08: close 60,700
2024-05-09: close 64,800
2024-05-10: high 72,400 / close 69,400
2024-05-14: low 62,400 / close 62,900
2024-06-24: low 52,400 / close 52,800
2024-08-02: high 65,000 / close 64,600
2024-11-15: low 46,100 / close 46,850
```

Approximate path from 2024-05-09 close:

```text
entry_close: 64,800
peak_high: 72,400
MFE: +11.7%
worst_low: 46,100
MAE: -28.9%
```

### Interpretation

This is a classic C27 false-positive candidate.

```text
Stage2-Watch: allowed from IP launch.
Stage2-Actionable: requires monetization and retention bridge.
Stage3-Green: blocked by shallow MFE and later high MAE.
```

The useful lesson is that even a huge IP launch can fail the C27 Green test if it does not turn quickly into revenue revision and sustained price survival.

### Stress-test components

```text
raw_component_score_proxy:
  IP_recognition: high
  launch_download_or_ranking_signal: high
  owned_IP_economics: medium_low
  retention_bridge: unclear
  margin/revision_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
```

---

## 7. Case 3 — 194480 데브시스터즈

```yaml
case_id: C27_R8L90_194480_2024_03_08
symbol: "194480"
name: "데브시스터즈"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE
trigger_date: 2024-03-08
entry_date: 2024-03-08
entry_price_basis: close
entry_price: 47200
classification: hard_4c_candidate_china_ip_launch_without_retention_revenue_bridge
calibration_usable: true
```

### Evidence interpretation

The event frame is Cookie Run IP / China launch and franchise monetization expectation after the late-2023 China release of **Cookie Run: Kingdom**.

The China release itself was a real event. But the 2024 forward path shows that C27 cannot treat China launch / app rank / franchise familiarity as enough. The conversion bridge has to include retention, payer quality, live-service cadence, and margin conversion.

### Price path

Key Stock-Web rows:

```text
2024-03-08: close 47,200
2024-03-11: high 50,200 / close 49,100
2024-04-01: high 50,900 / close 49,800
2024-07-24: high 53,300 / close 52,600
2024-08-05: low 42,250 / close 42,800
2024-10-16: low 35,400 / close 35,450
2024-10-24: low 33,800 / close 33,950
```

Approximate path from entry close:

```text
entry_close: 47,200
peak_high: 53,300
MFE: +12.9%
worst_low: 33,800
MAE: -28.4%
```

### Interpretation

This is the second C27 counterexample and the hard-4C candidate:

```text
Stage2-Watch: allowed for China/IP launch.
Stage2-Actionable: only if retention and revenue bridge appear.
Stage3-Green: blocked.
Hard 4C candidate: yes, because MFE was shallow and the forward drawdown was large.
```

### Stress-test components

```text
raw_component_score_proxy:
  China_launch_or_IP_signal: high
  installed_fanbase_signal: medium_high
  monetization_bridge: weak
  retention_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
```

The three-case C27 grid:

```text
225570 넥슨게임즈:
  global launch traction can generate a huge MFE,
  but local 4B is needed because launch-window excitement can mean-revert violently.

251270 넷마블:
  external famous IP launch can make a short burst,
  but without sustained retention/revenue revision it becomes a Stage2 false-positive candidate.

194480 데브시스터즈:
  China/IP franchise launch expectation can be real,
  but shallow MFE + large MAE makes it a hard-4C candidate without revenue bridge.
```

The shared rule:

```text
C27 is not "IP is famous" or "global launch happened."
C27 is "IP launch + retention + payer conversion + revenue/margin revision + price survival."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C27_R8L90_225570_2024_07_02","scheduled_round":"R8","scheduled_loop":90,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE","symbol":"225570","name":"넥슨게임즈","trigger_date":"2024-07-02","entry_date":"2024-07-02","entry_price":15650,"peak_high":30950,"peak_date":"2024-08-09","worst_low":14760,"worst_low_date":"2024-09-10","mfe_pct":97.8,"mae_pct":-5.7,"peak_to_later_low_drawdown_pct":-52.3,"classification":"positive_with_local_4b_watch","calibration_usable":true,"evidence_family":"global_game_launch_initial_user_acquisition_to_retention_bridge","residual_error":"positive_entry_but_launch_spike_requires_local_4b_and_retention_check","shadow_rule_candidate":"allow_actionable_after_global_launch_traction_but_require_retention_monetization_bridge_for_green"}
{"row_type":"case","case_id":"C27_R8L90_251270_2024_05_09","scheduled_round":"R8","scheduled_loop":90,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE","symbol":"251270","name":"넷마블","trigger_date":"2024-05-08","entry_date":"2024-05-09","entry_price":64800,"peak_high":72400,"peak_date":"2024-05-10","worst_low":46100,"worst_low_date":"2024-11-15","mfe_pct":11.7,"mae_pct":-28.9,"classification":"counterexample_external_ip_launch_without_sustained_revision_bridge","calibration_usable":true,"evidence_family":"external_ip_game_launch_without_retention_or_margin_revision_bridge","residual_error":"famous_ip_launch_can_overpromote_to_green","shadow_rule_candidate":"cap_external_ip_launch_at_watch_or_yellow_without_retention_payer_conversion_revision_bridge"}
{"row_type":"case","case_id":"C27_R8L90_194480_2024_03_08","scheduled_round":"R8","scheduled_loop":90,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE","symbol":"194480","name":"데브시스터즈","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":47200,"peak_high":53300,"peak_date":"2024-07-24","worst_low":33800,"worst_low_date":"2024-10-24","mfe_pct":12.9,"mae_pct":-28.4,"classification":"hard_4c_candidate_china_ip_launch_without_retention_revenue_bridge","calibration_usable":true,"evidence_family":"china_ip_franchise_launch_without_live_service_revenue_bridge","residual_error":"china_launch_or_app_rank_headline_can_overstate_c27_quality","shadow_rule_candidate":"hard_4c_candidate_if_china_ip_launch_mfe_shallow_mae_large_without_revenue_bridge"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":90,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_AND_CONTENT_IP_GLOBAL_LAUNCH_MONETIZATION_RETENTION_BRIDGE_VS_LAUNCH_DOWNLOAD_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":90,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","rule_id":"C27_GLOBAL_IP_RETENTION_MONETIZATION_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C27, do not open Stage3-Green from global launch, app rank, Steam rank, player-count headline, famous IP, or China launch alone. Require retention, payer conversion, live-service cadence, revenue/margin revision, and post-launch price survival. If MFE is shallow and MAE is large, route to C27 false-positive or hard-4C candidate. If MFE is very large but peak drawdown exceeds 40%, preserve positive entry but attach local 4B watch.","expected_effect":"Reduce content/IP launch false positives while preserving true global launch winners with monetization and retention bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":90,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","residual_type":"content_ip_global_launch_retention_bridge_guard","contribution":"Adds one launch-positive and two launch-headline counterexamples to separate global launch excitement from durable content/IP monetization.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C27_GLOBAL_IP_RETENTION_MONETIZATION_BRIDGE_REQUIRED

IF canonical_archetype_id == C27_CONTENT_IP_GLOBAL_MONETIZATION:

  Do not open Stage3-Green from:
    - global game launch headline alone
    - app-store or Steam rank alone
    - player-count or download count alone
    - famous webtoon/anime/game IP alone
    - China release headline alone
    - one-day launch price spike alone

  Require at least two of:
    - retention / DAU survival
    - payer conversion or ARPPU evidence
    - live-service update cadence
    - revenue or margin revision
    - durable global ranking after launch window
    - company-owned economics or strong licensing economics
    - post-launch price survival

  If MFE < 15% and MAE < -25%:
    route to C27 false-positive / hard-4C candidate.

  If MFE > 50% but later peak drawdown > -40%:
    keep positive entry classification but attach local 4B watch.

  If the IP is externally licensed:
    require an explicit margin / revenue-share bridge before Green.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C27 content/IP global monetization cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C27_GLOBAL_IP_RETENTION_MONETIZATION_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C27 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C27 cases agree, consider implementing a canonical guard that:
   - blocks global launch / IP fame / app-rank headlines from Green without retention and monetization bridge,
   - allows Actionable when launch traction and price confirmation are real,
   - attaches local 4B after launch-window blowoff,
   - routes shallow-MFE/high-MAE launch cases to C27 false-positive or hard-4C.

Expected next schedule:
completed_round = R8
completed_loop = 90
next_round = R9
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```
