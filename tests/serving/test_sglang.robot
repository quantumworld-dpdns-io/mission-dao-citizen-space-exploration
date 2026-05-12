*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
SGLang Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/serving/sglang

Client Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/sglang/client.py

Server Config Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/sglang/server.py

Structured Gen Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/sglang/structured_gen.py

Has Telemetry Anomaly Schema
    ${content}    Get File    ${PROJECT_ROOT}/src/serving/sglang/structured_gen.py
    Should Contain    ${content}    TelemetryAnomalySchema

Has Generate Structured Function
    ${content}    Get File    ${PROJECT_ROOT}/src/serving/sglang/structured_gen.py
    Should Contain    ${content}    def generate_structured
