# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 110
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_SIGNED_CONTRACT_LOCAL_PRODUCTION_BACKLOG_VS_DOMESTIC_DEFENSE_ELECTRONICS_DELAYED_REPAIR
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

이번 실행은 `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` 보강이다. Repo index 기준 C03은 9 rows / 8 symbols로 아직 thin-coverage 구역이다. 기존 visible top-covered symbol은 `103140`, `005870`, `042660`, `047810`, `065450`, `077970`에 몰려 있고, 이 세션의 직전 로컬 C03에서는 `079550`, `012450`, `003570`을 사용했다. 이번 pass는 `064350`과 `272210`을 visible-new C03 symbol로 추가하고, `012450`은 같은 symbol이지만 2025-04-15의 새 export/local-production trigger family로만 재사용한다.

Loop 산정은 v12의 pair 기준 규칙을 따른다. Repo registry상 C03은 R1 loop 104와 108이 보이고, 이 세션 로컬 C03 산출물은 loop 109였으므로 이번 `R1/C03`은 loop 110으로 진행한다.

---

## 1. Research thesis

C03의 핵심은 “방산이라는 라벨”이 아니라 “수출 framework → signed contract → delivery/backlog/local production → listed-company revenue bridge”의 다리가 실제로 닫혔는지다.

이번 루프는 세 층을 분리한다.

1. **현대로템(064350)**: Poland K2 second batch signed-contract/local-production bridge.  
   - 2025-08-01 Poland second K2 contract signed.  
   - Direct listed-company bridge: Hyundai Rotem is the named tank supplier.
   - Price path: positive, but drawdown exists, so Stage2-Actionable은 허용하되 Stage3-Green은 delivery/production milestone refresh를 요구.

2. **한화에어로스페이스(012450)**: Poland missile JV / Chunmoo ecosystem local-production bridge.  
   - 2025-04-15 Hanwha Aerospace–WB Electronics missile-production JV.
   - Direct bridge: CGR-080 guided missiles for K239 Chunmoo ecosystem.
   - Price path: strong positive with shallow MAE.

3. **한화시스템(272210)**: domestic AESA/KF-21 defense-electronics label and delayed broad defense re-rating.  
   - Domestic defense-electronics / KF-21 radar milestone exists.
   - But trigger is not export framework/backlog cash bridge.
   - Immediate 30D/90D alignment is weak; later 180D repair appears, so C03 contribution should be capped or reclassified until export/backlog bridge is refreshed.

---

## 2. Source validation

### 2.1 Price atlas

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action windows blocked by default.
```

Symbol profile caveats:

```yaml
064350:
  name: 현대로템
  market: KOSPI
  corporate_action_candidate_count: 1
  relevant_window_after_candidate: true

012450:
  name: 한화에어로스페이스
  market: KOSPI
  reused_symbol_in_C03: true
  new_trigger_family: Poland missile JV / local production

272210:
  name: 한화시스템
  market: KOSPI
  corporate_action_candidate_count: 1
  relevant_window_after_candidate: true
