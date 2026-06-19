# E2R Historical Calibration Prompt v12 — Stock-Web OHLC Atlas / Sector-Archetype Residual Expansion / MD Handoff

## 0. Metadata

```yaml
research_file: e2r_stock_web_v12_residual_round_R1_loop_181_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selected_round: R1
selected_loop: 181
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement after Priority 0 quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING
loop_objective: C05 margin / working-capital failure and over-hard 4C timing repair
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This file is a standalone v12 residual research MD. It does not patch `stock_agent`, does not run live discovery, and does not change production scoring.

---

## 1. Current calibrated profile assumption

Current profile is treated as already post-global calibration. The repeated global axes are not re-proposed. This loop only tests C05-specific residual behavior:

- Stage2-Actionable evidence bonus is already assumed.
- Stage3-Green remains strict and is not loosened.
- Price-only blowoff remains blocked from positive stage promotion.
- Full 4B still requires non-price evidence.
- Hard 4C still routes to 4C when the thesis break is non-price and confirmed.

Residual question for this loop:

> In C05 EPC mega-contracts, does a large EPC award/backlog convert into margin and cash quickly enough, and when should bad-debt / cost-rate language be hard 4C versus only a watch-stage offset?

---

## 2. Selection / coverage gap check

The No-Repeat Index says the cumulative corpus now uses `--include-archive`, with 2,081 v12 result MDs, 12,410 validated rows, and 11,200 representative rows. It also states all C01~C32 archetypes exceed the 80-row level; the next task is quality and balance repair rather than simple row filling.

Selected target:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rows = 180
symbols = 54
positive/counter = 29/39
4B/4C = 23/10
runtime weights = EPS/Vis/Bott/Mis/Val/Cap/Info = 18/22/10/12/10/8/20
next direction = margin/working-capital failure rebuttals and 4C timing repair
```

Duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Batch hard keys:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2-Actionable|2023-06-27
C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C|2023-08-28
C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2025-02-04
C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4C|2025-02-07
C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage4C|2025-02-07
```

Within-batch same-entry dedupe: pass. Search over public GitHub snippets did not surface these exact C05 hard-key strings.

---

## 3. Stock-Web manifest / schema validation

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
```

Tradable shard columns used: `d,o,h,l,c,v,a,mc,s,m`.

MFE / MAE method:

```text
entry_price = entry_date close
MFE_N_pct = (max high from entry_date through N tradable sessions / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable sessions / entry_price - 1) * 100
```

All five rows have at least 180 forward tradable sessions before the manifest max date. No selected 180D window overlaps a corporate-action candidate date in the corresponding symbol profile.

---

