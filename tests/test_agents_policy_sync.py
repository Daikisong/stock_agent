import unittest
from pathlib import Path


class AgentsPolicySyncTests(unittest.TestCase):
    def test_agents_documents_three_operational_modes(self):
        text = Path("AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Research/backfill mode", text)
        self.assertIn("Production daily mode", text)
        self.assertIn("Test mode", text)
        self.assertIn("top_results=None", text)
        self.assertIn("Provider/Source Pending", text)


if __name__ == "__main__":
    unittest.main()
