# E2R Stock-Web v12 Residual Research — C04 Nuclear Policy / Project / Legal Delay Holdout

```yaml
schema_version: v12_stock_web_residual_research
selected_round: R1
selected_loop: 113
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout after current-session Priority-0/Priority-1 fills; static C04 rows=71
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout
loop_objective:
  - holdout_validation
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - sector_specific_rule_discovery
  - canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

The static No-Repeat ledger still shows Priority 0 archetypes, but the current execution chain has already produced multiple C02/C09/C14/C10/C06/C07/C11/C01/C28/C12 passes. This loop therefore follows the last quality-holdout recommendations and selects `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY`, a Priority 2 area where additional work should not be simple row stuffing. The point of this loop is to test whether a nuclear preferred-bidder headline should remain Stage2-Actionable, advance to Stage3-Yellow, or be capped by local 4B when legal/project finalization is still unresolved.

Loop number rule: GitHub `docs/round` already contains standard C04 files through `R1_loop_112`; this file uses `R1_loop_113`.

Novelty:

```yaml
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 4
new_trigger_family_count: 4
positive_case_count: 3
counterexample_count: 4
local_4B_watch_count: 6
4C_case_count: 0
current_profile_error_count: 6
diversity_score_summary: 7 symbols / Czech preferred-bidder directness split / legal-delay high-MAE split / indirect supplier theme cap / missed direct equipment positive
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 2. Source and timing frame

Trigger date is `2024-07-17`, when KHNP was selected as preferred bidder for the Czech nuclear project. The project headline was powerful, but it was not the same as a signed final contract or signed vendor-level revenue recognition. The South Korean consortium included KEPCO E&C, KEPCO KPS, Doosan Enerbility and others; the final result/contract was still expected later. Westinghouse filed an appeal in August 2024, and Czech anti-monopoly proceedings in October 2024 showed that legal/process risk could remain inside the forward window.

Evidence URLs used:

- KHNP preferred bidder / Team Korea consortium: https://en.yna.co.kr/view/AEN20240716006751320
- Czech official project page / KHNP selection: https://www.njzedu.cz/en/the-dukovany-ii-power-plant/about-the-project
- Westinghouse protest / appeal: https://info.westinghousenuclear.com/news/westinghouse-protests-czechia-nuclear-tender-decision
- Reuters on Czech watchdog appeal rejection / not-final legal path: https://www.reuters.com/business/energy/czech-watchdog-rejects-appeals-nuclear-power-tender-2024-10-31/
- Doosan Czech nuclear project context: https://www.doosan.com/en/media-center/press-release_view/?id=20172654&page=0
- KEPCO KPS nuclear maintenance scope: https://www.kps.co.kr/eng/about/about_05_04_03.do
- Woojin nuclear instrumentation: https://money2.daishin.com/PDF/Out/intranet_data/product/researchcenter/report/2024/04/49655_com_woojin.pdf
- Woori Technology nuclear I&C/MMIS: https://ssl.pstatic.net/imgstock/upload/research/company/1713913715116.pdf
- BHI nuclear power-plant references: https://www.bhi.co.kr/index.php?act=dispMemberLogout&listStyle=gallery&mid=e_menu_experiences_of_atomic

## 3. Stock-Web validation

Stock-Web manifest basis:

```yaml
source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
MFE_N_pct: max high from entry_date through N tradable rows / entry_price - 1
MAE_N_pct: min low from entry_date through N tradable rows / entry_price - 1
```

Profile/corporate-action check for this 180D window:

```yaml
034020: corporate_action_candidate_dates=[2019-05-29, 2020-02-18, 2020-12-24], 2024-07-18_to_180D_clean=true
052690: corporate_action_candidate_dates=[], 2024-07-18_to_180D_clean=true
051600: corporate_action_candidate_dates=[], 2024-07-18_to_180D_clean=true
105840: corporate_action_candidate_dates=[2012-11-19, 2012-12-11], 2024-07-18_to_180D_clean=true
032820: corporate_action_candidate_dates=[2003-10-28, 2005-06-07, 2007-07-03, 2007-07-31, 2009-07-29], 2024-07-18_to_180D_clean=true
011700: corporate_action_candidate_dates=[1998-06-15, 1998-11-06, 2006-05-09], 2024-07-18_to_180D_clean=true
083650: corporate_action_candidate_dates=[2006-06-16, 2006-07-12, 2015-04-10, 2015-05-12], 2024-07-18_to_180D_clean=true
```

## 4. Case-level interpretation

