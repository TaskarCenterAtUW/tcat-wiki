---
uid: 9c2001fd-2f7e-4b17-b9c9-42b17a7adc86
title: What APIs does Workspaces provide?
slug: workspaces-api
doc_type: concept
questions:
    - What APIs does Workspaces provide?
    - Which endpoints manage Workspaces, teams, settings, and Tasking projects?
    - Does the Workspaces API document an export or publish endpoint?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
topics:
    - workspaces
    - documentation
    - tasking-manager
    - roles
    - teams
    - changesets
    - osm-interoperability
    - configuration
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-technical-definition.md
    - assistant/workspaces/concept/tasking-projects-and-tasks.md
    - assistant/workspaces/concept/workspace-creation-methods.md
    - assistant/workspaces/concept/workspace-metadata.md
    - assistant/workspaces/concept/roles.md
    - assistant/workspaces/concept/teams.md
    - assistant/workspaces/concept/changesets.md
    - assistant/workspaces/concept/osm-api-emulation.md
    - assistant/workspaces/concept/edit-auditing.md
    - assistant/workspaces/concept/imagery-layer-overview.md
    - assistant/workspaces/concept/quest-definition-url-requirements.md
tags:
    - Assistant
---

<!-- @format -->

# What APIs does Workspaces provide?

## Short Answer

The Workspaces Swagger UI publishes an OpenAPI 3.1.0 specification for API version `0.1.0`. It documents versioned APIs for workspace records and settings, teams and roles, Tasking projects and tasks, audit events, jobs, and changesets, as well as OSM capability routes. This article summarizes the published contract; deployment availability and runtime behavior can vary.

## Significance

An endpoint catalog helps integrators and support staff identify the documented route and method before troubleshooting request bodies, permissions, or returned data. Workspaces routes, Tasking project routes, and OSM-compatible routes are separate API surfaces.

## What This Means

### API reference and authentication

