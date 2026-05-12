"""LanceDB telemetry ingestion pipeline."""

import json
from datetime import datetime
from typing import List, Dict
import pyarrow as pa
from sentence_transformers import SentenceTransformer

from .schema import get_db, TELEMETRY_TABLE_NAME, EMBEDDINGS_TABLE_NAME

_encoder = None


def get_encoder() -> SentenceTransformer:
    global _encoder
    if _encoder is None:
        _encoder = SentenceTransformer("all-MiniLM-L6-v2")
    return _encoder


def ingest_telemetry_batch(db, records: List[Dict]) -> int:
    """Ingest a batch of telemetry records into LanceDB."""
    table = db.open_table(TELEMETRY_TABLE_NAME)
    batch_data = []

    for r in records:
        batch_data.append({
            "satellite_id": r.get("satellite_id"),
            "timestamp": datetime.fromisoformat(r.get("timestamp", datetime.utcnow().isoformat())),
            "temperature_c": r.get("temperature_c"),
            "voltage_v": r.get("voltage_v"),
            "current_a": r.get("current_a"),
            "altitude_km": r.get("altitude_km"),
            "latitude": r.get("latitude"),
            "longitude": r.get("longitude"),
            "signal_strength_db": r.get("signal_strength_db"),
            "payload_status": r.get("payload_status"),
            "mission_id": r.get("mission_id"),
        })

    table.add(batch_data)
    return len(batch_data)


def ingest_embedding(db, point_id: str, satellite_id: str, mission_id: str, text: str) -> None:
    """Ingest a text embedding into LanceDB for multimodal search."""
    encoder = get_encoder()
    table = db.open_table(EMBEDDINGS_TABLE_NAME)
    vector = encoder.encode(text).tolist()

    table.add([{
        "point_id": point_id,
        "satellite_id": satellite_id,
        "timestamp": datetime.utcnow(),
        "embedding": vector,
        "text_summary": text,
        "mission_id": mission_id,
    }])


def search_similar(db, query_text: str, limit: int = 5) -> List[Dict]:
    """Search similar telemetry contexts by embedding similarity."""
    encoder = get_encoder()
    table = db.open_table(EMBEDDINGS_TABLE_NAME)
    query_vector = encoder.encode(query_text).tolist()

    results = table.search(query_vector).limit(limit).to_list()
    return results