### Core rule tested

C04 should not treat `preferred bidder` as equal to `signed contract + workshare + revenue recognition`. The Czech event produced one broad macro headline, but the forward price paths separated into three buckets:

1. **Direct scope with later confirmation potential**: Doosan Enerbility, BHI, KEPCO KPS.
2. **Direct but legally/timing-sensitive**: KEPCO E&C.
3. **Indirect component/theme read-through**: Woojin, Woori Technology, Hanshin Machinery.

The mechanism is simple: nuclear projects are long steel bridges. Preferred-bidder news is the ceremony at the bridgehead; Stage3 needs evidence that load-bearing beams are actually being placed: signed contract, named workshare, delivery schedule, A/E or equipment contract, revenue recognition, and legal clearance. Without that, the crowd can run onto the bridge before the deck is bolted down.

### Price-path table

| symbol | name | role | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | drawdown_after_peak |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 034020 | 두산에너빌리티 | positive_with_4B_watch | 2024-07-18 | 21000 | 19.05 | -27.86 | 19.05 | -27.86 | 47.14 | -27.86 | 2025-02-19 | -35.40 |
| 052690 | 한국전력기술 | counterexample_legal_delay_high_MAE | 2024-07-18 | 82000 | 19.63 | -24.88 | 19.63 | -24.88 | 19.63 | -39.94 | 2024-07-18 | -49.80 |
| 051600 | 한전KPS | positive_low_MAE_service_bridge | 2024-07-18 | 38900 | 21.98 | -7.84 | 24.04 | -7.84 | 26.22 | -7.84 | 2024-12-03 | -22.61 |
| 105840 | 우진 | counterexample_component_optionality | 2024-07-18 | 9300 | 17.74 | -23.87 | 17.74 | -23.87 | 17.74 | -39.46 | 2024-07-18 | -48.58 |
| 032820 | 우리기술 | counterexample_control_system_optionality | 2024-07-18 | 2700 | 22.22 | -33.33 | 22.22 | -33.33 | 22.22 | -46.19 | 2024-07-18 | -55.97 |
| 011700 | 한신기계 | counterexample_theme_supplier | 2024-07-18 | 4585 | 14.94 | -32.82 | 14.94 | -33.91 | 14.94 | -48.53 | 2024-07-18 | -55.22 |
| 083650 | BHI | missed_structural_positive_with_4B_watch | 2024-07-18 | 8810 | 19.52 | -19.41 | 126.11 | -20.54 | 181.50 | -20.54 | 2025-02-14 | -38.43 |

## 5. Score / return alignment

| symbol | name | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | total | expected shadow stage |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 034020 | 두산에너빌리티 | 18 | 20 | 17 | 12 | 10 | 4 | 8 | 89 | Stage2-Actionable + local 4B watch |
| 052690 | 한국전력기술 | 12 | 17 | 12 | 13 | 10 | 3 | 7 | 74 | Stage2-Watch / 4B cap until A/E contract or final contract |
| 051600 | 한전KPS | 13 | 22 | 12 | 11 | 12 | 6 | 8 | 84 | Stage3-Yellow if maintenance scope/direct service bridge is confirmed |
| 105840 | 우진 | 8 | 13 | 10 | 12 | 8 | 3 | 6 | 60 | Stage2-Watch / component-optionality cap |
| 032820 | 우리기술 | 7 | 12 | 11 | 13 | 7 | 2 | 6 | 58 | Stage2-Watch / MMIS optionality cap |
| 011700 | 한신기계 | 6 | 9 | 8 | 14 | 6 | 2 | 5 | 50 | Stage2-Watch / indirect theme cap |
| 083650 | BHI | 18 | 18 | 16 | 16 | 12 | 4 | 7 | 91 | Stage3-Yellow + local 4B watch after fast MFE |

Interpretation:

- `034020` and `083650` show that C04 should not become too conservative. Direct equipment/workshare evidence can still produce very large 180D MFE, but the same rows require local 4B after fast price appreciation.
- `051600` is the cleanest low-MAE service-bridge row. Its MAE180 of `-7.8406%` is the control case for why maintenance/service visibility deserves a different gate from pure optionality.
- `052690`, `105840`, `032820`, and `011700` show that preferred-bidder enthusiasm without final contract / named vendor scope / delivery bridge can create Stage2 false positives or local blowoff rows with MAE180 between `-39.9390%` and `-48.5278%`.

Aggregate:

