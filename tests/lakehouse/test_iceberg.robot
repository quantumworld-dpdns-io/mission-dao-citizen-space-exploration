*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Iceberg Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/lakehouse/iceberg

Schema Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/iceberg/schema.py

Catalog Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/iceberg/catalog.py

Queries Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/iceberg/queries.py

Defines Telemetry Schema
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/iceberg/schema.py
    Should Contain    ${content}    TELEMETRY_SCHEMA

Defines Mission Schema
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/iceberg/schema.py
    Should Contain    ${content}    MISSION_SCHEMA