## 4. Archetype compression map

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING
```

Fine/deep sub-archetype roles used in this loop:

1. `EPC_LOA_LSTK_MEGA_PACKAGE`: mega EPC award, but LSTK delivery/margin conversion is not yet proven.
2. `EPC_LOA_MODULAR_EXECUTION_BRIDGE`: mega EPC award with execution-system bridge and regional experience.
3. `QUALITY_TRUST_REGULATORY_SANCTION`: construction quality/regulatory trust break.
4. `BAD_DEBT_COST_RATE_WITH_NET_CASH_GUIDANCE`: bad-debt/cost-rate phrase with explicit offset evidence.
5. `OP_DROP_COST_RATE_WITH_OVERSEAS_PLANT_BACKLOG`: OP decline/cost-rate pressure with backlog and overseas plant offset.

---

## 5. Evidence source map

- `000720` Hyundai E&C: [https://www.hdec.kr/en/newsroom/news_view.aspx?NewsListType=news_list&NewsSeq=805&NewsType=FUTURE](https://www.hdec.kr/en/newsroom/news_view.aspx?NewsListType=news_list&NewsSeq=805&NewsType=FUTURE) — Official HDEC release dated 26 Jun 2023: awarded two EPC packages for the SATORP refinery petrochemical expansion in Jubail, Saudi Arabia; lump-sum turnkey value around USD 5B; detailed design, procurement, construction, commissioning and start-up activities.
- `006360` GS E&C: [https://en.yna.co.kr/view/AEN20230827002451320](https://en.yna.co.kr/view/AEN20230827002451320) — Yonhap, 27 Aug 2023: Korean land ministry sought a 10-month business suspension for GS E&C over the Geomdan parking-garage collapse; cited insufficient reinforcing rods and poor process management. Korea Times, 9 May 2023, separately reported GS E&C admission/apology over missed rebar.
- `028050` Samsung E&A: [https://www.samsungena.com/en/newsroom/news/view?idx=15676](https://www.samsungena.com/en/newsroom/news/view?idx=15676) — Official Samsung E&A release dated 3 Feb 2025: LOA on 31 Jan for EPC of TA'ZIZ Methanol Project in the UAE; contract value USD 1.7B; 44-month duration; execution bridge via Ruwais experience, modularization and automation.
- `375500` DL E&C: [https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword=](https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword=) — Official DL E&C release dated 6 Feb 2025: 2024 sales KRW 8.3184T and OP KRW 270.9B; OP fell 18% due to bad debts and cost-rate adjustments at DL Construction, but release also reports Q4 sequential improvement, cost-rate improvement, net cash and high financial stability.
- `047040` Daewoo E&C: [https://pulse.mk.co.kr/news/english/11234023](https://pulse.mk.co.kr/news/english/11234023) — Pulse/Maeil, 6 Feb 2025 11:28 KST: 2024 OP down 39.2%, revenue down 9.8%, decline attributed to ongoing project-site decline, rising cost rates and temporary additional residential costs; offset language included high-margin overseas plant projects and KRW 44.44T order backlog.

---

## 6. Actual 1D OHLC entry rows

| symbol | entry_date | o | h | l | c | v | window_180D_end |
|---|---|---|---|---|---|---|---|
| 000720 | 2023-06-27 | 40550 | 41350 | 39000 | 39100 | 2439159 | 2024-03-21 |
| 006360 | 2023-08-28 | 14000 | 14760 | 13440 | 14480 | 3145357 | 2024-05-27 |
| 028050 | 2025-02-04 | 18440 | 18470 | 18060 | 18070 | 1406457 | 2025-10-30 |
| 375500 | 2025-02-07 | 35250 | 37100 | 34950 | 36900 | 699699 | 2025-11-04 |
| 047040 | 2025-02-07 | 3325 | 3405 | 3315 | 3330 | 1022156 | 2025-11-04 |

---

## 7. Trigger-level backtest grid

| case_id | symbol | company | trigger | trigger_date | entry_date | entry_close | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | peak_180D | max_DD_after_peak | usable |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C05_000720_20230627_STAGE2_ACTIONABLE | 000720 | Hyundai E&C | Stage2-Actionable | 2023-06-26 | 2023-06-27 | 39100 | 5.75 / -11.64 | 5.75 / -14.96 | 5.75 / -20.2 | 2023-06-27 @ 41350 | -24.55 | true |
| C05_006360_20230828_STAGE4C | 006360 | GS E&C | Stage4C | 2023-08-27 | 2023-08-28 | 14480 | 3.38 / -12.5 | 20.17 / -12.5 | 20.17 / -12.5 | 2023-11-23 @ 17400 | -20.34 | true |
| C05_028050_20250204_STAGE2_ACTIONABLE | 028050 | Samsung E&A | Stage2-Actionable | 2025-02-03 | 2025-02-04 | 18070 | 14.83 / -9.35 | 32.82 / -9.35 | 69.62 / -9.35 | 2025-10-23 @ 30650 | -11.58 | true |
| C05_375500_20250207_STAGE4C_STRESS | 375500 | DL E&C | Stage4C | 2025-02-06 | 2025-02-07 | 36900 | 27.24 / -5.28 | 52.3 / -5.28 | 61.79 / -5.28 | 2025-06-26 @ 59700 | -32.91 | true |
| C05_047040_20250207_STAGE4C_STRESS | 047040 | Daewoo E&C | Stage4C | 2025-02-06 | 2025-02-07 | 3330 | 12.91 / -3.9 | 44.29 / -11.71 | 44.29 / -11.71 | 2025-06-05 @ 4805 | -26.74 | true |

---

## 8. Case interpretation

### 8.1 Hyundai E&C / 000720 — EPC award can be right but too early

HDEC's Saudi SATORP/Amiral packages are strong non-price evidence: awarded EPC packages, lump-sum turnkey contract, and direct design/procurement/construction scope. The 180D path was poor: MFE only `5.75%`, MAE `-20.20%`, and close return `-12.28%`. The 2Y window later reached `117.65%` MFE, so the case is not a thesis failure; it is a timing and margin-conversion delay case.

Calibration use: keep as Stage2-Actionable, but block Stage3-Yellow/Green unless later margin, cash conversion, or revision bridge appears. This is the cleanest example in the batch for `too_early_stage3_yellow_without_margin_cash_bridge`.

### 8.2 GS E&C / 006360 — trust break is non-price 4C even if price later recovers

The Geomdan collapse and the ministry's suspension push are not normal cost-rate noise. They are legal/regulatory trust-break evidence. The price path did recover later, but the initial 30D MAE was `-12.50%`, and the evidence itself damages construction-quality trust.

Calibration use: keep hard 4C confirmation when quality/regulatory trust is confirmed by a primary or highly reliable source. Price recovery does not erase the non-price thesis break; it only prevents using price-only post hoc strength to overrule 4C.

### 8.3 Samsung E&A / 028050 — clean positive C05 bridge

Samsung E&A's UAE Methanol Project has direct LOA/EPC scope, USD 1.7B value, 44-month duration, regional execution experience, and modularization/automation execution bridge. Price path confirms this as the clean positive row: 30D MFE `14.83%`, 90D MFE `32.82%`, 180D MFE `69.62%`, with MAE capped at `-9.35%`.

Calibration use: allow Stage3-Yellow if evidence includes direct EPC contract plus execution/margin-quality bridge. Still do not loosen Stage3-Green without revision/profit-confirmation evidence.

### 8.4 DL E&C / 375500 — bad-debt phrase alone is not automatic hard 4C

The official result contains negative words: OP down 18%, bad debts, and cost-rate adjustments. But the same source also gives offsets: Q4 sequential improvement, cost-rate improvement, net cash, guidance proximity, and high financial stability. The price path strongly rejects a simple hard-4C interpretation: 30D MFE `27.24%`, 90D MFE `52.30%`, 180D MFE `61.79%`.

Calibration use: strengthen `hard_4c_confirmation` only when bad-debt/cost-rate evidence is severe, recurring, legal/trust-based, or paired with cash/balance deterioration. If a source gives explicit offset evidence, route to Stage2 watch / recovery instead of hard 4C.

### 8.5 Daewoo E&C / 047040 — annual OP decline can coexist with backlog/rerating

Daewoo's 2024 OP fell sharply and cost-rate pressure was cited, but the same article includes high-margin overseas plant projects, backlog, and new-order targets. The 180D path had MFE `44.29%` and MAE `-11.71%`; the 1Y window later reached `148.05%` MFE by the manifest max date.

Calibration use: annual OP decline should not be hard 4C if backlog duration, high-margin overseas plant mix, and forward order target support remain intact. It should lower earnings-visibility score but not automatically break the C05 thesis.

---

## 9. Score-return alignment matrix

| symbol | current_total | current_stage | shadow_total | shadow_stage | error_label |
|---|---|---|---|---|---|
| 000720 | 78.4 | Stage3-Yellow risk / too-early promotion | 70.2 | Stage2-Actionable only | too_early_stage3_yellow_without_margin_cash_bridge |
| 006360 | 35.0 | Stage4C | 30.0 | Stage4C confirmed | none_confirmed_trust_break |
| 028050 | 74.8 | Stage2-Actionable / Stage3-Yellow border | 80.5 | Stage3-Yellow, not Green | none_positive_bridge_strengthened |
| 375500 | 42.0 | Stage4C risk if bad-debt phrase is over-weighted | 67.0 | Stage2 watch / recovery, not 4C | overhard_4c_if_bad_debt_cost_rate_without_offset_check |
| 047040 | 45.5 | Stage4C risk if annual OP decline dominates | 66.5 | Stage2 watch / backlog-offset, not 4C | overhard_margin_decline_without_backlog_overseas_offset |

Current profile residual errors counted in this loop: `3`.

```text
000720: too early positive promotion risk
375500: over-hard 4C risk if bad-debt phrase dominates offset evidence
047040: over-hard 4C risk if annual OP decline dominates backlog/overseas plant offset evidence
```

Correct / retained behavior:

```text
006360: hard 4C retained because the issue is quality/regulatory trust break
028050: positive Stage2-Actionable / Stage3-Yellow bridge retained
```

---

## 10. Raw component score breakdown

```json
{
  "000720": {
    "current_total": 78.4,
    "current_stage": "Stage3-Yellow risk / too-early promotion",
    "shadow_total": 70.2,
    "shadow_stage": "Stage2-Actionable only",
    "error_label": "too_early_stage3_yellow_without_margin_cash_bridge",
    "component_before": {
      "eps_fcf_explosion": 54,
      "earnings_visibility": 75,
      "bottleneck_pricing": 57,
      "market_mispricing": 58,
      "valuation_rerating": 45,
      "capital_allocation": 43,
      "information_confidence": 82
    },
    "component_after": {
      "eps_fcf_explosion": 45,
      "earnings_visibility": 66,
      "bottleneck_pricing": 52,
      "market_mispricing": 48,
      "valuation_rerating": 38,
      "capital_allocation": 42,
      "information_confidence": 84
    }
  },
  "006360": {
    "current_total": 35.0,
    "current_stage": "Stage4C",
    "shadow_total": 30.0,
    "shadow_stage": "Stage4C confirmed",
    "error_label": "none_confirmed_trust_break",
    "component_before": {
      "eps_fcf_explosion": 20,
      "earnings_visibility": 20,
      "bottleneck_pricing": 10,
      "market_mispricing": 20,
      "valuation_rerating": 15,
      "capital_allocation": 35,
      "information_confidence": 35
    },
    "component_after": {
      "eps_fcf_explosion": 15,
      "earnings_visibility": 15,
      "bottleneck_pricing": 8,
      "market_mispricing": 18,
      "valuation_rerating": 12,
      "capital_allocation": 28,
      "information_confidence": 45
    }
  },
  "028050": {
    "current_total": 74.8,
    "current_stage": "Stage2-Actionable / Stage3-Yellow border",
    "shadow_total": 80.5,
    "shadow_stage": "Stage3-Yellow, not Green",
    "error_label": "none_positive_bridge_strengthened",
    "component_before": {
      "eps_fcf_explosion": 63,
      "earnings_visibility": 73,
      "bottleneck_pricing": 55,
      "market_mispricing": 55,
      "valuation_rerating": 50,
      "capital_allocation": 58,
      "information_confidence": 82
    },
    "component_after": {
      "eps_fcf_explosion": 70,
      "earnings_visibility": 82,
      "bottleneck_pricing": 60,
      "market_mispricing": 58,
      "valuation_rerating": 52,
      "capital_allocation": 62,
      "information_confidence": 88
    }
  },
  "375500": {
    "current_total": 42.0,
    "current_stage": "Stage4C risk if bad-debt phrase is over-weighted",
    "shadow_total": 67.0,
    "shadow_stage": "Stage2 watch / recovery, not 4C",
    "error_label": "overhard_4c_if_bad_debt_cost_rate_without_offset_check",
    "component_before": {
      "eps_fcf_explosion": 25,
      "earnings_visibility": 35,
      "bottleneck_pricing": 18,
      "market_mispricing": 30,
      "valuation_rerating": 28,
      "capital_allocation": 55,
      "information_confidence": 62
    },
    "component_after": {
      "eps_fcf_explosion": 48,
      "earnings_visibility": 62,
      "bottleneck_pricing": 34,
      "market_mispricing": 46,
      "valuation_rerating": 42,
      "capital_allocation": 78,
      "information_confidence": 78
    }
  },
  "047040": {
    "current_total": 45.5,
    "current_stage": "Stage4C risk if annual OP decline dominates",
    "shadow_total": 66.5,
    "shadow_stage": "Stage2 watch / backlog-offset, not 4C",
    "error_label": "overhard_margin_decline_without_backlog_overseas_offset",
    "component_before": {
      "eps_fcf_explosion": 28,
      "earnings_visibility": 36,
      "bottleneck_pricing": 22,
      "market_mispricing": 34,
      "valuation_rerating": 30,
      "capital_allocation": 50,
      "information_confidence": 65
    },
    "component_after": {
      "eps_fcf_explosion": 47,
      "earnings_visibility": 60,
      "bottleneck_pricing": 38,
      "market_mispricing": 47,
      "valuation_rerating": 40,
      "capital_allocation": 62,
      "information_confidence": 78
    }
  }
}
```

Interpretation: the C05 runtime weight already reduces bottleneck/valuation and raises information confidence. This loop does not ask for a global weight change. It asks for an evidence gate: EPC headline evidence must pass a margin/cash/execution bridge to be promoted, and bad-debt/cost-rate language must pass a severity/offset check before hard 4C.

---

## 11. 4B local vs full-window proximity audit

No selected row is a price-only 4B. However, two cases test the 4B/4C border indirectly:

| symbol | audit | result |
|---|---|---|
| 000720 | early EPC order produced high MAE before later 2Y rerating | keep as Stage2-Actionable until non-price margin/cash bridge appears |
| 375500 | bad-debt/cost-rate language did not create a sustained downside path | block hard 4C if offset evidence is explicit |
| 047040 | OP decline did not block later rerating | use watch downgrade, not thesis break, when backlog/overseas mix offsets are present |

---

## 12. 4C thesis-break audit

Hard 4C should remain narrow and source-quality dependent.

Confirmed hard 4C:

```text
006360 / GS E&C / 2023-08-28
reason: regulator-backed quality/trust break, business-suspension process, construction-process failure
```

Blocked or softened hard 4C:

```text
375500 / DL E&C / 2025-02-07
reason: bad-debt/cost-rate words exist, but same source provides explicit balance-sheet, cost-rate, and guidance offsets

