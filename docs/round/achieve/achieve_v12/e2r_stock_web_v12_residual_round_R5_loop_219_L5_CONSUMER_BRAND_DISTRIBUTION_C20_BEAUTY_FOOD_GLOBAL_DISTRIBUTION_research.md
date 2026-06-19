# E2R Stock-Web v12 Residual Research — R5 / L5 / C20

```text
selected_round: R5
selected_loop: 219
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 URL/proxy quality + L5 balance continuation after C18/C19
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1
research_session: post_calibrated_sector_archetype_residual_research
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection rationale

The v12 main prompt requires `coverage_index_first`, actual Songdaiki/stock-web 1D OHLCV rows, 30/90/180D MFE·MAE for every usable trigger, canonical stage labels, and no stock_agent code patching. The No-Repeat Index now says every C01~C32 archetype exceeds 80 representative rows, so this loop is not raw row-filling. It is direct URL / source quality and residual error cleanup.

Recent session output already refreshed R5/C18 and R5/C19. This loop completes the L5 consumer triad with C20, using K-beauty global distribution / ODM / brand overseas expansion rows. The goal is to separate true repeatable channel/reorder bridges from one-quarter export heat, COSRX/China-offset ambiguity, or single-product virality.

## 2. Price source validation

- manifest: `atlas/manifest.json`
- max_date: `2026-02-20`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- tradable columns: `d,o,h,l,c,v,a,mc,s,m`
- price adjustment: `raw_unadjusted_marcap`
- default blocked condition: corporate-action contaminated forward windows are not used for calibration.

All usable rows below use tradable shards only. Corporate-action profile checks are recorded in each case. APR's 2024 post-IPO window has a 2024-10-31 corporate-action candidate, so this loop deliberately uses the 2025-05-08 direct earnings row instead.

## 3. Batch summary

```text
new_independent_case_count: 7
new_independent_trigger_count: 7
unique_symbol_count: 7

stage2_actionable_count: 5
stage4b_count: 2
stage4c_count: 0
positive_case_count: 5
counterexample_or_guardrail_count: 2
high_MAE_180D_count: 5

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 4. Trigger table

| symbol | name | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| 257720 | Silicon2 | Stage2-Actionable | 2024-05-16 | 28,900 | 87.54/-10.38 | 87.54/-10.38 | 87.54/-19.38 | 2024-06-19 | 2024-12-09 |
| 192820 | Cosmax | Stage2-Actionable | 2024-05-13 | 157,700 | 31.90/-6.28 | 31.90/-26.44 | 31.90/-26.44 | 2024-06-14 | 2024-08-13 |
| 161890 | Kolmar Korea | Stage2-Actionable | 2024-08-09 | 66,300 | 17.80/-8.90 | 18.70/-25.26 | 32.73/-25.26 | 2025-05-09 | 2024-12-09 |
| 278470 | APR | Stage2-Actionable | 2025-05-08 | 98,400 | 46.14/-22.56 | 145.43/-22.56 | 198.27/-22.56 | 2026-01-22 | 2025-05-08 |
| 018290 | VT | Stage2-Actionable | 2025-02-27 | 35,300 | 7.51/-16.86 | 29.04/-16.86 | 29.04/-43.97 | 2025-06-05 | 2025-11-24 |
| 090430 | Amorepacific | Stage4B | 2024-08-07 | 124,500 | 20.40/-6.91 | 26.91/-20.08 | 26.91/-20.08 | 2024-09-27 | 2024-12-09 |
| 051900 | LG H&H | Stage4B | 2024-07-26 | 351,000 | 4.27/-8.55 | 11.54/-11.82 | 11.54/-17.38 | 2024-09-27 | 2025-04-09 |

## 5. Case notes


### Case 1. 257720 Silicon2 — Stage2-Actionable

