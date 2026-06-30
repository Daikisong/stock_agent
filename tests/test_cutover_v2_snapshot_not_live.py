import unittest

from e2r.production.source_connectors import SourceFetchResult


class CutoverV2SnapshotNotLiveTests(unittest.TestCase):
    def test_snapshot_url_never_counts_as_live(self):
        result = SourceFetchResult(
            provider_name="OpenDART",
            source_class="DART",
            mode="snapshot",
            request_id="REQ",
            status="FETCHED",
            canonical_url="snapshot://OpenDART/foo",
            content_hash="abc",
        )
        self.assertFalse(result.counts_as_live)


if __name__ == "__main__":
    unittest.main()
