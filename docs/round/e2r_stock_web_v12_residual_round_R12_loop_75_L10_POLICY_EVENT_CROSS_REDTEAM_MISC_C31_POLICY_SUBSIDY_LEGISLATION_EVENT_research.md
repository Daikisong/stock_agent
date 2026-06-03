# E2R Stock-Web v12 Residual Research — R12 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R12
completed_loop: 75
next_round: R13
next_loop: 75
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This file follows the v12 historical calibration prompt as the execution procedure.  
`V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance ledger.

This is not a live stock discovery run, not investment advice, not a trading instruction, and not a `stock_agent` code patch.  
The only output is a standalone historical calibration / sector-archetype residual Markdown artifact.

The active execution prompt fixes the research mode:

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap

production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_score_return_alignment = true
must_include_current_calibrated_profile_stress_test = true
must_include_positive_and_counterexample_balance = true
must_output_every_usable_trigger_as_jsonl = true
```

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R11
completed_loop  = 75
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Therefore:

```text
scheduled_round = R12
scheduled_loop  = 75
```

R12 permits:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
under-covered service/agri/event sector
```

This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER
```

This is a valid R12/L10 policy-event pairing.

---

## 1. Why this R12/C31 run

The no-repeat ledger shows C31 is broad, policy-event-heavy, and still contains many possible fine-subtype holes:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT:
  rows: 155
  symbols: 63
  date_range: 2020-01-20~2024-07-31
  good/bad S2: 38/32
  4B/4C: 35/0
  URL/proxy: 0/7
  top covered symbols: UNKNOWN_SYMBOL(15), 036460(8), 112610(7), 005380(5), 005860(5), 218150(5)
```

This file avoids those top-covered symbols and adds a distinct R12 policy-event subtype:

```text
low-birth / childcare policy theme
```

Selected symbols:

```text
013990 아가방컴퍼니
159580 제로투세븐
407400 꿈비
317530 캐리소프트
```

Research question:

```text
Can C31 separate a policy-theme childcare rerating that actually creates MFE from low-birth/childcare/kids-content theme spikes where the entry-day peak or later drawdown shows no sell-through, policy-execution, margin, or monetization bridge?
```

C31 policy events are like a loudspeaker. They can broadcast a national policy priority, but the company still needs a business wire running from that policy to revenue, sell-through, margins, and cash. Without the wire, the sound is loud on the first day and then the room goes quiet.

---

## 2. Price atlas validation

### Stock-Web manifest snapshot

```json
{
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "research_pack_default_price_basis": "tradable_raw"
}
```

All price rows below use:

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

### Candidate profile checks

| symbol | name | market/profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|
| `013990` | 아가방컴퍼니 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2008-05-16 | true |
| `159580` | 제로투세븐 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2018-11-13 | true |
| `407400` | 꿈비 | active_like / KOSDAQ | no 2024 overlap; 2023-07-19 candidate before selected window | true |
| `317530` | 캐리소프트 | active_like / KOSDAQ | 2024-11-18 candidate is after selected entry~D+180 window | true for 180D |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 30D/90D/180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 317530, 1Y/2Y would be contaminated_or_unavailable because of the later 2024-11-18 candidate, but the 180D window used here remains usable.
```

---

## 3. Event family and trigger discipline

### Event family

```text
event_family = low-birth / childcare policy theme burst
trigger_date = 2024-01-02
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-01-03
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level policy execution, subsidy/program linkage, childcare product sell-through, channel inventory, brand demand, kids-content monetization, gross margin, and cash-flow evidence still require URL repair through filings, company IR, policy documents, channel data, or sell-side reports before production weight promotion.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
013990 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
159580 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
407400 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
317530 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
  "counterexample_count": 3,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R12L75_C31_013990_20240103` | `013990` 아가방컴퍼니 | low-birth childcare brand policy-theme MFE | positive-guarded holdout |
| `R12L75_C31_159580_20240103` | `159580` 제로투세븐 | childcare / infant brand initial MFE with later drawdown | first-window-MFE later-drawdown warning |
| `R12L75_C31_407400_20240103` | `407400` 꿈비 | childcare product entry-day peak / high MAE | entry-day peak high-MAE counterexample |
| `R12L75_C31_317530_20240103` | `317530` 캐리소프트 | kids-content policy theme weak-MFE / high-MAE | weak-MFE high-MAE counterexample |

