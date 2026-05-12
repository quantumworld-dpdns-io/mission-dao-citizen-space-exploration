"""Arize Phoenix exporter configuration for LLM evaluation and tracing."""

import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class PhoenixExporter:
    endpoint: str = "http://localhost:6006"
    project: str = "mission-dao"
    trace_headers: Optional[dict] = None

    def get_otlp_endpoint(self) -> str:
        return f"{self.endpoint}/v1/traces"


def setup_phoenix(endpoint: str = "http://localhost:6006") -> PhoenixExporter:
    """Configure Arize Phoenix for LLM observability."""
    exporter = PhoenixExporter(endpoint=endpoint)
    logger.info(f"Phoenix exporter configured at {exporter.get_otlp_endpoint()}")
    return exporter