```

---

## 3. Trigger rows

### 3.1 Trigger row JSONL

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":110,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"K2_SECOND_BATCH_POLAND_SIGNED_CONTRACT_LOCAL_PRODUCTION_BRIDGE","symbol":"064350","name":"현대로템","trigger_type":"Stage2-Actionable","entry_date":"2025-08-01","entry_close":194000,"price_basis":"tradable_raw","mfe_30d_pct":6.96,"mae_30d_pct":-14.95,"mfe_90d_pct":28.61,"mae_90d_pct":-14.95,"mfe_180d_pct":28.61,"mae_180d_pct":-14.95,"forward_high_30d":207500,"forward_low_30d":165000,"forward_high_90d":249500,"forward_low_90d":165000,"forward_high_180d":249500,"forward_low_180d":165000,"calibration_usable":true,"case_role":"positive_with_MAE_watch","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|Stage2-Actionable|2025-08-01","non_price_bridge":"signed K2 second-batch contract + local production foothold in Poland","score_alignment":"positive but requires delivery/local-production milestone refresh before Stage3-Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":110,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"CHUNMOO_MISSILE_JV_POLAND_LOCAL_PRODUCTION_BACKLOG_BRIDGE","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2025-04-15","entry_close":771000,"price_basis":"tradable_raw","mfe_30d_pct":16.60,"mae_30d_pct":-2.59,"mfe_90d_pct":28.02,"mae_90d_pct":-2.59,"mfe_180d_pct":46.17,"mae_180d_pct":-2.59,"forward_high_30d":899000,"forward_low_30d":751000,"forward_high_90d":987000,"forward_low_90d":751000,"forward_high_180d":1127000,"forward_low_180d":751000,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage2-Actionable|2025-04-15","non_price_bridge":"Poland missile JV/local production for CGR-080 guided missiles used by K239 Chunmoo system","score_alignment":"strong positive; keep Stage2-Actionable and allow Stage3 path when production/JV execution is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":110,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DOMESTIC_DEFENSE_ELECTRONICS_AESA_LABEL_DELAYED_REPAIR_NOT_EXPORT_BACKLOG","symbol":"272210","name":"한화시스템","trigger_type":"Stage2-Watch","entry_date":"2025-08-05","entry_close":58000,"price_basis":"tradable_raw","mfe_30d_pct":0.69,"mae_30d_pct":-18.02,"mfe_90d_pct":13.62,"mae_90d_pct":-18.02,"mfe_180d_pct":72.07,"mae_180d_pct":-22.84,"forward_high_30d":58400,"forward_low_30d":47550,"forward_high_90d":65900,"forward_low_90d":47550,"forward_high_180d":99800,"forward_low_180d":44750,"calibration_usable":true,"case_role":"delayed_repair_contribution_cap","novelty_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|272210|Stage2-Watch|2025-08-05","non_price_bridge":"domestic KF-21/AESA defense-electronics milestone, not signed export backlog","score_alignment":"do not reward C03 immediately; later 180D rally requires dominant-driver reclassification/refresh"}
```

---

## 4. Case analysis

### Case A — 064350 현대로템: signed K2 contract bridge, but not a free Green

**Trigger:** 2025-08-01, Poland signed the second K2 batch contract with Hyundai Rotem.

**Mechanism:** This is a clean C03 mechanism. It is not a vague “defense theme.” It is a named buyer, named platform, signed supply contract, and local-production footprint. That opens Stage2-Actionable because the price engine has a real axle: contract economics and European production presence.

**Price path:**

```yaml
entry_date: 2025-08-01
entry_close: 194000
30d_high: 207500
30d_low: 165000
90d_high: 249500
90d_low: 165000
180d_high: 249500
180d_low: 165000
mfe_30d_pct: 6.96
mae_30d_pct: -14.95
mfe_90d_pct: 28.61
mae_90d_pct: -14.95
mfe_180d_pct: 28.61
mae_180d_pct: -14.95
```

**Score interpretation:** C03 should reward this, but not blindly. The stock had a meaningful drawdown after the signed contract. The correct treatment is `Stage2-Actionable + MAE watch`, not instant `Stage3-Green`. The green path should require delivery schedule, local assembly/profit-share details, or order-margin refresh.

---

### Case B — 012450 한화에어로스페이스: missile JV/local-production positive-control

**Trigger:** 2025-04-15, Hanwha Aerospace and Poland’s WB Electronics agreed to establish a missile-production JV.

**Mechanism:** This is the cleanest positive-control in this loop. The contract sits inside a known export system, K239 Chunmoo. The JV localizes guided-missile production, so the C03 bridge is not just “export news” but “framework turns into durable local-production/backlog channel.”

**Price path:**

```yaml
entry_date: 2025-04-15
entry_close: 771000
30d_high: 899000
30d_low: 751000
90d_high: 987000
90d_low: 751000
180d_high: 1127000
180d_low: 751000
mfe_30d_pct: 16.60
mae_30d_pct: -2.59
mfe_90d_pct: 28.02
mae_90d_pct: -2.59
mfe_180d_pct: 46.17
mae_180d_pct: -2.59
```

**Score interpretation:** Keep Stage2-Actionable. This case strengthens `repeat government customer + local production + export ecosystem` as a C03 bonus condition. It also confirms that local production is not always a margin risk; when the structure expands the customer’s installed base and locks in repeat ammo/missile demand, it can become a backlog-quality positive.

---

### Case C — 272210 한화시스템: domestic defense-electronics milestone and delayed repair

