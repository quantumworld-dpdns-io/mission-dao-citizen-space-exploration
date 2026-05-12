"""DuckDB local analytics query templates."""

QUERIES = {
    "temperature_trend": """
        SELECT date_trunc('hour', timestamp) as hour,
               satellite_id,
               AVG(temperature_c) as avg_temp
        FROM telemetry
        WHERE temperature_c IS NOT NULL
        GROUP BY hour, satellite_id
        ORDER BY hour DESC
        LIMIT 100
    """,
    "power_analysis": """
        SELECT satellite_id,
               AVG(voltage_v) as avg_voltage,
               AVG(current_a) as avg_current,
               AVG(voltage_v * current_a) as avg_power_w
        FROM telemetry
        WHERE voltage_v IS NOT NULL AND current_a IS NOT NULL
        GROUP BY satellite_id
    """,
    "orbital_coverage": """
        SELECT satellite_id,
               COUNT(DISTINCT ROUND(latitude, 1)) as lat_bins,
               MIN(latitude) as min_lat,
               MAX(latitude) as max_lat,
               MIN(longitude) as min_lon,
               MAX(longitude) as max_lon
        FROM telemetry
        WHERE latitude IS NOT NULL
        GROUP BY satellite_id
    """,
    "signal_quality_ranking": """
        SELECT satellite_id,
               COUNT(*) as reports,
               AVG(signal_strength_db) as avg_signal,
               STDDEV(signal_strength_db) as signal_variance
        FROM telemetry
        WHERE signal_strength_db IS NOT NULL
        GROUP BY satellite_id
        ORDER BY avg_signal DESC
    """,
}
