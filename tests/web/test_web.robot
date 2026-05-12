*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/keywords.resource

*** Test Cases ***
Package JSON Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/package.json
Next Config Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/next.config.ts
TS Config Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/tsconfig.json
Tailwind Config Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/tailwind.config.ts
Layout Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/src/app/layout.tsx
Home Page Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/src/app/page.tsx
Missions Page Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/src/app/missions/page.tsx
Proposals Page Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/src/app/proposals/page.tsx
DAO Page Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/src/app/dao/page.tsx
Header Component Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/src/components/Header.tsx
API Client Exists
    File Should Exist And Not Be Empty    ${PROJECT_ROOT}/web/src/lib/api.ts
