# stock-web v12 residual research — R1 Loop 108 / C03 Defense Export Framework Backlog

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R1
selected_loop = 108
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_SUBSYSTEM_SIGNED_SUPPLY_BACKLOG_BRIDGE_VS_DELAYED_HIGH_MAE
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

## 1. Selection reason

이번 실행은 `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` 보강이다. No-Repeat Index의 Priority 1 표에서 C03은 30 rows / 50-row target까지 20개가 부족한 축으로 남아 있다. 기존 C03 산출물에서는 Hanwha Aerospace, LIG Nex1, Hyundai Rotem, KAI, Firstec, Victek 조합을 이미 사용했으므로 이번에는 같은 완제품 prime case set을 반복하지 않는다.

이번 fine axis는 완제품 수출계약이 아니라 **방산 수출 장비의 엔진·변속기·전자장비 같은 subsystem/component bridge**다. 핵심 질문은 단순하다.

> prime contractor의 수출 headline이 component listed company의 실제 계약 scope, delivery schedule, backlog, margin conversion으로 연결되는가?

이 질문은 C03의 Stage2/Stage3 구분에 중요하다. 방산 테마는 한 번 불이 붙으면 계열 전체를 데우지만, 난로의 열기와 회사별 현금흐름은 같은 것이 아니다.

## 2. Source discipline

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- price atlas manifest: https://github.com/Songdaiki/stock-web/blob/main/atlas/manifest.json
- price basis: `Songdaiki/stock-web` `atlas/ohlcv_tradable_by_symbol_year`
- price adjustment status: raw / unadjusted marcap
- calibration caveat: corporate-action contaminated windows blocked by default
- current/live candidate scan: not performed
- stock_agent source-code inspection/patch: not performed
- production scoring change: not performed

## 3. External evidence spine

### 3.1 SNT Dynamics / Altay transmission

Source proxy confirms that on 2023-01-30, BMC signed a supply agreement with SNT Dynamics to procure EST15K transmissions for Turkey's Altay tank program, including 90 transmissions by December 2027 and an option for additional units.

- external source proxy: https://en.wikipedia.org/wiki/Altay_(tank)

This is a true subsystem bridge, not merely a sector rumor. But the post-trigger price path has a deep interim drawdown, so it should not be promoted to Stage3-Green without delivery/margin confirmation.

### 3.2 STX Engine / K9 SMV1000 engine localization

Source proxy confirms that STX Engine began mass production of the domestic SMV1000 engine in September 2024 after development from 2020 to 2023; the engine is intended to remove German export-control friction in K9 export markets.

- external source proxy: https://en.wikipedia.org/wiki/K9_Thunder

This is not the same as a signed export order. It is an exportability bridge. The rule must therefore require later quantity/order/backlog conversion.

### 3.3 Hanwha Systems / M-SAM ecosystem theme

Reuters confirms that LIG Nex1 won a 3.71 trillion won / $2.8bn Iraq order for M-SAM II / Cheongung II systems, and that Iraq became the fourth country to operate the system after South Korea, UAE, and Saudi Arabia.

- Reuters source: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/

Hanwha Systems was not the contracting party in that Reuters event. Therefore, the Hanwha Systems price path is useful as a component/ecosystem 4B watch and as a false-Green counterexample for direct-backlog scoring.

## 4. Case table

| case | symbol | name | trigger | entry close | peak | low | MFE | MAE | classification |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| SNT Dynamics Altay EST15K transmission | 003570 | SNT다이내믹스 | 2023-01-30 | 10,710 | 17,290 | 8,210 | +61.44% | -23.34% | positive / high-MAE watch |
| STX Engine K9 SMV1000 exportability | 077970 | STX엔진 | 2024-09-27 | 18,150 | 22,450 | 15,150 | +23.69% | -16.53% | delayed positive / high-MAE watch |
| Hanwha Systems M-SAM ecosystem component theme | 272210 | 한화시스템 | 2024-09-20 | 19,040 | 30,200 | 17,640 | +58.61% | -7.35% | price-positive but direct backlog unverified 4B watch |

