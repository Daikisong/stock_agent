from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from e2r.production.v6_issuer_business_profile import (
    CANONICAL_COMPATIBILITY_PROVIDER,
)
from e2r.production.v6_issuer_business_profile_collaboration import (
    CollaborationIssuerBusinessCompatibilityProvider,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderResponse,
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexSubagentTransport,
)


class _RecordingTransport:
    def __init__(self) -> None:
        self.root: Path | None = None
        self.call: dict[str, object] | None = None

    def configure_journal_root(self, root: str | Path) -> None:
        self.root = Path(root)

    def complete(self, **kwargs: object) -> StructuredProviderResponse:
        self.call = dict(kwargs)
        payload = {"classification_complete": True, "decisions": []}
        return StructuredProviderResponse(
            payload=payload,
            raw_response=json.dumps(payload, sort_keys=True),
            stderr="",
            returncode=0,
        )


class IssuerBusinessProfileCollaborationTest(unittest.TestCase):
    def test_adapter_uses_one_exact_collaboration_schema(self) -> None:
        transport = _RecordingTransport()
        provider = CollaborationIssuerBusinessCompatibilityProvider(
            journal_root=Path("journal"),
            transport=transport,  # type: ignore[arg-type]
        )
        result = provider.complete(
            prompt="blind current profile",
            output_schema={"type": "object"},
        )
        self.assertEqual(provider.provider_name, CANONICAL_COMPATIBILITY_PROVIDER)
        self.assertTrue(provider.real_provider)
        self.assertFalse(provider.fake_provider)
        self.assertEqual(transport.root, Path("journal"))
        self.assertEqual(
            transport.call,
            {
                "prompt": "blind current profile",
                "output_schema": {"type": "object"},
                "schema_name": "e2r_v5_issuer_business_profile_compatibility",
            },
        )
        self.assertEqual(result.payload["classification_complete"], True)
        self.assertEqual(json.loads(result.raw_response), result.payload)

    def test_real_transport_writes_request_then_fails_closed_pending(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "profile_journal"
            provider = CollaborationIssuerBusinessCompatibilityProvider(
                journal_root=root,
                transport=CollaborationCodexSubagentTransport(),
            )
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                r"COLLABORATION_RESPONSE_PENDING:COLLABREQ-",
            ):
                provider.complete(
                    prompt="current official profile only",
                    output_schema={
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {},
                    },
                )
            requests = tuple((root / "requests").glob("COLLABREQ-*.json"))
            self.assertEqual(len(requests), 1)
            request = json.loads(requests[0].read_text(encoding="utf-8"))
            self.assertEqual(
                request["pass_name"], "ISSUER_BUSINESS_PROFILE_COMPATIBILITY"
            )
            self.assertFalse(request["score_or_stage_authority"])
            self.assertFalse(request["production_score_authority"])
            self.assertEqual(tuple((root / "responses").iterdir()), ())


if __name__ == "__main__":
    unittest.main()
