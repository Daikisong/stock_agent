import os
from datetime import date
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.env import load_project_env
from e2r.probe.api_probe import _naver_targets
from e2r.research.naver_search_provider import (
    NAVER_DEFAULT_SEARCH_DOMAINS,
    NAVER_SEARCH_ENDPOINTS,
    NaverFreeSearchProvider,
)


class EnvLoadingTests(unittest.TestCase):
    def test_load_project_env_fills_missing_values_without_overriding_existing_env(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict("os.environ", {"NAVER_CLIENT_ID": "EXISTING"}, clear=True):
            env_path = Path(directory) / ".env"
            env_path.write_text(
                "\n".join(
                    (
                        "# comment",
                        "NAVER_CLIENT_ID=FROM_FILE",
                        "NAVER_CLIENT_SECRET='SECRET_FROM_FILE'",
                        'DATA_GO_KR_SERVICE_KEY="DATA_FROM_FILE"',
                    )
                ),
                encoding="utf-8",
            )

            loaded = load_project_env(env_path)

            self.assertEqual(os.environ["NAVER_CLIENT_ID"], "EXISTING")
            self.assertEqual(os.environ["NAVER_CLIENT_SECRET"], "SECRET_FROM_FILE")
            self.assertEqual(os.environ["DATA_GO_KR_SERVICE_KEY"], "DATA_FROM_FILE")
            self.assertNotIn("NAVER_CLIENT_ID", loaded)
            self.assertIn("NAVER_CLIENT_SECRET", loaded)

    def test_live_naver_provider_reads_project_env_when_process_env_is_empty(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict("os.environ", {}, clear=True):
            env_path = Path(directory) / ".env"
            env_path.write_text(
                "NAVER_CLIENT_ID=ID_FROM_FILE\nNAVER_CLIENT_SECRET=SECRET_FROM_FILE\n",
                encoding="utf-8",
            )
            old_cwd = Path.cwd()
            try:
                os.chdir(directory)
                provider = NaverFreeSearchProvider(fixture_mode=False, live_enabled=True)
            finally:
                os.chdir(old_cwd)

        self.assertEqual(provider.client_id, "ID_FROM_FILE")
        self.assertEqual(provider.client_secret, "SECRET_FROM_FILE")

    def test_naver_production_defaults_exclude_retired_professional_document_api(self):
        provider = NaverFreeSearchProvider(
            client_id="ID",
            client_secret="SECRET",
            fixture_mode=False,
            live_enabled=True,
        )

        requests = provider.build_search_requests("issuer report", date(2026, 8, 11), 100)

        self.assertEqual(NAVER_DEFAULT_SEARCH_DOMAINS, ("news", "web"))
        self.assertEqual(tuple(NAVER_SEARCH_ENDPOINTS), NAVER_DEFAULT_SEARCH_DOMAINS)
        self.assertEqual(
            tuple(request.url for request in requests),
            (
                "https://openapi.naver.com/v1/search/news.json",
                "https://openapi.naver.com/v1/search/webkr.json",
            ),
        )
        self.assertNotIn("https://openapi.naver.com/v1/search/doc.json", tuple(request.url for request in requests))

    def test_api_probe_uses_only_current_naver_search_endpoints(self):
        targets = _naver_targets(date(2026, 8, 11), "issuer report")

        self.assertEqual(tuple(target.source_name for target in targets), ("naver_news", "naver_web"))


if __name__ == "__main__":
    unittest.main()
