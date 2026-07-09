import ast
import inspect
import unittest
from pathlib import Path

from e2r.research_brain.recipes import legacy_route_recovery


class LegacySourceRouteNotProductionReachableTests(unittest.TestCase):
    def test_parity_production_module_imports_canonical_recipe_projection(self) -> None:
        text = Path("src/e2r/census/research_to_runtime_parity.py").read_text(encoding="utf-8")
        self.assertNotIn("from e2r.source_routing", text)
        self.assertIn(
            "from e2r.research_brain.recipes.legacy_route_recovery",
            text,
        )

    def test_compatibility_route_does_not_inspect_primitive_name(self) -> None:
        signature = inspect.signature(legacy_route_recovery._compatibility_route_families)
        self.assertNotIn("primitive", signature.parameters)
        source = inspect.getsource(legacy_route_recovery._compatibility_route_families)
        self.assertNotIn("key in primitive", source)
        self.assertNotIn("primitive.lower", source)

    def test_legacy_source_route_module_is_adapter_only(self) -> None:
        path = Path("src/e2r/source_routing/research_source_route_recovery.py")
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        imports = [
            node.module
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module
        ]
        self.assertIn("e2r.research_brain.recipes.legacy_route_recovery", imports)


if __name__ == "__main__":
    unittest.main()
