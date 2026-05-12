"""LanceDB multimodal table schemas for telemetry data."""

import lancedb
import pyarrow as pa

TELEMETRY_TABLE_NAME = "telemetry_stream"
EMBEDDINGS_TABLE_NAME = "telemetry_embeddings"


def get_db(uri: str = "data/mission_lancedb") -> lancedb.DBConnection:
    return lancedb.connect(uri)


def ensure_tables(db: lancedb.DBConnection) -> None:
    tables = {
        TELEMETRY_TABLE_NAME: pa.schema([
            pa.field("satellite_id", pa.string()),
            pa.field("timestamp", pa.timestamp("us")),
            pa.field("temperature_c", pa.float64()),
            pa.field("voltage_v", pa.float64()),
            pa.field("current_a", pa.float64()),
            pa.field("altitude_km", pa.float64()),
            pa.field("latitude", pa.float64()),
            pa.field("longitude", pa.float64()),
            pa.field("signal_strength_db", pa.float64()),
            pa.field("payload_status", pa.string()),
            pa.field("mission_id", pa.string()),
        ]),
        EMBEDDINGS_TABLE_NAME: pa.schema([
            pa.field("point_id", pa.string()),
            pa.field("satellite_id", pa.string()),
            pa.field("timestamp", pa.timestamp("us")),
            pa.field("embedding", pa.list_(pa.float32(), 384)),
            pa.field("text_summary", pa.string()),
            pa.field("mission_id", pa.string()),
        ]),
    }

    for name, schema in tables.items():
        try:
            db.create_table(name, schema=schema, exist_ok=True)
        except Exception:
            pass