```yaml
avg_MFE_180D_pct: 47.0572
avg_MAE_180D_pct: -32.9081
rows_with_MAE180_below_minus_30pct: 4
rows_with_MFE180_above_40pct: 2
positive_case_count: 3
counterexample_count: 4
```

## 6. Residual contribution summary

```yaml
sector_specific_rule_candidate: L1_C04_NUCLEAR_PROJECT_DIRECT_WORKSHARE_LEGAL_CLEARANCE_GATE
canonical_archetype_rule_candidate: C04_NUCLEAR_POLICY_PROJECT_REQUIRES_FINAL_CONTRACT_WORKSHARE_REVENUE_BRIDGE_WITH_LEGAL_DELAY_4B_CAP
new_axis_proposed: C04_FINAL_CONTRACT_WORKSHARE_REVENUE_BRIDGE_AND_LEGAL_DELAY_4B_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
residual_error_found:
  - preferred_bidder_is_not_final_contract
  - direct_consortium_member_is_not_same_as_signed_revenue_scope
  - indirect_component_supplier_theme_requires_stricter_cap
  - direct_equipment_positive_must_not_be_overblocked_when later backlog/order evidence emerges
```

Proposed shadow rule:

```text
C04_NUCLEAR_POLICY_PROJECT_REQUIRES_FINAL_CONTRACT_WORKSHARE_REVENUE_BRIDGE_WITH_LEGAL_DELAY_4B_CAP
```

Rule detail:

```yaml
Stage2_Actionable_allowed_when:
  - sovereign_or_utility_preferred_bidder_event
  - named consortium member or clear nuclear value-chain role
  - non-price evidence dated at or before trigger date
Stage3_Yellow_allowed_when_two_or_more:
  - final contract or A/E/equipment/maintenance contract signed
  - named workshare or consortium responsibility is public
  - delivery schedule / revenue recognition window visible
  - margin or backlog bridge visible
  - legal/procurement challenge substantially cleared
local_4B_watch_required_when_any:
  - peak occurs on entry day and MAE90/180 exceeds -25%
  - legal appeal/procurement injunction remains within forward window
  - company is indirect theme supplier without named project order
  - project news produces fast MFE but not signed revenue bridge
hard_4C_required_only_when:
  - tender cancellation, final disqualification, or binding contract loss is confirmed
```

