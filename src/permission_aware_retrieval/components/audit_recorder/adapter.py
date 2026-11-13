"""Port and registry adapter for Audit Recorder.

Interface from the architecture specification: ``append(record) -> None``
"""

from __future__ import annotations

from typing import Protocol

from permission_aware_retrieval.components.audit_recorder.config import CONFIG
from permission_aware_retrieval.components.audit_recorder.service import AuditRecorderService
from permission_aware_retrieval.domain.models import PipelineContext

ROLE = CONFIG.role


class AuditRecorderPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> AuditRecorderService:
    return AuditRecorderService(services)