- duplicate key: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 257720 + Stage2-Actionable + 2024-05-16`
- trigger family: `SILICON2_GLOBAL_DISTRIBUTION_REPEAT_REORDER`
- evidence: Direct K-beauty export distributor, Q1 sales/OP jump, overseas warehouse/channel expansion.
- source URLs: https://www.asiae.co.kr/en/article/2024070210301137687, https://www.siliconii.com/en/sub/sub03_01.php?boardid=newsen&category=&idx=5&mode=view&offset=56&sk=&sw=
- profile check: corporate_action_candidate_dates=[2022-07-14,2022-08-02]; no overlap with 2024-05-16~D+180
- price shard: `atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv`
- entry OHLCV: o=28,400, h=29,450, l=25,900, c=28,900, v=2,934,787, amount=81,553,372,200, market_cap=1,745,248,862,600
- 30D MFE/MAE: 87.54% / -10.38%
- 90D MFE/MAE: 87.54% / -10.38%
- 180D MFE/MAE: 87.54% / -19.38%
- 180D peak/trough: 2024-06-19 / 2024-12-09
- calibration_usable: true

### Case 2. 192820 Cosmax — Stage2-Actionable

- duplicate key: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 192820 + Stage2-Actionable + 2024-05-13`
- trigger family: `COSMAX_ODM_GLOBAL_CLIENT_EXPORT_BRIDGE`
- evidence: Cosmetics ODM record Q1 sales/OP, domestic indie clients exporting to US/Japan and China subsidiary recovery.
- source URLs: https://www.asiae.co.kr/en/print.htm?idxno=2024051310023823498, https://www.mk.co.kr/en/business/11249094
- profile check: corporate_action_candidate_dates=[]
- price shard: `atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv`
- entry OHLCV: o=149,900, h=164,700, l=147,800, c=157,700, v=378,466, amount=59,798,794,500, market_cap=1,789,817,569,300
- 30D MFE/MAE: 31.90% / -6.28%
- 90D MFE/MAE: 31.90% / -26.44%
- 180D MFE/MAE: 31.90% / -26.44%
- 180D peak/trough: 2024-06-14 / 2024-08-13
- calibration_usable: true

### Case 3. 161890 Kolmar Korea — Stage2-Actionable

- duplicate key: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 161890 + Stage2-Actionable + 2024-08-09`
- trigger family: `KOLMAR_ODM_EXPORT_SUNCARE_GLOBAL_CLIENT_BRIDGE`
- evidence: ODM export growth and suncare/global indie-brand order bridge.
- source URLs: https://www.kolmar.co.kr/eng/ir/report.php, https://www.kolmar.co.kr/down.php?code=engReport&idx=6898&no=2
- profile check: corporate_action_candidate_dates=[]
- price shard: `atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv`
- entry OHLCV: o=61,000, h=67,000, l=60,800, c=66,300, v=1,507,177, amount=97,064,248,800, market_cap=1,565,016,605,100
- 30D MFE/MAE: 17.80% / -8.90%
- 90D MFE/MAE: 18.70% / -25.26%
- 180D MFE/MAE: 32.73% / -25.26%
- 180D peak/trough: 2025-05-09 / 2024-12-09
- calibration_usable: true

### Case 4. 278470 APR — Stage2-Actionable

- duplicate key: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 278470 + Stage2-Actionable + 2025-05-08`
- trigger family: `APR_MEDICUBE_OVERSEAS_ONLINE_OFFLINE_SCALE`
- evidence: APR Q1 2025 record overseas sales, Medicube/device global demand and overseas revenue share expansion.
- source URLs: https://www.asiae.co.kr/en/article/2025050811555201003, https://www.apr-in.aprd.io/ir/3542190065_HTkRLWZf_6a7530df5e15df09de4067cdf961b3c1fba48a9a.pdf
- profile check: corporate_action_candidate_dates=[2024-10-31]; selected 2025-05-08 row has no overlap with 180D window
- price shard: `atlas/ohlcv_tradable_by_symbol_year/278/278470/2025.csv`
- entry OHLCV: o=76,400, h=99,300, l=76,200, c=98,400, v=6,642,662, amount=616,196,204,850, market_cap=3,688,185,012,000
- 30D MFE/MAE: 46.14% / -22.56%
- 90D MFE/MAE: 145.43% / -22.56%
- 180D MFE/MAE: 198.27% / -22.56%
- 180D peak/trough: 2026-01-22 / 2025-05-08
- calibration_usable: true

### Case 5. 018290 VT — Stage2-Actionable