## 7. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "schema_version": "v12_stock_web_residual_research", "selected_round": "R1", "selected_loop": 113, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout", "symbol": "034020", "name": "두산에너빌리티", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 21000.0, "trigger_type": "Stage2-Actionable", "case_role": "positive_with_4B_watch", "evidence_family": "Czech preferred bidder + direct reactor/component workshare + legal-overhang buffer", "MFE_30D_pct": 19.0476, "MAE_30D_pct": -27.8571, "MFE_90D_pct": 19.0476, "MAE_90D_pct": -27.8571, "MFE_180D_pct": 47.1429, "MAE_180D_pct": -27.8571, "peak_date": "2025-02-19", "peak_price": 30900.0, "drawdown_after_peak_pct": -35.4045, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "price_source": "Songdaiki/stock-web tradable_raw raw_unadjusted_marcap", "expected_shadow_stage": "Stage2-Actionable + local 4B watch", "raw_component_scores": {"eps_fcf_explosion": 18, "earnings_visibility": 20, "bottleneck_pricing": 17, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 4, "information_confidence": 8, "total": 89}, "current_profile_error_flag": true, "source_proxy_only": false, "evidence_url_pending": false, "reuse_reason": "new trigger-family or C04 quality holdout row; not counted as duplicate because symbol+trigger framing is project-legal-delay directness split", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual_research", "selected_round": "R1", "selected_loop": 113, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout", "symbol": "052690", "name": "한국전력기술", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 82000.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_legal_delay_high_MAE", "evidence_family": "Czech preferred bidder + engineering workshare + missing signed A/E revenue bridge", "MFE_30D_pct": 19.6341, "MAE_30D_pct": -24.878, "MFE_90D_pct": 19.6341, "MAE_90D_pct": -24.878, "MFE_180D_pct": 19.6341, "MAE_180D_pct": -39.939, "peak_date": "2024-07-18", "peak_price": 98100.0, "drawdown_after_peak_pct": -49.7961, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "price_source": "Songdaiki/stock-web tradable_raw raw_unadjusted_marcap", "expected_shadow_stage": "Stage2-Watch / 4B cap until A/E contract or final contract", "raw_component_scores": {"eps_fcf_explosion": 12, "earnings_visibility": 17, "bottleneck_pricing": 12, "market_mispricing": 13, "valuation_rerating": 10, "capital_allocation": 3, "information_confidence": 7, "total": 74}, "current_profile_error_flag": true, "source_proxy_only": false, "evidence_url_pending": false, "reuse_reason": "new trigger-family or C04 quality holdout row; not counted as duplicate because symbol+trigger framing is project-legal-delay directness split", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual_research", "selected_round": "R1", "selected_loop": 113, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout", "symbol": "051600", "name": "한전KPS", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 38900.0, "trigger_type": "Stage3-Yellow", "case_role": "positive_low_MAE_service_bridge", "evidence_family": "Czech preferred bidder + consortium member + nuclear maintenance service bridge", "MFE_30D_pct": 21.9794, "MAE_30D_pct": -7.8406, "MFE_90D_pct": 24.036, "MAE_90D_pct": -7.8406, "MFE_180D_pct": 26.2211, "MAE_180D_pct": -7.8406, "peak_date": "2024-12-03", "peak_price": 49100.0, "drawdown_after_peak_pct": -22.6069, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "price_source": "Songdaiki/stock-web tradable_raw raw_unadjusted_marcap", "expected_shadow_stage": "Stage3-Yellow if maintenance scope/direct service bridge is confirmed", "raw_component_scores": {"eps_fcf_explosion": 13, "earnings_visibility": 22, "bottleneck_pricing": 12, "market_mispricing": 11, "valuation_rerating": 12, "capital_allocation": 6, "information_confidence": 8, "total": 84}, "current_profile_error_flag": false, "source_proxy_only": false, "evidence_url_pending": false, "reuse_reason": "new trigger-family or C04 quality holdout row; not counted as duplicate because symbol+trigger framing is project-legal-delay directness split", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual_research", "selected_round": "R1", "selected_loop": 113, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout", "symbol": "105840", "name": "우진", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 9300.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_component_optionality", "evidence_family": "nuclear instrumentation exposure + Czech project read-through without named order", "MFE_30D_pct": 17.7419, "MAE_30D_pct": -23.871, "MFE_90D_pct": 17.7419, "MAE_90D_pct": -23.871, "MFE_180D_pct": 17.7419, "MAE_180D_pct": -39.4624, "peak_date": "2024-07-18", "peak_price": 10950.0, "drawdown_after_peak_pct": -48.5845, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "price_source": "Songdaiki/stock-web tradable_raw raw_unadjusted_marcap", "expected_shadow_stage": "Stage2-Watch / component-optionality cap", "raw_component_scores": {"eps_fcf_explosion": 8, "earnings_visibility": 13, "bottleneck_pricing": 10, "market_mispricing": 12, "valuation_rerating": 8, "capital_allocation": 3, "information_confidence": 6, "total": 60}, "current_profile_error_flag": true, "source_proxy_only": false, "evidence_url_pending": false, "reuse_reason": "new trigger-family or C04 quality holdout row; not counted as duplicate because symbol+trigger framing is project-legal-delay directness split", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual_research", "selected_round": "R1", "selected_loop": 113, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout", "symbol": "032820", "name": "우리기술", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 2700.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_control_system_optionality", "evidence_family": "MMIS / nuclear control-system exposure + project read-through without contract bridge", "MFE_30D_pct": 22.2222, "MAE_30D_pct": -33.3333, "MFE_90D_pct": 22.2222, "MAE_90D_pct": -33.3333, "MFE_180D_pct": 22.2222, "MAE_180D_pct": -46.1852, "peak_date": "2024-07-18", "peak_price": 3300.0, "drawdown_after_peak_pct": -55.9697, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "price_source": "Songdaiki/stock-web tradable_raw raw_unadjusted_marcap", "expected_shadow_stage": "Stage2-Watch / MMIS optionality cap", "raw_component_scores": {"eps_fcf_explosion": 7, "earnings_visibility": 12, "bottleneck_pricing": 11, "market_mispricing": 13, "valuation_rerating": 7, "capital_allocation": 2, "information_confidence": 6, "total": 58}, "current_profile_error_flag": true, "source_proxy_only": false, "evidence_url_pending": false, "reuse_reason": "new trigger-family or C04 quality holdout row; not counted as duplicate because symbol+trigger framing is project-legal-delay directness split", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual_research", "selected_round": "R1", "selected_loop": 113, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout", "symbol": "011700", "name": "한신기계", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 4585.0, "trigger_type": "Stage2-Actionable", "case_role": "counterexample_theme_supplier", "evidence_family": "nuclear compressor supplier theme + no project-level order evidence", "MFE_30D_pct": 14.94, "MAE_30D_pct": -32.8244, "MFE_90D_pct": 14.94, "MAE_90D_pct": -33.9149, "MFE_180D_pct": 14.94, "MAE_180D_pct": -48.5278, "peak_date": "2024-07-18", "peak_price": 5270.0, "drawdown_after_peak_pct": -55.2182, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "price_source": "Songdaiki/stock-web tradable_raw raw_unadjusted_marcap", "expected_shadow_stage": "Stage2-Watch / indirect theme cap", "raw_component_scores": {"eps_fcf_explosion": 6, "earnings_visibility": 9, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 6, "capital_allocation": 2, "information_confidence": 5, "total": 50}, "current_profile_error_flag": true, "source_proxy_only": false, "evidence_url_pending": false, "reuse_reason": "new trigger-family or C04 quality holdout row; not counted as duplicate because symbol+trigger framing is project-legal-delay directness split", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "schema_version": "v12_stock_web_residual_research", "selected_round": "R1", "selected_loop": 113, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout", "symbol": "083650", "name": "BHI", "trigger_date": "2024-07-17", "entry_date": "2024-07-18", "entry_price": 8810.0, "trigger_type": "Stage3-Yellow", "case_role": "missed_structural_positive_with_4B_watch", "evidence_family": "nuclear BOP / project reference + broader power equipment order-cycle rerating", "MFE_30D_pct": 19.5233, "MAE_30D_pct": -19.4098, "MFE_90D_pct": 126.1067, "MAE_90D_pct": -20.5448, "MFE_180D_pct": 181.4983, "MAE_180D_pct": -20.5448, "peak_date": "2025-02-14", "peak_price": 24800.0, "drawdown_after_peak_pct": -38.4274, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "price_source": "Songdaiki/stock-web tradable_raw raw_unadjusted_marcap", "expected_shadow_stage": "Stage3-Yellow + local 4B watch after fast MFE", "raw_component_scores": {"eps_fcf_explosion": 18, "earnings_visibility": 18, "bottleneck_pricing": 16, "market_mispricing": 16, "valuation_rerating": 12, "capital_allocation": 4, "information_confidence": 7, "total": 91}, "current_profile_error_flag": true, "source_proxy_only": false, "evidence_url_pending": false, "reuse_reason": "new trigger-family or C04 quality holdout row; not counted as duplicate because symbol+trigger framing is project-legal-delay directness split", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

