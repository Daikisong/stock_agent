from __future__ import annotations

from pathlib import Path
import unittest
from unittest.mock import patch

from e2r.agentic.evidence_contract import (
    DEFAULT_EVIDENCE_CONTRACT_PATH,
    _load_contracts_cached,
    load_evidence_contracts,
)
from e2r.agentic.evidence_contract_v2 import (
    DEFAULT_EVIDENCE_CONTRACT_V2_PATH,
    load_evidence_contracts_v2,
)


class EvidenceContractUtf8Test(unittest.TestCase):
    def test_v2_loader_explicitly_reads_utf8_on_every_platform(self) -> None:
        payload = DEFAULT_EVIDENCE_CONTRACT_V2_PATH.read_text(encoding="utf-8")
        with patch.object(Path, "read_text", return_value=payload) as read_text:
            contracts = load_evidence_contracts_v2(
                path="portable-v2-contract.json",
                require_all_archetypes=True,
            )

        self.assertTrue(contracts)
        read_text.assert_called_once_with(encoding="utf-8")

    def test_v1_loader_explicitly_reads_utf8_on_every_platform(self) -> None:
        payload = DEFAULT_EVIDENCE_CONTRACT_PATH.read_text(encoding="utf-8")
        _load_contracts_cached.cache_clear()
        self.addCleanup(_load_contracts_cached.cache_clear)
        with patch.object(Path, "read_text", return_value=payload) as read_text:
            contracts = load_evidence_contracts(path="portable-v1-contract.json")

        self.assertTrue(contracts)
        read_text.assert_called_once_with(encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
