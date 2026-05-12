"""Apache Polaris Iceberg REST catalog client."""

import os
from pyiceberg.catalog import load_catalog


def get_polaris_catalog() -> object:
    """Create a Polaris-compatible Iceberg REST catalog."""
    return load_catalog(
        "polaris",
        **{
            "uri": os.getenv("POLARIS_URI", "http://localhost:8181"),
            "warehouse": os.getenv("POLARIS_WAREHOUSE", "mission-lakehouse"),
            "rest.sigv4-enabled": "false",
            "client.region": "us-east-1",
        },
    )


def init_namespace(catalog: object, namespace: str = "mission_dao") -> None:
    """Ensure a namespace exists in the catalog."""
    try:
        catalog.create_namespace(namespace)
    except Exception:
        pass  # namespace already exists


def register_table(catalog: object, namespace: str, table_name: str, schema) -> None:
    """Create or load an Iceberg table."""
    full_name = f"{namespace}.{table_name}"
    try:
        catalog.create_table(full_name, schema)
    except Exception:
        pass  # table already exists
