# E2R Stock-Web v12 Residual Research — R12 / L10 / C32 Governance Control Premium Tender Cap

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R12
selected_loop = 222
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality repair / direct URL and governance-event taxonomy reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

The current cumulative No-Repeat Index shows that all C01~C32 archetypes already exceed the 80-row coverage band, so the next useful work is not raw row filling. The index calls for URL/proxy quality repair, direct evidence, and residual-error cleanup. C32 has already accumulated many governance/control-premium rows, but its rows are prone to the same error: a tender, buyback, activist, or sale-process headline is treated as if it were an operating rerating.

This file therefore selects **C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP** and focuses on **control-premium event mechanics vs operating Green**. The selected cases are deliberately cross-industry: metals, entertainment, shipping, biopharma holding company, media privatization, and Samsung holding-company activism. The common mechanism is not sector economics. It is a change in control, tender offer, control premium, shareholder vote, or sale process.

## 2. Price atlas validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_schema = d,o,h,l,c,v,a,mc,s,m
mfe_mae_method = entry close 대비 entry row부터 N tradable rows window의 max high / min low
```

Corporate-action contamination check: all usable rows below have no corporate-action candidate inside the entry~D+180 window. HMM has an old corporate-action candidate on 2023-11-10, but it is before the selected 2023-12-19 and 2024-02-07 entries, so the forward windows remain usable. Samsung C&T and Hanmi Science have historical corporate-action candidates outside the selected 2024 forward windows.

## 3. Batch summary

```text
new_independent_case_count = 10
new_independent_trigger_count = 10
unique_symbol_count = 6

stage2_count = 3
stage2_actionable_count = 3
stage4b_count = 4
stage4c_count = 0

positive_or_control_premium_case_count = 4
counterexample_or_guardrail_case_count = 6
current_profile_error_count = 7

source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0

production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 4. Trigger-level price results

| symbol | company | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 010130 | Korea Zinc | Stage2-Actionable | 2024-09-13 | 666,000 | 131.68/-1.65 | 261.41/-1.65 | 261.41/-3.45 | 2024-12-06 | 2025-04-09 |
| 010130 | Korea Zinc | 4B | 2024-10-21 | 877,000 | 75.94/-13.23 | 174.46/-18.93 | 174.46/-26.68 | 2024-12-06 | 2025-04-09 |
| 041510 | SM Entertainment | Stage2-Actionable | 2023-02-10 | 114,700 | 40.54/-9.24 | 40.54/-23.63 | 40.54/-23.63 | 2023-03-08 | 2023-03-28 |
| 041510 | SM Entertainment | 4B | 2023-03-13 | 113,100 | 19.36/-22.55 | 19.36/-22.55 | 29.97/-25.02 | 2023-08-29 | 2023-12-01 |
| 011200 | HMM | Stage2 | 2023-12-19 | 18,430 | 26.42/-10.20 | 26.42/-22.68 | 26.42/-22.68 | 2023-12-20 | 2024-04-19 |
| 011200 | HMM | 4B | 2024-02-07 | 19,080 | 5.87/-18.45 | 5.87/-25.31 | 9.01/-25.31 | 2024-07-03 | 2024-04-19 |
| 008930 | Hanmi Science | Stage2 | 2024-01-12 | 38,400 | 46.35/-3.12 | 46.35/-19.27 | 46.35/-32.94 | 2024-01-16 | 2024-08-05 |
| 008930 | Hanmi Science | 4B | 2024-03-28 | 44,350 | 5.98/-29.54 | 5.98/-41.94 | 18.38/-41.94 | 2024-10-30 | 2024-08-05 |
| 040300 | YTN | Stage2-Actionable | 2023-10-23 | 6,000 | 60.00/-9.83 | 60.00/-17.17 | 60.00/-49.50 | 2023-10-25 | 2024-07-10 |
| 028260 | Samsung C&T | Stage2 | 2024-02-15 | 156,300 | 9.85/-5.95 | 9.85/-17.15 | 9.85/-25.14 | 2024-02-19 | 2024-10-31 |

## 5. Case notes


### 010130 Korea Zinc — Stage2-Actionable / 2024-09-13

