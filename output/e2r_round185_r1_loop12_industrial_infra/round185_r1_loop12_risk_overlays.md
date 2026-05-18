# Round-185 R1 Loop-12 Risk Overlays

| target | hard gate | red flags |
| --- | --- | --- |
| `GRID_TRANSFORMER_MIDCAP_KOREA` | false | customer_missing, counterparty_missing, price_only_rally, margin_unknown, capa_normalization |
| `POWER_CABLE_GRID_BACKLOG_KOREA` | false | customer_missing, margin_unknown, copper_passthrough_missing, price_only_rotation |
| `DEFENSE_ELECTRONICS_KF21_RADAR` | false | actual_revenue_missing, opm_missing, export_contract_missing |
| `SPACE_LAUNCH_PROGRAM_OF_RECORD` | false | capital_raise, dilution, fss_revision_request, contract_missing |
| `DEFENSE_CAPITAL_RAISE_DILUTION` | true | large_capital_raise, fss_revision_request, dilution, use_of_proceeds_unclear |
| `CONSTRUCTION_EQUIPMENT_CYCLE_KOREA` | false | dealer_inventory_risk, high_borrowing_cost, global_machinery_warning, china_real_estate |
| `CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY` | true | minority_shareholder_risk, controversial_restructuring, governance_discount |
| `NUCLEAR_DECOMMISSIONING_KOREA` | false | company_contract_missing, policy_only, opm_missing |
| `NUCLEAR_POLICY_STAGE1_2_NOT_GREEN` | false | policy_only, contract_missing, scope_unknown |
| `SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA` | false | delivery_missing, opm_missing, price_only_rotation, low_margin_order |
| `SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK` | true | investment_loss, strategy_retreat, theme_without_revenue |
| `DISCLOSURE_CONFIDENCE_CAP` | false | opendart_list_only, media_only, mou_loi, non_binding, detail_missing |

## Hard 4C Examples

- `DEFENSE_CAPITAL_RAISE_DILUTION`: large rights offering, FSS revision request, dilution, and disclosure confidence hit.
- `CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY`: controversial restructuring and minority shareholder value risk.
- `SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK`: satellite investment loss and strategy retreat.
- `DISCLOSURE_CONFIDENCE_CAP`: list-only, media-only, MOU/LOI, non-binding, or missing detail cannot create Green.
