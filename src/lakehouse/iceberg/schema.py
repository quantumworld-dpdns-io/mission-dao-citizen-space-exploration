"""Apache Iceberg table schemas for mission telemetry data."""

from pyiceberg.schema import Schema
from pyiceberg.types import (
    NestedField,
    StringType,
    LongType,
    DoubleType,
    TimestampType,
    StructType,
)

TELEMETRY_SCHEMA = Schema(
    NestedField(1, "satellite_id", StringType(), required=False),
    NestedField(2, "timestamp", TimestampType(), required=True),
    NestedField(3, "temperature_c", DoubleType(), required=False),
    NestedField(4, "voltage_v", DoubleType(), required=False),
    NestedField(5, "current_a", DoubleType(), required=False),
    NestedField(6, "altitude_km", DoubleType(), required=False),
    NestedField(7, "latitude", DoubleType(), required=False),
    NestedField(8, "longitude", DoubleType(), required=False),
    NestedField(9, "signal_strength_db", DoubleType(), required=False),
    NestedField(10, "payload_status", StringType(), required=False),
    NestedField(11, "mission_id", StringType(), required=True),
    NestedField(12, "data_hash", StringType(), required=False),
)

MISSION_SCHEMA = Schema(
    NestedField(1, "mission_id", StringType(), required=True),
    NestedField(2, "name", StringType(), required=True),
    NestedField(3, "description", StringType(), required=False),
    NestedField(4, "orbit_type", StringType(), required=False),
    NestedField(5, "altitude_km", DoubleType(), required=False),
    NestedField(6, "inclination_deg", DoubleType(), required=False),
    NestedField(7, "launch_date", TimestampType(), required=False),
    NestedField(8, "status", StringType(), required=False),
    NestedField(9, "funding_goal", DoubleType(), required=False),
    NestedField(10, "funding_raised", DoubleType(), required=False),
)

SCHEMAS = {
    "telemetry": TELEMETRY_SCHEMA,
    "missions": MISSION_SCHEMA,
}
