*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Qdrant Package Exists
    Directory Should Exist    ${PROJECT_ROOT}/src/lakehouse/qdrant

Collection Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/qdrant/collection.py

Ingestion Module Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/lakehouse/qdrant/ingestion.py

Has Mission Docs Collection Config
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/qdrant/collection.py
    Should Contain    ${content}    MISSION_DOCS_COLLECTION

Has Search Function
    ${content}    Get File    ${PROJECT_ROOT}/src/lakehouse/qdrant/ingestion.py
    Should Contain    ${content}    def search_documents
