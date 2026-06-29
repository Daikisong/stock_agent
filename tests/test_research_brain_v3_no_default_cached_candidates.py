import unittest
from pathlib import Path


class ResearchBrainV3NoDefaultCachedCandidatesTests(unittest.TestCase):
    def test_v3_orchestrator_does_not_reference_v2_cached_candidate_path(self):
        text = Path("src/e2r/research_brain/v3_production_orchestrator.py").read_text(encoding="utf-8")
        self.assertNotIn("DEFAULT_CANDIDATES_PATH", text)
        self.assertNotIn("live_operational_semis_2026-06-12_targeted_only_shared_cache", text)


if __name__ == "__main__":
    unittest.main()
