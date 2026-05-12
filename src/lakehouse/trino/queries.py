"""Trino federated SQL query templates for cross-mission analytics."""

QUERIES = {
    "cross_mission_telemetry_union": """
        SELECT satellite_id, timestamp, temperature_c, voltage_c, mission_id
        FROM iceberg.mission_dao.telemetry
        WHERE timestamp > CURRENT_TIMESTAMP - INTERVAL '7' DAY
        ORDER BY timestamp DESC
    """,
    "mission_performance_comparison": """
        SELECT m.name as mission_name,
               COUNT(t.*) as total_readings,
               AVG(t.temperature_c) as avg_temp,
               AVG(t.voltage_v) as avg_voltage
        FROM iceberg.mission_dao.missions m
        JOIN iceberg.mission_dao.telemetry t ON m.mission_id = t.mission_id
        GROUP BY m.name
        ORDER BY total_readings DESC
    """,
    "active_missions_by_funding": """
        SELECT name, funding_raised, funding_goal, status
        FROM iceberg.mission_dao.missions
        WHERE status IN ('active', 'funding')
        ORDER BY funding_raised DESC
    """,
    "telemetry_anomaly_candidates": """
        SELECT satellite_id, timestamp, temperature_c
        FROM iceberg.mission_dao.telemetry
        WHERE temperature_c > (
            SELECT AVG(temperature_c) + 3 * STDDEV(temperature_c)
            FROM iceberg.mission_dao.telemetry
        )
        ORDER BY timestamp DESC
    """,
}