- duplicate key: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 018290 + Stage2-Actionable + 2025-02-27`
- trigger family: `VT_REEDLE_SHOT_OVERSEAS_PRODUCT_REPEATABILITY`
- evidence: VT cosmetic sales/OP expansion from Reedle Shot/global channels; high-MAE Green blocker.
- source URLs: https://biz.chosun.com/en/en-finance/2025/02/27/6FS2ZOW7DBE6HAMFUR2UIOB2DI/, https://en.topdaily.kr/articles/6504
- profile check: corporate_action_candidate_dates all before 2020; no overlap with 2025-02-27~D+180
- price shard: `atlas/ohlcv_tradable_by_symbol_year/018/018290/2025.csv`
- entry OHLCV: o=36,550, h=37,950, l=35,150, c=35,300, v=3,604,946, amount=131,418,076,950, market_cap=1,263,669,647,100
- 30D MFE/MAE: 7.51% / -16.86%
- 90D MFE/MAE: 29.04% / -16.86%
- 180D MFE/MAE: 29.04% / -43.97%
- 180D peak/trough: 2025-06-05 / 2025-11-24
- calibration_usable: true

### Case 6. 090430 Amorepacific — Stage4B

- duplicate key: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 090430 + Stage4B + 2024-08-07`
- trigger family: `AMORE_COSRX_OFFSET_CHINA_LOSS_WATCH`
- evidence: COSRX/North America offset visible, but China losses and weak domestic cosmetics block positive escalation.
- source URLs: https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2326348, https://www.apgroup.com/int/en/investors/amorepacific-corporation/ir-reports/quarterly-results/__icsFiles/afieldfile/2025/02/06/AP_4Q24_EN_vff.pdf
- profile check: corporate_action_candidate_dates=[2015-05-08]; no overlap
- price shard: `atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv`
- entry OHLCV: o=130,700, h=134,800, l=123,200, c=124,500, v=3,345,422, amount=425,651,362,500, market_cap=7,282,348,495,500
- 30D MFE/MAE: 20.40% / -6.91%
- 90D MFE/MAE: 26.91% / -20.08%
- 180D MFE/MAE: 26.91% / -20.08%
- 180D peak/trough: 2024-09-27 / 2024-12-09
- calibration_usable: true

### Case 7. 051900 LG H&H — Stage4B

- duplicate key: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 051900 + Stage4B + 2024-07-26`
- trigger family: `LGHH_CHINA_WEAKNESS_GLOBAL_KBEAUTY_OFFSET_WATCH`
- evidence: China premium beauty weakness despite broader K-beauty/global offset; watch not hard 4C.
- source URLs: https://www.kedglobal.com/beauty-cosmetics/newsView/ked202407260006, https://www.lghnh.com/global/news/press/view.jsp?seq=49&title=
- profile check: corporate_action_candidate_dates=[]
- price shard: `atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv`
- entry OHLCV: o=347,500, h=364,000, l=347,500, c=351,000, v=94,653, amount=33,594,711,500, market_cap=5,481,987,147,000
- 30D MFE/MAE: 4.27% / -8.55%
- 90D MFE/MAE: 11.54% / -11.82%
- 180D MFE/MAE: 11.54% / -17.38%
- 180D peak/trough: 2024-09-27 / 2025-04-09
- calibration_usable: true


## 6. Score-return alignment and residual interpretation

C20 already receives higher visibility and market-mispricing emphasis in the rolling profile (`22/23/12/16/13/4/10`). This loop does not propose another broad C20 positive-weight increase. The residual error is more surgical:

- Silicon2 and APR show that a global distributor with logistics / overseas channel evidence can produce very large forward MFE, but even these winners can have post-spike MAE that should block Green looseness.
- Cosmax and Kolmar Korea show ODM global export/client demand can be Stage2-Actionable when sales and operating-profit conversion are visible, but not when the evidence is only “K-beauty is strong.”
- VT shows single-product global virality can carry direct revenue evidence, but repeatability risk and deep 180D MAE require a Green blocker.
- Amorepacific and LG H&H show that COSRX/North America or broad K-beauty offset does not erase China/premium-beauty drag; these rows should stay 4B/watch or capped Stage2 until regional profit recovery repeats.

## 7. Shadow rule candidate

```text
rule_candidate:
C20_GLOBAL_DISTRIBUTION_REPEATABILITY_SECOND_BRIDGE_GATE_V1

