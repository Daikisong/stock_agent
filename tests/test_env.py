import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from e2r.env import load_project_env
from e2r.research.naver_search_provider import NaverFreeSearchProvider


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


if __name__ == "__main__":
    unittest.main()
