# E2R Round-1 Research Framework

This document records the analyst Round-1 synthesis before any production
scoring changes.

The key correction is:

```text
Current implementation can keep detailed extension archetypes,
but the research frame should still roll up to 25 core archetypes.
```

For example:

```text
VALUE_UP_SHAREHOLDER_RETURN
-> useful detail
-> rolls up to FINANCIAL_SPREAD_BALANCE_SHEET in Round-1

BIOTECH_ROYALTY_COMMERCIALIZATION
-> useful detail
-> rolls up to BIOTECH_REGULATORY in Round-1
```

## Three Blocks

### A. Structural E2R Candidates

These can produce Stage 3-Green later, but only with strict evidence:

- `CONTRACT_BACKLOG_INDUSTRIAL`
- `DEFENSE_GOVERNMENT_BACKLOG`
- `SHIPBUILDING_OFFSHORE_BACKLOG`
- `EXPORT_RECURRING_CONSUMER`
- `K_BEAUTY_EXPORT_DISTRIBUTION`
- `MEMORY_HBM_CAPACITY`
- `SEMI_EQUIPMENT_CAPEX`
- `MEDICAL_DEVICE_HEALTHCARE_EXPORT`
- `FINANCIAL_SPREAD_BALANCE_SHEET`
- `TURNAROUND_COST_RESTRUCTURING`

### B. Cyclical / Spread Guardrailed

These can move a lot, but Green should be capped unless structural durability is
clear:

- `COMMODITY_SPREAD`
- `SHIPPING_FREIGHT_CYCLE`
- `BATTERY_MATERIALS_CAPEX_OVERHEAT`
- `AUTO_MOBILITY_COMPONENTS`
- `CONSTRUCTION_REAL_ESTATE_CREDIT`
- `UTILITIES_REGULATED_TARIFF`

### C. Red / Yellow Guardrail

These are more useful for avoiding false Green than for granting Green:

- `BIOTECH_REGULATORY`
- `ROBOTICS_FACTORY_AUTOMATION`
- `PLATFORM_SOFTWARE_INTERNET`
- `GAME_CONTENT_IP`
- `HOLDING_RESTRUCTURING_GOVERNANCE`
- `ONE_OFF_EVENT_DEMAND`
- `THEME_VALUATION_OVERHEAT`
- `RETAIL_DOMESTIC_CONSUMER`
- `GENERIC_UNCLASSIFIED`

## Extensions

Checkpoint 28A-2 added more detailed archetypes. They are retained, but Round-1
reports roll them up:

- `AI_DATA_CENTER_INFRASTRUCTURE` -> `SEMI_EQUIPMENT_CAPEX`
- `NUCLEAR_SMR_GRID_POLICY` -> `UTILITIES_REGULATED_TARIFF`
- `TRAVEL_LEISURE_REOPENING` -> `RETAIL_DOMESTIC_CONSUMER`
- `EDUCATION_SPECIALTY_SERVICES` -> `RETAIL_DOMESTIC_CONSUMER`
- `RARE_METALS_STRATEGIC_MATERIALS` -> `COMMODITY_SPREAD`
- `VALUE_UP_SHAREHOLDER_RETURN` -> `FINANCIAL_SPREAD_BALANCE_SHEET`
- `BIOTECH_PRE_REVENUE_REGULATORY` -> `BIOTECH_REGULATORY`
- `BIOTECH_ROYALTY_COMMERCIALIZATION` -> `BIOTECH_REGULATORY`
- `CDMO_HEALTHCARE_CONTRACT` -> `MEDICAL_DEVICE_HEALTHCARE_EXPORT`
- `AUTO_MOBILITY_COMPLETED_VEHICLE` -> `AUTO_MOBILITY_COMPONENTS`

## Guardrails

- Do not apply score weights yet.
- Do not use case records as candidate-generation input.
- Do not treat cycle/spread cases as structural Green without evidence.
- Do not treat event premium as true rerating.
- Do not collapse extension archetypes destructively until all analyst rounds are ingested.