- [Workspaces API Swagger UI](https://api.workspaces.sidewalks.washington.edu/docs) is the interactive reference.
- [Workspaces API OpenAPI specification](https://api.workspaces.sidewalks.washington.edu/openapi.json) is the machine-readable contract.
- Most `/api/v1` operations declare the `TDEIHTTPBearer` security scheme. Check the security requirements for the specific operation and deployment; do not infer that a route is public from a missing operation-level declaration.

### Workspace and configuration endpoints

| Method   | Path                                                     | Documented operation                     |
| -------- | -------------------------------------------------------- | ---------------------------------------- |
| `GET`    | `/api/v1/workspaces/mine`                                | List the signed-in user's workspaces     |
| `POST`   | `/api/v1/workspaces/check`                               | Check workspace-name availability        |
| `POST`   | `/api/v1/workspaces`                                     | Create a workspace                       |
| `POST`   | `/api/v1/workspaces/from-file`                           | Create a workspace from an uploaded file |
| `GET`    | `/api/v1/workspaces/{workspace_id}`                      | Get a workspace                          |
| `PATCH`  | `/api/v1/workspaces/{workspace_id}`                      | Update a workspace                       |
| `DELETE` | `/api/v1/workspaces/{workspace_id}`                      | Delete a workspace                       |
| `GET`    | `/api/v1/workspaces/{workspace_id}/bbox`                 | Get a workspace bounding box             |
| `GET`    | `/api/v1/workspaces/{workspace_id}/jobs`                 | List jobs for a workspace                |
| `GET`    | `/api/v1/workspaces/jobs/{job_id}`                       | Get a job by ID                          |
| `GET`    | `/api/v1/workspaces/{workspace_id}/imagery/settings`     | Get imagery settings                     |
| `PATCH`  | `/api/v1/workspaces/{workspace_id}/imagery/settings`     | Update imagery settings                  |
| `GET`    | `/api/v1/workspaces/{workspace_id}/quests/long`          | Get the long-quest definition            |
| `GET`    | `/api/v1/workspaces/{workspace_id}/quests/long/settings` | Get long-quest settings                  |
| `PATCH`  | `/api/v1/workspaces/{workspace_id}/quests/long/settings` | Update long-quest settings               |

The `WorkspaceCreate` request requires `type`, `title`, and `tdeiProjectGroupId`; it also has `description`, `tdeiRecordId`, `tdeiServiceId`, and `tdeiMetadata` fields. Its type values are `osw`, `pathways`, and `flex`. The file-creation request uses `multipart/form-data` and requires `file`, `type`, `title`, and `tdeiProjectGroupId`; it also has a `description` field. The name-check request requires `title` and `tdeiProjectGroupId`; its response contains `available`.

The workspace patch schema includes `title`, `description`, `externalAppAccess`, `autoFlagReview`, and `overrideConflicts`. Imagery settings use a `definition` field. Long-quest settings use `type`, `definition`, and `url`; the documented type values are `NONE`, `JSON`, and `URL`.

The `WorkspaceResponse` schema fields include `id`, `type`, `title`, `description`, `tdeiProjectGroupId`, `tdeiRecordId`, `tdeiServiceId`, `tdeiMetadata`, `createdAt`, `createdBy`, `createdByName`, `updatedAt`, `externalAppAccess`, `kartaViewToken`, `autoFlagReview`, `overrideConflicts`, `role`, `projectsCount`, `membersCount`, `longFormQuestDef`, `imageryListDef`, and `importStatus`. Do not share token values. A job response includes `id`, `job_type`, `status`, `request`, `created_at`, `updated_at`, current task information, `response`, and `workspace_id`.

### Teams and workspace roles

| Method                 | Path                                                                  | Documented operation             |
| ---------------------- | --------------------------------------------------------------------- | -------------------------------- |
| `GET`, `POST`          | `/api/v1/workspaces/{workspace_id}/teams`                             | List or create workspace teams   |
| `GET`, `PUT`, `DELETE` | `/api/v1/workspaces/{workspace_id}/teams/{team_id}`                   | Get, update, or delete a team    |
| `GET`, `POST`          | `/api/v1/workspaces/{workspace_id}/teams/{team_id}/members`           | List members or join a team      |
| `PUT`, `DELETE`        | `/api/v1/workspaces/{workspace_id}/teams/{team_id}/members/{user_id}` | Add or remove a team member      |
| `GET`                  | `/api/v1/workspaces/{workspace_id}/users`                             | Get privileged workspace members |
| `PUT`                  | `/api/v1/workspaces/{workspace_id}/users/{user_id}/role`              | Assign a workspace role          |
| `DELETE`               | `/api/v1/workspaces/{workspace_id}/users/{user_id}`                   | Remove a workspace role          |

Team create and update requests require `name`. A team response includes `id`, `name`, and `member_count`; a user response includes `id`, `auth_uid`, `email`, and `display_name`. Workspace role requests require `role`; the schema lists `lead`, `validator`, and `contributor`. The API reference does not define the permissions attached to those labels. See [Workspaces roles](roles.md) before interpreting them.

### Tasking projects, tasks, and audit

Tasking routes are nested under `/api/v1/workspaces/{workspace_id}/tasking/projects`. They cover project operations, areas of interest, project roles, task-boundary generation and validation, tasks, locks, submissions, feedback, and project or task audit events. The [Tasking projects and tasks article](tasking-projects-and-tasks.md) lists those methods, paths, filters, and request models.

### Changesets and OSM-compatible routes

| Method | Path                                                                  | Documented operation                      |
| ------ | --------------------------------------------------------------------- | ----------------------------------------- |
| `GET`  | `/api/v1/workspaces/{workspace_id}/changesets/{changeset_id}/adiff`   | Get a changeset augmented diff            |
| `PUT`  | `/api/v1/workspaces/{workspace_id}/changesets/{changeset_id}/resolve` | Resolve a changeset                       |
| `GET`  | `/api/0.6/capabilities`                                               | Get OSM API capabilities                  |
| `GET`  | `/api/capabilities`                                                   | Get capabilities                          |
| `GET`  | `/api/capabilities.json`                                              | Get capabilities as JSON                  |
| `GET`  | `/workspace/{workspace_id}/api/0.6/capabilities`                      | Get workspace-scoped OSM API capabilities |
| `GET`  | `/workspace/{workspace_id}/api/capabilities`                          | Get workspace-scoped capabilities         |
| `GET`  | `/workspace/{workspace_id}/api/capabilities.json`                     | Get workspace-scoped capabilities as JSON |

The specification also lists `GET`, `PUT`, `POST`, `DELETE`, and `PATCH` catch-all routes at `/{full_path}`. These generic routes do not enumerate supported OSM operations; see [OSM API emulation](osm-api-emulation.md) for the limits of what can be inferred.

### Service endpoints

| Method | Path      | Documented operation |
| ------ | --------- | -------------------- |
| `GET`  | `/`       | Root response        |
| `GET`  | `/health` | Health check         |

### Responses and request details

The OpenAPI operation defines each endpoint's response codes, response schema, parameters, and request-body schema. Many operations also document `422` validation responses. Use the operation entry for exact details rather than assuming every endpoint has the same response shape. A dedicated workspace export or TDEI publish route is not listed in this API specification.

## What This Does Not Mean

The specification does not define every permission, UI action, state transition, or deployment-specific behavior. It lists no dedicated workspace export or publish endpoint under this documented Workspaces API; this does not prove that the product has no export workflow or that another service has no such API. Do not invent a route or treat a generic catch-all route as evidence of undocumented functionality.

## How To Use This

Identify the API host and deployment, then cite the exact method and path. Check required fields, query and header parameters, security declarations, and response schemas in the OpenAPI entry. Use the Workspaces user manual for UI procedures and distinguish this API from the TDEI API and OSM-compatible routes.

## Example

To check a workspace title, a client sends `POST /api/v1/workspaces/check` with the required title and project-group ID, then reads the `available` response field. Workspace creation is a separate `POST /api/v1/workspaces` request; file-based creation uses `POST /api/v1/workspaces/from-file`.

## Assistant Guidance

Answer API questions from the published OpenAPI specification and identify whether a statement comes from a path, request schema, response schema, or separate product workflow. Do not infer access rights, successful runtime availability, export behavior, or undocumented endpoint semantics. Ask for the API host/version when deployment differences may matter.

## Related Concepts

- [What is a workspace in technical terms?](workspace-technical-definition.md)
- [How do Tasking projects and tasks work in Workspaces?](tasking-projects-and-tasks.md)
- [What roles exist in Workspaces?](roles.md)
- [Changesets (Workspaces)](changesets.md)
- [How does Workspaces emulate OSM APIs?](osm-api-emulation.md)
- [How can edits be audited?](edit-auditing.md)
- [Workspaces API Swagger documentation](https://api.workspaces.sidewalks.washington.edu/docs)
- [Workspaces API OpenAPI specification](https://api.workspaces.sidewalks.washington.edu/openapi.json)