The intended residual:

```text
C31 should separate:
1. childcare policy theme paths with real MFE and contained entry risk;
2. theme paths where first-window MFE exists but later MAE blocks Yellow/Green;
3. entry-day peak policy-theme spikes where the policy label has already spent the upside;
4. kids-content / childcare-adjacent labels where monetization bridge is too weak.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `013990` 아가방컴퍼니 — low-birth childcare brand policy-theme high-MFE holdout

Trigger:

```text
trigger_date = 2024-01-02
trigger_type = Stage2-Actionable-Guarded
trigger_family = low_birth_policy_childcare_brand_theme_high_mfe_low_mae_entry
entry_date = 2024-01-03
entry_price = 4200.0
entry_price_type = next_tradable_open_after_low_birth_childcare_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,3945.0,4335.0,3935.0,4335.0,4043998.0,16850363895.0,142567468560.0,32887536,KOSDAQ
2024-01-03,4200.0,5630.0,4130.0,5630.0,27999034.0,144862786370.0,185156827680.0,32887536,KOSDAQ
2024-01-04,6020.0,6180.0,5550.0,5680.0,38385383.0,223788377330.0,186801204480.0,32887536,KOSDAQ
2024-01-18,7040.0,7180.0,6000.0,6140.0,26729185.0,180027315740.0,201929471040.0,32887536,KOSDAQ
2024-02-29,6090.0,6940.0,6090.0,6450.0,23866582.0,157666474260.0,212124607200.0,32887536,KOSDAQ
2024-04-02,5110.0,5120.0,4925.0,5010.0,589074.0,2944556875.0,164766555360.0,32887536,KOSDAQ
2024-06-28,4650.0,4750.0,4570.0,4645.0,698571.0,3253014220.0,152762604720.0,32887536,KOSDAQ
2024-07-01,4715.0,4905.0,4700.0,4840.0,1122692.0,5414296525.0,159175674240.0,32887536,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7180 | 2024-01-18 | 4130 | 2024-01-03 | +70.95% | -1.67% |
| 90 calendar days | 7180 | 2024-01-18 | 4130 | 2024-01-03 | +70.95% | -1.67% |
| 180 calendar days | 7180 | 2024-01-18 | 4130 | 2024-01-03 | +70.95% | -1.67% |

Interpretation:

```text
013990 is the low-birth policy-theme positive holdout.
The entry had large MFE and very contained MAE, so C31 should not blindly block every childcare policy theme.
However, Green still requires URL-repaired evidence that policy execution connects to product sell-through, channel inventory, margin, and cash-flow conversion.
```

### 6.2 `159580` 제로투세븐 — childcare / infant brand initial-MFE later drawdown

Trigger:

