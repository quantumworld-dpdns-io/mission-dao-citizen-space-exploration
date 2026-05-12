"""Example Iceberg SQL queries for mission telemetry analytics."""

QUERIES = {
    "latest_telemetry_per_satellite": """
        SELECT satellite_id, MAX(timestamp) as last_report
        FROM mission_dao.telemetry
        GROUP BY satellite_id
    """,
    "temperature_range_by_mission": """
        SELECT mission_id,
               MIN(temperature_c) as min_temp,
               MAX(temperature_c) as max_temp,
               AVG(temperature_c) as avg_temp
        FROM mission_dao.telemetry
        WHERE temperature_c IS NOT NULL
        GROUP BY mission_id
    """,
    "mission_summary": """
        SELECT m.name,
               m.status,
               COUNT(t.*) as telemetry_points,
               MAX(t.timestamp) as latest_data
        FROM mission_dao.missions m
        LEFT JOIN mission_dao.telemetry t ON m.mission_id = t.mission_id
        GROUP BY m.name, m.status
    """,
    "active_missions": """
        SELECT * FROM mission_dao.missions
        WHERE status = 'active'
        ORDER BY launch_date DESC
    """,
    "funding_progress": """
        SELECT name,
               funding_raised,
               funding_goal,
               ROUND(funding_raised / NULLIF(funding_goal, 0) * 100, 1) as pct_funded
        FROM mission_dao.missions
        WHERE funding_goal > 0
        ORDER BY pct_funded DESC
    """,
}
