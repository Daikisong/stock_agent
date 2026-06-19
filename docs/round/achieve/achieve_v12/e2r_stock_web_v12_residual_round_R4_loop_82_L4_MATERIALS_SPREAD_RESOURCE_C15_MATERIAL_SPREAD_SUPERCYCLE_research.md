# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R4
selected_loop = 82
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 URL/proxy/MFE-MAE repair
round_schedule_status = coverage_index_selected; local C15 max loop 81 -> selected loop 82; 직전 C10 loop 220 반복 회피
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD
loop_objective = counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression
price_source = Songdaiki/stock-web / atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
output_file = e2r_stock_web_v12_residual_round_R4_loop_82_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

This loop adds 8 new independent cases, 5 counterexamples, and 8 residual errors for L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE. The selected loop follows the local C15 archive through loop 81 and avoids the immediately previous C10 loop 220.

## 1. Current Calibrated Profile Assumption

The stress-test reference is `e2r_2_2_rolling_calibrated_proxy`, with rollback comparison to `e2r_2_0_baseline_reference`. No production score is changed. The exercise is a shadow-only C15 canonical-archetype rule candidate.

Already-applied axes tested here: `stage2_required_bridge`, `stage3_green_revision_min_by_margin_cash_freshness`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R4`
- large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`
- canonical_archetype_id: `C15_MATERIAL_SPREAD_SUPERCYCLE`
- fine_archetype_id: `C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD`
- valid mapping: `C15~C17 -> R4 / L4`

Scope boundary: this is not a live scan and not an investment recommendation. It is a historical trigger-level calibration file using already-observed evidence and Stock-Web OHLC paths.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index marks C15 as a Priority 1 quality target for spread reversal and inventory-cycle counterexample reinforcement. Local C15 files through loop 81 were checked. The hard key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All eight representative trigger rows are new hard keys under C15. Strict-new local C15 symbols in this file: `001780, 001940, 006110, 007280, 007690, 009200, 021050, 213500`. The loop rotates away from the prior steel/cement/copper theme-spike sets into aluminum, paper/pulp, epoxy, copper rolling, and rebar spread/pass-through cases.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "manifest_max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "tradable_columns": ["d", "o", "h", "l", "c", "v", "a", "mc", "s", "m"]
}
```

The entry OHLC row is the `c` column close on the first Stock-Web tradable row at or after `trigger_date`. MFE/MAE are calculated by max high and min low from entry row through 30/90/180 tradable rows. The `s` shares column was screened for 20%+ share-count discontinuity over the 180D window.

## 5. Historical Eligibility Gate

All representative trigger rows pass:

- historical trigger date only
- actual Stock-Web tradable entry row exists
- 180 forward tradable rows are available before manifest max date `2026-02-20`
- positive OHLCV values
- complete 30D / 90D / 180D MFE and MAE
- 180D corporate-action contamination screen clean under the 20% share-count threshold

## 6. Canonical Archetype Compression Map

C15 is compressed as:

```text
commodity weather / raw-material headline
  -> product price or ASP pass-through
  -> demand, customer, or shipment route
  -> realized margin/cash conversion
  -> inventory-lag and price-phase sanity
