*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Trino Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/lakehouse/trino

Catalog Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/trino/catalog.py

Queries Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/trino/queries.py

Catalog Config Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/trino/catalog.yaml

Has Federated Queries
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/trino/queries.py
    Should Contain    ${content}    cross_mission_telemetry_union
