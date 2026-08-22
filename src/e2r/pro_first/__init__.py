"""Pro-first browser research platform.

ChatGPT Pro may propose research material, but deterministic E2R layers retain
all EvidenceFact, score, and canonical Stage authority.
"""

from .approval import ExactlyOnceSubmitCoordinator, ProApprovalService
from .capture import CaptureFilesystemReconciler, ProCaptureCoordinator
from .dossier import ProDossierImporter
from .gaps import ProGapAdjudicationService
from .job_store import ProFirstJobStore
from .models import (
    CandidateRecord,
    JobEvent,
    JobStatus,
    ProResearchJob,
    ResearchMode,
    ScanRunRecord,
    ScanWindow,
)
from .packet import PacketBuildInput, ResearchPacketBuilder, ResearchPacketV1
from .publication import ProPublishedResult, ProResultPublisher
from .prompt_contract import ProResearchPromptContract
from .scheduler import FrozenClock, PersistentKrxScheduler, SystemClock
from .scoring import ProScoringPipelineService
from .state_machine import ProJobStateMachine
from .verification import ProSourceVerificationService

__all__ = [
    "CandidateRecord",
    "CaptureFilesystemReconciler",
    "JobEvent",
    "JobStatus",
    "ProFirstJobStore",
    "ProGapAdjudicationService",
    "ProJobStateMachine",
    "ProResearchJob",
    "ProPublishedResult",
    "ProResultPublisher",
    "ProScoringPipelineService",
    "ProSourceVerificationService",
    "ResearchMode",
    "ScanRunRecord",
    "ScanWindow",
    "FrozenClock",
    "ExactlyOnceSubmitCoordinator",
    "PersistentKrxScheduler",
    "PacketBuildInput",
    "ProResearchPromptContract",
    "ProApprovalService",
    "ProCaptureCoordinator",
    "ProDossierImporter",
    "ResearchPacketBuilder",
    "ResearchPacketV1",
    "SystemClock",
]
