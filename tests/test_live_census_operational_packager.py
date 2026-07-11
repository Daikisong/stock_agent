from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.production.metadata import stable_hash
from e2r.research_brain.runtime import (
    CurrentOperationRunnerConfig,
    CurrentOperationRunnerInput,
    DailyBaselineLane,
    DailyBaselineLaneStatus,
    DailyBaselineLaneType,
    DailyUniverseMember,
    run_current_daily_census,
)
from e2r.research_brain.runtime.live_materialization import (
    audit_current_census_source_corpus_hash,
    package_live_census_operation,
)


class LiveCensusOperationalPackagerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        as_of_date = "2026-07-10"
        universe = tuple(
            DailyUniverseMember(
                target_id=f"{index:06d}",
                target_name=f"검증기업{index}",
                market="KOSPI" if index % 2 else "KOSDAQ",
                as_of_date=as_of_date,
            )
            for index in range(1, 8)
        )
        lanes = tuple(
            DailyBaselineLane(
                target_id=member.target_id,
                as_of_date=as_of_date,
                lane_type=lane.value,
                lane_status=DailyBaselineLaneStatus.OBSERVED.value,
                source_ids=(f"SRC-{member.target_id}-{lane.value}",),
                observed_date=as_of_date,
            )
            for member in universe
            for lane in DailyBaselineLaneType
        )
        cls.inputs = CurrentOperationRunnerInput(
            as_of_date=as_of_date,
            universe=universe,
            baseline_lanes=lanes,
            triggers=(),
            claims=(),
            source_tasks=(),
            atomic_decisions=(),
            deep_executions=(),
            config=CurrentOperationRunnerConfig(
                max_official_light_targets=3,
                max_deep_candidates=2,
                max_brain_candidates=2,
                max_acquisition_candidates=2,
                max_llm_calls_per_candidate=2,
                max_source_tasks_per_candidate=3,
                max_fetches_per_candidate=4,
                max_retries_per_candidate=1,
                max_general_web_fetches_per_candidate=1,
                max_runtime_seconds=60.0,
                test_mode=True,
            ),
        )
        cls.result = run_current_daily_census(cls.inputs)

    def test_full_map_shards_and_hard_acceptance_are_complete(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = package_live_census_operation(
                result=self.result,
                output_root=root,
                shard_count=3,
                resume=False,
            )
            rows = self._read_jsonl(paths["census_stage_map_jsonl"])
            audit = json.loads(
                paths["census_acceptance_audit"].read_text(encoding="utf-8")
            )

            self.assertEqual(len(rows), 7)
            self.assertEqual(len({row["target_id"] for row in rows}), 7)
            self.assertTrue(all(row["source_attempted"] for row in rows))
            self.assertEqual(audit["critical_count_sum"], 0)
            self.assertEqual(set(audit["hard_acceptance_counts"].values()), {0})
            self.assertEqual(audit["checkpoint_count"], 3)
            self.assertEqual(
                audit["current_source_corpus_hash"],
                self.result.manifest["source_corpus_hash"],
            )
            self.assertEqual(
                audit["census_source_corpus_hash"],
                self.result.manifest["source_corpus_hash"],
            )
            self.assertEqual(
                audit["source_corpus_hash"],
                self.result.manifest["source_corpus_hash"],
            )
            self.assertEqual(
                audit["source_corpus_hash_audit"]["status"],
                "CURRENT_CENSUS_SOURCE_CORPUS_HASH_PASS",
            )
            self.assertTrue((root / "census_stage_map.csv").is_file())
            self.assertTrue((root / "operator_digest.md").is_file())

    def test_resume_is_idempotent_and_repairs_corrupt_shard(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = package_live_census_operation(
                result=self.result,
                output_root=root,
                shard_count=4,
                resume=True,
            )
            first_rows = self._read_jsonl(first["census_stage_map_jsonl"])
            first_hash = stable_hash(first_rows)
            second = package_live_census_operation(
                result=self.result,
                output_root=root,
                shard_count=4,
                resume=True,
            )
            second_audit = json.loads(
                second["census_acceptance_audit"].read_text(encoding="utf-8")
            )
            self.assertEqual(second_audit["reused_shard_count"], 4)
            self.assertEqual(
                stable_hash(self._read_jsonl(second["census_stage_map_jsonl"])),
                first_hash,
            )

            first_shard = second["census_shard_0000"]
            first_shard.write_text('{"target_id":"CORRUPT"}\n', encoding="utf-8")
            repaired = package_live_census_operation(
                result=self.result,
                output_root=root,
                shard_count=4,
                resume=True,
            )
            repaired_audit = json.loads(
                repaired["census_acceptance_audit"].read_text(encoding="utf-8")
            )
            self.assertEqual(repaired_audit["reused_shard_count"], 3)
            self.assertEqual(
                stable_hash(self._read_jsonl(repaired["census_stage_map_jsonl"])),
                first_hash,
            )

    def test_same_source_snapshot_replay_has_zero_corpus_variance(self) -> None:
        first = run_current_daily_census(self.inputs)
        second = run_current_daily_census(self.inputs)

        self.assertEqual(
            first.manifest["source_corpus_hash"],
            second.manifest["source_corpus_hash"],
        )
        with tempfile.TemporaryDirectory() as first_tmp, tempfile.TemporaryDirectory() as second_tmp:
            first_paths = package_live_census_operation(
                result=first,
                output_root=first_tmp,
                shard_count=2,
                resume=False,
            )
            second_paths = package_live_census_operation(
                result=second,
                output_root=second_tmp,
                shard_count=2,
                resume=False,
            )
            first_audit = json.loads(
                first_paths["census_acceptance_audit"].read_text(encoding="utf-8")
            )
            second_audit = json.loads(
                second_paths["census_acceptance_audit"].read_text(encoding="utf-8")
            )
            self.assertEqual(
                first_audit["source_corpus_hash"],
                second_audit["source_corpus_hash"],
            )

    def test_current_census_source_corpus_hash_mismatch_is_rejected(self) -> None:
        audit = audit_current_census_source_corpus_hash(
            current_source_corpus_hash="a" * 64,
            census_source_corpus_hash="b" * 64,
        )

        self.assertEqual(audit["status"], "CURRENT_CENSUS_SOURCE_CORPUS_HASH_FAIL")
        self.assertEqual(
            audit["critical_counts"][
                "current_census_source_corpus_hash_mismatch"
            ],
            1,
        )
        original = self.result.manifest["source_corpus_hash"]
        self.result.manifest["source_corpus_hash"] = "b" * 64
        try:
            with tempfile.TemporaryDirectory() as tmp:
                with self.assertRaisesRegex(
                    ValueError,
                    "current_census_source_corpus_hash_mismatch",
                ):
                    package_live_census_operation(
                        result=self.result,
                        output_root=tmp,
                        shard_count=2,
                        resume=False,
                    )
        finally:
            self.result.manifest["source_corpus_hash"] = original

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, object]]:
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]


if __name__ == "__main__":
    unittest.main()
