import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.checkpoint_store import CheckpointStore, create_checkpoint


class CensusCheckpointResumeTests(unittest.TestCase):
    def test_checkpoint_round_trip_includes_hashes(self):
        with TemporaryDirectory() as tmp:
            store = CheckpointStore(Path(tmp) / "checkpoint.json")
            checkpoint = create_checkpoint(
                run_id="R",
                as_of_date="2026-07-01",
                shard_count=2,
                shard_index=0,
                processed_symbols=["005930"],
                failed_symbols=[],
                pending_symbols=[],
                source_corpus={"a": 1},
                config={"b": 2},
                completed=True,
            )
            store.save(checkpoint)
            loaded = store.load()
            self.assertEqual(loaded.processed_symbols, ("005930",))
            self.assertTrue(loaded.source_corpus_hash)
            self.assertTrue(loaded.config_hash)


if __name__ == "__main__":
    unittest.main()