## 5. Case notes

### 5.1 SNT다이내믹스 — direct subsystem contract but delayed/high-MAE path

`003570 / SNT다이내믹스`

- trigger date: 2023-01-30
- trigger type: signed subsystem export supply contract
- entry date: 2023-01-30
- entry price: 10,710
- forward peak: 17,290 on 2023-12-07
- forward low: 8,210 on 2023-03-24
- MFE: +61.44%
- MAE: -23.34%

Interpretation:

The contract bridge is real. The company is tied directly to the Altay tank transmission supply, so this is not the same as a generic defense sympathy name. But the path behaves like a bridge with a long tunnel: before the market eventually rewarded the export-subsystem story, the case produced a drawdown deeper than 20%.

Calibration implication:

- Stage2 watch: yes
- Stage2-Actionable: only after evidence of delivery schedule or revenue/backlog conversion
- Stage3-Yellow/Green: no, unless contract scope, delivery acceptance, and margin bridge are visible
- 4B watch: required because high MFE came with high MAE

### 5.2 STX엔진 — exportability bridge, not yet signed export backlog

`077970 / STX엔진`

- trigger date: 2024-09-27
- trigger type: domestic engine mass production / export-control barrier removal
- entry date: 2024-09-27
- entry price: 18,150
- forward peak: 22,450 on 2024-11-25
- forward low: 15,150 on 2024-12-09
- MFE: +23.69%
- MAE: -16.53%

Interpretation:

This is an important bridge because K9 engine localization can remove a bottleneck in export permission and supply chain. But it is still one step before signed export backlog. The engine is like a key that can open the door; it is not the purchase order itself.

Calibration implication:

- Stage2: possible
- Stage2-Actionable: only if engine order quantity / export customer / delivery date is disclosed
- Stage3: no, because the realized path has a large drawdown and the evidence is exportability, not booked backlog
- 4B watch: required

### 5.3 한화시스템 — strong price path, but direct backlog evidence not proven

`272210 / 한화시스템`

- trigger date: 2024-09-20
- trigger type: M-SAM II Iraq signed export contract ecosystem read-through
- entry date: 2024-09-20
- entry price: 19,040
- forward peak: 30,200 on 2024-11-14
- forward low: 17,640 on 2024-10-02
- MFE: +58.61%
- MAE: -7.35%

Interpretation:

The price path is strong. But the external event is LIG Nex1's signed Iraq M-SAM export contract. Without listed-company-specific scope for Hanwha Systems, this should not be treated as direct C03 Green evidence. It is a classic case where a hot prime-contractor contract lights up the surrounding electronics ecosystem, but the score should still ask: whose backlog is it?

Calibration implication:

- Stage2 price watch: yes
- Stage2-Actionable: only if company-specific radar/electronics scope or direct contract is confirmed
- Stage3-Green: no from this evidence alone
- 4B watch: yes, because price action can be real even when evidence attribution is not clean
- current profile residual error: false-Green risk if prime-contractor contract is propagated to all component names

## 6. Residual rule candidate

```text
rule_id = c03_subsystem_export_direct_scope_delivery_margin_bridge_required_shadow_only
scope = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG

positive gate:
  - listed company has a signed direct subsystem/export supply contract; OR
  - disclosure gives quantity / delivery schedule / contract amount for the listed company; OR
  - subsystem localization directly removes an export-control bottleneck AND later order/backlog conversion appears.

negative gate:
  - only prime-contractor export contract exists;
  - listed company is only ecosystem/component sympathy;
  - no direct company-specific scope, quantity, delivery schedule, backlog amount, or margin bridge;
  - price path is high-MFE but evidence attribution is weak.

stage behavior:
  - direct subsystem contract without delivery/margin confirmation: Stage2 watch / Stage2-Actionable max
  - exportability bridge without order: Stage2 watch max
  - ecosystem read-through from prime contractor: 4B watch, not Stage3
  - Stage3-Green requires company-specific non-price evidence.
```

## 7. Score simulation

