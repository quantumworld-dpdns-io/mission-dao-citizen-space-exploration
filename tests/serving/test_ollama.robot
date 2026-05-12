*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Ollama Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/serving/ollama

Client Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/ollama/client.py

Models Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/ollama/models.py

Prompts Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/serving/ollama/prompts.py

Has Anomaly Detection Prompt
    ${content}    Get File    ${PROJECT_ROOT}/src/serving/ollama/prompts.py
    Should Contain    ${content}    ANOMALY_DETECTION_PROMPT

Has Model Configurations
    ${content}    Get File    ${PROJECT_ROOT}/src/serving/ollama/models.py
    Should Contain    ${content}    OLLAMA_MODELS
