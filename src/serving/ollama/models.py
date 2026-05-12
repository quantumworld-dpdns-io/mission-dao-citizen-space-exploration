"""Model configuration for mission-specific tasks."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelConfig:
    name: str
    description: str
    context_length: int = 4096
    temperature: float = 0.7
    top_p: float = 0.9


OLLAMA_MODELS = {
    "telemetry-anomaly": ModelConfig(
        name="llama3.2:3b",
        description="Anomaly detection in satellite telemetry streams",
        temperature=0.1,
    ),
    "resource-optimizer": ModelConfig(
        name="llama3.2:3b",
        description="Satellite resource optimization suggestions",
        temperature=0.3,
    ),
    "mission-planner": ModelConfig(
        name="llama3.1:8b",
        description="Mission planning and procedure generation",
        temperature=0.5,
        context_length=8192,
    ),
    "community-summarizer": ModelConfig(
        name="llama3.2:3b",
        description="Summarize community discussions and votes",
        temperature=0.3,
    ),
    "report-generator": ModelConfig(
        name="llama3.1:8b",
        description="Generate mission status reports from telemetry data",
        temperature=0.2,
        context_length=8192,
    ),
}


def get_config(task: str) -> Optional[ModelConfig]:
    return OLLAMA_MODELS.get(task)