- **case_role:** `control_premium_positive_price_path`
- **evidence_family:** `hostile_tender_offer_initial`
- **evidence:** MBK Partners and Young Poong launched a tender offer for Korea Zinc shares; the event created a direct control-premium route but did not itself prove operating EPS/FCF rerating.
- **direct source:** Reuters, 2024-09-13, MBK/Young Poong launch tender offer for Korea Zinc — https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/
- **entry OHLCV:** O 660,000 / H 690,000 / L 655,000 / C 666,000 / V 586,718
- **30D MFE/MAE:** 131.68% / -1.65%
- **90D MFE/MAE:** 261.41% / -1.65%
- **180D MFE/MAE:** 261.41% / -3.45%
- **180D peak/trough:** 2024-12-06 @ 2,407,000 / 2025-04-09 @ 643,000
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 010130 Korea Zinc — 4B / 2024-10-21

- **case_role:** `self_tender_legal_clearance_late_extension`
- **evidence_family:** `court_buyback_clearance_self_tender`
- **evidence:** Court clearance for Korea Zinc’s buyback/self-tender extended the control battle and price, but also raised balance-sheet/leverage quality questions; this is local 4B/watch, not operating Green.
- **direct source:** Reuters, 2024-10-21, court clears buyback offer — https://www.reuters.com/markets/deals/korea-zinc-shares-surge-record-high-after-court-clears-hurdle-buyback-offer-2024-10-21/
- **entry OHLCV:** O 827,000 / H 889,000 / L 761,000 / C 877,000 / V 638,694
- **30D MFE/MAE:** 75.94% / -13.23%
- **90D MFE/MAE:** 174.46% / -18.93%
- **180D MFE/MAE:** 174.46% / -26.68%
- **180D peak/trough:** 2024-12-06 @ 2,407,000 / 2025-04-09 @ 643,000
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 041510 SM Entertainment — Stage2-Actionable / 2023-02-10

- **case_role:** `tender_competition_control_premium`
- **evidence_family:** `hybe_stake_purchase_tender_offer`
- **evidence:** HYBE agreed to buy Lee Soo-man’s 14.8% stake and launched a tender offer; this created a real control-premium route but remained governance/event-driven rather than repeat IP monetization proof.
- **direct source:** KED Global timeline, 2023-03-12; AP context — https://www.kedglobal.com/mergers-acquisitions/newsView/ked202303120002
- **entry OHLCV:** O 115,200 / H 117,000 / L 107,300 / C 114,700 / V 8,882,805
- **30D MFE/MAE:** 40.54% / -9.24%
- **90D MFE/MAE:** 40.54% / -23.63%
- **180D MFE/MAE:** 40.54% / -23.63%
- **180D peak/trough:** 2023-03-08 @ 161,200 / 2023-03-28 @ 87,600
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 041510 SM Entertainment — 4B / 2023-03-13

- **case_role:** `control_premium_fade_after_bidding_resolution`
- **evidence_family:** `hybe_bid_failure_kakao_tender_resolution`
- **evidence:** Kakao’s higher tender and HYBE’s failed tender shifted the control premium mechanics; the event path became a 4B/watch case rather than a durable operating-stage escalation.
- **direct source:** Yonhap, 2023-03-07; AP, 2023 Kakao tender — https://en.yna.co.kr/view/AEN20230307003251320
- **entry OHLCV:** O 135,000 / H 135,000 / L 111,300 / C 113,100 / V 5,457,572
- **30D MFE/MAE:** 19.36% / -22.55%
- **90D MFE/MAE:** 19.36% / -22.55%
- **180D MFE/MAE:** 29.97% / -25.02%
- **180D peak/trough:** 2023-08-29 @ 147,000 / 2023-12-01 @ 84,800
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 011200 HMM — Stage2 / 2023-12-19

- **case_role:** `privatization_preferred_bidder_without_closing`
- **evidence_family:** `preferred_bidder_control_sale`
- **evidence:** Harim-JKL was selected as preferred bidder for a controlling stake in HMM. The route was real but still dependent on definitive terms, creditor agreement, and closing.
- **direct source:** Yonhap, 2023-12-18, Harim named preferred bidder — https://en.yna.co.kr/view/AEN20231218009052320
- **entry OHLCV:** O 16,680 / H 19,220 / L 16,550 / C 18,430 / V 24,244,550
- **30D MFE/MAE:** 26.42% / -10.20%
- **90D MFE/MAE:** 26.42% / -22.68%
- **180D MFE/MAE:** 26.42% / -22.68%
- **180D peak/trough:** 2023-12-20 @ 23,300 / 2024-04-19 @ 14,250
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 011200 HMM — 4B / 2024-02-07

