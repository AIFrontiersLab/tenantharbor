"""Relevance Scorer.

Scores query-candidate relevance with a deterministic BM25-style reference model.
"""

from permission_aware_retrieval.components.relevance_scorer.adapter import ROLE, build
from permission_aware_retrieval.components.relevance_scorer.config import CONFIG, RelevanceScorerConfig
from permission_aware_retrieval.components.relevance_scorer.errors import RelevanceScorerError
from permission_aware_retrieval.components.relevance_scorer.service import RelevanceScorerService

__all__ = ["CONFIG", "ROLE", "build", "RelevanceScorerConfig", "RelevanceScorerError", "RelevanceScorerService"]