| case | old profile likely behavior | residual risk | proposed shadow behavior |
|---|---|---|---|
| SNT Dynamics | likely Stage2/Stage2-Actionable from signed export-subsystem event | high interim MAE | cap at Stage2-Actionable until delivery/margin evidence |
| STX Engine | likely Stage2 from K9 exportability bridge | exportability is not order | Stage2 watch only unless signed export order appears |
| Hanwha Systems | possible false Stage3-Yellow/Green from M-SAM export ecosystem | direct backlog attribution weak | 4B watch only unless company-specific scope appears |

## 8. Machine-readable rows

```jsonl
{"calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "classification": "positive_high_mae_watch", "entry_date": "2023-01-30", "entry_price": 10710, "evidence_source": "Altay tank / BMC-SNT Dynamics EST15K transmission supply agreement source-proxy", "fine_archetype_id": "DEFENSE_SUBSYSTEM_SIGNED_SUPPLY_BACKLOG_BRIDGE_VS_DELAYED_HIGH_MAE", "forward_low_date": "2023-03-24", "forward_low_price": 8210, "forward_peak_date": "2023-12-07", "forward_peak_price": 17290, "interpretation": "Signed subsystem export contract is real enough for C03 watch, but large early MAE means no direct Stage3-Green without delivery/margin confirmation.", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_pct": -23.34, "mfe_pct": 61.44, "name": "SNT다이내믹스", "research_id": "R1_L108_C03_SNTDYNAMICS_ALTAY_TRANSMISSION_2023_01_30", "row_type": "case", "source_url": "https://en.wikipedia.org/wiki/Altay_(tank)", "symbol": "003570", "trigger_date": "2023-01-30", "url_repair_needed": true}
{"calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "classification": "delayed_positive_high_mae_watch", "entry_date": "2024-09-27", "entry_price": 18150, "evidence_source": "K9 SMV1000 engine mass-production/export restriction removal source-proxy", "fine_archetype_id": "DEFENSE_SUBSYSTEM_SIGNED_SUPPLY_BACKLOG_BRIDGE_VS_DELAYED_HIGH_MAE", "forward_low_date": "2024-12-09", "forward_low_price": 15150, "forward_peak_date": "2024-11-25", "forward_peak_price": 22450, "interpretation": "Engine localization can improve exportability, but stock path has high MAE; requires signed export quantity or engine order bridge before Stage2-Actionable.", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_pct": -16.53, "mfe_pct": 23.69, "name": "STX엔진", "research_id": "R1_L108_C03_STXENGINE_K9_DOMESTIC_ENGINE_EXPORT_BARRIER_2024_09_27", "row_type": "case", "source_url": "https://en.wikipedia.org/wiki/K9_Thunder", "symbol": "077970", "trigger_date": "2024-09-27", "url_repair_needed": true}
{"calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "classification": "price_positive_but_direct_backlog_unverified_4b_watch", "entry_date": "2024-09-20", "entry_price": 19040, "evidence_source": "LIG Iraq M-SAM export contract + Hanwha/M-SAM ecosystem source-proxy", "fine_archetype_id": "DEFENSE_SUBSYSTEM_SIGNED_SUPPLY_BACKLOG_BRIDGE_VS_DELAYED_HIGH_MAE", "forward_low_date": "2024-10-02", "forward_low_price": 17640, "forward_peak_date": "2024-11-14", "forward_peak_price": 30200, "interpretation": "Large positive path exists, but direct signed backlog evidence for the listed company is not proven here; this is a false-Green counterexample for component-theme scoring.", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_pct": -7.35, "mfe_pct": 58.61, "name": "한화시스템", "research_id": "R1_L108_C03_HANWHA_SYSTEMS_MSAM_COMPONENT_THEME_2024_09_20", "row_type": "case", "source_url": "https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/", "symbol": "272210", "trigger_date": "2024-09-20", "url_repair_needed": false}
{"date": "2023-01-30", "expected_stage_without_new_rule": "Stage2-Actionable", "row_type": "trigger", "rule_after_research": "Stage2 watch only unless delivery schedule/margin bridge is confirmed", "symbol": "003570", "trigger_id": "TRG_C03_ALTAY_EST15K_BMC_SNT_2023_01_30", "trigger_type": "signed_subsystem_export_supply_contract"}
{"date": "2024-09-27", "expected_stage_without_new_rule": "Stage2", "row_type": "trigger", "rule_after_research": "Stage2 watch only unless signed export order/backlog conversion appears", "symbol": "077970", "trigger_id": "TRG_C03_K9_SMV1000_ENGINE_EXPORT_BARRIER_2024_09_27", "trigger_type": "domestic_engine_mass_production_export_barrier_removal"}
{"date": "2024-09-20", "expected_stage_without_new_rule": "Stage2-Actionable_or_Stage3_Yellow_false_positive", "row_type": "trigger", "rule_after_research": "4B watch unless direct contract/backlog scope is evidenced", "symbol": "272210", "trigger_id": "TRG_C03_MSAM_IRAQ_COMPONENT_THEME_2024_09_20", "trigger_type": "ecosystem_component_theme_from_signed_prime_contract"}
{"avg_mae_pct": -15.74, "avg_mfe_pct": 47.91, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_count": 3, "counterexample_count": 1, "fine_archetype_id": "DEFENSE_SUBSYSTEM_SIGNED_SUPPLY_BACKLOG_BRIDGE_VS_DELAYED_HIGH_MAE", "positive_case_count": 2, "row_type": "aggregate", "rule_candidate": "c03_subsystem_export_requires_direct_scope_delivery_margin_bridge", "shadow_only": true}
{"canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "negative_gate": "- if only sector sympathy, component rumor, or prime-contractor export contract without company-specific scope", "new_axis_proposed": "c03_subsystem_export_direct_scope_delivery_margin_bridge_required_shadow_only", "positive_gate": "+ if signed direct subsystem supply contract OR disclosed engine/transmission/radar quantity with delivery dates", "production_change_now": false, "proposed_effect": "Do not raise defense component/subsystem events to Stage3-Green solely from prime-contractor signed export news. Require listed-company contract scope, delivery schedule, backlog amount, or margin conversion.", "row_type": "shadow_weight"}
{"canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "contribution": "Adds subsystem layer to C03. Separates direct SNT/STX supply bridges from Hanwha Systems/M-SAM ecosystem price action where direct backlog is unverified.", "current_profile_error_count": 2, "residual_type": "defense_component_theme_false_green_vs_direct_subsystem_backlog", "row_type": "residual_contribution"}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as a production patch request. Batch this together with other v12 residual research MDs.

Task:
1. Parse this MD's JSONL rows.
2. Add or update only shadow/calibration research artifacts, not production scoring, unless a later human-approved batch says otherwise.
3. For C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, add a shadow candidate axis:
   c03_subsystem_export_direct_scope_delivery_margin_bridge_required_shadow_only
4. The axis should penalize defense component/subsystem events when the only evidence is a prime-contractor signed export contract.
5. It should reward direct listed-company contract scope, delivery schedule, backlog amount, export customer, or margin conversion.
6. Keep this as shadow-only until enough independent rows are accumulated.
7. Do not change live scan behavior or brokerage/API logic.
8. Preserve no-repeat keys:
   canonical_archetype_id + symbol + trigger_type + entry_date.
```

## 10. Final status block

```text
selected_round: R1
selected_loop: 108
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_SUBSYSTEM_SIGNED_SUPPLY_BACKLOG_BRIDGE_VS_DELAYED_HIGH_MAE

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
verified_url_repair_needed_count: 2

diversity_score_summary: C03 Priority 1 보강 + SNT Dynamics direct Altay transmission subsystem bridge + STX Engine K9 engine exportability bridge + Hanwha Systems M-SAM ecosystem/direct-backlog attribution stress case
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C03 rows 30, 50-row target까지 20 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c03_subsystem_export_direct_scope_delivery_margin_bridge_required_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C03 defense component/theme beta
existing_axis_weakened: null
next_recommended_archetypes: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```