## 8. Machine-readable aggregate row

```json
{
  "row_type": "aggregate",
  "schema_version": "v12_stock_web_residual_research",
  "selected_round": "R1",
  "selected_loop": 113,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "mixed_C04_czech_nuclear_preferred_bidder_legal_delay_directness_holdout",
  "new_independent_case_count": 7,
  "reused_case_count": 0,
  "positive_case_count": 3,
  "counterexample_count": 4,
  "local_4B_watch_count": 6,
  "4C_case_count": 0,
  "current_profile_error_count": 6,
  "avg_MFE_180D_pct": 47.0572,
  "avg_MAE_180D_pct": -32.9081,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "ready_for_batch_ingest": true
}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation coding agent for stock_agent. Do not treat this research MD as an instruction to patch production scoring immediately. Ingest this file together with the other v12 research MD files. Parse the JSONL trigger rows and the aggregate row. Validate that all rows have canonical_archetype_id=C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, selected_round=R1, large_sector_id=L1_INDUSTRIALS_INFRA_DEFENSE_GRID, entry_date, entry_price, and complete MFE/MAE 30D/90D/180D fields. Then evaluate whether a shadow rule named C04_NUCLEAR_POLICY_PROJECT_REQUIRES_FINAL_CONTRACT_WORKSHARE_REVENUE_BRIDGE_WITH_LEGAL_DELAY_4B_CAP should be added as a C04-specific guardrail. Do not apply a global rule. Do not change production scoring unless the aggregate batch promotion process approves the patch.
```

## 10. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 7
calibration_usable_rows: 7
representative_rows: 7
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 11. Next research state

```text
completed_round = R1
completed_loop = 113
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality holdout after current-session Priority-0/Priority-1 fills; static C04 rows=71
next_recommended_archetypes = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_quality_holdout | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_holdout_only_if_new_legal_clearance_or_final_contract_path | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

This loop adds 7 independent C04 holdout cases, 4 counterexamples, and 6 residual errors for R1/L1/C04.