- **case_role:** `sale_breakdown_control_premium_reversal`
- **evidence_family:** `deal_collapse_creditor_negotiation_failure`
- **evidence:** HMM sale negotiations collapsed after the Harim bid failed to reach final agreement. Governance premium broke, but shipping-cycle fundamentals remained separate, so this is 4B/watch rather than issuer hard 4C.
- **direct source:** Yonhap / Korea JoongAng Daily, 2024-02-07 — https://en.yna.co.kr/view/AEN20240207001452320
- **entry OHLCV:** O 19,030 / H 20,200 / L 17,500 / C 19,080 / V 5,677,567
- **30D MFE/MAE:** 5.87% / -18.45%
- **90D MFE/MAE:** 5.87% / -25.31%
- **180D MFE/MAE:** 9.01% / -25.31%
- **180D peak/trough:** 2024-07-03 @ 20,800 / 2024-04-19 @ 14,250
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 008930 Hanmi Science — Stage2 / 2024-01-12

- **case_role:** `family_control_merger_optional_route`
- **evidence_family:** `hanmi_oci_integration_announcement`
- **evidence:** Hanmi Group and OCI announced an integration/merger plan. It created a control-structure and strategic optionality event, but operating/rerating bridge was still conditional.
- **direct source:** Yonhap/KED later summary of Jan announcement and Mar vote — https://en.yna.co.kr/view/AEN20240328007700320
- **entry OHLCV:** O 37,300 / H 38,900 / L 37,200 / C 38,400 / V 191,932
- **30D MFE/MAE:** 46.35% / -3.12%
- **90D MFE/MAE:** 46.35% / -19.27%
- **180D MFE/MAE:** 46.35% / -32.94%
- **180D peak/trough:** 2024-01-16 @ 56,200 / 2024-08-05 @ 25,750
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 008930 Hanmi Science — 4B / 2024-03-28

- **case_role:** `merger_scrapped_control_dispute_resolution`
- **evidence_family:** `shareholder_vote_merger_scrapped`
- **evidence:** Hanmi-OCI merger was scrapped after the shareholder vote and family-control dispute outcome. This is a damaged governance-event path, but not automatic operating hard 4C.
- **direct source:** Yonhap, 2024-03-28; KED Global — https://en.yna.co.kr/view/AEN20240328007700320
- **entry OHLCV:** O 41,350 / H 47,000 / L 38,000 / C 44,350 / V 2,969,887
- **30D MFE/MAE:** 5.98% / -29.54%
- **90D MFE/MAE:** 5.98% / -41.94%
- **180D MFE/MAE:** 18.38% / -41.94%
- **180D peak/trough:** 2024-10-30 @ 52,500 / 2024-08-05 @ 25,750
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 040300 YTN — Stage2-Actionable / 2023-10-23

- **case_role:** `public_stake_sale_control_premium`
- **evidence_family:** `eugene_wins_public_stake_bid`
- **evidence:** Eugene Group won the bid for a 30.95% stake held by public entities. The control-premium bridge was direct, but regulatory approval and operating media monetization remained separate.
- **direct source:** Yonhap, 2023-10-23, Eugene wins bid for YTN stake — https://en.yna.co.kr/view/AEN20231023003351320
- **entry OHLCV:** O 6,270 / H 6,600 / L 5,660 / C 6,000 / V 2,538,410
- **30D MFE/MAE:** 60.00% / -9.83%
- **90D MFE/MAE:** 60.00% / -17.17%
- **180D MFE/MAE:** 60.00% / -49.50%
- **180D peak/trough:** 2023-10-25 @ 9,600 / 2024-07-10 @ 3,030
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.

### 028260 Samsung C&T — Stage2 / 2024-02-15