```text
trigger_date = 2024-01-02
trigger_type = Stage2-Actionable-Guarded
trigger_family = low_birth_policy_childcare_cosmetics_brand_initial_mfe_later_drawdown
entry_date = 2024-01-03
entry_price = 6730.0
entry_price_type = next_tradable_open_after_low_birth_childcare_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,6470.0,6850.0,6400.0,6850.0,592732.0,3960720120.0,137223556600.0,20032636,KOSDAQ
2024-01-03,6730.0,8440.0,6650.0,8020.0,11689953.0,91717609560.0,160661740720.0,20032636,KOSDAQ
2024-01-04,8550.0,8550.0,7500.0,7600.0,3811478.0,30073470050.0,152248033600.0,20032636,KOSDAQ
2024-01-18,7570.0,8590.0,7020.0,7320.0,19035703.0,150887600440.0,146638895520.0,20032636,KOSDAQ
2024-02-01,6670.0,6730.0,6480.0,6500.0,269046.0,1763975290.0,130212134000.0,20032636,KOSDAQ
2024-04-02,6010.0,6090.0,5750.0,5890.0,220027.0,1283316350.0,117992226040.0,20032636,KOSDAQ
2024-06-28,5300.0,5430.0,5210.0,5310.0,154671.0,824446470.0,106373297160.0,20032636,KOSDAQ
2024-07-01,5340.0,5570.0,5340.0,5460.0,209391.0,1147472780.0,109378192560.0,20032636,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8590 | 2024-01-18 | 6480 | 2024-02-01 | +27.64% | -3.71% |
| 90 calendar days | 8590 | 2024-01-18 | 5750 | 2024-04-02 | +27.64% | -14.56% |
| 180 calendar days | 8590 | 2024-01-18 | 5210 | 2024-06-28 | +27.64% | -22.59% |

Interpretation:

```text
159580 is the first-window-MFE / later-drawdown warning.
The early MFE was real, but 90D/180D drawdown widened before a company-specific policy/sell-through/margin bridge was repaired.
This should cap at Stage2-Guarded or local 4B watch, not Yellow/Green.
```

### 6.3 `407400` 꿈비 — childcare product entry-day peak / high-MAE counterexample

Trigger:

```text
trigger_date = 2024-01-02
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = low_birth_policy_childcare_product_entry_day_peak_high_mae
entry_date = 2024-01-03
entry_price = 12390.0
entry_price_type = next_tradable_open_after_low_birth_childcare_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,12170.0,12600.0,12040.0,12600.0,980913.0,12135125130.0,154469372400.0,12259474,KOSDAQ
2024-01-03,12390.0,14700.0,12230.0,13410.0,8097482.0,110708948340.0,164399546340.0,12259474,KOSDAQ
2024-01-04,13540.0,13650.0,12520.0,12810.0,1486101.0,19297293900.0,157043861940.0,12259474,KOSDAQ
2024-02-01,10070.0,10190.0,9740.0,9980.0,134012.0,1332275460.0,122349550520.0,12259474,KOSDAQ
2024-03-20,9290.0,10960.0,9290.0,10150.0,5042367.0,52405637070.0,124433661100.0,12259474,KOSDAQ
2024-04-08,8310.0,8350.0,8100.0,8210.0,68262.0,558961640.0,100650281540.0,12259474,KOSDAQ
2024-07-01,8840.0,9570.0,8820.0,9240.0,1858802.0,17208583220.0,113277539760.0,12259474,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 14700 | 2024-01-03 | 9740 | 2024-02-01 | +18.64% | -21.39% |
| 90 calendar days | 14700 | 2024-01-03 | 8920 | 2024-04-02 | +18.64% | -28.01% |
| 180 calendar days | 14700 | 2024-01-03 | 8100 | 2024-04-08 | +18.64% | -34.62% |

Interpretation:

```text
407400 is the entry-day-peak / high-MAE counterexample.
The policy theme created a first-day spike, but the same selected entry immediately carried high MAE.
This should block Stage2 or route to local 4B/high-MAE watch unless policy execution and sell-through evidence was repaired before entry.
```

### 6.4 `317530` 캐리소프트 — kids-content policy label with weak-MFE / high-MAE

Trigger:

