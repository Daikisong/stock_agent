from datetime import date
import json
from pathlib import Path
import tempfile
import unittest

from e2r.backtest.blind_discovery_replay import BlindDiscoveryConfig, BlindDiscoveryReplay
from e2r.models import Stage


ROOT = Path(__file__).resolve().parents[1]


class BenchmarkLeakageTests(unittest.TestCase):
    def test_production_modules_do_not_import_benchmark_labels(self):
        module_paths = [
            ROOT / "src/e2r/pipeline/e2r_standard_flow.py",
            ROOT / "src/e2r/cheap_scan/korea_scanner.py",
            ROOT / "src/e2r/cheap_scan/event_rules.py",
            ROOT / "src/e2r/features.py",
            ROOT / "src/e2r/staging.py",
            ROOT / "src/e2r/red_team.py",
            ROOT / "src/e2r/llm/prompts.py",
        ] + sorted((ROOT / "src/e2r/research").glob("*.py"))
        for path in module_paths:
            with self.subTest(path=path.name):
                self.assertNotIn("benchmark_labels", path.read_text(encoding="utf-8"))

    def test_fake_label_without_evidence_only_appears_as_missed(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            labels = [
                {
                    "label_id": "fake_green_label",
                    "symbol": "999999",
                    "company_name": "가짜그린",
                    "market": "KR",
                    "expected_window_start": "2023-01-01",
                    "expected_window_end": "2023-12-31",
                    "expected_group": "structural",
                    "expected_min_layer": "stage3",
                    "expected_safe_stage": "Green",
                    "notes": "Adversarial label with no source evidence.",
                    "evaluation_only": True,
                }
            ]
            label_path = root_path / "labels.json"
            label_path.write_text(json.dumps(labels, ensure_ascii=False), encoding="utf-8")
            result = BlindDiscoveryReplay().run(
                BlindDiscoveryConfig(
                    start_date=date(2023, 1, 1),
                    end_date=date(2023, 12, 31),
                    benchmark_label_path=label_path,
                    search_snapshot_root=root_path / "missing_search",
                    report_snapshot_root=root_path / "missing_reports",
                ),
                write_outputs=False,
            )

        self.assertFalse(result.discovered_candidates)
        self.assertEqual(result.benchmark_recall[0].label_id, "fake_green_label")
        self.assertFalse(result.benchmark_recall[0].appeared_in_candidates)
        self.assertIsNone(result.benchmark_recall[0].first_stage)

    def test_expected_green_label_cannot_create_stage_green_without_evidence(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            label_path = root_path / "labels.json"
            label_path.write_text(
                json.dumps(
                    [
                        {
                            "label_id": "fake_expected_green",
                            "symbol": "123456",
                            "company_name": "증거없는회사",
                            "market": "KR",
                            "expected_window_start": "2024-01-01",
                            "expected_window_end": "2024-12-31",
                            "expected_group": "structural",
                            "expected_min_layer": "stage3",
                            "expected_safe_stage": "Green",
                            "notes": "The label expects Green but no evidence exists.",
                            "evaluation_only": True,
                        }
                    ],
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            result = BlindDiscoveryReplay().run(
                BlindDiscoveryConfig(
                    start_date=date(2024, 1, 1),
                    end_date=date(2024, 12, 31),
                    benchmark_label_path=label_path,
                    search_snapshot_root=root_path / "search",
                    report_snapshot_root=root_path / "reports",
                ),
                write_outputs=False,
            )

        self.assertNotIn(Stage.STAGE_3_GREEN, {item.stage for item in result.discovered_candidates})
        self.assertFalse(result.benchmark_recall[0].appeared_in_candidates)


if __name__ == "__main__":
    unittest.main()