- **case_role:** `activist_shareholder_return_proposal`
- **evidence_family:** `activist_buyback_dividend_proposal`
- **evidence:** Activist funds demanded share buybacks and higher dividends. The event was a governance/shareholder-return catalyst, but management opposed it and execution was not yet secured.
- **direct source:** Yonhap, 2024-02-15, activist proposals — https://en.yna.co.kr/view/AEN20240215003800320
- **entry OHLCV:** O 155,700 / H 161,000 / L 152,900 / C 156,300 / V 1,098,381
- **30D MFE/MAE:** 9.85% / -5.95%
- **90D MFE/MAE:** 9.85% / -17.15%
- **180D MFE/MAE:** 9.85% / -25.14%
- **180D peak/trough:** 2024-02-19 @ 171,700 / 2024-10-31 @ 117,000
- **residual read:** Governance/control-premium signal is real, but it should be routed through a tender/control cap before any operating Green. Operational Green requires post-event EPS/FCF/cash conversion, not only a control premium.


## 6. Residual contribution

```text
canonical_rule_candidate = C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1
sector_rule_candidate = L10_GOVERNANCE_EVENT_TO_OPERATING_RERATING_GATE_V1
loop_contribution_label = C32_governance_event_control_premium_cap_quality_repair
new_axis_proposed = no_global_axis
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, stage3_green_not_loosened
existing_axis_weakened = none
```

### Core residual

- Tender offers, control battles, activist proposals, public-stake sales, and shareholder-vote outcomes can be legitimate **Stage2 / Stage2-Actionable** catalysts.
- They should not automatically create **Stage3-Yellow** or **Stage3-Green**, even when 30D/90D/180D MFE is very large.
- C32 needs a **control-premium cap**: price path may be strong because the event price itself is strong, not because EPS/FCF/operating moat improved.
- Stage2-Actionable requires at least one direct event-execution bridge: signed tender terms, tender price, secured stake, creditor/seller approval, shareholder-vote result, regulatory approval path, buyback/cancellation mechanics, or confirmed transaction closing.
- Stage3-Yellow/Green require a second operating bridge after the governance event: realized capital return, sustained buyback cancellation, cash conversion, ROE/TBVPS accretion, operating margin conversion, post-acquisition integration economics, or durable earnings revision.
- Deal failure, shareholder-vote defeat, or tender premium fade should route first to **4B/watch** unless the operating thesis itself breaks.
- Hard 4C requires confirmed non-price thesis break: transaction collapse plus weak operating offset, accounting/trust damage, financing stress, legal/regulatory block, or governance outcome that impairs durable value creation.

## 7. Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff and requires non-price evidence for full 4B. C32 still needs a specific distinction:

```text
if canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:
    if trigger_evidence in [tender_offer, control_battle, activist_proposal, stake_sale, shareholder_vote]:
        allow_stage2_or_actionable = true only when event execution bridge exists
        block_stage3_green = true unless operating/cashflow bridge exists after event
        route_control_premium_extension_to_local_4b_watch = true
        route_deal_failure_to_4b_watch unless confirmed operating thesis break
```

This is not a global Green threshold change. It is an archetype-specific guardrail: **C32 price path is event-mechanical first, operating-rerating second.**

## 8. Raw component score simulation

```text
base_components = EPS/FCF, visibility, bottleneck/pricing, market_mispricing, valuation_rerating, capital_allocation, information_confidence
C32_expected_weight_shape = 12/18/5/20/25/15/5
```

| row type | expected component tilt | stage handling |
|---|---|---|
| tender/control offer with clear price and stake target | market_mispricing + valuation + information confidence | Stage2-Actionable allowed, Green blocked |
| self-tender/buyback defense | capital allocation + valuation, with trust/leverage penalty | local 4B/watch if price extended |
| preferred bidder without definitive agreement | information confidence partial, low operating visibility | Stage2 cap |
| deal collapse / vote defeat | information confidence down, valuation premium fade | 4B/watch unless hard operating break |
| activist proposal without management acceptance | capital allocation option value only | Stage2 cap |
| public-stake sale pending regulatory approval | control-premium route with approval dependency | Actionable cap, Green blocked |

