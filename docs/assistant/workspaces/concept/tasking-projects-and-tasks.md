---
uid: 4510d7a9-e300-48ac-a109-4675da390913
title: How do Tasking projects and tasks work in Workspaces?
slug: tasking-projects-and-tasks
doc_type: concept
questions:
    - What are Tasking projects and tasks in Workspaces?
    - What states and operations does the Workspaces Tasking API document?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - Workspaces
topics:
    - workspaces
    - tasking-manager
    - review
    - roles
    - changesets
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
    - assistant/workspaces/concept/workspaces-api.md
    - assistant/workspaces/concept/workspace-technical-definition.md
    - assistant/workspaces/concept/roles.md
    - assistant/workspaces/concept/changesets.md
    - assistant/workspaces/concept/edit-auditing.md
    - assistant/workspaces/workflow/set-up-tasking-manager-project.md
tags:
    - Assistant
---

<!-- @format -->

# How do Tasking projects and tasks work in Workspaces?

## Short Answer

The Workspaces API models a Tasking project as a resource inside a workspace. Its documented routes cover project settings and areas of interest, project roles, task boundaries and states, locks, submissions, feedback, and project or task audit events. The OpenAPI specification describes the API contract, not every user-interface rule or permission.

## Significance

The API uses distinct scopes for a workspace, a Tasking project, and an individual task. Keeping those scopes separate helps avoid confusing Tasking project roles with workspace roles or TDEI Project Group membership.

## What This Means

Tasking resources are nested under a workspace. The following routes and parameters are listed in the [Workspaces API reference](https://api.workspaces.sidewalks.washington.edu/docs).

### Project and role endpoints

| Method                          | Path                                                                              | Documented operation or parameters                  |
| ------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------- |
| `GET`, `POST`                   | `/api/v1/workspaces/{workspace_id}/tasking/projects`                              | List or create projects                             |
| `GET`                           | `/api/v1/workspaces/{workspace_id}/tasking/projects/validate-name`                | Validate a name; query parameter `name`             |
| `GET`, `PATCH`, `DELETE`        | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}`                 | Get, update, or delete a project                    |
| `POST`                          | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/activate`        | Activate a project                                  |
| `POST`                          | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/close`           | Close a project                                     |
| `POST`                          | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/reset`           | Reset a project                                     |
| `GET`, `POST`, `DELETE`         | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/aoi`             | Get, upload, or delete the area of interest         |
| `GET`, `POST`                   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/roles`           | List or add project roles                           |
| `GET`, `PUT`, `PATCH`, `DELETE` | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/roles/{user_id}` | Get, set, update, or remove a project role          |
| `GET`                           | `/api/v1/me/workspaces/{workspace_id}/tasking/projects/roles`                     | List the current user's workspace and project roles |

The project-list endpoint documents query parameters `status`, `text_search`, `page`, `page_size`, `order_by`, and `order_by_type`. Project-name validation accepts the `name` query parameter and returns an `exists` field. A project-create request requires `name`; its schema also includes instructions, review settings, lock timeout, area of interest, role assignments, custom imagery, and description. Project updates can include name, instructions, lock timeout, review setting, custom imagery, and description. Project status values are `draft`, `open`, and `done`. Project-role values are `lead`, `validator`, and `contributor`.

### Task endpoints

| Method   | Path                                                                                                   | Documented operation or parameters                                                                   |
| -------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/grid`                           | Generate a grid; query parameter `cell_size_meters`                                                  |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/validate`                       | Validate a task-boundary feature collection                                                          |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/save`                           | Save tasks; request uses `SaveTasksRequest` and an `Idempotency-Key` header                          |
| `GET`    | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks`                                | List tasks; filters include `status`, `locked_by_user_id`, `last_mapper_id`, `page`, and `page_size` |
| `GET`    | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}`                  | Get a task                                                                                           |
| `GET`    | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/boundary.geojson` | Get a task boundary as GeoJSON                                                                       |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/lock`             | Lock a task                                                                                          |
| `DELETE` | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/lock`             | Unlock a task; query parameter `force`                                                               |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/extend`           | Extend a task lock                                                                                   |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/reset`            | Reset a task                                                                                         |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/submit`           | Submit a task                                                                                        |
| `POST`   | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/submit-changeset` | Submit an OSM changeset ID for a task                                                                |

Task-boundary sources are `grid` and `import`. Task validation takes a feature collection and returns a validity flag, warnings, source, and feature collection. The task-save request requires `source` and `feature_collection`; its response includes the task-boundary type, task count, tasks, and whether the request was replayed. A task-submit request requires `done` and can include feedback; when present, feedback requires `notes` and can include a `reason_category` of `incomplete_mapping`, `data_quality_issue`, `wrong_area`, or `other`. The changeset-submission request requires `osm_changeset_id`.

Task statuses are `to_map`, `to_review`, `to_remap`, and `completed`. Task responses can include geometry, area, a lock summary, last mapper, feedback, and timestamps. These are documented schema values and fields; the specification does not define every state transition or permission.

### Audit endpoints

| Method | Path                                                                                        | Documented filters                                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `GET`  | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/audit`                     | `event_type`, `task_number`, `actor_user_id`, `occurred_from`, `occurred_to`, `include_deleted`, `page`, `page_size`, `order_by_type` |
| `GET`  | `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/tasks/{task_number}/audit` | `event_type`, `actor_user_id`, `occurred_from`, `occurred_to`, `page`, `page_size`, `order_by_type`                                   |

Audit responses contain paginated events with event type, project ID, actor, time, details, and a project-deleted indicator. The event enum includes `project_created`, `project_activated`, `project_closed`, `project_edited`, `project_deleted`, `project_reset`, `aoi_uploaded`, `aoi_deleted`, `tasks_created`, `task_state_changed`, `task_locked`, `task_lock_extended`, `task_lock_renewed`, `task_unlocked`, `task_reset`, `changeset_submitted`, and `feedback_submitted`.

## What This Does Not Mean

The API specification does not define the permission set for each role, the exact meaning or transition rules for every status, lock-expiration behavior, review criteria, or whether a particular UI exposes every operation. An API route or task status does not by itself mean that data has been published to TDEI or OpenStreetMap.

## How To Use This

Keep `workspace_id`, project ID, and task number distinct when identifying an API resource. Use the current API reference for request and response shapes, and use the [Tasking project setup workflow](../workflow/set-up-tasking-manager-project.md) for user-interface steps. Confirm the deployment environment when availability or permissions matter.

## Example

A client reads a Tasking project in a workspace with status `open`, then requests one task and receives status `to_review` with its geometry and lock summary. Those values describe the API response; they do not prove that the task passed review or that its data was released.

## Assistant Guidance

Cite the [Workspaces API documentation](https://api.workspaces.sidewalks.washington.edu/docs) for endpoint names, fields, query parameters, and enum values. Do not infer role permissions, state-transition rules, lock timing, review outcomes, or publication behavior from the schema alone. Distinguish Tasking projects from workspaces and TDEI Project Groups; ask for the environment and resource identifiers when needed.

## Related Concepts

- [What APIs does Workspaces provide?](workspaces-api.md)
- [What is a workspace in technical terms?](workspace-technical-definition.md)
- [What roles exist in Workspaces?](roles.md)
- [How can edits be audited?](edit-auditing.md)
- [How do I set up a Tasking Manager project in Workspaces?](../workflow/set-up-tasking-manager-project.md)
- [Workspaces API Swagger documentation](https://api.workspaces.sidewalks.washington.edu/docs)
- [Workspaces API OpenAPI specification](https://api.workspaces.sidewalks.washington.edu/openapi.json)
