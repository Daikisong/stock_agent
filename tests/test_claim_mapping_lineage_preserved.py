from __future__ import annotations

import hashlib
import unittest

from e2r.research_brain.runtime.current_operation_runner import DailyClaimProvenance
from e2r.research_brain.runtime.live_materialization.current_claim_compiler import _merge_claim_provenance


def provenance(mapping_id: str) -> DailyClaimProvenance:
    text = "exact quote"
    return DailyClaimProvenance(
        provenance_id="P-"+mapping_id, claim_id="CLM-1", target_id="005930",
        document_id="DOC-1", source_url="https://example.org/issuer/document",
        published_date="2026-07-01", available_date="2026-07-01",
        content_sha256=hashlib.sha256(text.encode()).hexdigest(), document_text=text, exact_quote=text,
        source_ids=("SRC-1",), anchor_ids=("ANCH-1",), mapping_ids=(mapping_id,),
        extraction_provider_kind="CODEX", mapping_provider_kind="CODEX",
        decision_use="SCORE", directness="DIRECT", temporal_status="CURRENT",
        mapping_status="ACCEPTED", fetched=True, anchor_verified=True,
        source_proxy_only=False, test_only=False,
    )


class ClaimMappingLineagePreservedTests(unittest.TestCase):
    def test_same_claim_provenance_unions_every_mapping_id(self) -> None:
        merged = _merge_claim_provenance((provenance("MAP-1"),provenance("MAP-2")))
        self.assertEqual(len(merged),1)
        self.assertEqual(merged[0].mapping_ids,("MAP-1","MAP-2"))


if __name__ == "__main__": unittest.main()