047040 / Daewoo E&C / 2025-02-07
reason: OP decline and rising cost rates exist, but backlog and high-margin overseas plant offsets remain visible
```

---

## 13. Sector-specific / canonical-specific shadow rule candidates

### Sector rule candidate

```yaml
rule_id: L1_C05_EPC_STAGE2_MARGIN_CASH_BRIDGE_GATE
scope:
  large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_type: shadow_rule_only
production_scoring_changed: false
logic:
  - EPC mega contract / LOA / backlog evidence can qualify for Stage2-Actionable.
  - Stage3-Yellow requires at least one non-price bridge:
      1. margin guidance / revision confirmation
      2. working-capital or cash conversion quality
      3. execution-risk reducer such as proven regional client/project type, modularization, or repeated delivery record
      4. quarterly profitability improvement tied to the project/order mix
  - Stage3-Green still requires revision/profit confirmation and is not loosened.
```

### Canonical rule candidate

```yaml
rule_id: C05_HARD_4C_SEVERITY_OFFSET_CHECK
scope:
  canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_type: guardrail_refinement
production_scoring_changed: false
logic:
  hard_4c_confirm_if:
    - quality/regulatory/legal trust break is confirmed; or
    - cost overrun / bad-debt evidence is severe and recurring; or
    - balance-sheet / liquidity / cash conversion evidence deteriorates alongside margin failure.
  avoid_hard_4c_if:
    - bad-debt or cost-rate language is one-period/affiliate-contained; and
    - same source gives explicit offset evidence such as net cash, cost-rate improvement, backlog duration, high-margin overseas order mix, or guidance proximity.
