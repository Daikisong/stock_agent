# Checkpoint 28A Round 74 - R8 Loop 3 Platform / Content / SW / Security

Round 74 반영 완료.

## Scope

- source round: `docs/round/round_74.md`
- large sector: `PLATFORM_CONTENT_SW_SECURITY`
- loop: `R8 Loop 3 / v3.0`
- production scoring changed: `false`
- case records are candidate-generation input: `false`

이번 라운드는 `AI 기능`, `유저 수`, `신작 기대`, `광고 회복`, `보안 수요`를 실제 E2R 증거와 분리한다.
쉬운 예로, 보안 회사의 ARR이 커도 전 세계 장애와 고객 소송이 생기면 Stage 3-Green 근거가 아니라 `SECURITY_OPERATIONAL_TRUST_OVERLAY`로 Green 차단을 검토해야 한다.

## Targets

- target_count: 17
- green_possible_count: 2
- watch_yellow_first_count: 10
- redteam_first_count: 5
- gate_only_target_count: 4

추가/강화된 핵심 타깃:

- `B2B_SAAS_ERP_WORKFLOW`: ERP, 회계, 세무, 컴플라이언스 SaaS의 ARR, churn, lock-in, OPM, FCF를 분리.
- `OBSERVABILITY_AI_OPERATIONS`: AIOps, AI workload monitoring, SRE/security analyst agent를 별도 구조로 분리.
- `UGC_GAME_PLATFORM_SAFETY`: Roblox류 UGC 플랫폼을 게임 IP와 분리하고 child-safety friction을 gate로 추적.
- `ADTECH_PLATFORM_PREMIUM`: 전통 광고 사이클과 CTV/retail media ad-tech premium을 분리.
- `SECURITY_OPERATIONAL_TRUST_OVERLAY`: 보안 장애, 고객피해, 소송, 갱신위험을 hard RedTeam gate로 분리.
- `PLATFORM_AD_TRUST_OVERLAY`: scam ads, 광고품질, consumer lawsuit를 광고 플랫폼 RedTeam gate로 분리.

## Case Pack

- case_candidate_count: 18
- structural_success_count: 1
- success_candidate_count: 4
- event_premium_count: 1
- stage4b_case_count: 7
- stage4c_case_count: 6

우선 검증 케이스:

- `douzone_bizon_eqt_cloud_erp_case`
- `palantir_q4_2025_ai_revenue_case`
- `palantir_q1_2026_fastest_growth_case`
- `datadog_q1_2026_ai_observability_case`
- `fortinet_q1_2026_security_billings_case`
- `netflix_ad_tier_250m_case`
- `trade_desk_revenue_miss_case`
- `crowdstrike_outage_shareholder_case`
- `delta_crowdstrike_lawsuit_case`
- `kakao_founder_legal_overhang_case`
- `roblox_safety_forecast_cut_case`
- `take_two_gta_delay_case`
- `take_two_gta_preorder_rumor_case`
- `wpp_ad_forecast_cut_case`
- `wpp_profit_drop_ai_disruption_case`
- `netflix_texas_privacy_lawsuit_case`
- `meta_scam_ads_lawsuit_case`
- `meta_youth_safety_trial_case`

## Outputs

- `data/e2r_case_library/cases_r8_loop3_round74.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round74_r8_loop3_v3.csv`
- `output/e2r_round74_r8_loop3_platform_content_sw_security/round74_r8_loop3_platform_content_sw_security_summary.md`
- `output/e2r_round74_r8_loop3_platform_content_sw_security/round74_r8_loop3_case_matrix.csv`
- `output/e2r_round74_r8_loop3_platform_content_sw_security/round74_r8_loop3_stage_date_plan.csv`
- `output/e2r_round74_r8_loop3_platform_content_sw_security/round74_r8_loop3_green_guardrails.md`
- `output/e2r_round74_r8_loop3_platform_content_sw_security/round74_r8_loop3_risk_overlays.md`
- `output/e2r_round74_r8_loop3_platform_content_sw_security/round74_r8_loop3_price_validation_plan.md`
- `output/e2r_round74_r8_loop3_platform_content_sw_security/round74_r8_loop3_price_fields.csv`

## Guardrails

- R8 Loop 3 weights are calibration material only.
- Case records must not be used as candidate-generation input.
- User count, AI feature, new game title, ad recovery, security demand, NFT, or metaverse theme cannot create Green alone.
- Green requires repeat revenue, ARR/ARPU/bookings, OPM, FCF, low churn, customer retention, operational trust, legal stability, and ad-quality confidence.
- Scam ads, privacy lawsuits, youth-safety issues, founder legal cases, security outages, and single-IP delays are RedTeam gates.
- Do not invent ARR, ARPU, bookings, churn, FCF, customer-damage, lawsuit, or stage-price fields.

## Verification

- `PYTHONPATH=src python -m e2r.cli.build_round74_r8_loop3_report`
- `PYTHONPATH=src python -m unittest tests.test_round74_r8_loop3_platform_content_sw_security -v`