```

A raw-material headline is only the gauge needle moving. The calibration question is whether pressure reaches the issuer's income statement before the price cycle exhausts itself.

## 7. Case Selection Summary

| case_id | symbol | company | trigger_date | entry_date | trigger_type | role | MFE90 | MAE90 | MFE180 | MAE180 | evidence_family |
|---|---:|---|---|---|---|---|---:|---:|---:|---:|---|
| C15-L82-01 | 006110 | 삼아알미늄 | 2021-09-09 | 2021-09-09 | Stage4B | counterexample | 10.65 | -37.07 | 10.65 | -39.28 | aluminum_supercycle_without_confirmed_passthrough |
| C15-L82-02 | 001780 | 알루코 | 2021-09-09 | 2021-09-09 | Stage4B | counterexample | 7.61 | -39.09 | 7.61 | -39.09 | aluminum_extrusion_proxy_theme_spike |
| C15-L82-03 | 021050 | 서원 | 2021-12-29 | 2021-12-29 | Stage2-Actionable | counterexample | 15.54 | -13.21 | 15.54 | -34.72 | copper_roll_margin_positive_but_cycle_late |
| C15-L82-04 | 213500 | 한솔제지 | 2022-04-20 | 2022-04-20 | Stage2-Actionable | positive | 6.51 | -15.75 | 20.21 | -16.44 | paper_price_hike_cost_passthrough_positive |
| C15-L82-05 | 009200 | 무림페이퍼 | 2022-04-20 | 2022-04-20 | Stage4B | positive | 34.91 | -27.99 | 34.91 | -36.01 | paper_price_hike_early_mfe_then_peak_risk |
| C15-L82-06 | 007690 | 국도화학 | 2021-09-09 | 2021-09-09 | Stage3-Green | counterexample | 4.4 | -43.4 | 4.4 | -43.4 | epoxy_price_spread_record_result_late_green_trap |
| C15-L82-07 | 001940 | KISCO홀딩스 | 2022-01-20 | 2022-01-20 | Stage2-Actionable | positive | 23.84 | -7.95 | 23.84 | -21.19 | rebar_spread_margin_positive_but_holding_proxy_discount |
| C15-L82-08 | 007280 | 한국특강 | 2022-10-07 | 2022-10-07 | Stage4B | counterexample | 1.33 | -18.81 | 1.33 | -18.81 | rebar_capacity_addition_supply_demand_reversal |


## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `5`
- 4B/watch or phase-cap cases: `4`
- current_profile_error_count: `8`

The positives are not simple Green proofs. They are cases where an issuer-level pass-through bridge or margin route existed and the price path gave enough MFE to justify Stage2-Actionable or Yellow support. The counterexamples show that aluminum/copper/epoxy/steel headlines can become local-peak traps when inventory lag, pass-through, demand, or phase is ignored.

## 9. Evidence Source Map

| case_id | source | evidence note |
|---|---|---|
| C15-L82-01 | https://v.daum.net/v/kqcRDsSWEX?f=p | 국제 알루미늄 10년래 고가와 조일·삼아알미늄 급등. 원재료/전기차 수요 headline은 있었지만 entry가 local peak에 가까웠다. |
| C15-L82-02 | https://v.daum.net/v/kqcRDsSWEX?f=p | 알루미늄 가격 급등과 친환경 수요 headline은 broad proxy였고, 알루코 issuer-level spread/margin bridge는 직접 확인되지 않았다. |
| C15-L82-03 | https://www.hankyung.com/article/2021122925651 | 구리 가격 상승이 구리 가공기업 roll-margin을 키운다는 설명과 서원 실적 개선 전망이 있었다. 그러나 180D에는 깊은 MAE가 발생했다. |
| C15-L82-04 | https://www.newspim.com/news/view/20220420000994 | 한솔제지·무림페이퍼가 국제 펄프가격과 해상운임 급등을 이유로 5월 1일부터 인쇄용지 가격 15% 인상을 결정했다. |
| C15-L82-05 | https://www.newspim.com/news/view/20220420000994 | 동일한 종이가격 인상 event에서 초기 MFE는 컸으나 peak 이후 drawdown도 컸다. price hike pass-through와 4B phase guard를 동시에 검증한다. |
| C15-L82-06 | https://www.hanwhawm.com/main/common/common_file/fileView.cmd?bldid=bbs10031&category=2&depth3_id=anls1&key1=56534&key2=1 | 2Q21 영업이익 급증과 epoxy 가격 상승, 조선·건설·풍력 수요 개선이 제시됐지만 trigger 직후가 고점권이었다. |
| C15-L82-07 | https://www.snmnews.com/news/articleView.html?idxno=489529 | 한국철강의 철근 스프레드 확대와 4Q21 높은 수익성 지속 전망은 KISCO 그룹 look-through spread bridge를 만들었다. holding proxy discount는 필요하다. |
| C15-L82-08 | https://www.steelin.co.kr/news/articleView.html?idxno=7951 | 철근 시장은 수요 감소와 공급능력 증가가 맞물리는 부정적 국면으로 진입했고 한국특강의 100만톤 생산능력은 기존 최적화 질서의 변수였다. |


## 10. Price Data Source Map

| case_id | symbol | entry_date | open | high | low | close | volume | peak_date | peak_price | drawdown_after_peak_pct | share_count_change_180D |
|---|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| C15-L82-01 | 006110 | 2021-09-09 | 39500.0 | 40000.0 | 35550.0 | 36150.0 | 1927952 | 2021-09-09 | 40000.0 | -45.13 | 0.0% |
| C15-L82-02 | 001780 | 2021-09-09 | 4935.0 | 5110.0 | 4865.0 | 4925.0 | 3681323 | 2022-01-17 | 5300.0 | -38.87 | 7.3% |
| C15-L82-03 | 021050 | 2021-12-29 | 1920.0 | 1940.0 | 1905.0 | 1930.0 | 153491 | 2022-03-04 | 2230.0 | -43.5 | 0.0% |
| C15-L82-04 | 213500 | 2022-04-20 | 14300.0 | 14650.0 | 14100.0 | 14600.0 | 191934 | 2022-09-19 | 17550.0 | -30.48 | 0.0% |
| C15-L82-05 | 009200 | 2022-04-20 | 2985.0 | 3270.0 | 2985.0 | 3180.0 | 3901243 | 2022-04-26 | 4290.0 | -52.56 | 0.0% |
| C15-L82-06 | 007690 | 2021-09-09 | 85900.0 | 89500.0 | 83400.0 | 88700.0 | 498742 | 2021-09-10 | 92600.0 | -45.79 | 0.0% |
| C15-L82-07 | 001940 | 2022-01-20 | 14750.0 | 15150.0 | 14600.0 | 15100.0 | 15742 | 2022-05-03 | 18700.0 | -36.36 | 12.45% |
| C15-L82-08 | 007280 | 2022-10-07 | 2200.0 | 2290.0 | 2180.0 | 2260.0 | 35720 | 2022-10-07 | 2290.0 | -19.87 | 0.0% |


## 11. Case-by-Case Trigger Grid

### C15-L82-01 — 006110 삼아알미늄
Aluminum supercycle evidence was visible, but the entry row itself was close to the observed 180D peak. MFE90 was only `10.65%` while MAE90 was `-37.07%`. The current profile can over-credit a raw commodity headline as Actionable; the shadow ladder caps it as Stage4B/local watch unless issuer-level pass-through and fresh margin evidence exist.

### C15-L82-02 — 001780 알루코
Aluminum exposure was more indirect than Sam-A. The same macro headline produced a proxy theme rather than a direct foil/margin bridge. MFE180 was `7.61%` and MAE180 was `-39.09%`, so the row is a proxy-stage cap counterexample.

### C15-L82-03 — 021050 서원
The copper roll-margin thesis had issuer relevance, but the later 180D low was deep. MFE90 `15.54%` was not enough to compensate for MAE180 `-34.72%`. The case keeps a Stage2 watch/Actionable bridge only when position-size and phase risk are explicit.

### C15-L82-04 — 213500 한솔제지
The paper price hike was an issuer-level pass-through event rather than just commodity weather. MFE180 reached `20.21%` with MAE180 `-16.44%`. This supports Stage2-Actionable but still requires margin/cash freshness before Green.

### C15-L82-05 — 009200 무림페이퍼
The same paper price hike produced a large early MFE but also a full-cycle drawdown after the local peak. This is a 4B overlay success: C15 should capture the pass-through event, but full positive promotion without phase guard is too loose.

### C15-L82-06 — 007690 국도화학
The epoxy result/spread evidence looked strong enough for Green on paper, but the entry came at a late phase. MFE90 `4.4%` and MAE90 `-43.4%` make this a result-only Green trap.

### C15-L82-07 — 001940 KISCO홀딩스
The rebar spread thesis was real at the operating-company level, and the path produced MFE90 `23.84%`. Because this is a holding-company look-through route, it receives a proxy discount rather than a full Green promotion.

### C15-L82-08 — 007280 한국특강
The October 2022 evidence was a supply/demand reversal warning rather than a pass-through success. MFE180 was only `1.33%`, while the stock spent much of the window below entry. This is an early Stage4B/watch row, not a positive spread bridge.

## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | below30 | below90 | current_profile_verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| C15-L82-01 | 006110 | 10.65 | -28.77 | 10.65 | -37.07 | 10.65 | -39.28 | True | True | current_profile_false_positive |
| C15-L82-02 | 001780 | 3.96 | -19.19 | 7.61 | -39.09 | 7.61 | -39.09 | True | True | current_profile_false_positive |
| C15-L82-03 | 021050 | 8.29 | -13.21 | 15.54 | -13.21 | 15.54 | -34.72 | True | True | current_profile_false_positive |
| C15-L82-04 | 213500 | 4.45 | -8.56 | 6.51 | -15.75 | 20.21 | -16.44 | True | True | current_profile_too_late |
| C15-L82-05 | 009200 | 34.91 | -11.16 | 34.91 | -27.99 | 34.91 | -36.01 | True | True | current_profile_4B_too_late |
| C15-L82-06 | 007690 | 4.4 | -23.68 | 4.4 | -43.4 | 4.4 | -43.4 | True | True | current_profile_false_positive |
| C15-L82-07 | 001940 | 10.6 | -7.95 | 23.84 | -7.95 | 23.84 | -21.19 | True | True | current_profile_too_late |
| C15-L82-08 | 007280 | 1.33 | -7.52 | 1.33 | -18.81 | 1.33 | -18.81 | True | True | current_profile_false_positive |


## 13. Current Calibrated Profile Stress Test

The current profile is mostly correct about requiring a bridge, but C15 still has two residual traps. First, raw commodity headlines can masquerade as issuer-level pass-through. Second, result evidence can arrive after the price already consumed most of the upside. Under the current proxy, `8` of `8` rows are false positive, too late, or 4B timing errors.

## 14. Stage2 / Yellow / Green Comparison

- Stage2-watch should be allowed for broad commodity weather.
- Stage2-Actionable requires product price, customer route, or issuer-specific pass-through.
- Stage3-Yellow requires realized margin or visible cash/working-capital conversion.
- Stage3-Green requires fresh forward spread visibility, not merely record results from a completed spread cycle.

## 15. 4B Local vs Full-window Timing Audit

Aluminum and epoxy entries show local-peak risk: high non-price narrative quality did not protect from deep MAE because the evidence arrived near or after the theme spike. Paper and rebar rows show the opposite: early pass-through can work, but the local peak must be treated as 4B overlay once MFE is realized.

## 16. 4C Protection Audit

No row requires a hard Stage4C thesis-death route. Even high-MAE rows are mostly pass-through failure or phase error, not confirmed business death. This weakens hard-4C routing for C15 rows where a customer/product route survives.

## 17. Sector-Specific Rule Candidate

`L4 material-spread rows should split commodity weather, product price/pass-through, inventory-cost lag, demand/customer route, realized margin/cash conversion, and price phase. A raw-material headline is only the gauge; calibration should check whether pressure reaches the issuer's income statement.`