## 9. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_01_010130_20240913", "symbol": "010130", "company_name": "Korea Zinc", "trigger_type": "Stage2-Actionable", "case_role": "control_premium_positive_price_path", "evidence_family": "hostile_tender_offer_initial", "entry_signal_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000.0, "entry_ohlcv": {"o": 660000.0, "h": 690000.0, "l": 655000.0, "c": 666000.0, "v": 586718}, "mfe_30d_pct": 131.68, "mae_30d_pct": -1.65, "mfe_90d_pct": 261.41, "mae_90d_pct": -1.65, "mfe_180d_pct": 261.41, "mae_180d_pct": -3.45, "peak_180d_date": "2024-12-06", "peak_180d_price": 2407000.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 643000.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/", "evidence_summary": "MBK Partners and Young Poong launched a tender offer for Korea Zinc shares; the event created a direct control-premium route but did not itself prove operating EPS/FCF rerating.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|010130|Stage2-Actionable|2024-09-13", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_02_010130_20241021", "symbol": "010130", "company_name": "Korea Zinc", "trigger_type": "4B", "case_role": "self_tender_legal_clearance_late_extension", "evidence_family": "court_buyback_clearance_self_tender", "entry_signal_date": "2024-10-21", "entry_date": "2024-10-21", "entry_price": 877000.0, "entry_ohlcv": {"o": 827000.0, "h": 889000.0, "l": 761000.0, "c": 877000.0, "v": 638694}, "mfe_30d_pct": 75.94, "mae_30d_pct": -13.23, "mfe_90d_pct": 174.46, "mae_90d_pct": -18.93, "mfe_180d_pct": 174.46, "mae_180d_pct": -26.68, "peak_180d_date": "2024-12-06", "peak_180d_price": 2407000.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 643000.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://www.reuters.com/markets/deals/korea-zinc-shares-surge-record-high-after-court-clears-hurdle-buyback-offer-2024-10-21/", "evidence_summary": "Court clearance for Korea Zinc’s buyback/self-tender extended the control battle and price, but also raised balance-sheet/leverage quality questions; this is local 4B/watch, not operating Green.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|010130|4B|2024-10-21", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_03_041510_20230210", "symbol": "041510", "company_name": "SM Entertainment", "trigger_type": "Stage2-Actionable", "case_role": "tender_competition_control_premium", "evidence_family": "hybe_stake_purchase_tender_offer", "entry_signal_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 114700.0, "entry_ohlcv": {"o": 115200.0, "h": 117000.0, "l": 107300.0, "c": 114700.0, "v": 8882805}, "mfe_30d_pct": 40.54, "mae_30d_pct": -9.24, "mfe_90d_pct": 40.54, "mae_90d_pct": -23.63, "mfe_180d_pct": 40.54, "mae_180d_pct": -23.63, "peak_180d_date": "2023-03-08", "peak_180d_price": 161200.0, "trough_180d_date": "2023-03-28", "trough_180d_price": 87600.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://www.kedglobal.com/mergers-acquisitions/newsView/ked202303120002", "evidence_summary": "HYBE agreed to buy Lee Soo-man’s 14.8% stake and launched a tender offer; this created a real control-premium route but remained governance/event-driven rather than repeat IP monetization proof.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|Stage2-Actionable|2023-02-10", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_04_041510_20230313", "symbol": "041510", "company_name": "SM Entertainment", "trigger_type": "4B", "case_role": "control_premium_fade_after_bidding_resolution", "evidence_family": "hybe_bid_failure_kakao_tender_resolution", "entry_signal_date": "2023-03-13", "entry_date": "2023-03-13", "entry_price": 113100.0, "entry_ohlcv": {"o": 135000.0, "h": 135000.0, "l": 111300.0, "c": 113100.0, "v": 5457572}, "mfe_30d_pct": 19.36, "mae_30d_pct": -22.55, "mfe_90d_pct": 19.36, "mae_90d_pct": -22.55, "mfe_180d_pct": 29.97, "mae_180d_pct": -25.02, "peak_180d_date": "2023-08-29", "peak_180d_price": 147000.0, "trough_180d_date": "2023-12-01", "trough_180d_price": 84800.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://en.yna.co.kr/view/AEN20230307003251320", "evidence_summary": "Kakao’s higher tender and HYBE’s failed tender shifted the control premium mechanics; the event path became a 4B/watch case rather than a durable operating-stage escalation.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|4B|2023-03-13", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_05_011200_20231219", "symbol": "011200", "company_name": "HMM", "trigger_type": "Stage2", "case_role": "privatization_preferred_bidder_without_closing", "evidence_family": "preferred_bidder_control_sale", "entry_signal_date": "2023-12-19", "entry_date": "2023-12-19", "entry_price": 18430.0, "entry_ohlcv": {"o": 16680.0, "h": 19220.0, "l": 16550.0, "c": 18430.0, "v": 24244550}, "mfe_30d_pct": 26.42, "mae_30d_pct": -10.2, "mfe_90d_pct": 26.42, "mae_90d_pct": -22.68, "mfe_180d_pct": 26.42, "mae_180d_pct": -22.68, "peak_180d_date": "2023-12-20", "peak_180d_price": 23300.0, "trough_180d_date": "2024-04-19", "trough_180d_price": 14250.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://en.yna.co.kr/view/AEN20231218009052320", "evidence_summary": "Harim-JKL was selected as preferred bidder for a controlling stake in HMM. The route was real but still dependent on definitive terms, creditor agreement, and closing.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|011200|Stage2|2023-12-19", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_06_011200_20240207", "symbol": "011200", "company_name": "HMM", "trigger_type": "4B", "case_role": "sale_breakdown_control_premium_reversal", "evidence_family": "deal_collapse_creditor_negotiation_failure", "entry_signal_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 19080.0, "entry_ohlcv": {"o": 19030.0, "h": 20200.0, "l": 17500.0, "c": 19080.0, "v": 5677567}, "mfe_30d_pct": 5.87, "mae_30d_pct": -18.45, "mfe_90d_pct": 5.87, "mae_90d_pct": -25.31, "mfe_180d_pct": 9.01, "mae_180d_pct": -25.31, "peak_180d_date": "2024-07-03", "peak_180d_price": 20800.0, "trough_180d_date": "2024-04-19", "trough_180d_price": 14250.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://en.yna.co.kr/view/AEN20240207001452320", "evidence_summary": "HMM sale negotiations collapsed after the Harim bid failed to reach final agreement. Governance premium broke, but shipping-cycle fundamentals remained separate, so this is 4B/watch rather than issuer hard 4C.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|011200|4B|2024-02-07", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_07_008930_20240112", "symbol": "008930", "company_name": "Hanmi Science", "trigger_type": "Stage2", "case_role": "family_control_merger_optional_route", "evidence_family": "hanmi_oci_integration_announcement", "entry_signal_date": "2024-01-12", "entry_date": "2024-01-12", "entry_price": 38400.0, "entry_ohlcv": {"o": 37300.0, "h": 38900.0, "l": 37200.0, "c": 38400.0, "v": 191932}, "mfe_30d_pct": 46.35, "mae_30d_pct": -3.12, "mfe_90d_pct": 46.35, "mae_90d_pct": -19.27, "mfe_180d_pct": 46.35, "mae_180d_pct": -32.94, "peak_180d_date": "2024-01-16", "peak_180d_price": 56200.0, "trough_180d_date": "2024-08-05", "trough_180d_price": 25750.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://en.yna.co.kr/view/AEN20240328007700320", "evidence_summary": "Hanmi Group and OCI announced an integration/merger plan. It created a control-structure and strategic optionality event, but operating/rerating bridge was still conditional.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|008930|Stage2|2024-01-12", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_08_008930_20240328", "symbol": "008930", "company_name": "Hanmi Science", "trigger_type": "4B", "case_role": "merger_scrapped_control_dispute_resolution", "evidence_family": "shareholder_vote_merger_scrapped", "entry_signal_date": "2024-03-28", "entry_date": "2024-03-28", "entry_price": 44350.0, "entry_ohlcv": {"o": 41350.0, "h": 47000.0, "l": 38000.0, "c": 44350.0, "v": 2969887}, "mfe_30d_pct": 5.98, "mae_30d_pct": -29.54, "mfe_90d_pct": 5.98, "mae_90d_pct": -41.94, "mfe_180d_pct": 18.38, "mae_180d_pct": -41.94, "peak_180d_date": "2024-10-30", "peak_180d_price": 52500.0, "trough_180d_date": "2024-08-05", "trough_180d_price": 25750.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://en.yna.co.kr/view/AEN20240328007700320", "evidence_summary": "Hanmi-OCI merger was scrapped after the shareholder vote and family-control dispute outcome. This is a damaged governance-event path, but not automatic operating hard 4C.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|008930|4B|2024-03-28", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_09_040300_20231023", "symbol": "040300", "company_name": "YTN", "trigger_type": "Stage2-Actionable", "case_role": "public_stake_sale_control_premium", "evidence_family": "eugene_wins_public_stake_bid", "entry_signal_date": "2023-10-23", "entry_date": "2023-10-23", "entry_price": 6000.0, "entry_ohlcv": {"o": 6270.0, "h": 6600.0, "l": 5660.0, "c": 6000.0, "v": 2538410}, "mfe_30d_pct": 60.0, "mae_30d_pct": -9.83, "mfe_90d_pct": 60.0, "mae_90d_pct": -17.17, "mfe_180d_pct": 60.0, "mae_180d_pct": -49.5, "peak_180d_date": "2023-10-25", "peak_180d_price": 9600.0, "trough_180d_date": "2024-07-10", "trough_180d_price": 3030.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://en.yna.co.kr/view/AEN20231023003351320", "evidence_summary": "Eugene Group won the bid for a 30.95% stake held by public entities. The control-premium bridge was direct, but regulatory approval and operating media monetization remained separate.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|040300|Stage2-Actionable|2023-10-23", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R12", "selected_loop": 222, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1", "case_id": "C32_R12_222_10_028260_20240215", "symbol": "028260", "company_name": "Samsung C&T", "trigger_type": "Stage2", "case_role": "activist_shareholder_return_proposal", "evidence_family": "activist_buyback_dividend_proposal", "entry_signal_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 156300.0, "entry_ohlcv": {"o": 155700.0, "h": 161000.0, "l": 152900.0, "c": 156300.0, "v": 1098381}, "mfe_30d_pct": 9.85, "mae_30d_pct": -5.95, "mfe_90d_pct": 9.85, "mae_90d_pct": -17.15, "mfe_180d_pct": 9.85, "mae_180d_pct": -25.14, "peak_180d_date": "2024-02-19", "peak_180d_price": 171700.0, "trough_180d_date": "2024-10-31", "trough_180d_price": 117000.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "insufficient_forward_window_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://en.yna.co.kr/view/AEN20240215003800320", "evidence_summary": "Activist funds demanded share buybacks and higher dividends. The event was a governance/shareholder-return catalyst, but management opposed it and execution was not yet secured.", "hard_duplicate_key": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|028260|Stage2|2024-02-15", "production_scoring_changed": false, "shadow_weight_only": true}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD alone.
Batch-ingest this file with other V12 results, then evaluate whether C32 needs an archetype-scoped guardrail:

