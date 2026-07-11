from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.dossier import merge_dossier_source_runs


class DossierSourceMergeTests(unittest.TestCase):
    def test_documents_and_task_lineage_merge_without_duplicate_credit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a, b, output = root / "a", root / "b", root / "out"
            for path in (a, b):
                path.mkdir()
            self._jsonl(a / "question_source_tasks.jsonl", [{"task_id": "T1", "target_id": "X"}])
            self._jsonl(b / "question_source_tasks.jsonl", [{"task_id": "T2", "target_id": "X"}])
            self._jsonl(
                a / "evidence_documents.jsonl",
                [{"document_id": "D1", "target_id": "X", "content_hash": "H", "source_task_ids": ["T1"]}],
            )
            self._jsonl(
                b / "evidence_documents.jsonl",
                [{"document_id": "D1", "target_id": "X", "content_hash": "H", "source_task_ids": ["T2"]}],
            )
            result = merge_dossier_source_runs(
                source_roots=(a, b), output_root=output, target_id="X"
            )
            self.assertEqual(result["status"], "DOSSIER_SOURCE_MERGE_PASS")
            documents = [json.loads(line) for line in (output / "evidence_documents.jsonl").read_text().splitlines()]
            self.assertEqual(documents[0]["source_task_ids"], ["T1", "T2"])

    @staticmethod
    def _jsonl(path: Path, rows) -> None:
        path.write_text("".join(json.dumps(row) + "\n" for row in rows))


if __name__ == "__main__":
    unittest.main()
