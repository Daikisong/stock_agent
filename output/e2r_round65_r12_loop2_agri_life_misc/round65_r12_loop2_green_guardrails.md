# Round-65 R12 Loop-2 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `SMART_FARM_AGRI_TECH` | WATCH_YELLOW_FIRST | actual_order, operation_contract, unit_economics_positive, fcf_conversion | energy_cost, capex_burden, unit_economics_failure, subsidy_dependency |
| `AGRI_MACHINERY_PRECISION_CYCLE` | WATCH_YELLOW_FIRST | equipment_sales_growth, farmer_roi, software_attach_rate, service_revenue | farm_income, financing_cost, replacement_cycle, right_to_repair, dealer_inventory |
| `AGRI_LIVESTOCK_FOOD_COMMODITY` | REDTEAM_FIRST | price_pass_through, cost_stabilization, multi_period_margin_stability | disease_event, feed_cost, weather, price_normalization, government_inquiry |
| `ANIMAL_HEALTH_BIOSECURITY` | WATCH_YELLOW_FIRST | government_purchase_contract, repeat_vaccination, recurring_revenue, fcf_conversion | emergency_license, one_off_stockpile, government_policy_uncertain, outbreak_normalization |
| `EDUCATION_SPECIALTY_SERVICES` | WATCH_YELLOW_FIRST | enterprise_contract, completion_rate, student_roi, opm_improvement, fcf_conversion | ai_disruption, cac, completion_rate, student_roi, debt, bookings_miss |
| `HOME_CHILD_EDUCATION` | REDTEAM_FIRST | repeat_subscription, export_channel, low_birthrate_offset, fcf_conversion | birthrate_decline, tam_shrink, inventory, policy_risk |
| `HOME_LIVING_APPLIANCE_RENTAL` | WATCH_YELLOW_FIRST | rental_churn_stable, recurring_service_revenue, opm_fcf_improvement, overseas_margin | replacement_cycle, housing_turnover, churn, hardware_only, dividend_suspension |
| `SERVICE_KIOSK_SELF_CHECKOUT` | WATCH_YELLOW_FIRST | maintenance_revenue, payment_fee_revenue, loss_prevention_effect, recurring_service_revenue | theft, customer_friction, retailer_retreat, employee_workload, one_off_hardware |
| `CONSUMER_REGULATED_PRODUCT` | WATCH_YELLOW_FIRST | sales_authorization, channel_access, repeat_consumption, regulatory_stability | public_health, social_backlash, legal_conflict, license_scope, youth_usage |
| `FOOD_INPUT_REGULATED_CYCLE` | WATCH_YELLOW_FIRST | price_pass_through, regulated_margin, cost_stabilization, fcf_conversion | cost, price_control, regulation, commodity_cycle |
| `POLICY_LOCAL_SERVICE_THEME` | REDTEAM_FIRST | budget_approved, contract_awarded, revenue_visibility, fcf_conversion | policy_dependency, budget_missing, no_contract, no_revenue |
| `AGRI_DISEASE_EVENT_OVERLAY` | REDTEAM_FIRST | repeat_procurement, multi_period_margin, low_normalization_risk | one_off_disease, price_normalization, government_inquiry |
| `AI_EDUCATION_DISRUPTION_OVERLAY` | REDTEAM_FIRST | b2b_contract, completion_rate, student_roi, fcf_conversion | ai_substitution, cac_spike, bookings_miss, debt |
| `REGULATED_CONSUMER_APPROVAL_OVERLAY` | REDTEAM_FIRST | authorization_scope, sales_channel, repeat_consumption, regulatory_stability | license_scope, legal_conflict, youth_usage, public_health |

## What Not To Change

- Do not apply these R12 Loop-2 v2 weights to production scoring yet.
- Do not treat essential demand, policy support, weather, disease, grain prices, education users, rental accounts, or FDA/DEA headlines as Green evidence by itself.
- Do not invent unit economics, government orders, completion rates, CAC, churn, regulatory scope, software attach rate, or price-path fields.
- Do not lower Stage 3-Green for R12 recall. Green requires repeat contracts, repeat revenue, unit economics, regulatory stability, and FCF conversion.
- Treat Chapter 11, AI substitution, bookings misses, dividend suspension, retailer retreat, theft/shrink, public-health reversal, commodity normalization, and right-to-repair risk as RedTeam evidence.
