# Round 242 R12 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- recurring_revenue_or_repeat_purchase_confirmed
- churn_or_retention_stable
- arpu_or_pricing_power_confirmed
- paid_enrollment_or_utilization_confirmed
- unit_economics_confirmed
- cash_conversion_visible
- input_cost_pass_through_confirmed
- inventory_or_receivables_stable
- subsidy_dependency_low
- price_path_after_evidence

## Forbidden Patterns

- policy_news_only
- education_quota_only
- ai_textbook_theme_only
- birthrate_headline_only
- pet_welfare_policy_only
- agri_input_price_spike_only
- feed_cost_spike_without_pass_through
- celebrity_food_event_only
- subsidy_dependent_revenue
- unconfirmed_demand_conversion

## Easy Example
- `출산율 반등 + 유아주 기대` is Stage 1/2 routing.
- `유료 이용률 + 반복매출 + margin + cash conversion` is the evidence bundle required for deeper Stage review.
- `치킨 이벤트 +20-30%` is 4B-watch/event premium until repeat demand and margin prove otherwise.
