"""DuckDB local analytics setup with Iceberg integration."""

import os
import duckdb


def get_duckdb_connection() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(os.getenv("DUCKDB_PATH", "mission_lakehouse.db"))
    conn.install_extension("iceberg")
    conn.load_extension("iceberg")
    conn.install_extension("httpfs")
    conn.load_extension("httpfs")
    return conn


def register_iceberg_catalog(conn: duckdb.DuckDBPyConnection, namespace: str = "mission_dao") -> None:
    conn.execute(f"""
        CREATE OR REPLACE VIEW telemetry AS
        SELECT * FROM iceberg_scan('{namespace}.telemetry');
    """)
    conn.execute(f"""
        CREATE OR REPLACE VIEW missions AS
        SELECT * FROM iceberg_scan('{namespace}.missions');
    """)
