"""Canonical research-calibrated scoring contracts."""

from .loader import load_archetype_scoring_contract, load_scoring_contract_catalog
from .schemas import ArchetypeScoringContract, ScoringContractCatalog
from .scoring_policy_v2 import (
    ScoringContractIncompleteError,
    audit_scoring_schema_totality,
    load_scoring_policy_v2,
    require_scoring_key,
)
from .validator import audit_scoring_contract_catalog, validate_scoring_contract

__all__ = [
    "ArchetypeScoringContract",
    "ScoringContractCatalog",
    "ScoringContractIncompleteError",
    "audit_scoring_schema_totality",
    "audit_scoring_contract_catalog",
    "load_archetype_scoring_contract",
    "load_scoring_contract_catalog",
    "load_scoring_policy_v2",
    "require_scoring_key",
    "validate_scoring_contract",
]
