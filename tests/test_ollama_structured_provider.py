from __future__ import annotations

import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

from e2r.cli.run_e2r_researcher_mode_until_pass import (
    _build_research_provider,
    _research_provider_manifest,
    build_parser,
)
from e2r.research_brain.planning.provider_transport import (
    OllamaStructuredProviderTransport,
    StructuredProviderRejected,
    StructuredProviderResponse,
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode import (
    CodexResearcherProvider,
    CurrentResearcherModeTargetRunner,
    OllamaResearcherProvider,
)


class _FakeHTTPResponse:
    def __init__(self, value=None, *, raw=None, headers=None):
        self.value = value
        self.raw = raw
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self, limit=None):
        raw = self.raw
        if raw is None:
            raw = json.dumps(self.value, ensure_ascii=False).encode("utf-8")
        return raw if limit is None else raw[:limit]


class OllamaStructuredProviderTests(unittest.TestCase):
    def test_transport_sends_schema_bound_non_thinking_request(self) -> None:
        schema = {
            "type": "object",
            "additionalProperties": False,
            "required": ["usable"],
            "properties": {"usable": {"type": "boolean"}},
        }
        captured = {}

        def fake_urlopen(request, *, timeout):
            captured["url"] = request.full_url
            captured["body"] = json.loads(request.data.decode("utf-8"))
            captured["timeout"] = timeout
            return _FakeHTTPResponse(
                {
                    "message": {"content": '{"usable":false}'},
                    "done": True,
                    "done_reason": "stop",
                    "prompt_eval_count": 10,
                }
            )

        transport = OllamaStructuredProviderTransport(
            model="test-model",
            context_length=65_536,
            timeout_seconds=123,
        )
        with patch("urllib.request.urlopen", side_effect=fake_urlopen):
            response = transport.complete(
                prompt="Use only as-of-date evidence.",
                output_schema=schema,
                schema_name="e2r_test",
            )

        self.assertEqual(response.payload, {"usable": False})
        self.assertEqual(captured["url"], "http://127.0.0.1:11434/api/chat")
        self.assertEqual(captured["timeout"], 123)
        self.assertEqual(captured["body"]["format"], schema)
        self.assertEqual(captured["body"]["options"]["num_ctx"], 65_536)
        self.assertEqual(captured["body"]["options"]["num_predict"], 32_768)
        self.assertFalse(captured["body"]["think"])
        self.assertFalse(captured["body"]["stream"])

    def test_transport_failure_is_provider_pending_class_not_empty_output(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        with patch(
            "urllib.request.urlopen",
            side_effect=urllib.error.URLError("offline"),
        ):
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "ollama_transport_error",
            ):
                transport.complete(
                    prompt="prompt",
                    output_schema={"type": "object"},
                    schema_name="e2r_test",
                )

    def test_transport_rejects_non_object_model_output(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        response = _FakeHTTPResponse(
            {
                "message": {"content": "[]"},
                "done": True,
                "done_reason": "stop",
                "prompt_eval_count": 10,
            }
        )
        with patch("urllib.request.urlopen", return_value=response):
            with self.assertRaisesRegex(
                StructuredProviderRejected,
                "non-object",
            ):
                transport.complete(
                    prompt="prompt",
                    output_schema={"type": "object"},
                    schema_name="e2r_test",
                )

    def test_provider_cache_is_bound_to_ollama_inference_identity(self) -> None:
        transport = OllamaStructuredProviderTransport(
            base_url="http://127.0.0.1:11434",
            model="model-a",
            context_length=65_536,
            model_digest="a" * 64,
            server_version="0.32.1",
        )
        provider = OllamaResearcherProvider(transport=transport)
        identity = provider._provider_identity()
        self.assertEqual(identity["model"], "model-a")
        self.assertEqual(identity["context_length"], 65_536)
        self.assertEqual(identity["model_digest"], "a" * 64)
        self.assertEqual(identity["base_url"], "http://127.0.0.1:11434")
        with tempfile.TemporaryDirectory() as directory:
            provider.configure_response_cache(Path(directory))
            self.assertEqual(
                provider.response_cache_audit()["provider_name"],
                "OLLAMA_STRUCTURED_RESEARCHER_MODE",
            )

    def test_cli_uses_ollama_only_after_explicit_selection(self) -> None:
        base = [
            "--as-of-date", "2026-06-29",
            "--symbols", "005930",
            "--archetype", "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "--live-materialization-authorized", "true",
            "--checkpoint-resume", "true",
            "--gold-lane-isolated", "true",
            "--require-researcher-parity", "true",
            "--output-root", "output/test",
        ]
        default_args = build_parser().parse_args(base)
        self.assertIsNone(_build_research_provider(default_args))

        local_args = build_parser().parse_args(
            [
                *base,
                "--research-provider", "ollama",
                "--ollama-model", "model-b",
                "--ollama-context-length", "65536",
                "--ollama-fact-document-chunk-chars", "90000",
            ]
        )
        provider = _build_research_provider(local_args)
        self.assertIsInstance(provider, OllamaResearcherProvider)
        self.assertEqual(provider.transport.model, "model-b")
        self.assertEqual(provider.transport.context_length, 65_536)
        self.assertEqual(provider.fact_document_chunk_chars, 90_000)
        runner = CurrentResearcherModeTargetRunner(provider=provider)
        self.assertEqual(
            runner.fact_extractor.max_document_chars_per_call,
            90_000,
        )
        provider.transport.model_digest = "b" * 64
        provider.transport.server_version = "0.32.1"
        manifest = _research_provider_manifest(provider)
        self.assertTrue(manifest["provider_selected_explicitly"])
        self.assertFalse(manifest["score_or_stage_authority"])
        self.assertEqual(
            manifest["provider_identity"]["model_digest"],
            "b" * 64,
        )

    def test_incomplete_or_unaccounted_response_is_rejected(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        for envelope in (
            {
                "message": {"content": '{}'},
                "done_reason": "stop",
                "prompt_eval_count": 10,
            },
            {
                "message": {"content": '{}'},
                "done": True,
                "done_reason": "length",
                "prompt_eval_count": 10,
            },
            {
                "message": {"content": '{}'},
                "done": True,
                "done_reason": "stop",
            },
        ):
            with self.subTest(envelope=envelope):
                with patch(
                    "urllib.request.urlopen",
                    return_value=_FakeHTTPResponse(envelope),
                ):
                    with self.assertRaises(StructuredProviderRejected):
                        transport.complete(
                            prompt="prompt",
                            output_schema={"type": "object"},
                            schema_name="e2r_test",
                        )

    def test_malformed_utf8_is_rejected_and_response_is_bounded(self) -> None:
        transport = OllamaStructuredProviderTransport(model="test-model")
        with patch(
            "urllib.request.urlopen",
            return_value=_FakeHTTPResponse(raw=b"\xff\xfe"),
        ):
            with self.assertRaisesRegex(
                StructuredProviderRejected,
                "malformed UTF-8",
            ):
                transport.complete(
                    prompt="prompt",
                    output_schema={"type": "object"},
                    schema_name="e2r_test",
                )

    def test_prompt_cap_and_remote_plaintext_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "loopback"):
            OllamaStructuredProviderTransport(
                base_url="http://192.0.2.10:11434",
                model="test-model",
            )
        transport = OllamaStructuredProviderTransport(
            model="test-model",
            prompt_character_limit=10,
        )
        with self.assertRaisesRegex(
            StructuredProviderRejected,
            "prompt_transport_too_large",
        ):
            transport.complete(
                prompt="x" * 11,
                output_schema={"type": "object"},
                schema_name="e2r_test",
            )

    def test_mutable_model_tag_resolves_to_digest_and_server_version(self) -> None:
        transport = OllamaStructuredProviderTransport(model="model-a")

        def fake_urlopen(request, *, timeout):
            if request.full_url.endswith("/api/tags"):
                return _FakeHTTPResponse(
                    {
                        "models": [
                            {
                                "name": "model-a",
                                "model": "model-a",
                                "digest": "c" * 64,
                            }
                        ]
                    }
                )
            if request.full_url.endswith("/api/version"):
                return _FakeHTTPResponse({"version": "0.32.1"})
            raise AssertionError(request.full_url)

        with patch("urllib.request.urlopen", side_effect=fake_urlopen):
            identity = transport.provider_identity()
        self.assertEqual(identity["model_digest"], "c" * 64)
        self.assertEqual(identity["server_version"], "0.32.1")

    def test_blind_output_violation_is_audited_and_never_cached(self) -> None:
        class ForbiddenOutputTransport:
            model = "test"
            profile = None
            extra_args = ()
            codex_command = None

            def complete(self, **kwargs):
                return StructuredProviderResponse(
                    payload={"total_score": 99},
                    raw_response='{"total_score":99}',
                    stderr="",
                    returncode=0,
                )

        provider = CodexResearcherProvider(
            transport=ForbiddenOutputTransport()
        )
        with tempfile.TemporaryDirectory() as directory:
            provider.configure_response_cache(directory)
            with self.assertRaisesRegex(
                StructuredProviderRejected,
                "blind_output_rejected",
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={"target_id": "TEST", "as_of_date": "2026-06-29"},
                )
            self.assertEqual(
                provider.calls[-1]["status"],
                "PROVIDER_OUTPUT_REJECTED",
            )
            self.assertEqual(
                provider.response_cache_audit()[
                    "provider_output_rejected_count"
                ],
                1,
            )
            self.assertEqual(tuple(Path(directory).glob("*.json")), ())

    def test_codex_selection_rejects_silently_ignored_ollama_option(self) -> None:
        args = build_parser().parse_args(
            [
                "--as-of-date", "2026-06-29",
                "--symbols", "005930",
                "--archetype", "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "--live-materialization-authorized", "true",
                "--checkpoint-resume", "true",
                "--gold-lane-isolated", "true",
                "--require-researcher-parity", "true",
                "--output-root", "output/test",
                "--ollama-model", "model-b",
            ]
        )
        with self.assertRaisesRegex(ValueError, "require"):
            _build_research_provider(args)


if __name__ == "__main__":
    unittest.main()
