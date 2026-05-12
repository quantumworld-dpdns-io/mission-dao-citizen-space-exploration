"""Teaclave TEE function definitions for confidential mission data processing."""

import base64
from typing import Dict, Any


def telemetry_decrypt(payload: bytes, key: bytes) -> bytes:
    """Decrypt telemetry payload inside TEE enclave."""
    from cryptography.fernet import Fernet
    f = Fernet(base64.urlsafe_b64encode(key))
    return f.decrypt(payload)


def payload_verify(data: Dict[str, Any], expected_hash: str) -> bool:
    """Verify data integrity inside TEE enclave."""
    import hashlib
    import json
    serialized = json.dumps(data, sort_keys=True).encode()
    computed = hashlib.sha256(serialized).hexdigest()
    return computed == expected_hash


def mission_data_aggregate(records: list) -> Dict[str, float]:
    """Aggregate mission telemetry data inside TEE for privacy."""
    if not records:
        return {"avg_temp": 0.0, "avg_voltage": 0.0, "count": 0}

    total_temp = sum(r.get("temperature_c", 0) for r in records)
    total_voltage = sum(r.get("voltage_v", 0) for r in records)

    return {
        "avg_temp": round(total_temp / len(records), 2),
        "avg_voltage": round(total_voltage / len(records), 2),
        "count": len(records),
    }
