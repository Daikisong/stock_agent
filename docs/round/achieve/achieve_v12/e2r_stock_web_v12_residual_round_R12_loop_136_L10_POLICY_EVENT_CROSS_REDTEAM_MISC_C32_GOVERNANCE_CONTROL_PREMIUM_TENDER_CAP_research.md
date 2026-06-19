# E2R Stock-Web v12 Residual Research — R12 / C32 Governance Control Premium Tender Cap

## 0. Metadata

```json
{
  "doc_type": "stock_web_v12_residual_calibration_research",
  "selected_round": "R12",
  "selected_loop": 136,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 0/1 quality repair — C32 governance/control-premium/tender-cap event bridge, direct URL/proxy repair, tender cap vs shareholder-protection split",
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_SHAREHOLDER_PROTECTION_GATE",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "price_basis": "tradable_raw",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "created_at_kst": "2026-06-16"
}
```

## 1. Selection / No-Repeat basis

- `V12_Research_No_Repeat_Index.md` 누적 장부 기준 C32는 이미 360 representative rows / 66 symbols / positive-counter 25·50 / 4B·4C 52·12로 수량은 충분하지만, `evidence_url_pending`와 `source_proxy_only` 품질 보강이 전체 우선순위다.
- 이번 실행은 직전 C31 정책/보조금 축과 겹치지 않게 R12/L10/C32를 선택했다.
- 선택 목적은 `control premium`과 `minority-shareholder value participation`을 분리하는 것이다. C32에서 tender headline은 문패일 뿐이고, E2R이 인정해야 하는 것은 일반주주가 실제로 그 프리미엄에 참여했는지, 혹은 지배주주·PEF·인수자가 프리미엄을 가져가고 상장주주에게 MAE만 남겼는지다.

