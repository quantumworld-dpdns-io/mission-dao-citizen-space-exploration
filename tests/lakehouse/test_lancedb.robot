*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
LanceDB Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/lakehouse/lancedb

Schema Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/lancedb/schema.py

Ingestion Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/lancedb/ingestion.py

Has Telemetry Table Schema
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/lancedb/schema.py
    Should Contain    ${content}    TELEMETRY_TABLE_NAME

Has Search Similar Function
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/lancedb/ingestion.py
    Should Contain    ${content}    def search_similar
