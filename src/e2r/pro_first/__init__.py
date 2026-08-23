"""Pro-first browser research platform.

ChatGPT Pro may propose research material, but deterministic E2R layers retain
all EvidenceFact, score, and canonical Stage authority.

Public symbols are loaded lazily so the Windows browser helper can import the
Playwright adapter without importing unrelated POSIX-only research providers.
Accessing a public symbol still resolves to the same module and object.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any


_PUBLIC_SYMBOLS = {
    "CandidateRecord": (".models", "CandidateRecord"),
    "CaptureFilesystemReconciler": (".capture", "CaptureFilesystemReconciler"),
    "DeltaScoringReuseContext": (".reuse", "DeltaScoringReuseContext"),
    "ExactlyOnceSubmitCoordinator": (".approval", "ExactlyOnceSubmitCoordinator"),
    "FrozenClock": (".scheduler", "FrozenClock"),
    "JobEvent": (".models", "JobEvent"),
    "JobStatus": (".models", "JobStatus"),
    "PacketBuildInput": (".packet", "PacketBuildInput"),
    "PersistentKrxScheduler": (".scheduler", "PersistentKrxScheduler"),
    "ProApprovalService": (".approval", "ProApprovalService"),
    "ProCaptureCoordinator": (".capture", "ProCaptureCoordinator"),
    "ProDossierImporter": (".dossier", "ProDossierImporter"),
    "ProFirstJobStore": (".job_store", "ProFirstJobStore"),
    "ProGapAdjudicationService": (".gaps", "ProGapAdjudicationService"),
    "ProJobStateMachine": (".state_machine", "ProJobStateMachine"),
    "ProMultiPassLedger": (".multi_pass", "ProMultiPassLedger"),
    "ProMultiPassResearchOrchestrator": (
        ".multi_pass",
        "ProMultiPassResearchOrchestrator",
    ),
    "ProPublishedResult": (".publication", "ProPublishedResult"),
    "ProResearchJob": (".models", "ProResearchJob"),
    "ProResearchPromptContract": (".prompt_contract", "ProResearchPromptContract"),
    "ProResultPublisher": (".publication", "ProResultPublisher"),
    "ProSameInputReuseGate": (".reuse", "ProSameInputReuseGate"),
    "ProScoringPipelineService": (".scoring", "ProScoringPipelineService"),
    "ProSourceVerificationService": (".verification", "ProSourceVerificationService"),
    "ResearchMode": (".models", "ResearchMode"),
    "ResearchPacketBuilder": (".packet", "ResearchPacketBuilder"),
    "ResearchPacketV1": (".packet", "ResearchPacketV1"),
    "SameInputNoopResult": (".reuse", "SameInputNoopResult"),
    "ScanRunRecord": (".models", "ScanRunRecord"),
    "ScanWindow": (".models", "ScanWindow"),
    "SystemClock": (".scheduler", "SystemClock"),
}

__all__ = sorted(_PUBLIC_SYMBOLS)


def __getattr__(name: str) -> Any:
    try:
        module_name, attribute_name = _PUBLIC_SYMBOLS[name]
    except KeyError as error:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from error
    value = getattr(import_module(module_name, __name__), attribute_name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted((*globals(), *__all__))