sector_rule_candidate:
L5_CONSUMER_GLOBAL_CHANNEL_REORDER_AND_MARGIN_GATE_V1

core residual:
- K-beauty / global beauty / export headline alone cannot create Stage2-Actionable, Stage3-Yellow, or Stage3-Green.
- Stage2-Actionable requires at least one direct second bridge:
  repeat reorder, distributor sell-through, overseas subsidiary growth,
  logistics/channel expansion tied to revenue, ODM client export growth,
  operating-profit conversion, margin conversion, or cashflow bridge.
- One-product virality or single-quarter export spike remains Actionable-capped and Green-blocked until repeat revenue is visible.
- COSRX / North America / overseas-growth offset does not neutralize China weakness unless regional operating-profit recovery or channel repeatability is visible.
- High MAE after a valid direct bridge blocks Yellow/Green first; it does not erase Stage2-Actionable.
- Hard 4C requires confirmed channel collapse, brand deterioration, repeated margin failure, inventory/write-down cascade, or weak offset quality.
```

## 8. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "selected_round": "R5", "selected_loop": 219, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1", "symbol": "257720", "symbol_name": "Silicon2", "trigger_type": "Stage2-Actionable", "trigger_family": "SILICON2_GLOBAL_DISTRIBUTION_REPEAT_REORDER", "entry_date": "2024-05-16", "entry_price": 28900.0, "entry_ohlcv": {"o": 28400.0, "h": 29450.0, "l": 25900.0, "c": 28900.0, "v": 2934787.0, "a": 81553372200.0, "mc": 1745248862600.0, "m": "KOSDAQ"}, "mfe_30d_pct": 87.54, "mae_30d_pct": -10.38, "mfe_90d_pct": 87.54, "mae_90d_pct": -10.38, "mfe_180d_pct": 87.54, "mae_180d_pct": -19.38, "peak_180d_date": "2024-06-19", "trough_180d_date": "2024-12-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "case_role": "positive", "evidence_summary": "Direct K-beauty export distributor, Q1 sales/OP jump, overseas warehouse/channel expansion.", "source_urls": ["https://www.asiae.co.kr/en/article/2024070210301137687", "https://www.siliconii.com/en/sub/sub03_01.php?boardid=newsen&category=&idx=5&mode=view&offset=56&sk=&sw="], "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "weights_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10", "production_scoring_changed": false, "shadow_weight_only": true}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "selected_round": "R5", "selected_loop": 219, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1", "symbol": "192820", "symbol_name": "Cosmax", "trigger_type": "Stage2-Actionable", "trigger_family": "COSMAX_ODM_GLOBAL_CLIENT_EXPORT_BRIDGE", "entry_date": "2024-05-13", "entry_price": 157700.0, "entry_ohlcv": {"o": 149900.0, "h": 164700.0, "l": 147800.0, "c": 157700.0, "v": 378466.0, "a": 59798794500.0, "mc": 1789817569300.0, "m": "KOSPI"}, "mfe_30d_pct": 31.9, "mae_30d_pct": -6.28, "mfe_90d_pct": 31.9, "mae_90d_pct": -26.44, "mfe_180d_pct": 31.9, "mae_180d_pct": -26.44, "peak_180d_date": "2024-06-14", "trough_180d_date": "2024-08-13", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "case_role": "positive", "evidence_summary": "Cosmetics ODM record Q1 sales/OP, domestic indie clients exporting to US/Japan and China subsidiary recovery.", "source_urls": ["https://www.asiae.co.kr/en/print.htm?idxno=2024051310023823498", "https://www.mk.co.kr/en/business/11249094"], "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "weights_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10", "production_scoring_changed": false, "shadow_weight_only": true}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "selected_round": "R5", "selected_loop": 219, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1", "symbol": "161890", "symbol_name": "Kolmar Korea", "trigger_type": "Stage2-Actionable", "trigger_family": "KOLMAR_ODM_EXPORT_SUNCARE_GLOBAL_CLIENT_BRIDGE", "entry_date": "2024-08-09", "entry_price": 66300.0, "entry_ohlcv": {"o": 61000.0, "h": 67000.0, "l": 60800.0, "c": 66300.0, "v": 1507177.0, "a": 97064248800.0, "mc": 1565016605100.0, "m": "KOSPI"}, "mfe_30d_pct": 17.8, "mae_30d_pct": -8.9, "mfe_90d_pct": 18.7, "mae_90d_pct": -25.26, "mfe_180d_pct": 32.73, "mae_180d_pct": -25.26, "peak_180d_date": "2025-05-09", "trough_180d_date": "2024-12-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "case_role": "positive", "evidence_summary": "ODM export growth and suncare/global indie-brand order bridge.", "source_urls": ["https://www.kolmar.co.kr/eng/ir/report.php", "https://www.kolmar.co.kr/down.php?code=engReport&idx=6898&no=2"], "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "weights_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10", "production_scoring_changed": false, "shadow_weight_only": true}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "selected_round": "R5", "selected_loop": 219, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1", "symbol": "278470", "symbol_name": "APR", "trigger_type": "Stage2-Actionable", "trigger_family": "APR_MEDICUBE_OVERSEAS_ONLINE_OFFLINE_SCALE", "entry_date": "2025-05-08", "entry_price": 98400.0, "entry_ohlcv": {"o": 76400.0, "h": 99300.0, "l": 76200.0, "c": 98400.0, "v": 6642662.0, "a": 616196204850.0, "mc": 3688185012000.0, "m": "KOSPI"}, "mfe_30d_pct": 46.14, "mae_30d_pct": -22.56, "mfe_90d_pct": 145.43, "mae_90d_pct": -22.56, "mfe_180d_pct": 198.27, "mae_180d_pct": -22.56, "peak_180d_date": "2026-01-22", "trough_180d_date": "2025-05-08", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "case_role": "positive", "evidence_summary": "APR Q1 2025 record overseas sales, Medicube/device global demand and overseas revenue share expansion.", "source_urls": ["https://www.asiae.co.kr/en/article/2025050811555201003", "https://www.apr-in.aprd.io/ir/3542190065_HTkRLWZf_6a7530df5e15df09de4067cdf961b3c1fba48a9a.pdf"], "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "weights_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10", "production_scoring_changed": false, "shadow_weight_only": true}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "selected_round": "R5", "selected_loop": 219, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1", "symbol": "018290", "symbol_name": "VT", "trigger_type": "Stage2-Actionable", "trigger_family": "VT_REEDLE_SHOT_OVERSEAS_PRODUCT_REPEATABILITY", "entry_date": "2025-02-27", "entry_price": 35300.0, "entry_ohlcv": {"o": 36550.0, "h": 37950.0, "l": 35150.0, "c": 35300.0, "v": 3604946.0, "a": 131418076950.0, "mc": 1263669647100.0, "m": "KOSDAQ"}, "mfe_30d_pct": 7.51, "mae_30d_pct": -16.86, "mfe_90d_pct": 29.04, "mae_90d_pct": -16.86, "mfe_180d_pct": 29.04, "mae_180d_pct": -43.97, "peak_180d_date": "2025-06-05", "trough_180d_date": "2025-11-24", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "case_role": "positive", "evidence_summary": "VT cosmetic sales/OP expansion from Reedle Shot/global channels; high-MAE Green blocker.", "source_urls": ["https://biz.chosun.com/en/en-finance/2025/02/27/6FS2ZOW7DBE6HAMFUR2UIOB2DI/", "https://en.topdaily.kr/articles/6504"], "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "weights_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10", "production_scoring_changed": false, "shadow_weight_only": true}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "selected_round": "R5", "selected_loop": 219, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1", "symbol": "090430", "symbol_name": "Amorepacific", "trigger_type": "Stage4B", "trigger_family": "AMORE_COSRX_OFFSET_CHINA_LOSS_WATCH", "entry_date": "2024-08-07", "entry_price": 124500.0, "entry_ohlcv": {"o": 130700.0, "h": 134800.0, "l": 123200.0, "c": 124500.0, "v": 3345422.0, "a": 425651362500.0, "mc": 7282348495500.0, "m": "KOSPI"}, "mfe_30d_pct": 20.4, "mae_30d_pct": -6.91, "mfe_90d_pct": 26.91, "mae_90d_pct": -20.08, "mfe_180d_pct": 26.91, "mae_180d_pct": -20.08, "peak_180d_date": "2024-09-27", "trough_180d_date": "2024-12-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "case_role": "guardrail_4b", "evidence_summary": "COSRX/North America offset visible, but China losses and weak domestic cosmetics block positive escalation.", "source_urls": ["https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2326348", "https://www.apgroup.com/int/en/investors/amorepacific-corporation/ir-reports/quarterly-results/__icsFiles/afieldfile/2025/02/06/AP_4Q24_EN_vff.pdf"], "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "weights_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10", "production_scoring_changed": false, "shadow_weight_only": true}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R5_loop_219_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md", "selected_round": "R5", "selected_loop": 219, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "C20_KBEAUTY_GLOBAL_DISTRIBUTION_REPEATABILITY_GATE_V1", "symbol": "051900", "symbol_name": "LG H&H", "trigger_type": "Stage4B", "trigger_family": "LGHH_CHINA_WEAKNESS_GLOBAL_KBEAUTY_OFFSET_WATCH", "entry_date": "2024-07-26", "entry_price": 351000.0, "entry_ohlcv": {"o": 347500.0, "h": 364000.0, "l": 347500.0, "c": 351000.0, "v": 94653.0, "a": 33594711500.0, "mc": 5481987147000.0, "m": "KOSPI"}, "mfe_30d_pct": 4.27, "mae_30d_pct": -8.55, "mfe_90d_pct": 11.54, "mae_90d_pct": -11.82, "mfe_180d_pct": 11.54, "mae_180d_pct": -17.38, "peak_180d_date": "2024-09-27", "trough_180d_date": "2025-04-09", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "case_role": "guardrail_4b", "evidence_summary": "China premium beauty weakness despite broader K-beauty/global offset; watch not hard 4C.", "source_urls": ["https://www.kedglobal.com/beauty-cosmetics/newsView/ked202407260006", "https://www.lghnh.com/global/news/press/view.jsp?seq=49&title="], "score_simulation": {"profile": "e2r_2_2_rolling_calibrated_proxy", "weights_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10", "production_scoring_changed": false, "shadow_weight_only": true}}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in this research session.
Later coding agent task:
- ingest this MD as a standard v12 result file;
- parse trigger JSONL rows;
- validate stock-web price fields;
- dedupe by canonical_archetype_id + symbol + trigger_type + entry_date;
- evaluate whether C20_GLOBAL_DISTRIBUTION_REPEATABILITY_SECOND_BRIDGE_GATE_V1 should be added as a narrow shadow rule candidate;
- do not loosen Stage3-Green globally;
- treat high-MAE direct-bridge rows as Green blockers before Stage2 deletion.
```

## 10. Batch Ingest Self-Audit

```text
filename_regex_pass: true
filename_round_matches_metadata: true
filename_loop_matches_metadata: true
selected_round: R5
selected_loop: 219
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_sector_consistency: pass
all_trigger_rows_have_entry_date: true
all_trigger_rows_have_entry_price: true
all_trigger_rows_have_30_90_180_mfe_mae: true
all_trigger_rows_have_actual_entry_ohlcv: true
calibration_usable_rows: 7
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
source_proxy_only_count: 0
evidence_url_pending_count: 0
production_scoring_changed: false
shadow_weight_only: true
```

## 11. Next Research State

```text
completed_round: R5
completed_loop: 219
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 URL/proxy quality + L5 C20 balance refresh
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_CHANNEL_REPEATABILITY_DIRECT_ROW_REPAIR
- C18_CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_REORDER_DIRECT_ROW_REPAIR
- C19_BRAND_RETAIL_INVENTORY_MARGIN_INVENTORY_NRV_DIRECT_URL_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_CONSUMER_EXPORT_HOLDOUT_REFRESH
```
