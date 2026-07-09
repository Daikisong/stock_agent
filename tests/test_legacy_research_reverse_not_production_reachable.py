import ast
import unittest
from pathlib import Path


class LegacyResearchReverseNotProductionReachableTests(unittest.TestCase):
    def test_parity_production_module_imports_canonical_compiler(self) -> None:
        path = Path("src/e2r/census/research_to_runtime_parity.py")
        text = path.read_text(encoding="utf-8")
        self.assertNotIn("from e2r.research_reverse", text)
        self.assertIn(
            "from e2r.research_brain.compiler.legacy_compatibility_reports",
            text,
        )

    def test_legacy_reverse_modules_are_one_way_adapters(self) -> None:
        root = Path("src/e2r/research_reverse")
        for path in root.glob("*.py"):
            if path.name == "__init__.py":
                continue
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            imports = [
                node.module
                for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom) and node.module
            ]
            self.assertTrue(
                any(module.startswith("e2r.research_brain") for module in imports),
                path.name,
            )

    def test_canonical_compatibility_compiler_does_not_import_reverse(self) -> None:
        path = Path("src/e2r/research_brain/compiler/legacy_compatibility_reports.py")
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        imports: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.append(node.module)
        self.assertFalse(
            any(module.startswith("e2r.research_reverse") for module in imports),
            imports,
        )


if __name__ == "__main__":
    unittest.main()
