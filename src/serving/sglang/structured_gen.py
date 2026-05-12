"""Structured JSON generation schemas for mission data."""

from typing import Dict, Any


TelemetryAnomalySchema: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "anomalies_found": {"type": "boolean"},
        "anomaly_details": {"type": "array", "items": {"type": "string"}},
        "severity": {"type": "string", "enum": ["low", "medium", "high"]},
        "affected_parameters": {"type": "array", "items": {"type": "string"}},
        "recommendations": {"type": "array", "items": {"type": "string"}},
        "confidence_score": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": ["anomalies_found", "severity", "recommendations"],
}

ResourceOptimizationSchema: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "power_savings_watts": {"type": "number"},
        "data_efficiency_suggestions": {"type": "array", "items": {"type": "string"}},
        "orbit_adjustments": {"type": "array", "items": {"type": "string"}},
        "estimated_impact": {"type": "string"},
        "priority": {"type": "string", "enum": ["low", "medium", "high"]},
    },
    "required": ["power_savings_watts", "estimated_impact"],
}

MissionPlanSchema: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "procedure_steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "step": {"type": "integer"},
                    "action": {"type": "string"},
                    "duration_minutes": {"type": "number"},
                    "critical": {"type": "boolean"},
                },
                "required": ["step", "action"],
            },
        },
        "risk_level": {"type": "string", "enum": ["low", "medium", "high"]},
        "contingency_plans": {"type": "array", "items": {"type": "string"}},
        "resource_requirements": {"type": "object"},
        "expected_outcome": {"type": "string"},
    },
    "required": ["procedure_steps", "risk_level", "expected_outcome"],
}


def generate_structured(client: Any, model: str, prompt: str, schema: Dict) -> Dict:
    """Generate structured JSON output using SGLang's constrained decoding."""
    return client.generate_structured(model, prompt, schema)
