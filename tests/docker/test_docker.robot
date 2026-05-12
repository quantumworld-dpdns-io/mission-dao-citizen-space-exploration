*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Docker Compose Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/docker/docker-compose.yml
Dev Compose Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/docker/docker-compose.dev.yml
Prod Compose Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/docker/docker-compose.prod.yml
Web Dockerfile Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/docker/web.Dockerfile
API Dockerfile Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/docker/api.Dockerfile
Dockerignore Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/docker/.dockerignore
Trino Config Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/docker/config/trino/catalog/iceberg.properties
