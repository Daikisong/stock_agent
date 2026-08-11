from __future__ import annotations

import unittest

from e2r.research_brain.researcher_mode.collaboration_envelope_contract import (
    _validate_schema_definition,
    _validate_schema_instance,
)


class CollaborationEnvelopeContractTests(unittest.TestCase):
    def test_prefix_items_bind_array_positions_and_allow_a_valid_tail(self) -> None:
        schema = {
            "type": "array",
            "prefixItems": [
                {"type": "integer", "enum": [2]},
                {"type": "integer", "enum": [5]},
            ],
            "items": {"type": "integer", "enum": [9]},
            "minItems": 2,
            "maxItems": 3,
        }

        _validate_schema_definition(schema, path="$")
        _validate_schema_instance([2, 5], schema, path="$")
        _validate_schema_instance([2, 5, 9], schema, path="$")

        with self.assertRaisesRegex(ValueError, r"\$/0:enum"):
            _validate_schema_instance([5, 2], schema, path="$")
        with self.assertRaisesRegex(ValueError, r"\$/2:enum"):
            _validate_schema_instance([2, 5, 8], schema, path="$")

    def test_false_items_rejects_only_values_after_the_prefix(self) -> None:
        schema = {
            "type": "array",
            "prefixItems": [
                {"type": "string", "enum": ["first"]},
                {"type": "string", "enum": ["second"]},
            ],
            "items": False,
        }

        _validate_schema_definition(schema, path="$")
        _validate_schema_instance(["first", "second"], schema, path="$")
        with self.assertRaisesRegex(ValueError, r"\$/2:falseSchema"):
            _validate_schema_instance(
                ["first", "second", "unexpected"],
                schema,
                path="$",
            )

    def test_prefix_items_definition_is_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "prefixItems invalid"):
            _validate_schema_definition(
                {"type": "array", "prefixItems": []},
                path="$",
            )
        with self.assertRaisesRegex(ValueError, "unsupported collaboration schema keyword"):
            _validate_schema_definition(
                {
                    "type": "array",
                    "prefixItems": [{"type": "integer", "const": 1}],
                },
                path="$",
            )


if __name__ == "__main__":
    unittest.main()