C32_CONTROL_PREMIUM_TENDER_CAP_AND_OPERATIONAL_GREEN_BLOCKER_GATE_V1

Candidate behavior:
1. Permit Stage2 / Stage2-Actionable for tender, control battle, public-stake sale, activist proposal, shareholder vote, or buyback/cancellation event only when the event terms/execution bridge are explicit.
2. Cap Stage3-Yellow/Green until operating or cashflow conversion appears after the governance event.
3. Route late control-premium extension and deal-resolution volatility to local 4B/watch.
4. Route deal collapse to hard 4C only when weak operating offset or governance/accounting/financing impairment is confirmed.
5. Preserve current global Green strictness. Do not loosen Stage3-Green globally.
```

## 11. Batch Ingest Self-Audit

```text
standard_v12_filename = pass
selected_round_matches_filename = pass
selected_loop_matches_filename = pass
large_sector_round_pair = pass
canonical_archetype_valid = pass
trigger_type_canonical_stage_label = pass
stock_web_actual_1d_ohlcv_used = pass
entry_price_present_every_trigger = pass
mfe_mae_30_90_180_present_every_trigger = pass
corporate_action_window_checked = pass
forward_window_180d_available = pass
jsonl_rows_present = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 12. Next Research State

```text
completed_round = R12
completed_loop = 222
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality repair / C32 governance event direct evidence
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes =
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_CASHFLOW_EXECUTION_REPAIR
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
