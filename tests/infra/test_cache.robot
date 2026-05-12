*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Dragonfly Client Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/src/infra/dragonfly/client.py
Has DragonflyCache Class
    ${content}    Get File    ${PROJECT_ROOT}/src/infra/dragonfly/client.py
    Should Contain    ${content}    class DragonflyCache