```

---

## 14. Residual contribution summary

| label | value |
|---|---:|
| new_independent_case_count | 5 |
| new_independent_trigger_count | 5 |
| unique_symbol_count_in_batch | 5 |
| positive_case_count | 2 |
| counterexample_or_guardrail_case_count | 3 |
| calibration_usable_case_count | 5 |
| calibration_usable_trigger_count | 5 |
| source_proxy_only_count | 0 |
| evidence_url_pending_count | 0 |
| missing_required_mfe_mae_count | 0 |
| corporate_action_contaminated_180D_count | 0 |
| insufficient_forward_window_180D_count | 0 |
| current_profile_error_count | 3 |
| new_independent_ratio | 1.00 |

Loop contribution label:

```text
C05_margin_bridge_and_overhard_4c_quality_repair
```

---

## 15. Shadow weight calibration table

```csv
axis,scope,before,shadow_after,delta,direction,reason,production_scoring_changed
stage2_required_bridge,L1/C05,existing,stronger,+1,strengthen,"EPC headline must be tied to margin/cash/execution bridge before Stage3-Yellow",false
earlier_thesis_break_watch,L1/C05,existing,stronger,+1,strengthen,"Quality/regulatory construction trust break should be detected before price recovery masks it",false
hard_4c_confirmation,L1/C05,existing,more_selective,0,refine,"Bad debt/cost-rate phrase alone should not hard-4C if explicit offset evidence exists",false
local_4b_watch_guard,L1/C05,existing,unchanged,0,hold,"No price-only 4B promotion used in this loop",false
```

No global weight delta is proposed. The current C05 information-confidence overweight is directionally justified, but this batch says information confidence should be used as a gate, not as a blunt bearish/positive force.

---

## 16. Validation scope / non-validation scope

Validated:

- selected round / sector consistency
- canonical/fine archetype consistency
- Stock-Web tradable raw shard use
- entry_date and entry_close for every row
- complete 30D/90D/180D MFE/MAE for every row
- peak date / peak price / drawdown after peak
- 180D forward-window availability
- 180D corporate-action contamination check
- non-price evidence URL for every trigger
- machine-readable JSONL row for every trigger

Not validated in this MD:

- production implementation behavior in `src/e2r`
- full md_registry exact-key scan beyond No-Repeat summary and public snippet search
- intraday evidence timestamp precision beyond next-trading-day conservative entries
- broker/live execution suitability
- current 2026 stock recommendation

---

## 17. Coverage matrix contribution

| dimension | contribution |
|---|---|
| broad C05 evidence | EPC award, quality/regulatory trust break, bad debt/cost-rate, backlog/overseas mix offset |
| stage labels | Stage2-Actionable and Stage4C |
| positive/counter balance | 2 positive, 3 counterexample/guardrail |
| time regimes | 2023 post-award / 2025 results and EPC cycle |
| price paths | delayed winner, clean winner, trust break, over-hard 4C false-negative stress |
| source quality | 3 official company sources, 2 reliable press/regulatory news sources |

---

## 18. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_181_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":181,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2-Actionable|2023-06-27","case_id":"C05_000720_20230627_STAGE2_ACTIONABLE","symbol":"000720","company":"Hyundai E&C","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-26","entry_date":"2023-06-27","entry_price":39100.0,"entry_open":40550.0,"entry_high":41350.0,"entry_low":39000.0,"entry_close":39100.0,"entry_volume":2439159,"MFE_30D_pct":5.75,"MAE_30D_pct":-11.64,"MFE_90D_pct":5.75,"MAE_90D_pct":-14.96,"MFE_180D_pct":5.75,"MAE_180D_pct":-20.2,"MFE_1Y_pct":5.75,"MAE_1Y_pct":-20.2,"MFE_2Y_pct":117.65,"MAE_2Y_pct":-38.36,"peak_date":"2023-06-27","peak_price":41350.0,"drawdown_after_peak_pct":-24.55,"drawdown_trough_date":"2024-01-25","window_180D_end_date":"2024-03-21","forward_available_after_entry":611,"price_source_validation":{"price_source":"Songdaiki/stock-web","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/<year>.csv","shard_files_used":["000720_2023.csv","000720_2024.csv","000720_2025.csv"],"profile_note":"profile: atlas/symbol_profiles/000/000720.json; corporate-action candidates are historical and outside 2023-06-27~2024-03-21 180D window.","corporate_action_candidate_overlap_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"evidence":{"evidence_family":"EPC_LOA_LSTK_MEGA_PACKAGE","case_role":"positive_delayed","primary_source_url":"https://www.hdec.kr/en/newsroom/news_view.aspx?NewsListType=news_list&NewsSeq=805&NewsType=FUTURE","summary":"Official HDEC release dated 26 Jun 2023: awarded two EPC packages for the SATORP refinery petrochemical expansion in Jubail, Saudi Arabia; lump-sum turnkey value around USD 5B; detailed design, procurement, construction, commissioning and start-up activities.","source_proxy_only":false,"evidence_url_pending":false},"score_simulation":{"current_profile_total":78.4,"current_profile_stage":"Stage3-Yellow risk / too-early promotion","shadow_total":70.2,"shadow_stage":"Stage2-Actionable only","current_profile_error_label":"too_early_stage3_yellow_without_margin_cash_bridge","component_before":{"eps_fcf_explosion":54,"earnings_visibility":75,"bottleneck_pricing":57,"market_mispricing":58,"valuation_rerating":45,"capital_allocation":43,"information_confidence":82},"component_after":{"eps_fcf_explosion":45,"earnings_visibility":66,"bottleneck_pricing":52,"market_mispricing":48,"valuation_rerating":38,"capital_allocation":42,"information_confidence":84}},"residual_contribution":{"residual_label":"C05_margin_bridge_quality_repair","new_independent_trigger":true,"representative_for_aggregate":true,"positive_case":true,"counterexample_or_guardrail_case":false,"production_scoring_changed":false,"shadow_weight_only":true}}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_181_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":181,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C|2023-08-28","case_id":"C05_006360_20230828_STAGE4C","symbol":"006360","company":"GS E&C","trigger_type":"Stage4C","trigger_date":"2023-08-27","entry_date":"2023-08-28","entry_price":14480.0,"entry_open":14000.0,"entry_high":14760.0,"entry_low":13440.0,"entry_close":14480.0,"entry_volume":3145357,"MFE_30D_pct":3.38,"MAE_30D_pct":-12.5,"MFE_90D_pct":20.17,"MAE_90D_pct":-12.5,"MFE_180D_pct":20.17,"MAE_180D_pct":-12.5,"MFE_1Y_pct":50.21,"MAE_1Y_pct":-12.5,"MFE_2Y_pct":71.62,"MAE_2Y_pct":-12.5,"peak_date":"2023-11-23","peak_price":17400.0,"drawdown_after_peak_pct":-20.34,"drawdown_trough_date":"2024-01-23","window_180D_end_date":"2024-05-27","forward_available_after_entry":568,"price_source_validation":{"price_source":"Songdaiki/stock-web","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/<year>.csv","shard_files_used":["006360_2023.csv","006360_2024.csv","006360_2025.csv"],"profile_note":"profile: atlas/symbol_profiles/006/006360.json; corporate-action candidates are historical and outside 2023-08-28~2024-05-27 180D window.","corporate_action_candidate_overlap_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"evidence":{"evidence_family":"QUALITY_TRUST_REGULATORY_SANCTION","case_role":"trust_break","primary_source_url":"https://en.yna.co.kr/view/AEN20230827002451320","summary":"Yonhap, 27 Aug 2023: Korean land ministry sought a 10-month business suspension for GS E&C over the Geomdan parking-garage collapse; cited insufficient reinforcing rods and poor process management. Korea Times, 9 May 2023, separately reported GS E&C admission/apology over missed rebar.","source_proxy_only":false,"evidence_url_pending":false},"score_simulation":{"current_profile_total":35.0,"current_profile_stage":"Stage4C","shadow_total":30.0,"shadow_stage":"Stage4C confirmed","current_profile_error_label":"none_confirmed_trust_break","component_before":{"eps_fcf_explosion":20,"earnings_visibility":20,"bottleneck_pricing":10,"market_mispricing":20,"valuation_rerating":15,"capital_allocation":35,"information_confidence":35},"component_after":{"eps_fcf_explosion":15,"earnings_visibility":15,"bottleneck_pricing":8,"market_mispricing":18,"valuation_rerating":12,"capital_allocation":28,"information_confidence":45}},"residual_contribution":{"residual_label":"C05_margin_bridge_quality_repair","new_independent_trigger":true,"representative_for_aggregate":true,"positive_case":false,"counterexample_or_guardrail_case":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_181_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":181,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2025-02-04","case_id":"C05_028050_20250204_STAGE2_ACTIONABLE","symbol":"028050","company":"Samsung E&A","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-03","entry_date":"2025-02-04","entry_price":18070.0,"entry_open":18440.0,"entry_high":18470.0,"entry_low":18060.0,"entry_close":18070.0,"entry_volume":1406457,"MFE_30D_pct":14.83,"MAE_30D_pct":-9.35,"MFE_90D_pct":32.82,"MAE_90D_pct":-9.35,"MFE_180D_pct":69.62,"MAE_180D_pct":-9.35,"MFE_1Y_pct":90.09,"MAE_1Y_pct":-9.35,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2025-10-23","peak_price":30650.0,"drawdown_after_peak_pct":-11.58,"drawdown_trough_date":"2025-10-28","window_180D_end_date":"2025-10-30","forward_available_after_entry":255,"price_source_validation":{"price_source":"Songdaiki/stock-web","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/<year>.csv","shard_files_used":["028050_2025.csv","028050_2026.csv"],"profile_note":"profile: atlas/symbol_profiles/028/028050.json; name changed from Samsung Engineering to Samsung E&A before trigger; corporate-action candidates are outside 2025-02-04~2025-10-30 180D window.","corporate_action_candidate_overlap_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"evidence":{"evidence_family":"EPC_LOA_MODULAR_EXECUTION_BRIDGE","case_role":"positive_clean","primary_source_url":"https://www.samsungena.com/en/newsroom/news/view?idx=15676","summary":"Official Samsung E&A release dated 3 Feb 2025: LOA on 31 Jan for EPC of TA'ZIZ Methanol Project in the UAE; contract value USD 1.7B; 44-month duration; execution bridge via Ruwais experience, modularization and automation.","source_proxy_only":false,"evidence_url_pending":false},"score_simulation":{"current_profile_total":74.8,"current_profile_stage":"Stage2-Actionable / Stage3-Yellow border","shadow_total":80.5,"shadow_stage":"Stage3-Yellow, not Green","current_profile_error_label":"none_positive_bridge_strengthened","component_before":{"eps_fcf_explosion":63,"earnings_visibility":73,"bottleneck_pricing":55,"market_mispricing":55,"valuation_rerating":50,"capital_allocation":58,"information_confidence":82},"component_after":{"eps_fcf_explosion":70,"earnings_visibility":82,"bottleneck_pricing":60,"market_mispricing":58,"valuation_rerating":52,"capital_allocation":62,"information_confidence":88}},"residual_contribution":{"residual_label":"C05_margin_bridge_quality_repair","new_independent_trigger":true,"representative_for_aggregate":true,"positive_case":true,"counterexample_or_guardrail_case":false,"production_scoring_changed":false,"shadow_weight_only":true}}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_181_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":181,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4C|2025-02-07","case_id":"C05_375500_20250207_STAGE4C_STRESS","symbol":"375500","company":"DL E&C","trigger_type":"Stage4C","trigger_date":"2025-02-06","entry_date":"2025-02-07","entry_price":36900.0,"entry_open":35250.0,"entry_high":37100.0,"entry_low":34950.0,"entry_close":36900.0,"entry_volume":699699,"MFE_30D_pct":27.24,"MAE_30D_pct":-5.28,"MFE_90D_pct":52.3,"MAE_90D_pct":-5.28,"MFE_180D_pct":61.79,"MAE_180D_pct":-5.28,"MFE_1Y_pct":61.79,"MAE_1Y_pct":-5.28,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2025-06-26","peak_price":59700.0,"drawdown_after_peak_pct":-32.91,"drawdown_trough_date":"2025-10-20","window_180D_end_date":"2025-11-04","forward_available_after_entry":252,"price_source_validation":{"price_source":"Songdaiki/stock-web","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/<year>.csv","shard_files_used":["375500_2025.csv","375500_2026.csv"],"profile_note":"profile: atlas/symbol_profiles/375/375500.json; corporate-action candidates in 2022 only; outside 2025-02-07~2025-11-04 180D window.","corporate_action_candidate_overlap_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"evidence":{"evidence_family":"BAD_DEBT_COST_RATE_WITH_NET_CASH_GUIDANCE","case_role":"mixed_counterexample_to_overhard_4c","primary_source_url":"https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword=","summary":"Official DL E&C release dated 6 Feb 2025: 2024 sales KRW 8.3184T and OP KRW 270.9B; OP fell 18% due to bad debts and cost-rate adjustments at DL Construction, but release also reports Q4 sequential improvement, cost-rate improvement, net cash and high financial stability.","source_proxy_only":false,"evidence_url_pending":false},"score_simulation":{"current_profile_total":42.0,"current_profile_stage":"Stage4C risk if bad-debt phrase is over-weighted","shadow_total":67.0,"shadow_stage":"Stage2 watch / recovery, not 4C","current_profile_error_label":"overhard_4c_if_bad_debt_cost_rate_without_offset_check","component_before":{"eps_fcf_explosion":25,"earnings_visibility":35,"bottleneck_pricing":18,"market_mispricing":30,"valuation_rerating":28,"capital_allocation":55,"information_confidence":62},"component_after":{"eps_fcf_explosion":48,"earnings_visibility":62,"bottleneck_pricing":34,"market_mispricing":46,"valuation_rerating":42,"capital_allocation":78,"information_confidence":78}},"residual_contribution":{"residual_label":"C05_margin_bridge_quality_repair","new_independent_trigger":true,"representative_for_aggregate":true,"positive_case":false,"counterexample_or_guardrail_case":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_181_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":181,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage4C|2025-02-07","case_id":"C05_047040_20250207_STAGE4C_STRESS","symbol":"047040","company":"Daewoo E&C","trigger_type":"Stage4C","trigger_date":"2025-02-06","entry_date":"2025-02-07","entry_price":3330.0,"entry_open":3325.0,"entry_high":3405.0,"entry_low":3315.0,"entry_close":3330.0,"entry_volume":1022156,"MFE_30D_pct":12.91,"MAE_30D_pct":-3.9,"MFE_90D_pct":44.29,"MAE_90D_pct":-11.71,"MFE_180D_pct":44.29,"MAE_180D_pct":-11.71,"MFE_1Y_pct":148.05,"MAE_1Y_pct":-11.71,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2025-06-05","peak_price":4805.0,"drawdown_after_peak_pct":-26.74,"drawdown_trough_date":"2025-11-04","window_180D_end_date":"2025-11-04","forward_available_after_entry":252,"price_source_validation":{"price_source":"Songdaiki/stock-web","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/<year>.csv","shard_files_used":["047040_2025.csv","047040_2026.csv"],"profile_note":"profile: atlas/symbol_profiles/047/047040.json; corporate-action candidates are historical and outside 2025-02-07~2025-11-04 180D window.","corporate_action_candidate_overlap_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"evidence":{"evidence_family":"OP_DROP_COST_RATE_WITH_OVERSEAS_PLANT_BACKLOG","case_role":"mixed_counterexample_to_overhard_4c","primary_source_url":"https://pulse.mk.co.kr/news/english/11234023","summary":"Pulse/Maeil, 6 Feb 2025 11:28 KST: 2024 OP down 39.2%, revenue down 9.8%, decline attributed to ongoing project-site decline, rising cost rates and temporary additional residential costs; offset language included high-margin overseas plant projects and KRW 44.44T order backlog.","source_proxy_only":false,"evidence_url_pending":false},"score_simulation":{"current_profile_total":45.5,"current_profile_stage":"Stage4C risk if annual OP decline dominates","shadow_total":66.5,"shadow_stage":"Stage2 watch / backlog-offset, not 4C","current_profile_error_label":"overhard_margin_decline_without_backlog_overseas_offset","component_before":{"eps_fcf_explosion":28,"earnings_visibility":36,"bottleneck_pricing":22,"market_mispricing":34,"valuation_rerating":30,"capital_allocation":50,"information_confidence":65},"component_after":{"eps_fcf_explosion":47,"earnings_visibility":60,"bottleneck_pricing":38,"market_mispricing":47,"valuation_rerating":40,"capital_allocation":62,"information_confidence":78}},"residual_contribution":{"residual_label":"C05_margin_bridge_quality_repair","new_independent_trigger":true,"representative_for_aggregate":true,"positive_case":false,"counterexample_or_guardrail_case":true,"production_scoring_changed":false,"shadow_weight_only":true}}
```

