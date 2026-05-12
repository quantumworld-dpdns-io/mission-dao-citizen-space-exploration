*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
OpenTelemetry Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/serving/openllmetry

Tracing Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/openllmetry/tracing.py

Phoenix Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/openllmetry/phoenix.py

Metrics Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/openllmetry/metrics.py

Has Setup Tracing Function
    ${content}    Get File    ${PROJECT_ROOT}/src/serving/openllmetry/tracing.py
    Should Contain    ${content}    def setup_tracing

Has Telemetry Metrics Class
    ${content}    Get File    ${PROJECT_ROOT}/src/serving/openllmetry/metrics.py
    Should Contain    ${content}    class TelemetryMetrics
