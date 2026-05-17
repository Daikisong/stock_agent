# Round-104 R12 Loop-5 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `SMART_FARM_AGRI_TECH` | WATCH_YELLOW_FIRST | actual_order, operation_contract, unit_economics_positive, fcf_conversion | energy_cost, capex_burden, unit_economics_failure, subsidy_dependency |
| `VERTICAL_FARMING_UNIT_ECONOMICS` | REDTEAM_FIRST | unit_economics_positive, customer_contract, energy_cost_control, fcf_conversion | energy_cost_failure, capex_burden, premium_pricing_failure, shutdown, chapter11 |
| `AGRI_MACHINERY_PRECISION_CYCLE` | WATCH_YELLOW_FIRST | equipment_sales_growth, farmer_roi, software_attach_rate, service_revenue | farm_income, financing_cost, replacement_cycle, right_to_repair, dealer_inventory |
| `AGRI_MACHINERY_DEMAND_CYCLE` | WATCH_YELLOW_FIRST | equipment_sales_growth, dealer_inventory_normalization, service_revenue, fcf_conversion | farm_income_weakness, crop_price, dealer_inventory, farmer_financing_cost |
| `AGRI_MACHINERY_SOFTWARE_LOCKIN` | WATCH_YELLOW_FIRST | software_attach_rate, service_revenue, customer_retention, fcf_conversion | right_to_repair, repair_monopoly, ftc_lawsuit, customer_backlash |
| `RIGHT_TO_REPAIR_REGULATORY_OVERLAY` | REDTEAM_FIRST | regulatory_risk_resolved, customer_retention, service_revenue | right_to_repair, repair_monopoly, settlement_cost, ftc_lawsuit, customer_backlash |
| `AGRI_INPUT_SEED_CROP_PROTECTION` | WATCH_YELLOW_FIRST | licensing_revenue, farmer_roi, ebitda_improvement, fcf_conversion | litigation, patent_expiry, regulation, farmer_margin |
| `FERTILIZER_INPUT_COST_CYCLE` | WATCH_YELLOW_FIRST | volume_growth, price_margin, farmer_roi, fcf_conversion | crop_price, farmer_margin, input_cost, demand_deferral, geopolitical_supply |
| `AGRI_LIVESTOCK_FOOD_COMMODITY` | REDTEAM_FIRST | price_pass_through, cost_stabilization, multi_period_margin_stability | disease_event, feed_cost, weather, price_normalization, government_inquiry |
| `ANIMAL_HEALTH_BIOSECURITY` | WATCH_YELLOW_FIRST | government_purchase_contract, repeat_vaccination, recurring_revenue, fcf_conversion | emergency_license, one_off_stockpile, government_policy_uncertain, outbreak_normalization |
| `AGRI_DISEASE_AI_MONITORING` | WATCH_YELLOW_FIRST | farm_contract, repeat_subscription, data_quality, fcf_conversion | data_quality, privacy, adoption_missing, subsidy_dependency |
| `EDUCATION_SPECIALTY_SERVICES` | WATCH_YELLOW_FIRST | enterprise_contract, completion_rate, student_roi, opm_improvement, fcf_conversion | ai_disruption, cac, completion_rate, student_roi, debt, bookings_miss |
| `EDTECH_AI_MONETIZATION_TRADEOFF` | WATCH_YELLOW_FIRST | bookings_growth, paid_conversion, margin_stability, fcf_conversion | ai_cost, bookings_miss, monetization_retreat, paid_conversion_slowdown |
| `EDTECH_AI_DISRUPTION` | REDTEAM_FIRST | b2b_contract, completion_rate, student_roi, fcf_conversion | ai_substitution, traffic_decline, subscriber_decline, bookings_miss, cac_spike |
| `ONLINE_EDUCATION_OPM_DISTRESS` | REDTEAM_FIRST | student_roi, completion_rate, partner_retention, fcf_conversion | debt, student_roi, regulatory_oversight, partner_concentration, chapter11 |
| `HOME_CHILD_EDUCATION` | REDTEAM_FIRST | repeat_subscription, export_channel, low_birthrate_offset, fcf_conversion | birthrate_decline, tam_shrink, inventory, policy_risk |
| `HOME_LIVING_APPLIANCE_RENTAL` | WATCH_YELLOW_FIRST | rental_churn_stable, recurring_service_revenue, opm_fcf_improvement, overseas_margin | replacement_cycle, housing_turnover, churn, hardware_only, dividend_suspension |
| `HOME_APPLIANCE_HARDWARE_CYCLE` | WATCH_YELLOW_FIRST | repeat_service_revenue, margin_stability, fcf_conversion | replacement_cycle, housing_turnover, dividend_suspension, guidance_cut, debt |
| `SERVICE_KIOSK_SELF_CHECKOUT` | WATCH_YELLOW_FIRST | maintenance_revenue, payment_fee_revenue, loss_prevention_effect, recurring_service_revenue | theft, customer_friction, retailer_retreat, employee_workload, one_off_hardware |
| `SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY` | REDTEAM_FIRST | regulation_resolved, maintenance_revenue, retailer_retention | item_limit, staff_required, local_ordinance, retailer_retreat |
| `CONSUMER_REGULATED_PRODUCT` | WATCH_YELLOW_FIRST | sales_authorization, channel_access, repeat_consumption, regulatory_stability | public_health, social_backlash, legal_conflict, license_scope, youth_usage |
| `NICOTINE_ALTERNATIVE_REGULATED` | WATCH_YELLOW_FIRST | sales_authorization, license_scope, authorized_channel, repeat_consumption | youth_usage, public_health, flavor_restriction, unauthorized_status |
| `NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY` | REDTEAM_FIRST | age_verification, authorization_scope, public_health_risk_contained | youth_addiction, high_nicotine, flavor, advertising, public_health |
| `CANNABIS_REGULATED_PRODUCT` | WATCH_YELLOW_FIRST | license_scope, sales_channel, tax_effect, regulatory_stability | no_full_legalization, dea_registration_required, state_federal_conflict, legal_challenge |
| `FOOD_INPUT_REGULATED_CYCLE` | WATCH_YELLOW_FIRST | price_pass_through, regulated_margin, cost_stabilization, fcf_conversion | cost, price_control, regulation, commodity_cycle |
| `AGRI_DISEASE_EVENT_OVERLAY` | REDTEAM_FIRST | repeat_procurement, multi_period_margin, low_normalization_risk | one_off_disease, price_normalization, government_inquiry |
| `REGULATED_CONSUMER_APPROVAL_OVERLAY` | REDTEAM_FIRST | authorization_scope, sales_channel, repeat_consumption, regulatory_stability | license_scope, legal_conflict, youth_usage, public_health |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST |  | contract_value_missing, churn_missing, cac_missing, regulatory_scope_missing, unit_economics_missing, parser_confidence_low |

## What Not To Change

- Do not apply these R12 Loop-5 v5 weights to production scoring yet.
- Do not treat essential demand, policy support, weather, disease, grain prices, education users, rental accounts, or FDA/DEA headlines as Green evidence by itself.
- Do not invent unit economics, government orders, completion rates, CAC, churn, regulatory scope, software attach rate, or price-path fields.
- Do not lower Stage 3-Green for R12 recall. Green requires repeat contracts, repeat revenue, unit economics, regulatory stability, and FCF conversion.
- Treat Chapter 11, AI substitution, bookings misses, dividend suspension, retailer retreat, theft/shrink, public-health reversal, commodity normalization, and right-to-repair risk as RedTeam evidence.
