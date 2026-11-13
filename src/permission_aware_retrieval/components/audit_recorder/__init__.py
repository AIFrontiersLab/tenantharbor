"""Audit Recorder.

Writes a hash-chainable audit record for every run, including denials and degradations.
"""

from permission_aware_retrieval.components.audit_recorder.adapter import ROLE, build
from permission_aware_retrieval.components.audit_recorder.config import CONFIG, AuditRecorderConfig
from permission_aware_retrieval.components.audit_recorder.errors import AuditRecorderError
from permission_aware_retrieval.components.audit_recorder.service import AuditRecorderService

__all__ = ["CONFIG", "ROLE", "build", "AuditRecorderConfig", "AuditRecorderError", "AuditRecorderService"]