---

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename: e2r_stock_web_v12_residual_round_R1_loop_181_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
filename_pattern_pass: true
metadata_filename_consistency: pass
selected_round: R1
selected_loop: 181
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING
jsonl_trigger_row_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_entry_date: 0
rows_missing_entry_price: 0
rows_missing_MFE_30D_pct: 0
rows_missing_MAE_30D_pct: 0
rows_missing_MFE_90D_pct: 0
rows_missing_MAE_90D_pct: 0
rows_missing_MFE_180D_pct: 0
rows_missing_MAE_180D_pct: 0
rows_with_source_proxy_only: 0
rows_with_evidence_url_pending: 0
rows_with_corporate_action_contaminated_180D: 0
rows_with_insufficient_forward_window_180D: 0
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

---

## 19. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not use this research file as a direct production patch. First run the v12 calibration ingest pipeline against docs/round including archive, validate this MD against the v12 schema, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and compare its representative trigger rows against existing C05 rows.

If the rows validate, consider only shadow/candidate updates in the C05 scope:
1. Strengthen C05/L1 stage2_required_bridge so EPC mega-contract promotion requires a margin/cash/execution bridge before Stage3-Yellow.
2. Preserve hard_4c_confirmation for confirmed quality/regulatory/legal trust breaks.
3. Add or refine an offset check so bad-debt/cost-rate language alone does not hard-4C if the same source contains explicit net-cash, cost-rate improvement, backlog, high-margin overseas order, or guidance-proximity offsets.
4. Do not loosen global Stage3-Green thresholds.
5. Do not alter production scoring unless aggregate validation and promotion planner approve a small-scope patch.
```

---

## 20. Next Round State

```yaml
completed_round: R1
completed_loop: 181
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement after Priority 0 URL/proxy/MFE quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_BACKLOG_MARGIN_WORKING_CAPITAL_4C_TIMING
loop_contribution_label: C05_margin_bridge_and_overhard_4c_quality_repair
new_axis_proposed: false
existing_axis_strengthened:
  - stage2_required_bridge
  - earlier_thesis_break_watch
existing_axis_weakened:
  - none_global
existing_axis_refined:
  - hard_4c_confirmation_with_offset_check
next_recommended_archetypes:
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```
