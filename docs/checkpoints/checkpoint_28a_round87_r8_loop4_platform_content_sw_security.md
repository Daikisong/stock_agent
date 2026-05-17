# Checkpoint 28A Round87 R8 Loop4 Platform / Content / SW / Security

## Summary

- source_round: `docs/round/round_87.md`
- large_sector: `PLATFORM_CONTENT_SW_SECURITY`
- target_count: 20
- case_candidate_count: 19
- structural_success_count: 1
- success_candidate_count: 5
- event_premium_count: 1
- stage4b_case_count: 8
- stage4c_case_count: 6
- green_possible_count: 2
- watch_yellow_first_count: 11
- redteam_first_count: 7
- gate_only_target_count: 6
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## What Changed

Round87 upgrades the R8 platform/software/security pack from Loop3 to Loop4. The main change is that AI features, user count, new-title expectation, advertising recovery, security demand, and platform scale are separated from real repeat-revenue evidence.

New or newly separated targets:

- `EDGE_AI_CLOUD_INFRASTRUCTURE`
- `OBSERVABILITY_GUIDANCE_RISK`
- `PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY`

Example: an AI cloud contract can make a Stage 2 candidate. It should not become Stage 3-Green until margin, capex, customer concentration, revenue recognition, and FCF are checked.

## Case Pack

Generated:

- `data/e2r_case_library/cases_r8_loop4_round87.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round87_r8_loop4_v4.csv`
- `output/e2r_round87_r8_loop4_platform_content_sw_security/round87_r8_loop4_platform_content_sw_security_summary.md`
- `output/e2r_round87_r8_loop4_platform_content_sw_security/round87_r8_loop4_case_matrix.csv`
- `output/e2r_round87_r8_loop4_platform_content_sw_security/round87_r8_loop4_stage_date_plan.csv`
- `output/e2r_round87_r8_loop4_platform_content_sw_security/round87_r8_loop4_green_guardrails.md`
- `output/e2r_round87_r8_loop4_platform_content_sw_security/round87_r8_loop4_risk_overlays.md`
- `output/e2r_round87_r8_loop4_platform_content_sw_security/round87_r8_loop4_price_validation_plan.md`
- `output/e2r_round87_r8_loop4_platform_content_sw_security/round87_r8_loop4_price_fields.csv`

## Guardrails

- AI feature launch is not revenue.
- User count is not ARPU, ARR, bookings, or FCF.
- Security demand is not operational trust.
- Streaming ad growth must pass privacy, youth-safety, ad-quality, and churn checks.
- Observability earnings beats can still fail if ARR or guidance misses.
- Metaverse/NFT remains Red/Watch before repeat cash revenue appears.

## Verification

Targeted tests passed:

```bash
PYTHONPATH=src python -m unittest tests.test_round87_r8_loop4_platform_content_sw_security -v
```

Full repository verification was run after report generation before commit.

