"""Trino catalog configuration for federated cross-mission queries."""

import os
from trino.dbapi import Connection
from trino.auth import BasicAuthentication


def get_trino_connection() -> Connection:
    return Connection(
        host=os.getenv("TRINO_HOST", "localhost"),
        port=int(os.getenv("TRINO_PORT", "8080")),
        user=os.getenv("TRINO_USER", "admin"),
        catalog=os.getenv("TRINO_CATALOG", "mission_lakehouse"),
        schema=os.getenv("TRINO_SCHEMA", "mission_dao"),
        auth=BasicAuthentication(
            os.getenv("TRINO_USER", "admin"),
            os.getenv("TRINO_PASSWORD", ""),
        ) if os.getenv("TRINO_PASSWORD") else None,
    )
