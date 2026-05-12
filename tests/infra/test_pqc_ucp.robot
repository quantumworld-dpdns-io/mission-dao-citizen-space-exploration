*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
UCP Client Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/infra/ucp/client.py
Has UCPClient Class
    ${content}    Get File    ${PROJECT_ROOT}/src/infra/ucp/client.py
    Should Contain    ${content}    class UCPClient
PQC Hybrid Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/infra/pqc/hybrid.py
Has Hybrid Key Exchange
    ${content}    Get File    ${PROJECT_ROOT}/src/infra/pqc/hybrid.py
    Should Contain    ${content}    def generate_hybrid_keypair
PQC Setup Script Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/infra/pqc/setup.sh
