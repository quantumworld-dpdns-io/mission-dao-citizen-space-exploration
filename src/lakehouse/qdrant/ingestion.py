"""Qdrant document ingestion pipeline for mission RAG."""

from typing import List, Dict
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from sentence_transformers import SentenceTransformer

from .collection import (
    get_client,
    MISSION_DOCS_COLLECTION,
    TELEMETRY_LOG_COLLECTION,
)

_encoder = None


def get_encoder() -> SentenceTransformer:
    global _encoder
    if _encoder is None:
        _encoder = SentenceTransformer("all-MiniLM-L6-v2")
    return _encoder


def ingest_document(client: QdrantClient, doc: Dict, point_id: int) -> None:
    """Ingest a single mission document into Qdrant."""
    encoder = get_encoder()
    text = f"{doc['title']} {doc['content']}"
    vector = encoder.encode(text).tolist()

    client.upsert(
        collection_name=MISSION_DOCS_COLLECTION,
        points=[
            PointStruct(
                id=point_id,
                vector=vector,
                payload={
                    "doc_type": doc.get("doc_type", "general"),
                    "mission_id": doc.get("mission_id", ""),
                    "title": doc.get("title", ""),
                    "source": doc.get("source", ""),
                },
            )
        ],
    )


def search_documents(client: QdrantClient, query: str, mission_id: str = None, limit: int = 5) -> List[Dict]:
    """Semantic search across mission documents."""
    encoder = get_encoder()
    query_vector = encoder.encode(query).tolist()

    filter_conditions = {}
    if mission_id:
        filter_conditions["must"] = [{"key": "mission_id", "match": {"value": mission_id}}]

    results = client.search(
        collection_name=MISSION_DOCS_COLLECTION,
        query_vector=query_vector,
        limit=limit,
        query_filter=filter_conditions if filter_conditions else None,
    )

    return [
        {
            "id": r.id,
            "score": r.score,
            "title": r.payload.get("title"),
            "doc_type": r.payload.get("doc_type"),
            "mission_id": r.payload.get("mission_id"),
        }
        for r in results
    ]
