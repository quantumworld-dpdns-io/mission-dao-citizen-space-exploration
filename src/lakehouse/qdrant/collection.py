"""Qdrant vector collection schemas for mission document RAG."""

from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    VectorParams,
    Distance,
    CollectionStatus,
    PayloadSchemaType,
)

MISSION_DOCS_COLLECTION = "mission_documents"
MISSION_DOCS_VECTOR_SIZE = 384  # sentence-transformers all-MiniLM-L6-v2
MISSION_DOCS_DISTANCE = Distance.COSINE

TELEMETRY_LOG_COLLECTION = "telemetry_logs"
TELEMETRY_LOG_VECTOR_SIZE = 384
TELEMETRY_LOG_DISTANCE = Distance.COSINE


def get_client() -> QdrantClient:
    return QdrantClient(
        host="localhost",
        port=6333,
    )


def ensure_collections(client: QdrantClient) -> None:
    collections = [
        {
            "name": MISSION_DOCS_COLLECTION,
            "vectors_config": VectorParams(
                size=MISSION_DOCS_VECTOR_SIZE,
                distance=MISSION_DOCS_DISTANCE,
            ),
            "payload_schema": {
                "doc_type": PayloadSchemaType.KEYWORD,
                "mission_id": PayloadSchemaType.KEYWORD,
                "title": PayloadSchemaType.TEXT,
                "source": PayloadSchemaType.KEYWORD,
            },
        },
        {
            "name": TELEMETRY_LOG_COLLECTION,
            "vectors_config": VectorParams(
                size=TELEMETRY_LOG_VECTOR_SIZE,
                distance=TELEMETRY_LOG_DISTANCE,
            ),
            "payload_schema": {
                "satellite_id": PayloadSchemaType.KEYWORD,
                "timestamp": PayloadSchemaType.DATETIME,
                "parameter": PayloadSchemaType.KEYWORD,
                "severity": PayloadSchemaType.KEYWORD,
            },
        },
    ]

    for col in collections:
        try:
            client.create_collection(**col)
        except Exception:
            pass  # collection already exists
