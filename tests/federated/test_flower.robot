*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Federated Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/federated

Client Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/federated/client.py

Server Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/federated/server.py

Strategy Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/federated/strategy.py

Models Directory Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/federated/models

Has Flower Client Class
    ${content}    Get File    ${PROJECT_ROOT}/src/federated/client.py
    Should Contain    ${content}    class TelemetryFlowerClient

Has Anomaly Detector Model
    ${content}    Get File    ${PROJECT_ROOT}/src/federated/models/anomaly_detector.py
    Should Contain    ${content}    class AnomalyDetector