## 18. Canonical-Archetype Rule Candidate

`C15 should use a multi-material pass-through ladder: raw commodity move -> Stage2-watch; product price or customer route -> Stage2-Actionable; realized margin/cash with forward spread freshness -> Yellow/Green; stale result after theme rerating -> 4B-watch; high-MAE without route death -> watch/phase cap, not hard 4C.`

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false-positive or misroute count | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2 rolling proxy | 8 | 13.1 | -25.41 | 14.81 | -31.12 | 8 | over-credits commodity/proxy headlines |
| P2 C15 pass-through inventory phase guard | 8 | 13.1 | -25.41 | 14.81 | -31.12 | 2 | better label/phase alignment |

## 20. Score-Return Alignment Matrix

The proposed shadow profile does not change production scoring. It changes interpretation: lower credit for raw commodity visibility without pass-through; higher information/capital-risk weight for inventory lag, product-price finality, and phase.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD | 3 | 5 | 4 | 0 | 8 | 0 | 8 | 8 | 8 | yes | yes | C15 pass-through/freshness/phase guard strengthened; no hard 4C added |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge; local_4b_watch_guard; stage3_green_revision_min_by_margin_cash_freshness; hard_4c_confirmation
residual_error_types_found: raw_commodity_proxy_false_positive; result_only_green_trap; inventory_lag_or_passthrough_missing; high_mae_live_bridge_not_hard4c
new_axis_proposed: c15_multimaterial_passthrough_inventory_phase_guard
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; stage3_green_revision_min_by_margin_cash_freshness
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c qualified for high-MAE C15 rows without route death
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L4 commodity weather must be separated from issuer pass-through and cash conversion.
canonical_archetype_rule_candidate: C15 multi-material pass-through ladder.
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical event timing, Stock-Web tradable entry row, 30/90/180D MFE/MAE, 180D forward availability, share-count contamination screen, duplicate-key avoidance against local C15 loop 72~81 files.

