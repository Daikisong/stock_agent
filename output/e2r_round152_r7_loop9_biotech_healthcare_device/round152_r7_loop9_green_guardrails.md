# Round-152 R7 Loop-9 Green Guardrails

| target | posture | Green unlock evidence | Loop-9 penalties |
| --- | --- | --- | --- |
| `CDMO_HEALTHCARE_CONTRACT` | GREEN_POSSIBLE | long_term_contract, capacity_utilization, customer_diversification, fcf_conversion | utilization, customer_contract, capex, quality |
| `CDMO_US_TARIFF_HEDGE_CAPACITY` | WATCH_YELLOW_FIRST | customer_contract, capacity_utilization, technology_transfer, opm_fcf_conversion | us_capacity, utilization, customer_contract, technology_transfer, operating_cost |
| `CDMO_ADC_CELL_GENE_CAPABILITY` | WATCH_YELLOW_FIRST | customer_contract, capacity_utilization, regulatory_tech_transfer, opm_fcf_conversion | customer_contract, technology_transfer, utilization, quality, capex |
| `CRO_CLINICAL_SERVICE` | WATCH_YELLOW_FIRST | service_backlog, customer_diversification, repeat_service_revenue, opm_improvement | funding_cycle, customer_budget, forecast_cut |
| `CRO_FUNDING_CYCLE_OVERLAY` | REDTEAM_FIRST |  | funding_cycle, forecast_cut, customer_budget, backlog_conversion |
| `BIOSIMILAR_COMMERCIALIZATION` | WATCH_YELLOW_FIRST | pbm_listing, insurance_coverage, prescription_conversion, revenue_conversion | pbm, coverage, prescription_switch, margin |
| `BIOSIMILAR_ACCESS_CASH_PAY` | WATCH_YELLOW_FIRST | prescription_conversion, margin_defense, pbm_or_cash_channel_scaled, payer_access | discount, prescription_switch, pbm, margin, access |
| `BIOSIMILAR_PBM_FORMULARY_SWITCH` | WATCH_YELLOW_FIRST | pbm_listing, insurance_coverage, prescription_conversion, margin_defense | pbm, formulary, prescription_switch, margin, patent |
| `BIOSIMILAR_PATENT_LITIGATION` | REDTEAM_FIRST |  | patent, launch_timing, settlement, margin |
| `OBESITY_GLP1_COMMERCIALIZATION` | GREEN_POSSIBLE | prescription_volume, insurance_coverage, supply_capacity, price_defense, op_eps_revision | scripts, coverage, price, competition, compounded_drugs |
| `ORAL_GLP1_APPROVAL_COMMERCIALIZATION` | WATCH_YELLOW_FIRST | weekly_scripts, insurance_coverage, gross_to_net_visible, repeat_refill, op_eps_revision | scripts, coverage, gross_to_net, refill, price |
| `ORAL_GLP1_MAINTENANCE_THERAPY` | WATCH_YELLOW_FIRST | weekly_scripts, insurance_coverage, repeat_refill, op_eps_revision, price_defense | scripts, coverage, price, maintenance, safety |
| `GLP1_PRICE_WAR_OVERLAY` | REDTEAM_FIRST |  | price, gross_to_net, competition, coverage, scripts |
| `GLP1_TELEHEALTH_CHANNEL` | WATCH_YELLOW_FIRST | branded_drug_attach, cac_stable, gross_margin_stable, compliance_clean, fcf_conversion | cac, compounding, revenue_recognition, legal_cost |
| `COMPOUNDED_GLP1_REGULATORY_RISK` | REDTEAM_FIRST |  | compounding, fda, doj, quality, legal |
| `GENE_THERAPY_RARE_DISEASE` | REDTEAM_FIRST | patient_uptake, reimbursement, cash_runway, commercial_revenue | cash_runway, reimbursement, patient_uptake, dilution |
| `AI_DRUG_DISCOVERY_PLATFORM` | REDTEAM_FIRST | big_pharma_partnership, clinical_progress, cash_runway, milestone_revenue | milestone, clinical_progress, cash_runway, approved_drug |
| `DIGITAL_HEALTHCARE_AI` | WATCH_YELLOW_FIRST | external_validation, hospital_adoption, reimbursement_or_paid_usage, recurring_revenue | hospital_adoption, reimbursement, subgroup, liability |
| `MEDICAL_AI_EXTERNAL_VALIDATION` | WATCH_YELLOW_FIRST | external_validation, hospital_adoption, reimbursement_or_paid_usage, recurring_revenue | external_validation, subgroup, deployment, reimbursement, liability |
| `MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK` | REDTEAM_FIRST |  | subgroup, dataset_bias, liability, deployment, reimbursement |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` | WATCH_YELLOW_FIRST | hospital_or_insurer_contract, recurring_revenue, unit_economics, regulatory_clearance | regulation, reimbursement, unit_economics, privacy |
| `TELEHEALTH_BEHAVIORAL_HEALTH` | REDTEAM_FIRST | employer_or_insurer_contract, cac_stable, churn_stable, fcf_margin | cac, privacy, impairment, churn |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT` | GREEN_POSSIBLE | export_growth, consumable_repeat_revenue, regulatory_approval, opm_roe_improvement | approval, safety, channel_quality, procedure_repeat |
| `MEDICAL_DEVICE_DENTAL_IMPLANT` | GREEN_POSSIBLE | recurring_procedure_consumable, approval_stable, opm_roe_improvement, channel_quality | vbp, asp, approval, procedure_repeat |
| `SURGICAL_ROBOT_INSTALLED_BASE` | GREEN_POSSIBLE | installed_base, procedure_growth, instruments_accessories_revenue, opm_fcf_improvement | installed_base, procedure_growth, consumables, hospital_capex |
| `SURGICAL_ROBOT_GLP1_PROCEDURE_MIX_OVERLAY` | REDTEAM_FIRST |  | procedure_mix, glp1_bariatric, system_placements, hospital_capex |
| `BOTULINUM_AESTHETIC_REGULATED` | WATCH_YELLOW_FIRST | regulatory_approval, repeat_procedure, safe_distribution_channel, op_eps_revision | counterfeit, approval, licensed_channel, safety |
| `DIAGNOSTICS_INFECTIOUS_DISEASE` | REDTEAM_FIRST | recurring_non_event_demand, post_event_revenue, margin_normalization | one_off_demand, inventory, guidance_down |
| `COMMERCIALIZATION_FAILURE_OVERLAY` | REDTEAM_FIRST |  | uptake, reimbursement, commercial_revenue, cash_runway |
| `REIMBURSEMENT_ACCESS_OVERLAY` | REDTEAM_FIRST |  | coverage, pbm, reimbursement, gross_to_net, prescription_conversion |
| `DEVICE_SAFETY_COUNTERFEIT_OVERLAY` | REDTEAM_FIRST |  | safety, license, channel, recall, counterfeit |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST |  | disclosure_confidence, contract_terms, prescriptions, reimbursement |

## What Not To Change

- Do not apply R7 Loop-9 v9.0 weights to production scoring yet.
- Do not treat FDA/EMA approval, clinical success, AI model AUC, external-validation paper, pilot, user growth, or disease-event demand as Green evidence by itself.
- Do not invent prescription volume, PBM/insurance coverage, reimbursement, capacity utilization, patient uptake, hospital adoption, external validation, procedure volume, consumable revenue, cash runway, CAC, churn, legal costs, restructuring costs, or stage prices.
- Green requires commercialization, reimbursement, recurring revenue, FCF conversion, contracted utilization, or repeated procedure/consumable evidence.
- Treat slow uptake, cash crunch, dilution, take-private, forecast cut, FDA crackdown, DOJ referral, unapproved copycat, biosimilar patent litigation, privacy breach, impairment, counterfeit product, safety issue, price control, and one-off diagnostic normalization as RedTeam evidence.