```text
selected_round = R12
selected_loop = 136
selected_priority_bucket = Priority 0/1 quality repair — C32 governance/control-premium/tender-cap event bridge, direct URL/proxy repair, tender cap vs shareholder-protection split
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 2. Price atlas confirmation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

All trigger rows below use Stock-Web tradable rows and include complete `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct` fields.

## 3. Novelty / duplicate check

```text
new_independent_case_count = 8
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 8
hard_duplicate_key_policy = canonical_archetype_id + symbol + trigger_type + entry_date
exact_duplicate_key_reused = false
source_proxy_only_count = 7
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
```

The known overused C32 names such as SM, Kakao, HYBE, and DB HiTek are intentionally used only with event-date separation and distinct trigger families: tender result/proration, target legal probe, acquirer capital-discipline withdrawal, acquirer regulatory overhang, founder arrest, first greenmail/control-premium break, and late-repeat governance complaint.

## 4. Case table

| case_id | symbol | company | trigger_date | trigger_type | outcome | MFE90 | MAE90 | stage read |
|---|---:|---|---|---|---|---:|---:|---|
| C32_R12L136_001 | 041510 | SM Entertainment | 2023-03-28 | Stage2-Actionable | positive_target_post_tender_control_stabilization | 51.33 | -7.1 | Stage2-Actionable. Confirmed control-stake outcome is real evidence, but Green needs post-tender operating governance and monetization bridge because the tender price can also cap upside. |
| C32_R12L136_002 | 041510 | SM Entertainment | 2023-04-18 | Stage4B | counterexample_legal_overhang_not_hard_4c | 43.14 | -3.99 | Stage4B. Investigation headlines after a control battle should block Green, but hard 4C requires confirmed transaction collapse, delisting harm, financing break, or irreversible minority-shareholder value destruction. |
| C32_R12L136_003 | 352820 | HYBE | 2023-03-12 | Stage3-Yellow | positive_acquirer_capital_discipline_reopen | 64.82 | -10.18 | Stage3-Yellow. C32 should distinguish target tender premium from acquirer capital discipline: withdrawal from an overpriced fight can reopen positive stages if capital-allocation logic is explicit and later price confirms. |
| C32_R12L136_004 | 035720 | Kakao | 2023-03-28 | Stage4C | counterexample_acquirer_control_premium_financing_and_regulatory_overhang | 1.48 | -23.15 | Stage4C. For acquirers, a tender-win headline can be a thesis break if control premium, governance/regulatory scrutiny, and weak immediate monetization combine while price confirms high downside. |
| C32_R12L136_005 | 035720 | Kakao | 2023-08-10 | Stage4C | counterexample_regulatory_probe_deep_mae | 4.56 | -29.09 | Stage4C until legal clarity. Governance/legal break is company-level and linked to the transaction itself; later rebound should not retroactively erase the 90D protection value. |
| C32_R12L136_006 | 035720 | Kakao | 2024-07-23 | Stage4B | counterexample_hard_4c_requires_persistence_test | 21.24 | -16.22 | Stage4B. Founder arrest is a hard positive-stage cap, but C32 hard 4C should require persistent legal/operating conversion rather than headline severity alone. |
| C32_R12L136_007 | 000990 | DB HiTek | 2024-01-03 | Stage4C | counterexample_greenmail_control_premium_minorities_harmed | 3.81 | -23.71 | Stage4C. A premium block sale that strengthens controller ownership while public holders absorb downside should route to hard 4C unless there is explicit minority-compensation or value-return bridge. |
| C32_R12L136_008 | 000990 | DB HiTek | 2024-11-19 | Stage4B | positive_4c_overblock_exception_after_governance_discount_priced | 48.24 | -14.41 | Stage4B, not hard 4C. Repeated governance-negative news after the first break should require fresh incremental damage; otherwise it can become a false hard-4C overblock at depressed prices. |


## 5. Trigger rows JSONL

```jsonl
{"case_id":"C32_R12L136_001","symbol":"041510","company":"SM Entertainment","trigger_date":"2023-03-28","entry_date":"2023-03-28","entry_price":94300,"trigger_type":"Stage2-Actionable","case_outcome":"positive_target_post_tender_control_stabilization","evidence_family":"kakao_tender_offer_result_proration_control_stake_confirmed","source_quality":"major_wire_direct_event","evidence_url":"https://www.reuters.com/business/media-telecom/kakao-reaches-40-stake-k-pop-agency-sm-hybe-keeps-88-2023-03-28/","evidence_summary":"Kakao's tender offer for 35% of SM at 150,000 won was oversubscribed and Kakao/Kakao Entertainment reached about a 40% stake. For the target, the tender battle converted from rumor into a confirmed control-stake event, but because the tender price also creates a ceiling, C32 should still delay Green until minority-shareholder economics and post-control earnings path are clear.","bridge_tags":"tender_offer_result,control_stake_confirmed,minority_proration,tender_cap,post_control_bridge","entry_row":"d=2023-03-28,o=88200,h=95700,l=87600,c=94300,v=2789272","peak_30_date":"2023-05-03","peak_30_price":116600,"trough_30_date":"2023-03-28","trough_30_price":87600,"peak_90_date":"2023-08-03","peak_90_price":142700,"trough_90_date":"2023-03-28","trough_90_price":87600,"peak_180_date":"2023-08-29","peak_180_price":147000,"trough_180_date":"2023-12-05","trough_180_price":82500,"MFE_30D_pct":23.65,"MAE_30D_pct":-7.1,"MFE_90D_pct":51.33,"MAE_90D_pct":-7.1,"MFE_180D_pct":55.89,"MAE_180D_pct":-12.51,"stage_read":"Stage2-Actionable. Confirmed control-stake outcome is real evidence, but Green needs post-tender operating governance and monetization bridge because the tender price can also cap upside.","current_profile_error":"too_late_if_all_tender_cap_events_are_blocked_after_control_stake_confirmed","same_entry_group":"C32_SM_20230328_kakao_40pct_prorated_tender_result","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false}
{"case_id":"C32_R12L136_002","symbol":"041510","company":"SM Entertainment","trigger_date":"2023-04-18","entry_date":"2023-04-18","entry_price":102700,"trigger_type":"Stage4B","case_outcome":"counterexample_legal_overhang_not_hard_4c","evidence_family":"sm_kakao_market_manipulation_probe_company_level_legal_overhang","source_quality":"major_news_direct_event","evidence_url":"https://koreajoongangdaily.joins.com/2023/04/18/business/industry/SM-Kakao/20230418122809736.html","evidence_summary":"SM was raided in the post-tender market-manipulation probe around the Kakao-HYBE control battle. The event adds governance/legal overhang, but the later price path still produced large MFE; therefore C32 should cap positive stages with 4B watch rather than automatically hard-4C every investigation headline for the target.","bridge_tags":"legal_probe,market_manipulation_allegation,post_tender_overhang,4b_not_4c,governance_noise","entry_row":"d=2023-04-18,o=106100,h=109100,l=101300,c=102700,v=564128","peak_30_date":"2023-05-17","peak_30_price":119100,"trough_30_date":"2023-04-21","trough_30_price":98800,"peak_90_date":"2023-08-29","peak_90_price":147000,"trough_90_date":"2023-06-05","trough_90_price":98600,"peak_180_date":"2023-08-29","peak_180_price":147000,"trough_180_date":"2023-12-05","trough_180_price":82500,"MFE_30D_pct":15.97,"MAE_30D_pct":-3.8,"MFE_90D_pct":43.14,"MAE_90D_pct":-3.99,"MFE_180D_pct":43.14,"MAE_180D_pct":-19.67,"stage_read":"Stage4B. Investigation headlines after a control battle should block Green, but hard 4C requires confirmed transaction collapse, delisting harm, financing break, or irreversible minority-shareholder value destruction.","current_profile_error":"overblock_if_legal_probe_headline_routes_target_to_4c_without_price_and_operating_break","same_entry_group":"C32_SM_20230418_post_tender_probe_4b_not_4c","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false}
{"case_id":"C32_R12L136_003","symbol":"352820","company":"HYBE","trigger_date":"2023-03-12","entry_date":"2023-03-13","entry_price":189600,"trigger_type":"Stage3-Yellow","case_outcome":"positive_acquirer_capital_discipline_reopen","evidence_family":"hybe_drops_sm_takeover_after_price_exceeds_fair_range","source_quality":"major_wire_direct_company_statement","evidence_url":"https://www.reuters.com/markets/deals/hybe-drops-bid-take-over-sm-entertainment-2023-03-12/","evidence_summary":"HYBE dropped its SM takeover bid after stating the acquisition price exceeded a fair range as competition intensified. For an acquirer, abandoning an over-expensive control-premium battle can be a positive governance/capital-allocation signal, especially when subsequent price action validates the discipline.","bridge_tags":"acquirer_capital_discipline,tender_withdrawal,overpay_avoidance,governance_reopen,capital_allocation","entry_row":"d=2023-03-13,o=185600,h=196600,l=182600,c=189600,v=849993","peak_30_date":"2023-04-17","peak_30_price":270000,"trough_30_date":"2023-03-15","trough_30_price":170300,"peak_90_date":"2023-06-22","peak_90_price":312500,"trough_90_date":"2023-03-15","trough_90_price":170300,"peak_180_date":"2023-06-22","peak_180_price":312500,"trough_180_date":"2023-03-15","trough_180_price":170300,"MFE_30D_pct":42.41,"MAE_30D_pct":-10.18,"MFE_90D_pct":64.82,"MAE_90D_pct":-10.18,"MFE_180D_pct":64.82,"MAE_180D_pct":-10.18,"stage_read":"Stage3-Yellow. C32 should distinguish target tender premium from acquirer capital discipline: withdrawal from an overpriced fight can reopen positive stages if capital-allocation logic is explicit and later price confirms.","current_profile_error":"false_negative_if_all_control_battle_withdrawals_are_treated_as_failed_mna","same_entry_group":"C32_HYBE_20230313_sm_bid_withdrawal_capital_discipline","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false}
{"case_id":"C32_R12L136_004","symbol":"035720","company":"Kakao","trigger_date":"2023-03-28","entry_date":"2023-03-28","entry_price":60700,"trigger_type":"Stage4C","case_outcome":"counterexample_acquirer_control_premium_financing_and_regulatory_overhang","evidence_family":"kakao_reaches_40pct_sm_after_oversubscribed_tender_proration","source_quality":"major_wire_direct_event","evidence_url":"https://www.reuters.com/business/media-telecom/kakao-reaches-40-stake-k-pop-agency-sm-hybe-keeps-88-2023-03-28/","evidence_summary":"Kakao reached roughly 40% of SM after a tender offer that was oversubscribed and prorated. For the acquirer, the event is not automatically positive: it combines control-premium cash outflow, integration uncertainty, and later regulatory risk. The price path showed very low MFE and deep 180D MAE.","bridge_tags":"acquirer_overhang,control_premium_cash_out,proration,regulatory_follow_through,hard_4c_candidate","entry_row":"d=2023-03-28,o=60600,h=61000,l=59900,c=60700,v=1326335","peak_30_date":"2023-04-03","peak_30_price":61600,"trough_30_date":"2023-04-27","trough_30_price":55300,"peak_90_date":"2023-04-03","peak_90_price":61600,"trough_90_date":"2023-07-26","trough_90_price":46650,"peak_180_date":"2023-04-03","peak_180_price":61600,"trough_180_date":"2023-10-27","trough_180_price":37300,"MFE_30D_pct":1.48,"MAE_30D_pct":-8.9,"MFE_90D_pct":1.48,"MAE_90D_pct":-23.15,"MFE_180D_pct":1.48,"MAE_180D_pct":-38.55,"stage_read":"Stage4C. For acquirers, a tender-win headline can be a thesis break if control premium, governance/regulatory scrutiny, and weak immediate monetization combine while price confirms high downside.","current_profile_error":"false_positive_if_acquirer_control_stake_headline_is_scored_like_target_tender_premium","same_entry_group":"C32_KAKAO_20230328_sm_tender_win_acquirer_overhang","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false}
{"case_id":"C32_R12L136_005","symbol":"035720","company":"Kakao","trigger_date":"2023-08-10","entry_date":"2023-08-10","entry_price":52600,"trigger_type":"Stage4C","case_outcome":"counterexample_regulatory_probe_deep_mae","evidence_family":"fss_raid_founder_office_sm_stock_manipulation_probe","source_quality":"official_regulator_action_reported_by_yonhap","evidence_url":"https://en.yna.co.kr/view/AEN20230810009200320","evidence_summary":"The FSS raided Kakao founder Kim Beom-su's office over suspected stock manipulation during the SM control battle. Kakao had become the largest shareholder after the takeover battle, but the probe transformed the control-premium event into a governance/legal-risk event. Price path showed almost no 30D/90D MFE and deep MAE before later rebound.","bridge_tags":"regulatory_probe,fss_raid,stock_manipulation_allegation,governance_legal_break,deep_mae","entry_row":"d=2023-08-10,o=52300,h=53100,l=51900,c=52600,v=1645198","peak_30_date":"2023-08-10","peak_30_price":53100,"trough_30_date":"2023-09-22","trough_30_price":44800,"peak_90_date":"2023-12-15","peak_90_price":55000,"trough_90_date":"2023-10-27","trough_90_price":37300,"peak_180_date":"2024-01-11","peak_180_price":61900,"trough_180_date":"2023-10-27","trough_180_price":37300,"MFE_30D_pct":0.95,"MAE_30D_pct":-14.83,"MFE_90D_pct":4.56,"MAE_90D_pct":-29.09,"MFE_180D_pct":17.68,"MAE_180D_pct":-29.09,"stage_read":"Stage4C until legal clarity. Governance/legal break is company-level and linked to the transaction itself; later rebound should not retroactively erase the 90D protection value.","current_profile_error":"too_late_if_regulatory_probe_is_classified_only_as_information_noise","same_entry_group":"C32_KAKAO_20230810_fss_raid_sm_probe","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":false,"evidence_url_pending":false}
{"case_id":"C32_R12L136_006","symbol":"035720","company":"Kakao","trigger_date":"2024-07-23","entry_date":"2024-07-23","entry_price":38850,"trigger_type":"Stage4B","case_outcome":"counterexample_hard_4c_requires_persistence_test","evidence_family":"founder_arrest_stock_manipulation_case_regulatory_expansion_risk","source_quality":"major_wire_direct_legal_event","evidence_url":"https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/","evidence_summary":"Kim Beom-su was arrested on accusations related to SM stock manipulation; Reuters noted Kakao shares fell and regulatory scrutiny could affect AI/expansion plans. The event is serious enough to block positive stages, but the forward path had material rebound; therefore the C32 rule should use 4B unless the legal overhang converts into financing, license, or operating-rights break.","bridge_tags":"founder_arrest,legal_overhang,regulatory_expansion_risk,4b_vs_4c_persistence_test","entry_row":"d=2024-07-23,o=40500,h=41450,l=38700,c=38850,v=4258210","peak_30_date":"2024-07-23","peak_30_price":41450,"trough_30_date":"2024-09-04","trough_30_price":33950,"peak_90_date":"2024-12-04","peak_90_price":47100,"trough_90_date":"2024-11-14","trough_90_price":32550,"peak_180_date":"2024-12-04","peak_180_price":47100,"trough_180_date":"2024-11-14","trough_180_price":32550,"MFE_30D_pct":6.69,"MAE_30D_pct":-12.61,"MFE_90D_pct":21.24,"MAE_90D_pct":-16.22,"MFE_180D_pct":21.24,"MAE_180D_pct":-16.22,"stage_read":"Stage4B. Founder arrest is a hard positive-stage cap, but C32 hard 4C should require persistent legal/operating conversion rather than headline severity alone.","current_profile_error":"overblock_if_founder_arrest_always_routes_to_hard_4c_without_forward_rebound_exception","same_entry_group":"C32_KAKAO_20240723_founder_arrest_4b_persistence_test","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false}
{"case_id":"C32_R12L136_007","symbol":"000990","company":"DB HiTek","trigger_date":"2024-01-03","entry_date":"2024-01-03","entry_price":52500,"trigger_type":"Stage4C","case_outcome":"counterexample_greenmail_control_premium_minorities_harmed","evidence_family":"kcgi_block_sale_to_db_inc_control_reinforcement_minority_shareholder_loss","source_quality":"major_news_plus_followup_complaint","evidence_url":"https://alphabiz.co.kr/news/print.html?newsid=98021 ; https://www.mk.co.kr/en/stock/11172641","evidence_summary":"KCGI sold a 5.6% DB HiTek stake to DB Inc in a block deal at 66,000 won per share, raising DB Inc's stake from 12.42% to 18% while KCGI's stake fell sharply. Later minority shareholders alleged greenmail-like conduct because the premium sale strengthened control but ordinary shareholders bore the post-deal price damage. This is a C32 minority-protection break, not normal semiconductor beta.","bridge_tags":"greenmail_claim,block_deal,control_reinforcement,minority_shareholder_harm,hard_4c","entry_row":"d=2024-01-03,o=53900,h=54500,l=52400,c=52500,v=843708","peak_30_date":"2024-01-03","peak_30_price":54500,"trough_30_date":"2024-02-14","trough_30_price":48000,"peak_90_date":"2024-01-03","peak_90_price":54500,"trough_90_date":"2024-04-16","trough_90_price":40050,"peak_180_date":"2024-06-20","peak_180_price":58900,"trough_180_date":"2024-09-09","trough_180_price":35200,"MFE_30D_pct":3.81,"MAE_30D_pct":-8.57,"MFE_90D_pct":3.81,"MAE_90D_pct":-23.71,"MFE_180D_pct":12.19,"MAE_180D_pct":-32.95,"stage_read":"Stage4C. A premium block sale that strengthens controller ownership while public holders absorb downside should route to hard 4C unless there is explicit minority-compensation or value-return bridge.","current_profile_error":"false_stage2_if_control_premium_is_counted_without_minority_value_participation","same_entry_group":"C32_DBHITEK_20240103_kcgi_block_sale_greenmail_claim","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false}
{"case_id":"C32_R12L136_008","symbol":"000990","company":"DB HiTek","trigger_date":"2024-11-19","entry_date":"2024-11-19","entry_price":34000,"trigger_type":"Stage4B","case_outcome":"positive_4c_overblock_exception_after_governance_discount_priced","evidence_family":"minority_shareholder_complaint_greenmail_followup_low_base_rebound_exception","source_quality":"major_news_followup","evidence_url":"https://www.mk.co.kr/en/stock/11172641 ; https://www.asiae.co.kr/en/article/2024111920053169108","evidence_summary":"Minority shareholders filed complaints claiming KCGI's DB HiTek trade harmed ordinary holders. The headline is governance-negative, but by late 2024 the price already reflected much of the governance discount and the forward path recovered strongly. This is a holdout showing why C32 should separate first-break hard 4C from late-repeat governance-noise overblocking.","bridge_tags":"minority_complaint,late_repeat_governance_noise,priced_discount,rebound_exception,4b_not_4c","entry_row":"d=2024-11-19,o=31850,h=34150,l=31850,c=34000,v=309257","peak_30_date":"2024-12-11","peak_30_price":35750,"trough_30_date":"2024-12-09","trough_30_price":29100,"peak_90_date":"2025-03-21","peak_90_price":50400,"trough_90_date":"2024-12-09","trough_90_price":29100,"peak_180_date":"2025-03-21","peak_180_price":50400,"trough_180_date":"2024-12-09","trough_180_price":29100,"MFE_30D_pct":5.15,"MAE_30D_pct":-14.41,"MFE_90D_pct":48.24,"MAE_90D_pct":-14.41,"MFE_180D_pct":48.24,"MAE_180D_pct":-14.41,"stage_read":"Stage4B, not hard 4C. Repeated governance-negative news after the first break should require fresh incremental damage; otherwise it can become a false hard-4C overblock at depressed prices.","current_profile_error":"overblock_if_late_repeat_governance_complaint_is_scored_like_first_control_premium_break","same_entry_group":"C32_DBHITEK_20241119_minority_complaint_rebound_exception","representative_for_aggregate":true,"calibration_usable":true,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","forward_window_basis":"Stock-Web tradable rows; entry row inclusive; max high/min low over 30/90/180 trading-row windows","corporate_action_contaminated_180D_window":false,"source_proxy_only":true,"evidence_url_pending":false}
```

## 6. Raw component score simulation

Weights shown in component order `EPS/Vis/Bott/Mis/Val/Cap/Info`. Scores are shadow-only research diagnostics, not production scoring changes.

| case_id | EPS | Vis | Bott | Mis | Val | Cap | Info | risk_penalty | simulated_total | current_profile_error |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C32_R12L136_001 | 10 | 22 | 4 | 20 | 22 | 16 | 8 | -4 | 98 | too_late_if_all_tender_cap_events_are_blocked_after_control_stake_confirmed |
| C32_R12L136_002 | 8 | 15 | 3 | 12 | 14 | 10 | 22 | -16 | 68 | overblock_if_legal_probe_headline_routes_target_to_4c_without_price_and_operating_break |
| C32_R12L136_003 | 14 | 24 | 4 | 14 | 10 | 22 | 10 | -6 | 92 | false_negative_if_all_control_battle_withdrawals_are_treated_as_failed_mna |
| C32_R12L136_004 | 6 | 14 | 3 | 6 | 8 | 6 | 24 | -22 | 45 | false_positive_if_acquirer_control_stake_headline_is_scored_like_target_tender_premium |
| C32_R12L136_005 | 5 | 12 | 3 | 5 | 7 | 4 | 30 | -24 | 42 | too_late_if_regulatory_probe_is_classified_only_as_information_noise |
| C32_R12L136_006 | 7 | 13 | 3 | 8 | 8 | 7 | 28 | -20 | 54 | overblock_if_founder_arrest_always_routes_to_hard_4c_without_forward_rebound_exception |
| C32_R12L136_007 | 5 | 10 | 3 | 4 | 7 | 5 | 32 | -26 | 40 | false_stage2_if_control_premium_is_counted_without_minority_value_participation |
| C32_R12L136_008 | 8 | 15 | 3 | 8 | 8 | 9 | 27 | -14 | 64 | overblock_if_late_repeat_governance_complaint_is_scored_like_first_control_premium_break |


## 7. Stage transition / residual read

### 7.1 Target tender premium is not the same as acquirer control-premium cost

SM target rows show why C32 needs two books. On the target side, a confirmed tender/control-stake outcome can be Stage2-Actionable when general shareholders can participate in a cash offer or when post-control governance stabilizes. On the acquirer side, the same tender can be 4B/4C if it consumes cash, raises legal scrutiny, and lacks near-term revenue or capital-return bridge.

### 7.2 Tender cap is a ceiling, not a floor

The 150,000 won SM tender price looked like a lighthouse, but for late entrants it could also become a ceiling. C32 should not convert tender price into Green unless there is a post-tender operating bridge: monetization, governance stability, buyback/cancellation, or clear shareholder-return participation.

### 7.3 Governance/legal overhang needs a persistence test

SM's 2023-04-18 probe row and Kakao's 2024-07-23 founder-arrest row show the difference between 4B and 4C. Severe headlines should block Green immediately, but hard 4C should require persistence: legal conversion into fines/financing/operating restrictions, transaction collapse, license impairment, or shareholder-value transfer confirmed by price and non-price evidence.

### 7.4 Minority-shareholder participation is the missing C32 bridge

DB HiTek is the cleanest C32 failure path in this set. A control-premium block deal may be good for the selling activist and the controller, but it can be bad for public holders if the premium is private and the controller's stake rises while the listed market price absorbs downside. C32 should ask: who receives the premium, and who keeps the MAE?

## 8. Aggregate / calibration summary

```json
{
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "fine_archetype_id": "CONTROL_PREMIUM_TENDER_CAP_SHAREHOLDER_PROTECTION_GATE",
  "calibration_usable_trigger_count": 8,
  "positive_case_count": 3,
  "counterexample_count": 5,
  "stage4b_case_count": 3,
  "stage4c_case_count": 3,
  "source_proxy_only_count": 7,
  "evidence_url_pending_count": 0,
  "rows_missing_required_mfe_mae": 0,
  "current_profile_error_count": 7,
  "diversity_score_summary": "4 symbols / 8 trigger families / target-vs-acquirer split / tender-cap vs hard-4C persistence split"
}
```

## 9. Shadow rule candidate

```yaml
new_axis_proposed: C32_CONTROL_PREMIUM_MINORITY_PARTICIPATION_GATE
production_scoring_changed: false
shadow_weight_only: true
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
  - information_confidence_gate
existing_axis_weakened: null
suggested_shadow_weight_delta:
  before_EPS_Vis_Bott_Mis_Val_Cap_Info: 12/18/5/20/25/15/5
  after_EPS_Vis_Bott_Mis_Val_Cap_Info: 10/20/5/16/22/18/9
  delta: -2/+2/0/-4/-3/+3/+4
```

### Rule candidate wording

For `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`, do not open Stage2-Actionable or Green on `tender offer`, `control premium`, `activist`, `governance reform`, `M&A battle`, or `white knight` vocabulary alone.

Require at least two of the following before positive stages:

1. general/minority shareholders can directly participate in the premium,
2. tender/buyback/cancellation terms are quantified and board-approved,
3. control change improves capital allocation or removes overpay risk,
4. post-control operating/monetization bridge is visible,
5. legal/regulatory overhang is cleared or clearly bounded,
6. capital return/per-share value is explicit rather than private-block-deal only.

Route to Stage4B/Stage4C when at least two of the following appear:

1. acquirer pays a high control premium with weak monetization bridge,
2. tender price creates a cap while public holders face proration or post-tender liquidity risk,
3. activist/controller captures a private premium not shared with ordinary holders,
4. regulatory probe/arrest/indictment connects directly to the transaction,
5. price path confirms low MFE and deep 90D/180D MAE,
6. legal or financing overhang persists beyond the first headline.

## 10. Validation scope

```text
validation_scope = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
live_candidate_mode = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
brokerage_api_allowed = false
auto_trading_allowed = false
price_route_hunt_allowed = false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not re-run live discovery. Read this MD as one v12 residual calibration result. Extract all JSONL trigger rows, validate complete 30/90/180D MFE/MAE fields, deduplicate on canonical_archetype_id + symbol + trigger_type + entry_date, and aggregate under C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / L10_POLICY_EVENT_CROSS_REDTEAM_MISC.

Evaluate the shadow-only rule candidate C32_CONTROL_PREMIUM_MINORITY_PARTICIPATION_GATE. If accepted, implement only as a canonical-archetype-specific scoring/profile patch. Do not loosen global Stage3-Green. Strengthen Stage2 bridge, 4B watch, hard-4C confirmation, drawdown-aware confirmation, and information-confidence gates for C32.
```

## 12. Completion state

```text
completed_round = R12
completed_loop = 136
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C32 governance/control-premium/tender-cap event bridge, direct URL/proxy repair, tender cap vs shareholder-protection split
next_recommended_archetypes = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION; R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW; C05_EPC_MEGA_CONTRACT_MARGIN_GAP; C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