**Trigger:** 2025-08-05, KF-21/AESA radar domestic production milestone.

**Mechanism:** This is a useful anti-overfit case. Hanwha Systems has real defense technology and the price eventually rallied hard in 2026. But the immediate C03 bridge is weak because the trigger is not a signed export framework/backlog contract. It is domestic defense-electronics execution. The initial 30D path barely moved and drew down deeply; the later 180D repair may belong to a different driver stack.

**Price path:**

```yaml
entry_date: 2025-08-05
entry_close: 58000
30d_high: 58400
30d_low: 47550
90d_high: 65900
90d_low: 47550
180d_high: 99800
180d_low: 44750
mfe_30d_pct: 0.69
mae_30d_pct: -18.02
mfe_90d_pct: 13.62
mae_90d_pct: -18.02
mfe_180d_pct: 72.07
mae_180d_pct: -22.84
```

**Score interpretation:** This should not be counted as a clean C03 export-backlog hit. It belongs in `Stage2-Watch` until an export customer, signed contract, radar-system sale, or platform backlog bridge is refreshed. The later 180D MFE should be capped or reclassified if the dominant driver is broader defense/AI electronics rather than C03 export framework backlog.

---

## 5. Aggregate score-return alignment

```yaml
case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counter_or_cap_case_count: 1
new_visible_symbol_count: 2
reused_symbol_new_trigger_family_count: 1
new_trigger_family_count: 3
current_profile_error_count: 1
```

### Alignment table

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | alignment |
|---|---:|---:|---:|---:|---|
| 064350 | positive with MAE watch | +6.96 / -14.95 | +28.61 / -14.95 | +28.61 / -14.95 | signed contract works, but Green needs delivery refresh |
| 012450 | positive-control | +16.60 / -2.59 | +28.02 / -2.59 | +46.17 / -2.59 | strong Stage2-Actionable |
| 272210 | contribution-cap / delayed repair | +0.69 / -18.02 | +13.62 / -18.02 | +72.07 / -22.84 | delayed rally; not clean C03 export-backlog credit |

---

## 6. Current calibrated profile stress test

### Existing profile risk

The current profile can over-reward:

```text
defense keyword + supplier/technology label + price spike
```

That over-rewards domestic electronics and component labels if no signed export/backlog bridge exists.

### Strengthened guardrail

```text
C03_SIGNED_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_REQUIREMENT

if C03
and defense_export_or_framework_label == true
and signed_contract_or_government_customer_framework == false
and listed_company_delivery_backlog_or_local_production_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

### Positive escape hatch

```text
C03_LOCAL_PRODUCTION_REPEAT_CUSTOMER_ESCAPE_HATCH

if C03
and signed_contract_or_JV_local_production == true
and named_foreign_government_customer == true
and listed_company_revenue_or_backlog_bridge == true:
    keep_stage2_actionable_bonus = true
    if MAE_90D_pct > -15:
        allow_stage3_yellow_path = true
```

### Contribution cap

```text
C03_DOMESTIC_DEFENSE_ELECTRONICS_DELAYED_REPAIR_CAP

if C03
and domestic_defense_electronics_or_platform_label == true
and export_customer_or_signed_backlog_bridge == false
and MFE_30D_pct < +5
and MAE_30D_pct <= -15:
    cap_C03_contribution = true
    require_driver_reclassification_if_180D_MFE_repairs = true
```

---

## 7. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C03_DOMESTIC_DEFENSE_ELECTRONICS_DELAYED_REPAIR_CAP
existing_axis_strengthened:
  - C03_signed_export_framework_backlog_delivery_bridge_requirement
  - C03_repeat_government_customer_local_production_bonus
  - C03_MAE_watch_after_signed_contract
  - C03_domestic_defense_electronics_without_export_bridge_stage2_cap
existing_axis_weakened: null
```

This loop adds two useful positives and one delayed-repair cap case. The most important calibration lesson is that C03 should prefer “foreign government signed contract + delivery/local production/backlog” over “defense technology label.” 현대로템 and 한화에어로스페이스 are real C03 positives; 한화시스템 is a legitimate defense company, but this trigger should not receive full C03 export-backlog credit until export cash bridge is explicit.

---

## 8. Next recommended archetypes

```text
C15_MATERIAL_SPREAD_SUPERCYCLE
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```
