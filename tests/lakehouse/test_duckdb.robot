*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
DuckDB Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/lakehouse/duckdb

Setup Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/duckdb/setup.py

Queries Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/duckdb/queries.py

Has Temperature Trend Query
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/duckdb/queries.py
    Should Contain    ${content}    temperature_trend

Has Power Analysis Query
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/duckdb/queries.py
    Should Contain    ${content}    power_analysis
