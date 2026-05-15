# Round-47 R7 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `CDMO_HEALTHCARE_CONTRACT` | GREEN_POSSIBLE | long_term_contract, capacity_utilization, customer_diversification, fcf_conversion | underutilization, customer_concentration, capex_burden, quality_issue, tariff |
| `CRO_CLINICAL_SERVICE` | WATCH_YELLOW_FIRST | service_backlog, customer_diversification, repeat_service_revenue, opm_improvement | biotech_funding_cycle_down, customer_budget_cut, trial_delay, low_margin_backlog |
| `BIOSIMILAR_COMMERCIALIZATION` | WATCH_YELLOW_FIRST | pbm_listing, insurance_coverage, prescription_conversion, revenue_conversion | price_competition, coverage_gap, slow_switching, margin_pressure |
| `BIOSIMILAR_ORIGINATOR_DEFENSE` | WATCH_YELLOW_FIRST | pipeline_revenue_offset, price_defense, margin_protection | patent_cliff, pipeline_failure, share_loss, pricing_pressure |
| `OBESITY_GLP1_COMMERCIALIZATION` | GREEN_POSSIBLE | prescription_volume, insurance_coverage, supply_capacity, price_defense, op_eps_revision | competition, compounded_alternative, coverage_gap, price_regulation, slow_uptake |
| `GENE_THERAPY_RARE_DISEASE` | REDTEAM_FIRST | patient_uptake, reimbursement, cash_runway, commercial_revenue | cash_burn, reimbursement_failure, slow_uptake, dilution, going_concern |
| `AI_DRUG_DISCOVERY_PLATFORM` | REDTEAM_FIRST | big_pharma_partnership, clinical_progress, cash_runway, milestone_revenue | no_approved_drug, cash_burn, clinical_failure, platform_hype |
| `DIGITAL_HEALTHCARE_AI` | WATCH_YELLOW_FIRST | external_validation, hospital_adoption, reimbursement_or_paid_usage, recurring_revenue | subgroup_bias, no_reimbursement, liability, poc_only, date_unverified |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` | WATCH_YELLOW_FIRST | hospital_or_insurer_contract, recurring_revenue, unit_economics, regulatory_clearance | regulation, privacy, reimbursement, cac, churn |
| `TELEHEALTH_BEHAVIORAL_HEALTH` | REDTEAM_FIRST | employer_or_insurer_contract, cac_stable, churn_stable, fcf_margin | cac, privacy, impairment, forecast_withdrawal, churn |
| `PHARMA_CHANNEL_AND_PRIVACY_RISK` | REDTEAM_FIRST | legal_prescription_channel, gross_margin, privacy_clean, fcf_visible | regulatory_scrutiny, privacy, quality_issue, margin_pressure |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT` | GREEN_POSSIBLE | export_growth, consumable_repeat_revenue, regulatory_approval, opm_roe_improvement | approval_delay, safety, competition, channel_quality, single_device_no_consumable |
| `MEDICAL_DEVICE_DENTAL_IMPLANT` | GREEN_POSSIBLE | recurring_procedure_consumable, approval_stable, opm_roe_improvement, channel_quality | vbp_price_control, approval, safety, competition, asp_drop |
| `BOTULINUM_AESTHETIC_REGULATED` | WATCH_YELLOW_FIRST | regulatory_approval, repeat_procedure, safe_distribution_channel, op_eps_revision | counterfeit, unapproved_product, safety, channel_failure |
| `DIAGNOSTICS_INFECTIOUS_DISEASE` | REDTEAM_FIRST | recurring_non_event_demand, post_event_revenue, margin_normalization | one_off_demand, inventory_build, guidance_down, demand_cliff |
| `ANIMAL_HEALTH_BIOSECURITY` | WATCH_YELLOW_FIRST | recurring_prevention_revenue, government_or_farm_contract, margin_visibility | event_normalization, policy_uncertainty, approval_issue, inventory |

## What Not To Change

- Do not apply these R7 v1.0 weights to production scoring yet.
- Do not treat approval, clinical success, AI model AUC, a paper, a pilot, user growth, or disease outbreak demand as Green evidence by itself.
- Do not invent prescription volume, reimbursement, hospital adoption, capacity utilization, patient uptake, cash runway, procedure volume, consumable revenue, CAC, churn, or price-path fields.
- Do not lower Stage 3-Green for biotech recall. Green requires commercialization, reimbursement, recurring revenue, FCF conversion, or contracted utilization evidence.
- Treat slow uptake, cash crunch, dilution, take-private, forecast cut, privacy breach, impairment, counterfeit product, safety issue, price control, and one-off diagnostic normalization as RedTeam evidence.