```text
trigger_date = 2024-01-02
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = low_birth_policy_kids_content_theme_weak_mfe_high_mae
entry_date = 2024-01-03
entry_price = 5440.0
entry_price_type = next_tradable_open_after_low_birth_kids_content_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,5140.0,5370.0,5130.0,5370.0,68766.0,361490650.0,37435322520.0,6971196,KOSDAQ
2024-01-03,5440.0,5970.0,5240.0,5650.0,517199.0,2951411870.0,39387257400.0,6971196,KOSDAQ
2024-01-04,5950.0,6000.0,5510.0,5590.0,198752.0,1137136760.0,38968985640.0,6971196,KOSDAQ
2024-02-02,4600.0,4700.0,4455.0,4670.0,15908.0,73674570.0,32555485320.0,6971196,KOSDAQ
2024-02-21,4740.0,6100.0,4740.0,5190.0,2767024.0,15921831675.0,36180507240.0,6971196,KOSDAQ
2024-04-02,4875.0,4875.0,4600.0,4700.0,16740.0,78335305.0,32764621200.0,6971196,KOSDAQ
2024-07-01,3965.0,4150.0,3770.0,3880.0,132617.0,519884670.0,27048240480.0,6971196,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6000 | 2024-01-04 | 4455 | 2024-02-02 | +10.29% | -18.11% |
| 90 calendar days | 6100 | 2024-02-21 | 4455 | 2024-02-02 | +12.13% | -18.11% |
| 180 calendar days | 6100 | 2024-02-21 | 3770 | 2024-07-01 | +12.13% | -30.70% |

Interpretation:

```text
317530 is the weak-MFE high-MAE kids-content counterexample.
The policy label was adjacent to childcare, but forward MFE stayed too weak while 180D MAE crossed -30%.
This should block Stage2 or route to local 4B/high-MAE watch until a real monetization or policy-execution bridge is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R12L75_C31_LOW_BIRTH_CHILDCARE_ROUTER","round":"R12","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER","symbol":"013990","name":"아가방컴퍼니","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"low_birth_policy_childcare_brand_theme_high_mfe_low_mae_entry","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":4200.0,"entry_price_type":"next_tradable_open_after_low_birth_childcare_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":70.95,"mae_30d_pct":-1.67,"mfe_90d_pct":70.95,"mae_90d_pct":-1.67,"mfe_180d_pct":70.95,"mae_180d_pct":-1.67,"peak_price_180d":7180.0,"peak_date_180d":"2024-01-18","trough_price_180d":4130.0,"trough_date_180d":"2024-01-03","calibration_usable":true,"case_polarity":"positive_guarded_policy_theme_high_mfe","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_childcare_policy_execution_sellthrough_margin_bridge_repaired","residual_error_type":"low_birth_policy_theme_had_real_mfe_but_green_requires_url_repaired_childcare_demand_sellthrough_margin_bridge"}
{"row_type":"trigger","research_id":"R12L75_C31_LOW_BIRTH_CHILDCARE_ROUTER","round":"R12","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER","symbol":"159580","name":"제로투세븐","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"low_birth_policy_childcare_cosmetics_brand_initial_mfe_later_drawdown","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":6730.0,"entry_price_type":"next_tradable_open_after_low_birth_childcare_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":27.64,"mae_30d_pct":-3.71,"mfe_90d_pct":27.64,"mae_90d_pct":-14.56,"mfe_180d_pct":27.64,"mae_180d_pct":-22.59,"peak_price_180d":8590.0,"peak_date_180d":"2024-01-18","trough_price_180d":5210.0,"trough_date_180d":"2024-06-28","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_drawdown","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_policy_execution_sellthrough_margin_bridge_repaired","residual_error_type":"low_birth_childcare_policy_theme_had_initial_mfe_but_180d_drawdown_requires_sellthrough_and_margin_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R12L75_C31_LOW_BIRTH_CHILDCARE_ROUTER","round":"R12","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER","symbol":"407400","name":"꿈비","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"low_birth_policy_childcare_product_entry_day_peak_high_mae","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":12390.0,"entry_price_type":"next_tradable_open_after_low_birth_childcare_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.64,"mae_30d_pct":-21.39,"mfe_90d_pct":18.64,"mae_90d_pct":-28.01,"mfe_180d_pct":18.64,"mae_180d_pct":-34.62,"peak_price_180d":14700.0,"peak_date_180d":"2024-01-03","trough_price_180d":8100.0,"trough_date_180d":"2024-04-08","calibration_usable":true,"case_polarity":"counterexample_entry_day_peak_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"low_birth_childcare_entry_day_spike_had_high_mae_without_policy_execution_or_sellthrough_bridge"}
{"row_type":"trigger","research_id":"R12L75_C31_LOW_BIRTH_CHILDCARE_ROUTER","round":"R12","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER","symbol":"317530","name":"캐리소프트","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"low_birth_policy_kids_content_theme_weak_mfe_high_mae","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":5440.0,"entry_price_type":"next_tradable_open_after_low_birth_kids_content_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.29,"mae_30d_pct":-18.11,"mfe_90d_pct":12.13,"mae_90d_pct":-18.11,"mfe_180d_pct":12.13,"mae_180d_pct":-30.7,"peak_price_180d":6100.0,"peak_date_180d":"2024-02-21","trough_price_180d":3770.0,"trough_date_180d":"2024-07-01","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_kids_content_monetization_bridge_repaired","residual_error_type":"kids_content_policy_label_had_weak_mfe_and_high_mae_without_monetization_or_policy_execution_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy relevance | company execution bridge | product sell-through | channel / inventory | market mispricing | margin / cash-flow conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `013990` | 12 | 6 | 7 | 6 | 13 | 5 | 5 | 54 | Stage2-Guarded / Yellow only after evidence repair |
| `159580` | 10 | 4 | 4 | 4 | 8 | 3 | 5 | 38 | Stage2-Guarded or local 4B watch |
| `407400` | 10 | 3 | 3 | 3 | 5 | 2 | 4 | 30 | blocked Stage2 / 4B high-MAE watch |
| `317530` | 8 | 2 | 2 | 2 | 4 | 1 | 4 | 23 | blocked Stage2 / 4B high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C31 issue is **policy relevance without company-specific conversion**:

```text
C31 low-birth positive holdout:
  policy relevance
  + MFE expands strongly
  + MAE remains contained
  + URL-repaired company bridge can later prove sell-through/margin
  => Stage2-Guarded, Yellow only after evidence repair

C31 first-window-MFE later-drawdown path:
  policy theme creates MFE
  + MAE_180D <= -20%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, local 4B watch, no Green

C31 entry-day peak high-MAE path:
  peak occurs on entry day
  + MAE_30D <= -20%
  + no policy execution / sell-through bridge
  => block Stage2 or local 4B/high-MAE watch

C31 weak-MFE policy-adjacent content path:
  MFE_90D <= +15%
  + MAE_180D <= -30%
  + monetization bridge missing
  => block Stage2
```

`013990` prevents overblocking: some low-birth policy themes did generate real MFE.  
`159580`, `407400`, and `317530` show why policy relevance alone should not become Yellow/Green without execution, sell-through, and margin evidence.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R12L75_C31_LOW_BIRTH_CHILDCARE_ROUTER",
  "round": "R12",
  "loop": 75,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 1,
  "counterexample_count": 3,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 31.88,
  "avg_mae_30d_pct": -11.22,
  "avg_mfe_90d_pct": 32.34,
  "avg_mae_90d_pct": -15.84,
  "avg_mfe_180d_pct": 32.34,
  "avg_mae_180d_pct": -22.39,
  "max_mfe_180d_pct": 70.95,
  "worst_mae_180d_pct": -34.62
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R12L75_C31_LOW_BIRTH_CHILDCARE_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "013990",
      "reason": "low-birth childcare policy path had +70.95% 180D MFE with only -1.67% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "159580",
      "reason": "first-window MFE existed, but 180D MAE reached -22.59%"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "407400",
      "reason": "entry-day peak with -21.39% 30D MAE and -34.62% 180D MAE"
    },
    {
      "symbol": "317530",
      "reason": "weak +12.13% 180D MFE and -30.70% 180D MAE without monetization bridge"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "actual policy execution and subsidy/program linkage",
    "childcare product sell-through",
    "channel inventory and reorder",
    "brand demand and pricing",
    "kids-content monetization where relevant",
    "gross margin and cash-flow conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER
rule_name: C31_low_birth_childcare_policy_sellthrough_and_entry_spike_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C31 low-birth / childcare policy theme cases:

Tier A: verified policy-to-demand winner
  Conditions:
    - policy relevance is clear
    - company-specific sell-through, channel, margin, or monetization evidence is URL-repaired
    - MFE_30D >= +40%
    - MAE_90D > -10%
  Routing:
    - Stage2-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after policy execution / sell-through / margin bridge is verified

Tier B: first-window-MFE / later-drawdown theme
  Conditions:
    - MFE_30D >= +20%
    - MAE_180D <= -20%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - no Yellow/Green

Tier C: entry-day peak high-MAE policy theme
  Conditions:
    - peak occurs on entry day or first 5 trading days
    - MAE_30D <= -20%
    - no repaired policy execution or sell-through bridge
  Routing:
    - block Stage2
    - local 4B/high-MAE watch
    - count as counterexample

Tier D: weak-MFE policy-adjacent content label
  Conditions:
    - MFE_90D <= +15%
    - MAE_180D <= -30%
    - monetization bridge missing
  Routing:
    - block Stage2
    - route to local 4B/high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c31_low_birth_childcare_policy_sellthrough_and_entry_spike_high_mae_router",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "policy_relevance_alone_stage2_allowed": false,
    "policy_execution_sellthrough_margin_bridge_required_for_green": true,
    "verified_policy_to_demand_mfe30_threshold_pct": 40.0,
    "verified_policy_to_demand_mae90_min_pct": -10.0,
    "first_window_mfe_threshold_30d_pct": 20.0,
    "later_drawdown_mae180_threshold_pct": -20.0,
    "entry_spike_mae30_threshold_pct": -20.0,
    "weak_mfe_threshold_90d_pct": 15.0,
    "weak_mfe_hard_mae180_threshold_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One childcare policy-theme MFE holdout and three later-drawdown or entry-spike failures show that C31 should not promote low-birth policy relevance without URL-repaired policy execution, sell-through, channel, margin, or monetization evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R12L75_C31_LOW_BIRTH_CHILDCARE_ROUTER",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds four non-top-covered C31 low-birth / childcare policy-event cases and separates a true high-MFE childcare policy-theme holdout from first-window-MFE/later-drawdown, entry-day-peak high-MAE, and weak-MFE kids-content failures. C31 Yellow/Green should require URL-repaired policy execution, product sell-through, channel inventory, brand demand, monetization, gross margin, and cash-flow evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 3,
  "new_symbol_count": 4,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "current_profile_error_count": 3,
  "diversity_score_summary": {
    "new_symbol_bonus": 12,
    "counterexample_gap_bonus": 6,
    "residual_error_bonus": 15,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 33
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All four non-price low-birth/childcare policy triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C31 source_proxy_only low-birth policy cases with entry-day peak and MAE_30D <= -20% should block Stage2; first-window-MFE cases with MAE_180D <= -20% should cap at Stage2-Guarded; weak-MFE policy-adjacent content cases with MAE_180D <= -30% should block Stage2."
}
```

One-line contribution:

```text
This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
```

---

## 13. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  price_basis: tradable_raw
  price_adjustment_status: raw_unadjusted_marcap
  manifest_max_date: 2026-02-20
  forward_window_required: 180_calendar_days
  forward_window_available: true
  raw_shard_used_for_weight_calibration: false
  corporate_action_contaminated_180D_window:
    013990: false
    159580: false
    407400: false
    317530: false
  evidence_url_pending:
    013990: true
    159580: true
    407400: true
    317530: true
  source_proxy_only:
    013990: true
    159580: true
    407400: true
    317530: true
  special_handling:
    317530:
      corporate_action_candidate_date: "2024-11-18"
      note: "Candidate date is after selected entry~D+180 window; 1Y/2Y fields would be contaminated_or_unavailable."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C31 low-birth / childcare policy-event residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, policy documents, channel data, or reports verify policy execution, subsidy/program linkage, sell-through, channel inventory, margin, and cash-flow conversion.
- It should not be read as a current investment view.
```

---

## 14. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve R12 / loop 75 metadata.
3. Add the cases to C31_POLICY_SUBSIDY_LEGISLATION_EVENT only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/policy-document/channel-data/report data verifies policy execution, subsidy/program linkage, product sell-through, channel inventory, brand demand, kids-content monetization, gross margin, and cash-flow conversion.
6. Add a shadow-only rule candidate named C31_low_birth_childcare_policy_sellthrough_and_entry_spike_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C31-specific guards:
   - source_proxy_only -> no Green
   - policy relevance alone -> no Stage2 promotion
   - Stage3-Yellow/Green requires company-specific policy execution / sell-through / margin bridge
   - MFE_30D >= +40% and MAE_90D > -10% may remain Stage2-Guarded until evidence repair
   - MFE_30D >= +20% and MAE_180D <= -20% -> Stage2-Guarded at most / local 4B watch
   - entry-day or first-5-day peak with MAE_30D <= -20% -> block Stage2 / local 4B watch
   - MFE_90D <= +15% and MAE_180D <= -30% -> block Stage2 / local 4B watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R12
completed_loop = 75
next_round = R13
next_loop = 75
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
next_allowed_scope = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW or R13_CROSS_ARCHETYPE_4B_4C_REDTEAM or R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION or R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = valid
round_sector_consistency = pass
```
