import unittest

from e2r.production.source_connectors import build_default_source_provider_registry


class CutoverV2LiveConnectorsNotAliasesTests(unittest.TestCase):
    def test_default_registry_has_no_snapshot_alias_connectors(self):
        registry = build_default_source_provider_registry(".")
        names = [connector.__class__.__name__ for connector in registry.connectors]
        self.assertNotIn("LocalSnapshotConnector", names)
        self.assertIn("OpenDARTLiveConnector", names)
        self.assertIn("CompanyGuideLiveConnector", names)


if __name__ == "__main__":
    unittest.main()
