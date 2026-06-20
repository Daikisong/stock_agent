import unittest

from e2r.calibration.v12_bridge_spec_runtime_field_audit import (
    build_v12_bridge_spec_runtime_field_audit,
    build_runtime_field_inventory,
    render_v12_bridge_spec_runtime_field_audit,
)


class V12BridgeSpecRuntimeFieldAuditTests(unittest.TestCase):
    def test_inventory_collects_parser_feature_and_derived_contracts(self) -> None:
        feature_source = '''
class X:
    def _contract_quality_score(self, fields):
        return fields.max_number("contract_duration_months")
    def _research_axis_bridge_diagnostics(self, fields):
        groups = {
            "research_axis_bridge_contract": (("contract_duration_months",), ("multi_year_contract",)),
        }
        return {}
'''
        parser_source = '''
def _extract_fields(text):
    fields = {}
    aliases = {"contract_duration_months": ("duration",)}
    fields["multi_year_contract"] = True
    parsed = {}
    parsed.setdefault("order_backlog_to_sales", 1.0)
    return fields
'''
        inventory = build_runtime_field_inventory(
            feature_source_text=feature_source,
            parser_source_text=parser_source,
        )

        self.assertIn("contract_duration_months", inventory["feature_method_arg_keys"])
        self.assertIn("contract_duration_months", inventory["bridge_diagnostic_group_keys"])
        self.assertIn("multi_year_contract", inventory["parser_output_keys"])
        self.assertIn("contract_quality", inventory["derived_runtime_metrics"])

    def test_audit_splits_missing_primitive_from_gate_axis_mismatch(self) -> None:
        bridge_specs = {
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY": {
                "runtime_bridge_group": "semiconductor_customer_capacity_bridge",
                "expected_runtime_primitives": (
                    "customer_preorder_or_allocation",
                    "hbm_capacity_pre_sold",
                    "medium_term_revision_visibility",
                ),
            },
            "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE": {
                "runtime_bridge_group": "software_platform_recurring_revenue_bridge",
                "expected_runtime_primitives": ("ad_revenue_growth_pct", "operating_leverage_visible"),
            },
        }
        signal_audit_payload = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "required_bridge_axes": ["customer", "backlog", "contract"],
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "diagnosis": "research_signal_not_structured_into_runtime_fields",
                    "research_clean_green_count": 6,
                    "research_raw_stage3_green_count": 9,
                },
                {
                    "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                    "required_bridge_axes": ["software_retention", "margin"],
                    "missing_required_bridge_axes": [],
                    "runtime_gap_status": "not_in_current_benchmark",
                    "diagnosis": "research_green_fixture_not_archived_for_runtime_replay",
                    "research_clean_green_count": 12,
                    "research_raw_stage3_green_count": 19,
                },
            ]
        }
        feature_source = '''
def f(fields):
    fields.any_bool("customer_preorder_or_allocation", "hbm_capacity_pre_sold")
    return {"medium_term_revision_visibility": 100.0}
'''
        payload = build_v12_bridge_spec_runtime_field_audit(
            bridge_specs=bridge_specs,
            signal_audit_payload=signal_audit_payload,
            feature_source_text=feature_source,
            parser_source_text="def p(): return {}",
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["missing_feature_parser_contract_count"],
            0,
        )
        c06_axis_statuses = {
            item["axis"]: item["status"] for item in by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["axis_contract_statuses"]
        }
        self.assertEqual(
            c06_axis_statuses["backlog"],
            "bridge_spec_axis_present_but_runtime_field_missing_or_too_weak",
        )
        self.assertEqual(c06_axis_statuses["contract"], "required_by_gate_but_absent_from_bridge_spec")
        self.assertEqual(
            by_arch["C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE"]["missing_feature_parser_contract_count"],
            2,
        )

        report = render_v12_bridge_spec_runtime_field_audit(payload)
        self.assertIn("required_by_gate_but_absent_from_bridge_spec", report)
        self.assertIn("missing_feature_parser_contract", report)


if __name__ == "__main__":
    unittest.main()