Not validated: live current suitability, future prediction, brokerage execution, production scoring code, or full DART financial restatement audit.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_multimaterial_passthrough_inventory_phase_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,20/12/20/10/10/8/20,20/10/18/10/10/10/22,"Visibility -2; Bottleneck -2; Capital +2; Info +2","Discount raw commodity and proxy headlines unless pass-through/margin/cash bridge exists","Reduced false-positive promotion in aluminum, copper, epoxy and rebar proxy rows","C15-L82-01-T1|C15-L82-02-T1|C15-L82-03-T1|C15-L82-04-T1|C15-L82-05-T1|C15-L82-06-T1|C15-L82-07-T1|C15-L82-08-T1",8,8,5,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C15-L82-01", "symbol": "006110", "company_name": "삼아알미늄", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "국제 알루미늄 10년래 고가와 조일·삼아알미늄 급등. 원재료/전기차 수요 headline은 있었지만 entry가 local peak에 가까웠다."}
{"row_type": "trigger", "trigger_id": "C15-L82-01-T1", "case_id": "C15-L82-01", "symbol": "006110", "company_name": "삼아알미늄", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2021-09-09", "evidence_available_at_that_date": "국제 알루미늄 10년래 고가와 조일·삼아알미늄 급등. 원재료/전기차 수요 headline은 있었지만 entry가 local peak에 가까웠다.", "evidence_source": "https://v.daum.net/v/kqcRDsSWEX?f=p", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2021.csv", "profile_path": "atlas/symbol_profiles/006/006110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-09", "entry_price": 36150.0, "MFE_30D_pct": 10.65, "MFE_90D_pct": 10.65, "MFE_180D_pct": 10.65, "MFE_1Y_pct": 10.65, "MFE_2Y_pct": null, "MAE_30D_pct": -28.77, "MAE_90D_pct": -37.07, "MAE_180D_pct": -39.28, "MAE_1Y_pct": -56.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-09-09", "peak_price": 40000.0, "drawdown_after_peak_pct": -45.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_or_phase_cap_required", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "aluminum_supercycle_without_confirmed_passthrough", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:006110:2021-09-09", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-01", "trigger_id": "C15-L82-01-T1", "symbol": "006110", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 4}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 4, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 12, "pass_through_score": 2}, "weighted_score_after": 56, "stage_label_after": "Stage4B", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 10.65, "MAE_90D_pct": -37.07, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "C15-L82-02", "symbol": "001780", "company_name": "알루코", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "알루미늄 가격 급등과 친환경 수요 headline은 broad proxy였고, 알루코 issuer-level spread/margin bridge는 직접 확인되지 않았다."}
{"row_type": "trigger", "trigger_id": "C15-L82-02-T1", "case_id": "C15-L82-02", "symbol": "001780", "company_name": "알루코", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2021-09-09", "evidence_available_at_that_date": "알루미늄 가격 급등과 친환경 수요 headline은 broad proxy였고, 알루코 issuer-level spread/margin bridge는 직접 확인되지 않았다.", "evidence_source": "https://v.daum.net/v/kqcRDsSWEX?f=p", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001780/2021.csv", "profile_path": "atlas/symbol_profiles/001/001780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-09", "entry_price": 4925.0, "MFE_30D_pct": 3.96, "MFE_90D_pct": 7.61, "MFE_180D_pct": 7.61, "MFE_1Y_pct": 7.61, "MFE_2Y_pct": null, "MAE_30D_pct": -19.19, "MAE_90D_pct": -39.09, "MAE_180D_pct": -39.09, "MAE_1Y_pct": -44.16, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-17", "peak_price": 5300.0, "drawdown_after_peak_pct": -38.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_or_phase_cap_required", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "aluminum_extrusion_proxy_theme_spike", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:001780:2021-09-09", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-02", "trigger_id": "C15-L82-02-T1", "symbol": "001780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 4}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 4, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 12, "pass_through_score": 2}, "weighted_score_after": 54, "stage_label_after": "Stage4B", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 7.61, "MAE_90D_pct": -39.09, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "C15-L82-03", "symbol": "021050", "company_name": "서원", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "구리 가격 상승이 구리 가공기업 roll-margin을 키운다는 설명과 서원 실적 개선 전망이 있었다. 그러나 180D에는 깊은 MAE가 발생했다."}
{"row_type": "trigger", "trigger_id": "C15-L82-03-T1", "case_id": "C15-L82-03", "symbol": "021050", "company_name": "서원", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-12-29", "evidence_available_at_that_date": "구리 가격 상승이 구리 가공기업 roll-margin을 키운다는 설명과 서원 실적 개선 전망이 있었다. 그러나 180D에는 깊은 MAE가 발생했다.", "evidence_source": "https://www.hankyung.com/article/2021122925651", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/021/021050/2021.csv", "profile_path": "atlas/symbol_profiles/021/021050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-12-29", "entry_price": 1930.0, "MFE_30D_pct": 8.29, "MFE_90D_pct": 15.54, "MFE_180D_pct": 15.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.21, "MAE_90D_pct": -13.21, "MAE_180D_pct": -34.72, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-04", "peak_price": 2230.0, "drawdown_after_peak_pct": -43.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "copper_roll_margin_positive_but_cycle_late", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:021050:2021-12-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-03", "trigger_id": "C15-L82-03-T1", "symbol": "021050", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 4}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 4, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 12, "pass_through_score": 2}, "weighted_score_after": 65, "stage_label_after": "Stage2", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 15.54, "MAE_90D_pct": -13.21, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "C15-L82-04", "symbol": "213500", "company_name": "한솔제지", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "한솔제지·무림페이퍼가 국제 펄프가격과 해상운임 급등을 이유로 5월 1일부터 인쇄용지 가격 15% 인상을 결정했다."}
{"row_type": "trigger", "trigger_id": "C15-L82-04-T1", "case_id": "C15-L82-04", "symbol": "213500", "company_name": "한솔제지", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-04-20", "evidence_available_at_that_date": "한솔제지·무림페이퍼가 국제 펄프가격과 해상운임 급등을 이유로 5월 1일부터 인쇄용지 가격 15% 인상을 결정했다.", "evidence_source": "https://www.newspim.com/news/view/20220420000994", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": ["margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/213/213500/2022.csv", "profile_path": "atlas/symbol_profiles/213/213500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-20", "entry_price": 14600.0, "MFE_30D_pct": 4.45, "MFE_90D_pct": 6.51, "MFE_180D_pct": 20.21, "MFE_1Y_pct": 20.21, "MFE_2Y_pct": null, "MAE_30D_pct": -8.56, "MAE_90D_pct": -15.75, "MAE_180D_pct": -16.44, "MAE_1Y_pct": -24.86, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-09-19", "peak_price": 17550.0, "drawdown_after_peak_pct": -30.48, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "paper_price_hike_cost_passthrough_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:213500:2022-04-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-04", "trigger_id": "C15-L82-04-T1", "symbol": "213500", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 12}, "weighted_score_before": 71, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 14}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 6.51, "MAE_90D_pct": -15.75, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "case", "case_id": "C15-L82-05", "symbol": "009200", "company_name": "무림페이퍼", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "동일한 종이가격 인상 event에서 초기 MFE는 컸으나 peak 이후 drawdown도 컸다. price hike pass-through와 4B phase guard를 동시에 검증한다."}
{"row_type": "trigger", "trigger_id": "C15-L82-05-T1", "case_id": "C15-L82-05", "symbol": "009200", "company_name": "무림페이퍼", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2022-04-20", "evidence_available_at_that_date": "동일한 종이가격 인상 event에서 초기 MFE는 컸으나 peak 이후 drawdown도 컸다. price hike pass-through와 4B phase guard를 동시에 검증한다.", "evidence_source": "https://www.newspim.com/news/view/20220420000994", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": ["margin_bridge"], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009200/2022.csv", "profile_path": "atlas/symbol_profiles/009/009200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-20", "entry_price": 3180.0, "MFE_30D_pct": 34.91, "MFE_90D_pct": 34.91, "MFE_180D_pct": 34.91, "MFE_1Y_pct": 34.91, "MFE_2Y_pct": null, "MAE_30D_pct": -11.16, "MAE_90D_pct": -27.99, "MAE_180D_pct": -36.01, "MAE_1Y_pct": -36.01, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-26", "peak_price": 4290.0, "drawdown_after_peak_pct": -52.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_or_phase_cap_required", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "paper_price_hike_early_mfe_then_peak_risk", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:009200:2022-04-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-05", "trigger_id": "C15-L82-05-T1", "symbol": "009200", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 12}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 14}, "weighted_score_after": 70, "stage_label_after": "Stage4B", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 34.91, "MAE_90D_pct": -27.99, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "case", "case_id": "C15-L82-06", "symbol": "007690", "company_name": "국도화학", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "Stage3-Green", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2Q21 영업이익 급증과 epoxy 가격 상승, 조선·건설·풍력 수요 개선이 제시됐지만 trigger 직후가 고점권이었다."}
{"row_type": "trigger", "trigger_id": "C15-L82-06-T1", "case_id": "C15-L82-06", "symbol": "007690", "company_name": "국도화학", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2021-09-09", "evidence_available_at_that_date": "2Q21 영업이익 급증과 epoxy 가격 상승, 조선·건설·풍력 수요 개선이 제시됐지만 trigger 직후가 고점권이었다.", "evidence_source": "https://www.hanwhawm.com/main/common/common_file/fileView.cmd?bldid=bbs10031&category=2&depth3_id=anls1&key1=56534&key2=1", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007690/2021.csv", "profile_path": "atlas/symbol_profiles/007/007690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-09", "entry_price": 88700.0, "MFE_30D_pct": 4.4, "MFE_90D_pct": 4.4, "MFE_180D_pct": 4.4, "MFE_1Y_pct": 4.4, "MFE_2Y_pct": null, "MAE_30D_pct": -23.68, "MAE_90D_pct": -43.4, "MAE_180D_pct": -43.4, "MAE_1Y_pct": -47.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-09-10", "peak_price": 92600.0, "drawdown_after_peak_pct": -45.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "epoxy_price_spread_record_result_late_green_trap", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:007690:2021-09-09", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-06", "trigger_id": "C15-L82-06-T1", "symbol": "007690", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 4}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 4, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 12, "pass_through_score": 2}, "weighted_score_after": 66, "stage_label_after": "Stage2-Actionable", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 4.4, "MAE_90D_pct": -43.4, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "C15-L82-07", "symbol": "001940", "company_name": "KISCO홀딩스", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "한국철강의 철근 스프레드 확대와 4Q21 높은 수익성 지속 전망은 KISCO 그룹 look-through spread bridge를 만들었다. holding proxy discount는 필요하다."}
{"row_type": "trigger", "trigger_id": "C15-L82-07-T1", "case_id": "C15-L82-07", "symbol": "001940", "company_name": "KISCO홀딩스", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-01-20", "evidence_available_at_that_date": "한국철강의 철근 스프레드 확대와 4Q21 높은 수익성 지속 전망은 KISCO 그룹 look-through spread bridge를 만들었다. holding proxy discount는 필요하다.", "evidence_source": "https://www.snmnews.com/news/articleView.html?idxno=489529", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": ["margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001940/2022.csv", "profile_path": "atlas/symbol_profiles/001/001940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-01-20", "entry_price": 15100.0, "MFE_30D_pct": 10.6, "MFE_90D_pct": 23.84, "MFE_180D_pct": 23.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.95, "MAE_90D_pct": -7.95, "MAE_180D_pct": -21.19, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-03", "peak_price": 18700.0, "drawdown_after_peak_pct": -36.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "rebar_spread_margin_positive_but_holding_proxy_discount", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:001940:2022-01-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-07", "trigger_id": "C15-L82-07-T1", "symbol": "001940", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 12}, "weighted_score_before": 73, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 14}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 23.84, "MAE_90D_pct": -7.95, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "case", "case_id": "C15-L82-08", "symbol": "007280", "company_name": "한국특강", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "철근 시장은 수요 감소와 공급능력 증가가 맞물리는 부정적 국면으로 진입했고 한국특강의 100만톤 생산능력은 기존 최적화 질서의 변수였다."}
{"row_type": "trigger", "trigger_id": "C15-L82-08-T1", "case_id": "C15-L82-08", "symbol": "007280", "company_name": "한국특강", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "C15_MULTI_MATERIAL_PASSTHROUGH_INVENTORY_LAG_AND_PHASE_GUARD", "sector": "materials_spread_resource", "primary_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "loop_objective": "counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2022-10-07", "evidence_available_at_that_date": "철근 시장은 수요 감소와 공급능력 증가가 맞물리는 부정적 국면으로 진입했고 한국특강의 100만톤 생산능력은 기존 최적화 질서의 변수였다.", "evidence_source": "https://www.steelin.co.kr/news/articleView.html?idxno=7951", "stage2_evidence_fields": ["public_event_or_disclosure", "asp_or_spread_route", "product_or_customer_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007280/2022.csv", "profile_path": "atlas/symbol_profiles/007/007280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-10-07", "entry_price": 2260.0, "MFE_30D_pct": 1.33, "MFE_90D_pct": 1.33, "MFE_180D_pct": 1.33, "MFE_1Y_pct": 1.33, "MFE_2Y_pct": null, "MAE_30D_pct": -7.52, "MAE_90D_pct": -18.81, "MAE_180D_pct": -18.81, "MAE_1Y_pct": -25.71, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-10-07", "peak_price": 2290.0, "drawdown_after_peak_pct": -19.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_or_phase_cap_required", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "rebar_capacity_addition_supply_demand_reversal", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C15_MATERIAL_SPREAD_SUPERCYCLE:007280:2022-10-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "C15-L82-08", "trigger_id": "C15-L82-08-T1", "symbol": "007280", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 4, "pass_through_score": 4}, "weighted_score_before": 70, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 4, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "inventory_lag_risk_score": 12, "pass_through_score": 2}, "weighted_score_after": 52, "stage_label_after": "Stage4B", "changed_components": ["pass_through_score", "inventory_lag_risk_score", "margin_bridge_score", "valuation_repricing_score"], "component_delta_explanation": "C15 shadow ladder discounts raw commodity/proxy headlines unless issuer-level pass-through and margin/cash conversion are visible; it also caps local peak phase rows as 4B-watch.", "MFE_90D_pct": 1.33, "MAE_90D_pct": -18.81, "score_return_alignment_label": "improved_by_shadow_ladder", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "profile_aggregate", "profile_id": "P0_e2r_2_2_rolling_calibrated_proxy", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "trigger_count": 8, "avg_MFE_90D_pct": 13.1, "avg_MAE_90D_pct": -25.41, "avg_MFE_180D_pct": 14.81, "avg_MAE_180D_pct": -31.12, "false_positive_rate": 0.62, "score_return_alignment_verdict": "current profile over-credits raw commodity/proxy headlines and under-separates pass-through/freshness."}
{"row_type": "profile_aggregate", "profile_id": "P2_c15_multimaterial_passthrough_inventory_phase_guard", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "trigger_count": 8, "avg_MFE_90D_pct": 13.1, "avg_MAE_90D_pct": -25.41, "avg_MFE_180D_pct": 14.81, "avg_MAE_180D_pct": -31.12, "false_positive_rate": 0.25, "score_return_alignment_verdict": "improved by separating commodity weather from issuer-level spread conversion and phase."}
{"row_type": "shadow_weight", "axis": "c15_multimaterial_passthrough_inventory_phase_guard", "scope": "canonical_archetype_specific", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "baseline_value": "20/12/20/10/10/8/20", "tested_value": "20/10/18/10/10/10/22", "delta": "Visibility -2; Bottleneck -2; Capital +2; Info +2", "reason": "Raw commodity headlines and sector proxies need pass-through, inventory-lag, margin/cash, and price-phase checks before promotion.", "backtest_effect": "reduced false positive Green/Actionable routing in aluminum, epoxy, copper, and rebar proxy rows while preserving paper/rebar spread positives.", "trigger_ids": "C15-L82-01-T1|C15-L82-02-T1|C15-L82-03-T1|C15-L82-04-T1|C15-L82-05-T1|C15-L82-06-T1|C15-L82-07-T1|C15-L82-08-T1", "calibration_usable_count": 8, "new_independent_case_count": 8, "counterexample_count": 5, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "residual_contribution", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "new_independent_case_count": 8, "reused_case_count": 0, "new_symbol_count": 8, "new_trigger_family_count": 8, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "stage3_green_revision_min_by_margin_cash_freshness", "hard_4c_confirmation"], "residual_error_types_found": ["raw_commodity_proxy_false_positive", "result_only_green_trap", "inventory_lag_or_pass_through_missing", "high_mae_live_bridge_not_hard4c"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied rolling calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large sectors support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 82
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 URL/proxy/MFE-MAE repair
next_recommended_archetypes = C01/C05 direct FCF or cash-conversion rows; C13 strict-new utilization/ex-credit rows; C10 strict-new order-conversion rows; C31 non-semi/battery awarded-cashflow rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest/schema: Songdaiki/stock-web `atlas/manifest.json`, `atlas/schema.json`.
- Evidence sources are recorded per case in Section 9 and in each JSONL trigger row.
- This file contains no investment recommendation language and no production patch.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
