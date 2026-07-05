import json
import unittest
from pathlib import Path


class ResearchMemoryNoFutureOutcomeInPromptTests(unittest.TestCase):
    def test_runtime_planner_payload_excludes_price_path_outcome_metrics(self) -> None:
        payload = json.loads(Path("docs/operational/research_runtime_memory_cards_v2.json").read_text(encoding="utf-8"))
        serialized = json.dumps(payload["runtime_planner_payloads"], ensure_ascii=False).lower()
        for token in ("price_path_metrics", "future_return", "outcome_label", "mfe_score", "mae_score"):
            self.assertNotIn(token, serialized)
        for item in payload["runtime_planner_payloads"]:
            self.assertNotIn("url_backed_replay_cases", item)
            self.assertNotIn("source_proxy_only_cases", item)
            self.assertNotIn("evidence_url_pending_cases", item)


if __name__ == "__main__":
    unittest.main()
