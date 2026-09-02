---
uid: 4998c5fd-0bf1-4dcf-9ad4-86ec698323c1
title: Assistant Knowledge Base — Dispatch
slug: dispatch
doc_type: workflow
questions:
    - What articles are available in the TCAT Wiki Assistant Knowledge Base?
audiences:
    - developer
products:
    - AccessMap
    - AVIV ScoutRoute
    - Cross-Platform
    - FleXR
    - iOSPointMapper
    - LivAbility
    - OpenSidewalks
    - OS-CONNECT
    - QA-QC Reports
    - Rapid
    - TDEI
    - Walksheds
    - WayKeeper
    - Workspaces
topics:
    - assistant-layer
    - governance
risk_level: low
authority_level: official
publication_status: draft
last_reviewed: 2026-09-02
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/index.md
    - assistant/schema.md
    - assistant/intents.md
tags:
    - Assistant
---

<!-- @format -->

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Produced by utilities/akb_generate_dispatch.py. Re-run the script
     (or utilities/build_site.py) to refresh this file after adding,
     removing, or re-statusing pages under docs/assistant/. -->

# Assistant Knowledge Base — Dispatch

## Short Answer

This file is the registry for all pages in the `docs/assistant/` knowledge base. It is the single source of truth for canonical file paths, authoring status, and section structure. External agents should fetch this file first to enumerate available knowledge-base pages before retrieving individual articles.

Related: [Overview](index.md) · [Schema](schema.md) · [Intents](intents.md)

## Significance

A stable registry decouples retrieval pipelines from the filesystem. Authors use this file to track what has been written, what is still a stub, and what needs review. Integrators can use it to detect new pages without crawling the entire site.

## What This Means

- Every article that physically exists in `docs/assistant/` has a row in this registry; nothing here is aspirational.
- **Publication status** is one of: `stub` (placeholder exists, body is `TODO`), `draft` (content authored, awaiting review), `published` (available in the human layer), or `archived` (retained for agents but not published).
- Every page listed here is served as raw Markdown at the same URL with an `.md` extension, regardless of status. See [schema](schema.md) for the human-layer vs. agent-layer distinction.
- Section index files (e.g., `workspaces/index.md`) carry that topic's policy content and per-topic assistant guidance.

## What This Does Not Mean

- This file does not replace the [schema](schema.md), which governs authoring conventions.
- This file does not replace section indexes, which provide richer per-section context.
- A `stub` status does not mean the content is wrong — it means the body has not yet been authored.

## How To Use This

**Agents**: Fetch `dispatch.md`, parse the registry tables, filter by `Publication Status`, `Authority Level`, or topic heading, then retrieve individual pages by constructing their URL as `https://taskarcenteratuw.github.io/tcat-wiki/` + the `Base:` path shown under the relevant heading + the filename in the table.

**Authors**: Write or edit files directly under `docs/assistant/`; do not hand-edit this file. Re-run `utilities/akb_generate_dispatch.py` (or the full `utilities/build_site.py` pipeline) to refresh the registry after adding a page or changing its `publication_status`.

**Maintainers**: This file is a generated build artifact. To change its structure, edit `utilities/akb_generate_dispatch.py`.

## Example

An agent looking for Workspaces content: fetches this file, finds the `## Workspaces` heading, selects a relevant row from its `### Concepts` or `### Workflows` table, then fetches that page using the `Base:` prefix plus the filename.

## Assistant Guidance

This page should be fetched fresh rather than cached aggressively; its registry reflects the current authoring state of the knowledge base. If a file listed here returns 404, the generator has not yet been re-run since the file was added.

## Related Concepts

- [Assistant Knowledge Base Index](index.md) — Overview of this retrieval-oriented TCAT knowledge base
- [Assistant Knowledge Base Schema](schema.md) — Authoring contract for Assistant Knowledge Base articles
- [Assistant Knowledge Base Intents](intents.md) — Mapping of retrieval intents to article paths

## Status Legend

| Status | Count | Meaning |
| :----- | ----: | :------ |
| `stub` | 63 | Frontmatter and heading scaffold exist; body is `TODO` |
| `draft` | 741 | Content authored; awaiting TCAT editorial review |
| `published` | 1 | Available in the human-facing site |
| `archived` | 0 | Retained for agents but not published |

## Authority Legend

| Authority level | Count | Meaning |
| :-------------- | ----: | :------ |
| `provisional` | 671 | Early or limited-confidence guidance |
| `explanatory` | 132 | Established explanation without formal policy authority |
| `official` | 2 | Formally endorsed organizational guidance |

## Registry

## Root Pages

Base: `assistant/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `e21aa637-e484-46d9-bc7d-57e929549f42` | `index.md` | explanatory | draft |
| `eb3ea5ca-9c11-4199-9614-8479d5eb7deb` | `schema.md` | official | draft |
| `36cf37f4-27cb-40e1-83ae-9171587dc2ac` | `intents.md` | provisional | draft |
| `4998c5fd-0bf1-4dcf-9ad4-86ec698323c1` | `dispatch.md` | official | draft |

## AccessMap — Assistant Knowledge Base

See [accessmap/index.md](accessmap/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/accessmap/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `2eec4238-4c6a-42f3-9054-a9c475ff29a4` | `index.md` | explanatory | draft |

### Concepts

Base: `assistant/accessmap/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `e4deaaf6-6462-48e0-ad4d-b038c2a39beb` | `accessibility-assumptions.md` | provisional | draft |
| `a5858d1a-220b-488c-8630-b99bbb029749` | `accessibility-mobility-metrics.md` | provisional | draft |
| `57acb4d0-6cad-4afe-b348-2fe0c3b2ea09` | `accessibility-needs.md` | provisional | draft |
| `abb42bac-60db-4565-b9b9-46959ca4e3ca` | `accessibility-preference-routing.md` | provisional | draft |
| `74738161-a13a-4d27-8b30-fbc9ec4f5889` | `accessible-routes-appear-longer.md` | provisional | draft |
| `06ab05b6-7749-4446-ae1a-d3d619129a1d` | `accessmap.md` | explanatory | draft |
| `44ddbdff-7047-4ee3-bf9e-66bc9f49cf6f` | `ada-compliance-support.md` | provisional | draft |
| `6f4ba36c-3827-4b8f-8f0c-38939834768a` | `agency-routing-customization.md` | provisional | draft |
| `37a2145d-2b6a-4299-aadf-99ee1886235f` | `avoid-missing-curb-ramps.md` | provisional | draft |
| `9d0d1a13-e300-47a6-9713-3825d2596b0c` | `avoid-steep-slopes.md` | provisional | draft |
| `41cd37cd-e354-4bb0-9f88-7e7825f5c016` | `blind-low-vision-support.md` | provisional | draft |
| `8cb93608-585b-4da6-81ee-c95dc5c9a304` | `campus-accessibility.md` | provisional | draft |
| `591cbbe1-5d04-4410-bda2-c5696924d1bd` | `combined-crossing-accessibility.md` | explanatory | draft |
| `9904029d-c72f-4f09-b0b9-0c1e04c3d132` | `community-accessibility-priorities.md` | provisional | draft |
| `97f238c3-ec39-4879-9b12-2d9720f1f51e` | `comparison-apple-maps.md` | provisional | draft |
| `841c5a81-ce33-4954-8b83-c1cf4da5056d` | `construction-routing-effect.md` | provisional | draft |
| `b93a2388-da98-4edb-a6c4-a064ab1b99fb` | `coverage-outside-washington.md` | provisional | draft |
| `203f1f3a-11d5-4126-a846-c4a15396c076` | `critical-pedestrian-corridors.md` | provisional | draft |
| `b1228a5d-f027-4e15-8aea-3d435be4909a` | `curb-ramp-routing.md` | provisional | draft |
| `0af77520-c27f-4e28-ae3f-0e79747f396f` | `data-sources.md` | explanatory | draft |
| `95ad30a0-0069-40c8-a452-23a4c03b3fcf` | `disconnected-sidewalks.md` | provisional | draft |
| `38c67b9c-867c-48e6-837e-fc37e7d801ba` | `emergency-planning.md` | provisional | draft |
| `a0197f6e-8c6e-47d2-87cc-090c96d10a08` | `explaining-metrics-publicly.md` | provisional | draft |
| `c3fe46c4-6db3-4e05-b3a2-a22e407ed16e` | `feature-feedback.md` | explanatory | draft |
| `d935b14d-70a1-40cd-890b-83080789bae0` | `field-validation.md` | provisional | draft |
| `459c7755-0c13-43ec-8503-4e767928c894` | `google-maps-comparison.md` | provisional | draft |
| `bb4dabc2-8f6b-4491-8360-923c0d614e1f` | `google-maps-design-rationale.md` | provisional | draft |
| `ca15dde9-af31-45f6-9044-21d22c621ffe` | `gtfs-integration.md` | provisional | draft |
| `adab452f-b9b6-4817-b49c-10e7e9ba2baf` | `gtfs-pathways.md` | explanatory | draft |
| `622342dd-bb05-4814-95e5-75286b469b66` | `here-routing-comparison.md` | provisional | draft |
| `f8ef7e10-ce26-40ed-856f-a6b440e707c9` | `hospital-campus-support.md` | provisional | draft |
| `def5bb9e-356c-4676-9b3a-2ad468262d32` | `inaccessible-transit-stations.md` | provisional | draft |
| `d3cac759-2870-4695-979b-c4383087ece7` | `local-datasets-routing-quality.md` | provisional | draft |
| `7d259a83-dc6a-4470-8042-e7adfbfaed3f` | `longer-route-selection.md` | explanatory | draft |
| `6034b0da-57ad-4588-a3c0-6ceb4cf6584d` | `manual-wheelchair-support.md` | provisional | draft |
| `07877d70-ca81-4fce-a8bd-a428258b0f3e` | `missing-accessibility-data.md` | provisional | draft |
| `065b5266-43c9-46a7-802e-d56f709ccf9f` | `missing-curb-ramps-effect.md` | provisional | draft |
| `e0fd2c85-f94d-4b70-8611-8fcd5f57c385` | `mobility-profiles.md` | explanatory | draft |
| `5ce514fb-4e2c-4703-b2da-61f6236bd216` | `network-redundancy.md` | provisional | draft |
| `119cd40e-c089-40b6-9282-cc3017482ad4` | `opensidewalks-data-consumption.md` | provisional | draft |
| `a9e9e9ac-0052-4b0e-a82f-a6fe7367aea4` | `operational-use.md` | provisional | draft |
| `c88fd955-21ca-466d-8ae1-5bcb04b88a6e` | `paratransit-planning-support.md` | provisional | draft |
| `1008ba37-ec37-465a-8c5a-a85fc3b5321f` | `pedestrian-resilience.md` | provisional | draft |
| `fec1b22c-f401-4b4a-855b-a5dc6c11e75f` | `planned-capabilities.md` | provisional | draft |
| `a2db4fb9-af25-4e5c-9cc4-29285cf62d4f` | `powered-wheelchair-support.md` | provisional | draft |
| `d6cc5c58-a17e-492f-8577-4af7821a4740` | `prioritization-metrics.md` | provisional | draft |
| `32982e7b-fe51-49d2-bbe8-5653294ec0ac` | `profile-responsive-map.md` | provisional | draft |
| `e1689a66-6818-4d44-a11d-8e02c9fd5271` | `public-engagement.md` | provisional | draft |
| `2a6b1bee-9a93-4cc5-99fa-9f784f3a7dc9` | `route-calculation.md` | explanatory | draft |
| `92e712b5-354b-421e-b1fe-13561b3aac82` | `route-planning-and-navigation.md` | provisional | draft |
| `79927cc0-871c-4fed-9a46-f28676068e6b` | `route-reliability.md` | provisional | draft |
| `c7896de9-9fac-422e-a7f2-e8bc15e4d5f0` | `routing-limitations.md` | provisional | draft |
| `b604a693-45de-4c4e-924e-dde9ec9b96ae` | `routing-profiles.md` | provisional | draft |
| `3d7f4c59-9192-4386-aa61-ebd76aa560e5` | `routing-system-comparison.md` | provisional | draft |
| `279d9e76-a0c3-43f2-99e3-f25e0a1247c5` | `routing-tradeoffs.md` | provisional | draft |
| `92351d12-f4b5-4b88-b99c-67d4368a2f52` | `school-use.md` | provisional | draft |
| `3d2b9770-ef79-4e85-91f8-1468def552d1` | `slope-routing.md` | provisional | draft |
| `0807e1e4-f16b-4165-96fa-fae2fbe682b2` | `steep-slopes-effect.md` | provisional | draft |
| `b1771e49-c109-42bf-b50a-c083da2efaea` | `temporary-barriers.md` | explanatory | draft |
| `f22cac9e-0b04-4f91-80d7-d26f9c4e8119` | `tourism-accessibility.md` | provisional | draft |
| `1d569bdc-4d8c-453d-8fde-a8f6ed33be30` | `transit-pedestrian-routing-integration.md` | provisional | draft |
| `4a9ac0b4-6523-4f3a-9284-c4d102b15828` | `transit-wayfinding.md` | provisional | draft |
| `f9ddd765-ced4-4e75-b325-bdd0b685d800` | `update-cadence.md` | provisional | draft |

### Workflows

Base: `assistant/accessmap/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `88fac7c3-3112-438e-9251-da4ac0c0dd17` | `follow-a-route-with-location.md` | provisional | draft |
| `5be36fff-c2b7-4fb6-b573-9a76834a83b7` | `get-accessmap-set-up-for-your-region.md` | explanatory | draft |
| `e338ea65-fb8c-46df-96c5-71f0065a1e2e` | `plan-and-share-a-route.md` | explanatory | draft |
| `75b0ed80-b6c5-4a0a-98a7-cd072244df24` | `prioritize-pedestrian-investments.md` | provisional | draft |
| `d2c54bfa-dcb4-486a-9d04-70147096e8cb` | `report-routing-problems.md` | explanatory | draft |
| `180a0bc8-9236-4053-b66d-ba22601b6fad` | `validate-routing-results.md` | provisional | draft |

## AVIV ScoutRoute — Assistant Knowledge Base

See [aviv-scoutroute/index.md](aviv-scoutroute/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/aviv-scoutroute/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `d8895c9a-7a18-4506-a8b0-b4d014aacaaf` | `index.md` | provisional | draft |

### Concepts

Base: `assistant/aviv-scoutroute/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `b96f1524-81e2-49ad-aebe-96f65d155d87` | `app-enabled-workspaces.md` | provisional | draft |
| `7a8e26e8-df9b-4b0d-8467-1073244761c5` | `aviv-scoutroute.md` | provisional | draft |
| `9dda9550-87ac-4f21-9570-7ceff5cbb627` | `conditional-team-questions.md` | provisional | draft |
| `bec3a581-558f-42f0-b34f-9ecc0f7a2554` | `field-observation.md` | provisional | draft |
| `ea76489b-a92b-4501-849c-74c57c4888fd` | `group-quest-selection.md` | provisional | draft |
| `c6d302c4-d775-476f-9fd9-9059e8dfb087` | `numeric-quest-input.md` | explanatory | draft |
| `c7035d9d-8488-411c-a937-8c04c55a9db5` | `numeric-quest-validation.md` | explanatory | draft |
| `9e865fd0-fe83-4ee2-be27-e8d0a179b590` | `offline-data-and-upload.md` | provisional | draft |
| `e36b6ff3-3a56-4b65-9127-374d1a554f29` | `quest-answer-dependency-logic.md` | explanatory | draft |
| `303f0036-d892-4fb0-8dbb-d29773b9e96c` | `quest-contributions.md` | provisional | draft |
| `a1595106-5792-4731-aa0e-36c461f221b9` | `quest-definition-application.md` | explanatory | draft |
| `779b1905-fca1-4d28-a561-d849c6dcc66e` | `quest-definition-creator.md` | explanatory | draft |
| `ecdd0450-cd47-4f1d-9a24-48dcab926551` | `quest-definition-custom-icons.md` | explanatory | draft |
| `7fd81643-1365-4494-9909-5bbd70961c74` | `quest-definition-element-icons.md` | explanatory | draft |
| `55f541aa-0bca-4b21-88f1-4dbd5c4f543a` | `quest-definition-element-targeting.md` | explanatory | draft |
| `3ef13a7d-44e9-4ebf-9c27-02a007db6795` | `quest-definition-feature-presets.md` | explanatory | draft |
| `a4ad0bc0-677f-4e0e-ad70-b6b898cc22d8` | `quest-definition-picture-questions.md` | provisional | draft |
| `226a3de6-025b-4085-98e9-72462dcf86c4` | `quest-definition-query-syntax.md` | explanatory | draft |
| `ce5fc63e-f411-43e1-9de7-a7d808e727e7` | `quest-definition-resurvey-interval.md` | explanatory | draft |
| `47942f15-f256-49a9-a3f0-f2e70c9a8063` | `quest-dependency-evaluators.md` | explanatory | draft |
| `0770da33-ded7-4e13-aa5d-0a5b37efa775` | `quest-input-types.md` | provisional | draft |
| `adafb96b-4eb2-4857-8aa4-2e876f2e5edd` | `quest-required-or-optional.md` | explanatory | draft |
| `557c7f7d-8153-4cda-8ad1-1511aad3c7a9` | `quest-visibility-and-local-state.md` | provisional | draft |
| `c1d960b6-ad07-4b10-a8c6-e5ce06b07c29` | `quest.md` | provisional | draft |

### Workflows

Base: `assistant/aviv-scoutroute/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `e9ed8f2b-8637-40ed-ace0-067f81a74215` | `answer-quest.md` | provisional | draft |
| `ce7a0d43-f792-472d-9c35-74ed27745081` | `complete-and-submit-a-quest.md` | provisional | draft |
| `31b29431-397c-42c8-af6a-70dae0bbbff8` | `design-conditional-follow-up-quests.md` | explanatory | draft |
| `1c219b5b-c233-41d3-a014-c5f94f6c5c28` | `install-aviv-scoutroute.md` | provisional | draft |
| `9ab89290-d73c-4a0c-a760-380199a8a642` | `join-a-project-and-find-quests.md` | provisional | draft |
| `5a33c504-7f5b-4426-8232-fcd088141f7c` | `manage-quest-visibility.md` | provisional | draft |
| `2e7b60cf-9c49-4e25-974c-ab4ce9d2105b` | `renumber-quest-definition.md` | explanatory | draft |
| `4618725f-61dc-4fef-8bab-ad5990c0db54` | `undo-a-quest-submission.md` | provisional | draft |
| `c93fc95f-c5c8-4a20-b217-fd49295ca9de` | `update-quest-definition-in-workspace.md` | provisional | draft |
| `e666abac-7806-4f58-a9b8-48a70cc8bdb6` | `upgrade-quest-definition.md` | explanatory | draft |

## Cross-Platform — Assistant Knowledge Base

See [cross-platform/index.md](cross-platform/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/cross-platform/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `8c5ec0a1-be5b-4fd2-833c-213a4ffb7efe` | `index.md` | explanatory | draft |

### Concepts

Base: `assistant/cross-platform/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `676fc317-6f75-4faf-9e08-f2b2c413e74a` | `abbreviations.md` | official | published |
| `fb975654-03fa-4c88-bf08-ee7ea5ff99d9` | `accessibility-islands.md` | explanatory | draft |
| `214efab0-d619-483f-8bf3-c87b51c93983` | `accessmap-routing.md` | explanatory | draft |
| `652f8306-3709-433c-9e3e-a76d5968ab14` | `ada-compliance-boundaries.md` | explanatory | draft |
| `de077cd7-9a60-4a24-b7e8-9e0eedc51cab` | `ada-safety-legal-boundaries.md` | provisional | draft |
| `208d4b39-6224-4178-9c87-b20131dd8124` | `assistant-abstention.md` | provisional | draft |
| `31391ff4-ec33-415b-b952-c97d2e8b2e10` | `completeness.md` | explanatory | draft |
| `6aef59c1-7136-4200-91cc-d42ce8b5f8b6` | `connected-pedestrian-graph.md` | explanatory | draft |
| `3d939b29-ea39-4f8b-a46d-697b90f2ef15` | `crossing-links.md` | explanatory | draft |
| `8527c07f-7f16-4bac-aa6f-7f81808d026b` | `data-freshness.md` | explanatory | draft |
| `d1f34cff-a68b-4671-9f2a-3ef5f66c126e` | `data-viewer-portal-workspaces-relationship.md` | provisional | draft |
| `5cc80254-791a-4505-b94e-7d405896a681` | `documentation-audience-baseline.md` | provisional | draft |
| `35a02f4f-b1fc-49e3-a577-1043370a3f8f` | `documentation-guide-types.md` | provisional | draft |
| `4b1d0b10-56ec-4b55-834f-463ac2f49df9` | `help-desk-questions-as-knowledge-sources.md` | provisional | draft |
| `59cd6566-9f1a-4b01-8e9b-a06e6c174cd8` | `how-should-ai-outputs-be-validated.md` | explanatory | draft |
| `f828118b-1a41-4817-8eee-41b2d225021d` | `knowledge-base-domain-review.md` | provisional | draft |
| `1783d183-b377-4c17-a303-f83701312400` | `mobile-and-web-validation-differences.md` | explanatory | draft |
| `9256ade4-dd52-4d0d-b74a-fb4e7d4ec200` | `os-connect-vs-gtfs-pathways.md` | explanatory | draft |
| `e663d78b-e757-4151-a7fc-ce04854a6e33` | `public-vs-internal-content.md` | provisional | draft |
| `a91711cd-6e9f-4932-bc2a-345663cde928` | `qa-qc-report-audience.md` | provisional | draft |
| `004f4eb1-1b05-40ff-b253-360b85ca3a55` | `rural-pedestrian-data-value.md` | provisional | draft |
| `14375ffe-f7c5-453b-bc1d-71ad2537953a` | `topic-based-assistant-content.md` | provisional | draft |
| `46efa8a7-bc18-4c89-959d-9f7cb672fe65` | `walksheds.md` | explanatory | draft |
| `06eb2010-0a38-463f-9590-004878cdc7ed` | `what-are-the-risks-of-automated-accessibility-analysis.md` | explanatory | draft |
| `448a1a98-673f-4710-b3f8-d962bcc3b32e` | `workspaces-user-audience.md` | provisional | draft |

### Workflows

Base: `assistant/cross-platform/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `d0e0f3db-cd76-4b1f-83dd-ef86bdd4f2ca` | `report-product-issues.md` | explanatory | draft |
| `65b96e01-d1b5-4d61-8423-5a9e5c023a44` | `review-assistant-article-stubs.md` | provisional | draft |
| `0065ef0c-3d41-467c-b167-761c1e948747` | `review-community-feedback.md` | explanatory | draft |
| `d5a8cd56-f0c9-4fbd-9c39-41f21c69f7ce` | `support-answer-patterns.md` | provisional | draft |
| `fd0a00ff-2b51-451e-97fd-5e3844483c46` | `update-jurisdiction-data.md` | explanatory | draft |
| `5a11848c-45c2-4f83-b740-0e9ff0ad3ca8` | `use-accessmap-for-public-engagement.md` | explanatory | draft |
| `e5dbbad8-03b9-4ff3-ad05-2f7f35e1f65e` | `use-os-connect-for-ada-transition-planning.md` | explanatory | draft |
| `ea86a1eb-7677-4090-8453-d5e64d945215` | `use-walksheds-for-safe-routes-to-school.md` | explanatory | draft |

## FleXR — Assistant Knowledge Base

See [flexr/index.md](flexr/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/flexr/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `7ec7294c-49d5-4756-9eea-141270e02ce2` | `index.md` | provisional | stub |

### Concepts

Base: `assistant/flexr/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `2a485ae0-ca36-41d6-93b8-bf57c964944b` | `flexr.md` | explanatory | draft |

### Workflows

Base: `assistant/flexr/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `0d9d82f4-7cf4-4149-a398-3ba53dfda726` | `get-involved-with-flexr.md` | explanatory | draft |

## iOSPointMapper — Assistant Knowledge Base

See [iospointmapper/index.md](iospointmapper/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/iospointmapper/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `d78da859-7f3a-4dc2-9a85-f1e6e64d66e5` | `index.md` | provisional | stub |

### Concepts

Base: `assistant/iospointmapper/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `6b474bd0-5310-451b-9a7c-2cd98ea08788` | `device-compatibility.md` | provisional | stub |

### Workflows

Base: `assistant/iospointmapper/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `b3b2312d-4a16-4ce5-99b2-694172106c79` | `start-collecting-data.md` | provisional | stub |

## LivAbility — Assistant Knowledge Base

See [livability/index.md](livability/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/livability/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `55521d6a-09e0-4475-b657-c130d40e6a6d` | `index.md` | provisional | stub |

### Concepts

Base: `assistant/livability/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `f09e5084-ff52-4dd1-8cd1-abd4822c56f5` | `poi-source.md` | provisional | stub |

### Workflows

Base: `assistant/livability/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `75e18a1d-cc14-4c3d-b092-45e6b1b7e574` | `select-mobility-profile.md` | provisional | stub |

## OpenSidewalks — Assistant Knowledge Base

See [opensidewalks/index.md](opensidewalks/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/opensidewalks/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `1df8e7aa-2bc6-4360-bb30-c1c69cc0e260` | `index.md` | provisional | draft |

### Concepts

Base: `assistant/opensidewalks/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `5c940667-37be-43d2-b356-7d1b1600c00f` | `adjacent-entities.md` | explanatory | draft |
| `0f78d245-6287-494c-b293-78534246ba30` | `adjacent-vs-custom-entities.md` | explanatory | draft |
| `34d58e62-1933-4601-8ea6-4390a5e693df` | `connector-segment-tagging.md` | explanatory | draft |
| `9cfc6245-ea9e-42bb-844c-b5ce7c50a882` | `coordinate-system-and-serialization.md` | provisional | draft |
| `30e8fc9c-9807-4698-903b-82ff2c572882` | `custom-entities.md` | explanatory | draft |
| `96c66875-cae9-4efd-994e-bac5b4f02c60` | `dataset-metadata-and-provenance.md` | provisional | draft |
| `ab93942b-5c60-4aa3-a946-01b306d7cbb0` | `ext-attributes-and-regional-flexibility.md` | provisional | draft |
| `41864860-3ae8-43f2-b951-8829efd2dc32` | `external-attributes.md` | explanatory | draft |
| `b9a44155-7d53-45aa-ad62-b71503c9cb72` | `external-data-overlay-boundary.md` | provisional | draft |
| `02534516-4b97-4c63-a62d-923077b6ea74` | `mapping-imagery-limitations.md` | provisional | draft |
| `a0b706cf-bdc0-4fe7-85cd-49b79734cfe1` | `maximum-extent-feasible.md` | provisional | draft |
| `9ceb3098-961a-4ff4-a1c3-dcef273e866b` | `network-entities.md` | provisional | draft |
| `29ffc0d9-3d14-43ae-98cc-6884872d5198` | `network-topology.md` | provisional | draft |
| `85c9e786-df58-40a6-af7c-8e5e680061a9` | `opensidewalks-schema.md` | provisional | draft |
| `f1ccd2a7-3563-4bcd-9046-1d92e2f694d3` | `opensidewalks.md` | provisional | draft |
| `6f85f542-fd51-4dde-b838-82f44c4fcd42` | `point-and-line-feature-workflows.md` | provisional | draft |
| `27a4a8a0-700d-4391-aaa5-4b5c470065f3` | `regional-dataset-derivatives.md` | provisional | draft |
| `38a79ef1-99e7-4c10-bcce-8416abde198c` | `roadside-surface-preferences.md` | provisional | draft |
| `d2ecc09b-5051-4aa1-959c-abce0f6efcc0` | `tasking-manager-roles.md` | provisional | draft |
| `6942366e-b725-4850-8c19-f21eb4ee362a` | `tdei-schema-validation.md` | provisional | draft |
| `727949a1-2099-46b1-8b56-8d868606b42f` | `workspace-editing-tools.md` | provisional | draft |

### Workflows

Base: `assistant/opensidewalks/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `35e258ba-6738-4c6e-a944-0003e6648342` | `add-custom-points-to-osw.md` | provisional | draft |
| `2f476704-7c83-47e7-b994-c0a6e4eaa428` | `convert-sidewalk-centerlines-to-osw.md` | provisional | draft |
| `b11f1b08-2161-4eb2-b108-88e82df975e7` | `find-latest-version.md` | provisional | draft |
| `abe2a4dc-4b8a-4424-8de1-16258f1da4a2` | `generate-task-polygons.md` | provisional | draft |
| `93bbc3a9-578b-4e3d-93aa-ac908baba833` | `map-osw-features-in-tasking-manager.md` | provisional | draft |
| `57966c8d-2cbf-434c-820c-039ff63aca84` | `validate-osw-tasking-manager-edits.md` | provisional | draft |

## OS-CONNECT — Assistant Knowledge Base

See [os-connect/index.md](os-connect/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/os-connect/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `eb972a50-0a11-44a8-8193-796ce9e7383c` | `index.md` | explanatory | draft |

### Concepts

Base: `assistant/os-connect/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `c1f739ff-91bc-439f-b38a-a4c1a0ee587e` | `accessibility-attribute.md` | provisional | draft |
| `04eafa76-4fa7-4a3a-a493-fa4716d2d371` | `accessibility-data-gaps.md` | provisional | draft |
| `79d46973-7732-4891-97e4-4610a44e206e` | `accessibility-equity.md` | provisional | draft |
| `e4c3ac31-f797-4d6f-aeff-1683a60a3e36` | `accessibility-improvement.md` | provisional | draft |
| `639d2079-3d3f-4085-ba74-c742a73eaeb1` | `accessibility-tradeoff-communication.md` | provisional | draft |
| `aab84dd3-64ec-4ff0-8c17-7ada93d2e29b` | `ada-title-ii-requirements.md` | provisional | draft |
| `b08a02d6-e1a9-48af-8773-dedbb975e04a` | `ada-transition-data-requirements.md` | provisional | draft |
| `a0f287e5-c881-4126-a8c4-792858292bc3` | `ada-transition-planning.md` | explanatory | draft |
| `e0ccd91a-63a4-40c5-bac3-ba603628e286` | `adoption-barriers.md` | provisional | draft |
| `6e3886d7-1071-4ed9-92d2-41418bba1204` | `advocacy-group-role.md` | provisional | draft |
| `a0653dc0-80d2-4d89-aa72-1a9e3aa74aa2` | `advocacy-group-use.md` | provisional | draft |
| `7e6a1b34-81a0-488c-a0ee-028098cdfcfe` | `advocacy-participation.md` | provisional | draft |
| `92f668fa-f944-4d03-b3fb-f74c47465fc7` | `advocate-contribution.md` | provisional | draft |
| `ec9d1602-8460-4f04-a4be-d7cf83efcace` | `agency-correction-reporting.md` | provisional | draft |
| `d67b4c7c-78a9-4b79-a054-dc922a255662` | `agency-data-integration.md` | provisional | draft |
| `27232a55-30f1-48f1-90af-2dc19b364e74` | `ai-barrier-identification.md` | provisional | draft |
| `48cfa97a-8651-4f38-8155-dc35489bfd3d` | `ai-curb-ramp-detection.md` | provisional | draft |
| `8ff15f9e-ed6e-42a1-9a0d-63eb33bf1aa0` | `ai-data-risks.md` | provisional | draft |
| `0ed1f849-f07c-442e-a7e6-26d2982e8f16` | `ai-inequity-identification.md` | provisional | draft |
| `daa742f9-501c-4990-b43c-add8b3cf72fd` | `ai-infrastructure-prioritization.md` | provisional | draft |
| `8c2210b2-c64b-467b-89b0-3f48368b41b0` | `ai-sidewalk-quality-estimation.md` | provisional | draft |
| `a54d5d95-8077-44c1-a1b2-b785e8097dfc` | `ai-stewardship-assistance.md` | provisional | draft |
| `8602231a-7020-4aa2-9fed-dcd4725c953e` | `attribute-documentation-location.md` | explanatory | draft |
| `c987db37-06a8-4b20-8cf6-5b55d31ffcd0` | `automated-data-risks.md` | provisional | draft |
| `64e03c3f-b20d-45f7-85a0-e7688e0a9edd` | `automated-system-limitations.md` | provisional | draft |
| `090dc77d-f4ac-43f7-bb3c-24225857d960` | `batch-correction-alternatives.md` | provisional | draft |
| `ad4e92be-7a15-44a4-8459-e60044c44f79` | `bulk-correction-submission.md` | provisional | draft |
| `1fffc62a-9d84-491d-bae5-1cc1a151bc84` | `campus-handling.md` | provisional | draft |
| `4d51a782-12a4-4dce-9b3e-5af77eddb58d` | `capital-planning.md` | provisional | draft |
| `4d60cca7-839b-49e4-a16b-4a15b9fedd03` | `centrality-metrics.md` | provisional | draft |
| `f03df76b-2445-4429-b3ca-79a67850adac` | `common-errors.md` | provisional | draft |
| `e9db4f57-4551-45b9-b3cb-0860768a1995` | `community-comment-review.md` | provisional | draft |
| `620eb711-0340-4863-8500-be9721d59d5c` | `community-correction-contribution.md` | provisional | draft |
| `d3915d99-9fb3-4122-9379-dcbd03323570` | `community-data-quality-checks.md` | provisional | draft |
| `1bd52b2e-4bb4-45e7-94d7-b4d5a7ac13ce` | `community-data-usability.md` | provisional | draft |
| `7891064b-3dd9-49ad-86d8-2c379ba70557` | `community-engagement-pathways.md` | provisional | draft |
| `8f43f17a-589d-4162-8042-8a50307cb4e3` | `community-feedback-use.md` | provisional | draft |
| `5aed9756-7b80-48cb-bd1c-ece21a169164` | `community-gap-identification.md` | provisional | draft |
| `e1eefae0-12d9-4baf-a225-595491602652` | `community-participation-pathways.md` | provisional | draft |
| `6d3e83aa-520c-44aa-9631-5495d022df90` | `community-validation-role.md` | provisional | draft |
| `b315586a-a18c-4266-9557-9e4ea65b6c03` | `completeness-score-interpretation.md` | explanatory | draft |
| `fbd822ed-b006-47fd-9b2a-bb4c38004fd5` | `completeness-vs-ada-compliance.md` | explanatory | draft |
| `ffa7be70-70af-4c81-bbb8-492673feab7d` | `complex-intersection-handling.md` | provisional | draft |
| `62d4ea5a-5198-46a8-9173-b73d957b2de9` | `confidence-measures.md` | provisional | draft |
| `56090dfc-f09d-445c-a3c1-f66a3dd2d564` | `conflicting-data-sources.md` | provisional | draft |
| `f07eaa2e-fd6a-492b-b5b7-b887a6b7f969` | `connectivity-depends-on-geometry.md` | provisional | draft |
| `68b701b9-3be9-4bc9-b338-a7b508b18b44` | `construction-changes.md` | provisional | draft |
| `b36dd30b-5ace-4850-9d20-dc3d440a2eb3` | `context-aware-routing.md` | provisional | draft |
| `27f771b1-961f-4d26-8d1c-65b8e61ed33f` | `coordinate-system.md` | provisional | draft |
| `830aed9e-1c4c-45d3-a8cd-38de1c43ad6c` | `correction-confirmation.md` | explanatory | draft |
| `cfc91197-0cc1-40be-aefb-2d17b8d14c1d` | `correction-propagation.md` | explanatory | draft |
| `45bd57c2-2fd9-49f6-adf5-3dea7ea3c63f` | `correction-release-lag.md` | explanatory | draft |
| `3aa38450-5138-4d14-a9be-bc214534017c` | `correction-tracking.md` | provisional | draft |
| `e41f2f83-5607-4005-b1a5-6c7946ca9b65` | `correction-validation.md` | provisional | draft |
| `da7fe226-a498-4f90-a47c-15439dc0ebbb` | `county-update-coordination.md` | provisional | draft |
| `58a260d4-f5ba-4f2c-84a6-62aa575d2eb5` | `cross-state-lessons.md` | provisional | draft |
| `5f372d9f-4ee7-489f-9c5c-98bd4a1c7c9a` | `crossing-attributes.md` | provisional | draft |
| `1fe0d981-058f-4241-9759-a0ab5cbc68cc` | `crossing-edge.md` | provisional | draft |
| `2c004a6d-ce79-4e97-8e51-32c84268c974` | `crossing-inference.md` | provisional | draft |
| `179b2014-733c-4e95-81c3-1b09412180f1` | `crowdsourcing-role.md` | provisional | draft |
| `ee52131e-e6a2-4a0c-98db-debef5c3ca8d` | `curb-ramp-attributes.md` | provisional | draft |
| `b355ff6e-9002-4dd3-8e87-2ad1bc47f7d6` | `curb-ramp-identification.md` | provisional | draft |
| `b019b1ac-bfa5-458c-b776-2c2d5bf20c35` | `curb-ramp-inventories.md` | provisional | draft |
| `265ccc3d-c792-4575-bea1-84c33513dd9b` | `data-accuracy.md` | provisional | draft |
| `924df6c9-7282-4e8b-9b3a-398ab6c69c41` | `data-collection-history.md` | provisional | draft |
| `ce7f789b-02b5-40ee-9bdd-3c7cf237f2d7` | `data-issue-reporting-requirements.md` | provisional | draft |
| `761bc51e-4fc5-4ced-952c-727fd64f604b` | `data-licensing.md` | provisional | draft |
| `5610997c-6889-4134-b293-d87169d52b1a` | `data-maintenance-challenges.md` | provisional | draft |
| `49fa9f5c-7a74-41d7-bab5-295888e49739` | `data-ownership.md` | provisional | draft |
| `9ff9a145-1ee4-467f-8bcf-748eec5aa2d1` | `dataset-scope-relationships.md` | explanatory | draft |
| `76b63ce5-e9c5-4210-91ed-6d4a882bbc90` | `destination-access-analysis.md` | explanatory | draft |
| `6df61b6e-68f3-45cd-926b-0bec041b0d55` | `disability-community-contribution.md` | provisional | draft |
| `e7ddd218-8c36-41c2-a6dd-42dbb0ea0a10` | `disconnected-dataset-problem.md` | provisional | draft |
| `cadb7b58-ce33-40aa-80d2-c52eef9984a5` | `disconnected-sidewalk-identification.md` | provisional | draft |
| `3ba79203-febb-4d7d-b4fa-94e25820a0fd` | `elevation-routing-effects.md` | provisional | draft |
| `da3560c8-ec34-4a42-97cc-127325c2ca14` | `excluded-infrastructure-types.md` | provisional | draft |
| `9c5bf55e-0e36-4dc5-a060-35e73fe19d46` | `feature-selection-display.md` | explanatory | draft |
| `3d5d5983-3d17-430c-8b34-f2a697e5fa3f` | `field-validation-role.md` | provisional | draft |
| `ba7cac77-2ae7-4f90-a2e1-ce31fdb2e003` | `field-validation.md` | provisional | draft |
| `2333602e-b43f-42b2-8fc6-45ae7ac6a406` | `geographic-coverage.md` | explanatory | draft |
| `9b68c707-1b57-4cb4-81b3-1cf4f4ec5981` | `gis-software-compatibility.md` | provisional | draft |
| `77695777-82fd-4459-b59b-4d96392640e4` | `governance-models.md` | provisional | draft |
| `b0db888e-9aaf-43fc-a061-7ed8e2d48925` | `gtfs-pathways-generation.md` | provisional | draft |
| `8eb9cfce-2b54-4169-93d1-ad14818d26f2` | `human-review.md` | provisional | draft |
| `eb492625-d684-41d7-a7f7-c32c5cf57848` | `imagery-role.md` | provisional | draft |
| `d67eab03-63f0-4b9a-918e-423a4da9496e` | `inaccessible-area-reporting.md` | provisional | draft |
| `c32dabcf-84ae-4926-8d01-fe2906b4b51b` | `included-infrastructure-types.md` | explanatory | draft |
| `68362541-2b15-49b3-a69e-b1269ee5624d` | `incomplete-coverage.md` | provisional | draft |
| `3abda96c-8274-42e4-b3aa-fdcd1a1d7334` | `interoperable-accessibility-ecosystem.md` | provisional | draft |
| `61e3d853-a1d8-42ff-9f71-04c3bd1fd6b0` | `intersection-attributes.md` | explanatory | draft |
| `6512f37c-6152-482b-bdbf-b5ae2cfc3aaa` | `issue-report-auto-update.md` | explanatory | draft |
| `2a8ae450-c65f-460e-bdb4-619453e3cdff` | `issue-report-follow-up.md` | provisional | draft |
| `ad82a900-a7c1-4e9c-9119-cc151f415050` | `issue-report-reviewers.md` | provisional | draft |
| `be8f2ba6-b3b9-4201-a17a-19e38f831039` | `jurisdiction-data-disputes.md` | provisional | draft |
| `c37e25a8-9fbd-49f6-ba01-f789724b45d9` | `jurisdiction-engagement-pathways.md` | provisional | draft |
| `e5d9dbdc-d4e9-484e-a45a-0fe0593aedea` | `jurisdiction-participation-pathways.md` | provisional | draft |
| `64dc8b8a-f5d8-4b56-b04b-d01415ceb55e` | `jurisdiction-stewardship.md` | provisional | draft |
| `9ff8fc54-273d-48cf-ba60-fb98104776aa` | `jurisdiction-update-maintenance.md` | provisional | draft |
| `7fe3f0e7-c8b0-4f4c-940b-9dd5a0bba0e1` | `lived-experience-importance.md` | provisional | draft |
| `0508b8ef-ebf5-49b4-8bc5-2af63e5f8865` | `local-data-validation.md` | provisional | draft |
| `1ec8adec-109e-49f1-8616-5210ad391824` | `local-vs-statewide-coordination.md` | provisional | draft |
| `eac8f05c-5246-4578-a110-0e13bf867315` | `long-term-maintenance-workflows.md` | provisional | draft |
| `3fd751b9-78a3-41e7-a1e4-4893dd6b63b8` | `long-term-stewardship-requirements.md` | provisional | draft |
| `d1ee6b3e-f828-47d5-a425-aa90cb654571` | `long-term-stewardship-responsibility.md` | provisional | draft |
| `4e468dc8-b2d6-48b9-be4b-1b6adbcdc8ab` | `machine-learning-role.md` | provisional | draft |
| `a94dd009-ca0d-4125-958f-7652a38ef00a` | `major-event-accessibility-planning.md` | provisional | draft |
| `396d6ae7-2c4b-49b9-8f7a-3994d12419a5` | `manual-wheelchair-profile.md` | provisional | draft |
| `242f493f-0fb0-404a-b58d-7690d537cc36` | `map-color-legend.md` | explanatory | draft |
| `092fb787-d775-47de-8c42-4feed6a809e0` | `map-layers.md` | explanatory | draft |
| `0281fc64-1dd1-4d4d-9e6e-26ee18965d56` | `mapper-training-materials.md` | provisional | draft |
| `bffc17e0-c79f-406f-bdbb-25194b453cec` | `mapping-prioritization.md` | provisional | draft |
| `62fbf213-1caf-4f95-bd72-6d71a01e398d` | `mapwithai-workflow-history.md` | provisional | draft |
| `54a5848f-4c28-426c-b6d1-1537aa4bf176` | `maximum-travel-cost.md` | provisional | draft |
| `f2aee116-0fb5-4195-92e1-29f4d4db5676` | `missing-accessibility-information.md` | provisional | draft |
| `95748c61-3f42-4832-823b-57835ad89373` | `missing-attribute-values.md` | provisional | draft |
| `47cc35c9-6a27-4f47-9732-aa9b8b72d1bf` | `missing-infrastructure-identification.md` | provisional | draft |
| `5ad5f1fd-e04c-4630-bcdd-d2f4d7245c40` | `missing-street-names-for-vendors.md` | provisional | draft |
| `edb1133a-11db-4a42-b17a-41d393613679` | `mobility-equity.md` | provisional | draft |
| `47d7c127-dabc-453c-a941-24bf1dcac011` | `mobility-justice.md` | provisional | draft |
| `54fcc426-25e1-4a16-b945-c08d32ca047b` | `mpo-contribution.md` | provisional | draft |
| `774d0238-f738-4664-8f1b-cadab006d4f1` | `mpo-role.md` | provisional | draft |
| `943f4923-0113-4a90-8edf-8a3c3b86e9e2` | `multimodal-accessibility-analysis.md` | provisional | draft |
| `a73a4561-b981-4a0b-8bbb-62fcca8a5fda` | `national-data-standards-evolution.md` | provisional | draft |
| `7cebb5c5-439a-4990-8b96-e0fa7fc927a2` | `nationwide-system-requirements.md` | provisional | draft |
| `a24fe128-a93a-4e32-aa4c-8dd487ce10fc` | `node-vs-edge.md` | provisional | draft |
| `a3dcbade-e2fc-4bba-a848-2d55efe82c31` | `nondriver-mobility.md` | provisional | draft |
| `b7ddfa2d-1dce-4fb3-a8da-d9db9a6adfcf` | `older-adult-contribution.md` | provisional | draft |
| `c15212b0-af18-46b4-adac-5de6f1d69020` | `open-source-community-role.md` | provisional | draft |
| `ce864ce8-26a4-454c-aa0c-6b563897d841` | `opensidewalks-community-mapping-groups.md` | provisional | draft |
| `92f378ce-2543-4b85-a08c-79f5e0f9e273` | `opensidewalks-schema-usage.md` | provisional | draft |
| `eaf1c9f6-5412-4b89-b882-f0e30fd55bc9` | `opensidewalks-schema.md` | provisional | draft |
| `ee0868ad-458c-47df-8707-a53196198634` | `opensidewalks.md` | provisional | draft |
| `52a781fe-94d4-42af-b01a-4503f683722d` | `operational-agency-use.md` | provisional | draft |
| `27717844-0f20-413d-8182-5a88fc0e5e09` | `os-connect-local-gis-relationship.md` | provisional | draft |
| `f3b4a358-1bfd-4f6e-bb33-da9b6f33d439` | `os-connect-maintenance.md` | provisional | draft |
| `88440307-f7af-4247-a8a7-7c71f3eb1458` | `os-connect-origin.md` | provisional | draft |
| `c21a0c67-75a1-4663-9e65-3ca693961003` | `os-connect-problem-statement.md` | provisional | draft |
| `dac3f116-f11f-4219-8113-8b1bb774028b` | `os-connect-tdei-relationship.md` | provisional | draft |
| `54c23042-73cf-47f7-ad0e-61480547f66a` | `os-connect-vs-openstreetmap.md` | provisional | draft |
| `8405961e-1ad1-4bc6-98f5-2b90113583f2` | `os-connect-vs-traditional-inventories.md` | provisional | draft |
| `90b52cda-ebcb-482f-bc5e-8aedb7af6b9b` | `os-connect.md` | explanatory | draft |
| `846c4905-d117-41b5-a6b0-51c3d3b23425` | `outdated-data-handling.md` | provisional | draft |
| `f487edfc-238c-439e-85ad-17865ee31fc1` | `outdated-imagery.md` | explanatory | draft |
| `1c3114bf-e872-4583-9691-c301a71afe92` | `participatory-accessibility-mapping.md` | provisional | draft |
| `a52bbd90-1aa8-4c84-a2ab-80dc44c78608` | `participatory-mapping.md` | provisional | draft |
| `6c3dbfbc-c161-4267-9b0e-4b2ca738d1da` | `partnership-needs.md` | provisional | draft |
| `f9b4d35c-e819-49a4-8706-cc3b6cb8ad90` | `pedestrian-data-complexity.md` | provisional | draft |
| `caf1b4b5-8dd9-4d0d-bd93-fb85b4e6e197` | `pedestrian-equity.md` | provisional | draft |
| `38b7ff04-8d36-486c-9344-48ef4cf6dbe7` | `pedestrian-feature-attributes.md` | provisional | draft |
| `4f56673b-8bfa-4e62-8d11-639e032b9113` | `pedestrian-only-facilities.md` | provisional | draft |
| `0ad4d063-a9c4-4e0a-8b43-fcd5384d8294` | `planned-capabilities.md` | provisional | draft |
| `a2bf3ef7-dd39-4aef-8035-5058744b6990` | `planner-data-validation.md` | provisional | draft |
| `22396853-14eb-48a6-be82-3bbe5b097778` | `planning-with-known-errors.md` | provisional | draft |
| `04eb0575-86dc-4025-baf1-0c695a68422b` | `poi-grouping-rationale.md` | provisional | draft |
| `2e163f92-be0b-435c-8cfd-5641376adaf2` | `post-collection-next-steps.md` | provisional | draft |
| `3a06837e-1c3a-4d0c-b259-41b93c38141b` | `private-facilities.md` | provisional | draft |
| `45fa3b5b-e4a8-4328-9311-2162067353de` | `public-data-value.md` | provisional | draft |
| `01d76520-3c35-4baf-aedf-b2e77fcba439` | `qa-qc-report-infrastructure.md` | provisional | draft |
| `9b05cee8-585e-401e-a8fe-c37b92c2ee26` | `qa-qc-report.md` | explanatory | draft |
| `b06a1417-5d3a-4b23-95a5-77e23443700f` | `recommended-sidewalk-tagging-pattern.md` | provisional | draft |
| `b8f496f9-4435-45fb-89cc-13c8343a8ef2` | `reportable-errors.md` | explanatory | draft |
| `ef725be9-e85f-4cd3-af0c-dd005d722749` | `required-vs-recommended-attributes.md` | provisional | draft |
| `f255535a-83b8-4743-9dde-096b80f28b07` | `resident-participation.md` | provisional | draft |
| `c9b0897b-7cbf-4960-9d82-3718a746de3c` | `routable-graph.md` | provisional | draft |
| `43bf6e40-901a-44e0-b14e-b9bd54cd4b5c` | `routing-assumptions.md` | provisional | draft |
| `342f1749-8884-4cbe-ae38-8eabbc15fec0` | `routing-personalization.md` | provisional | draft |
| `a1bed4a4-289b-41e0-a1a1-a5f1f967574c` | `rural-area-handling.md` | provisional | draft |
| `6ad1ab6f-e8a3-4a48-88af-e66326b423d4` | `rural-community-participation.md` | provisional | draft |
| `6060f162-9b96-4b19-8764-587fde2e514f` | `safe-routes-to-school.md` | provisional | draft |
| `51b2cfc9-56d3-427e-8e16-310070ed8484` | `safety-improvement.md` | provisional | draft |
| `b20de641-6da6-4ded-b663-f5e67727cc1a` | `school-participation.md` | provisional | draft |
| `da501179-baf0-4c40-a8be-6d50687de676` | `separated-sidewalk-mapping.md` | provisional | draft |
| `10a4708c-5ece-46ab-b511-c220de8c2a2b` | `service-planning.md` | provisional | draft |
| `4d328378-d4be-418a-a4c0-22eff37413bf` | `sidewalk-attributes.md` | provisional | draft |
| `15b469c9-2470-40fa-aa5c-fbeb441f07d9` | `sidewalk-disconnection-causes.md` | explanatory | draft |
| `d0f7f947-33ef-420c-9cc3-fc09156dcf9a` | `sidewalk-street-name-association.md` | provisional | draft |
| `004a0171-bb78-4b92-9f71-5a3fca439241` | `state-stewardship-role.md` | provisional | draft |
| `3d4cb083-1340-41cd-8957-faaccc0c42ff` | `statewide-data-importance.md` | provisional | draft |
| `cced324f-5797-404d-b0bd-4fd6f2731804` | `statewide-inventory.md` | explanatory | draft |
| `3a031f0e-9abd-466d-955d-ae93abf18662` | `stewardship-roles.md` | provisional | draft |
| `58e7cffe-f98d-43b3-be75-a6cbabb43df6` | `stewardship-sustainability.md` | provisional | draft |
| `7cebe688-abf2-4af2-9a99-9eb932eb4ab1` | `street-name-routing-importance.md` | provisional | draft |
| `f8e12f00-6b83-4cb2-bacc-35f019d8a973` | `street-name-tags-for-routing.md` | provisional | draft |
| `a18f0418-5032-46cb-a66e-8576e1f3ab5b` | `street-name-vs-is-sidepath-of-name.md` | explanatory | draft |
| `dbd66d49-8f9d-4a2f-811d-0d1a6e088a8f` | `surface-attribute.md` | provisional | draft |
| `90764228-e2ec-41cb-86be-93453bee64bb` | `tcat-mapping-project-support.md` | provisional | draft |
| `761bb617-3bdc-446c-913b-f6bd947c8e20` | `trail-handling.md` | provisional | draft |
| `9e051cf8-3725-4a62-bb5f-56a8ab4a54f1` | `transit-accessibility-analysis.md` | provisional | draft |
| `a7a50dbd-0760-4db2-9708-b274e2577189` | `transit-agency-contribution.md` | provisional | draft |
| `433d273a-a75d-42fd-a1f5-9bc1616ed4ce` | `transit-pedestrian-integration.md` | provisional | draft |
| `83dbd606-5bbd-4f0b-b967-f7520ce106f4` | `university-role.md` | provisional | draft |
| `14e0aae1-0251-4666-aeb1-154f57468a1d` | `unreachable-destinations.md` | provisional | draft |
| `0af27286-0738-49c3-a28e-1a424e7b79ea` | `update-cadence.md` | provisional | draft |
| `7b39a3d7-1193-4cb8-a205-92e6c717bb79` | `update-responsibility.md` | provisional | draft |
| `8a2fe76d-fa50-4ffc-8682-f31a95573410` | `urban-map-density.md` | provisional | draft |
| `1e703514-e4ab-40c9-b95b-f5e7cbb76422` | `urgent-correction-process.md` | provisional | draft |
| `efb382c5-369d-45a0-984f-2b8bd0e66ce5` | `viewer-overview.md` | explanatory | draft |
| `50988705-d705-4cf7-9d9b-3f42941e669b` | `viewer-vs-tdei-portal.md` | explanatory | draft |
| `8fc4f4a9-d207-4716-97b1-c809579bfb06` | `vision-zero.md` | provisional | draft |
| `b44fe9ec-972c-4f09-b00d-add4fcb35b9f` | `volunteer-data-contribution.md` | provisional | draft |
| `76e2b202-4641-46ad-b829-3454ef49125e` | `walkshed-advocacy.md` | provisional | draft |
| `cffc1c3d-00dc-4c9f-bec9-7e076dfa2eb7` | `walkshed-metrics.md` | explanatory | draft |
| `680def2a-5e3b-40f2-b33c-018a5c7010f4` | `washington-lessons.md` | provisional | stub |
| `07b716b4-105a-4db8-ac21-63d4f938cb4c` | `width-attribute.md` | provisional | stub |
| `7fb805f0-385d-49e0-8db2-26917817853f` | `workflow-improvement-areas.md` | provisional | stub |
| `eee83492-a21e-4dd3-b964-e617211ac70a` | `z-score-usage.md` | provisional | stub |

### Workflows

Base: `assistant/os-connect/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `8b10916c-8d15-40df-bb2a-78c07c2f2dd9` | `bus-stop-planning.md` | explanatory | draft |
| `afb34589-73d9-43b8-9ba6-a9450856969f` | `connect-to-gis.md` | provisional | stub |
| `649758af-178c-47be-9aed-32ba3c26f8ce` | `download-data.md` | explanatory | draft |
| `adeefd4e-94b5-4a1a-b82d-9e66e8b957ca` | `import-into-arcgis.md` | provisional | draft |
| `7260f5de-9bb2-4927-a5ea-9873bad6c3e9` | `report-connectivity-data-error.md` | provisional | draft |
| `53b4bb91-cc44-4ef5-b0b0-1b78b3c5a2eb` | `report-data-error.md` | explanatory | draft |
| `46721490-e839-43c1-ab02-aaf60e9e6e28` | `search-for-jurisdiction.md` | explanatory | draft |
| `d0ab91b6-e1a1-4cff-93e0-280a250ad81f` | `support-pedestrian-access-analysis-around-destinations.md` | explanatory | draft |

## QA/QC — Assistant Knowledge Base

See [qa-qc/index.md](qa-qc/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/qa-qc/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `19b860bf-74a1-4b1e-8d99-c4e8bd164799` | `index.md` | provisional | stub |

### Concepts

Base: `assistant/qa-qc/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `48d0ded2-e1d3-4caa-ad78-40041fd7e4d9` | `accessibility-island.md` | provisional | draft |
| `b4f6542d-8213-45af-9c68-667e93204aa2` | `attribute-completeness.md` | provisional | draft |
| `6d618115-a9d1-4ce0-9c72-ac4751cd4dc8` | `attribute-presence-vs-feature-completeness.md` | provisional | draft |
| `f414b8c1-23ef-439b-9e03-1187a8729fe2` | `before-after-walkshed-analysis.md` | provisional | draft |
| `2932c97d-2f41-488f-9054-1e864aeb1f97` | `bottleneck-hotspots.md` | provisional | draft |
| `9f0b255e-efe7-4ec0-9b9a-1849737b6a32` | `centrality-and-redundancy.md` | provisional | draft |
| `744a45ba-57f1-42fa-91cd-613ea8fac55f` | `centrality-metric-selection.md` | provisional | draft |
| `55cb2e2e-cb93-439c-8d4d-87d2addcfdc5` | `centrality-sampling-and-repeatability.md` | provisional | draft |
| `d1ecde27-33de-4b5b-9c5f-028e285625aa` | `centrality-tile-generation.md` | provisional | draft |
| `c09dafa2-2267-4971-96ef-d2fbb0143512` | `centrality.md` | explanatory | draft |
| `43f6971e-3cf4-47fb-a478-dcfa3b48ac5c` | `completeness-vs-accessibility-gaps.md` | provisional | draft |
| `eb60de21-6057-4771-bb60-a7fad9347e70` | `completeness-vs-ada-compliance.md` | explanatory | draft |
| `249155de-ed2a-4276-8ea3-004d4ce9128e` | `completeness.md` | explanatory | draft |
| `e0820a0e-84c0-4e38-99b6-bab0c16e2fa3` | `conditional-attribute-completeness.md` | provisional | draft |
| `38218e1c-5ab1-4817-971a-64240e1574fb` | `connected-pedestrian-graph.md` | provisional | draft |
| `e1199eaf-c060-41f3-bed8-259828b12cd3` | `crossing-count.md` | provisional | draft |
| `9dff609a-ac96-4dcb-805c-0f08e85a97c3` | `curb-completeness-metrics.md` | provisional | draft |
| `76ce1628-3c14-498b-aa1b-e52a895c9bc8` | `degree-centrality.md` | provisional | draft |
| `6f55f03d-8170-4c6e-998a-6142fe78dcf8` | `disconnected-poi.md` | provisional | draft |
| `ebf0cec2-a43f-4618-9d34-04b933aea3f5` | `edge-betweenness-centrality.md` | provisional | draft |
| `ab66f715-c718-4395-807f-f10e49c59bc6` | `edge-betweenness-operational-use.md` | provisional | draft |
| `79f77bc9-75ed-4b0d-8d0f-7b862a0ede07` | `edge-betweenness.md` | explanatory | draft |
| `a2a8ad51-f405-4ee8-8d59-bab4d0b2734f` | `eigenvector-centrality-display.md` | provisional | draft |
| `df77fa55-34b8-4c10-adc8-f3d60260e843` | `eigenvector-centrality-interpretation.md` | provisional | draft |
| `bec67c43-7e58-40ef-a719-bcc2f6615978` | `eigenvector-centrality-network-importance.md` | provisional | draft |
| `9f5f6817-bd7b-40a5-a5b7-d25b92d659f9` | `eigenvector-centrality.md` | explanatory | draft |
| `5f380c2d-e4a1-4a33-8bcd-f2edcd9410ee` | `field-verification-hotspots.md` | provisional | draft |
| `3ed1d499-4963-42c9-aa45-c4398c3d4b86` | `intersection-quality-metric.md` | provisional | draft |
| `0051ed26-3fe9-4843-8b4c-f3d246a6697b` | `intersection-tile.md` | provisional | draft |
| `4e05661f-70ab-473d-a633-97a58bf74de5` | `local-poi-corrections.md` | provisional | draft |
| `e7dcb5dd-2c65-47b2-8860-2a1fb592b9cc` | `log-normalized-value.md` | provisional | draft |
| `80590023-aa2e-4493-8c2f-26d33f8523dc` | `metric-boundaries.md` | provisional | draft |
| `dae21759-1cff-45bc-8522-ef8afafd0c30` | `metric-coverage-and-interpretation.md` | provisional | draft |
| `c30bbc0d-7dc4-4fa9-82f6-84f15b0fd04b` | `node-betweenness-centrality-operational-use.md` | explanatory | draft |
| `29e2f22b-4a69-417c-a0c5-29680ed3fe8f` | `node-betweenness-centrality.md` | provisional | draft |
| `bda69ac6-291c-474e-a1d0-71baf313f541` | `node-betweenness-operational-use.md` | provisional | draft |
| `6752b665-953f-4cd7-a757-21c171ab32fe` | `normalized-value.md` | provisional | draft |
| `5361e22e-1eff-41f7-aa38-1d7962b66303` | `path-count.md` | explanatory | draft |
| `d704d6df-2a85-464a-940a-a29189410d26` | `poi-density-and-prioritization.md` | provisional | draft |
| `e67aabd4-96fb-441a-9e14-0c1eeb86503c` | `poi-density.md` | provisional | draft |
| `6771e2e0-eff4-4ec8-b5a6-95a40053c950` | `point-of-interest-sources.md` | provisional | draft |
| `ef6ebe5e-10f0-4220-a545-cf10131491fb` | `presence-percent.md` | provisional | draft |
| `21312609-bb45-4d65-9492-6c37a6ac9cd4` | `project-completeness-standard.md` | provisional | draft |
| `b8b24c38-967e-4995-bb5e-6d9758bbe29f` | `project-completeness-vs-ada-compliance.md` | provisional | draft |
| `00ad81f4-9bb8-472c-9e78-de21a7adc298` | `projection-for-walkshed-lengths.md` | provisional | draft |
| `a92a193e-5517-4740-a788-9aed1146f823` | `qa-qc-analysis-limitations.md` | provisional | draft |
| `93884632-e918-41fb-94f1-66ce2e1dd2d9` | `qa-qc-limitations.md` | explanatory | draft |
| `72a3f427-34f6-40f1-866c-c618a29e28cd` | `qa-qc-visual-accessibility.md` | provisional | draft |
| `d5f1ad9f-0a8b-4586-bcfe-980430abc088` | `quality-metrics-and-local-priorities.md` | provisional | draft |
| `049313cd-c906-4878-b495-56590c5fc81b` | `quality-scoring-boundaries.md` | provisional | draft |
| `609531ff-60a8-48ca-a3ba-3650998f038e` | `report-data-sources.md` | provisional | draft |
| `0f57f435-7da0-42f0-b876-fb32ffc6ff31` | `report-feature-counts-and-lengths.md` | provisional | draft |
| `b0e449f3-b7bc-4c50-a3d1-4a887d6c8108` | `report-glossary.md` | provisional | draft |
| `77a9a7e4-6462-4f8d-8eaf-68f1c0b5c62c` | `report-map-interpretation.md` | provisional | draft |
| `d99c51e4-adc0-44dc-9068-a7729475a2ed` | `report-provenance.md` | provisional | draft |
| `cb61e0fd-f44f-4549-8d2d-b392de487edc` | `report-purpose-and-limitations.md` | provisional | draft |
| `c079a4b4-c8a8-4bca-acfc-ccc144208c6c` | `report-question-sections.md` | provisional | draft |
| `8f452b12-145a-488c-b92c-505992797c25` | `report-scope-by-jurisdiction.md` | provisional | draft |
| `44e7cf77-c4f6-4911-97bb-8cd20f26c76c` | `small-dataset-limitations.md` | explanatory | draft |
| `23396803-7d80-4bc6-b902-66a8cc90c07e` | `task-grid-overlays.md` | provisional | draft |
| `76f824a9-e59e-40fa-8f1b-26465b547a23` | `traversability.md` | provisional | draft |
| `22d1cd80-e62e-4a6a-9325-3accbdbf0fe2` | `walkshed-profile-assumptions.md` | provisional | draft |
| `a6047a48-8d1f-43a9-b60b-49a50565b2cf` | `walkshed-profile-comparison.md` | provisional | draft |
| `fc8b8686-ebe5-4af3-9c9a-8fc0648a68b2` | `z-score.md` | provisional | draft |

### Workflows

Base: `assistant/qa-qc/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `649ba898-e1da-4865-bda0-58f75f14a185` | `identify-accessibility-islands.md` | provisional | draft |
| `76d768a3-0d9d-40aa-adb2-715e6791971d` | `interpret-report-sections.md` | provisional | draft |
| `30f9a280-d113-4e12-aed0-81346a500dc7` | `use-report-for-ada-planning.md` | provisional | draft |

## Rapid — Assistant Knowledge Base

See [rapid/index.md](rapid/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/rapid/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `26f6b603-638f-4077-a878-7fd44ae9bd3e` | `index.md` | provisional | stub |

### Concepts

Base: `assistant/rapid/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `17911acf-f9c0-489c-99e5-612a869e2ec1` | `rapid.md` | provisional | draft |

### Workflows

Base: `assistant/rapid/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `92f3af12-0ecd-4ea0-8bba-b941b5384fc4` | `add-sidewalk-using-rapid.md` | provisional | draft |

## Support — Assistant Knowledge Base

See [support/index.md](support/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/support/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `ad27a23d-1df1-40d3-9821-239e49b50fb1` | `index.md` | explanatory | draft |

### Concepts

Base: `assistant/support/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `cd4672b1-8311-48a3-9e31-8ce1eb39d3c8` | `accessmap-vs-walksheds.md` | provisional | draft |
| `1c93065d-884d-497c-9094-f6c8cf04c05a` | `cross-team-followup-ownership.md` | provisional | draft |
| `3c0f0798-5ea9-47f4-b513-1a5fc67b595e` | `data-citation.md` | provisional | draft |
| `29bd9af0-db16-4051-bbc2-46a422ce802b` | `dataset-authority.md` | provisional | draft |
| `6a494c93-24a2-4b28-93a3-3a4d00f271e3` | `ecosystem-overview.md` | provisional | draft |
| `07559100-b9f0-4a58-af67-e55e76e023bc` | `fallback-when-gtfs-pathways-missing.md` | provisional | draft |
| `8df6683d-2df1-4a8f-9730-f7ecee12ac21` | `gtfs-pathways-agency-adoption.md` | provisional | draft |
| `8a4df597-73e5-41af-ae42-36ba4c384462` | `mappy-hours-eligibility.md` | provisional | draft |
| `1e14fcc7-d6db-46c4-9337-5e85f4e26877` | `opensidewalks-contact.md` | provisional | draft |
| `cca616b4-1f0a-4e0f-9d0c-38a4ed5631ee` | `os-connect-contact.md` | provisional | draft |
| `2669c8bd-2d2f-4e33-8d73-5d94608c9c87` | `osm-pedestrian-paths-vs-gtfs-pathways.md` | explanatory | draft |
| `ab86795c-ddcf-470a-b6d4-53526f845563` | `partner-response-time.md` | provisional | draft |
| `a3b3c062-7cfd-463c-8fb4-938f676a1658` | `staff-email-antipatterns.md` | provisional | draft |
| `09b1b059-d611-493e-a190-028c10c19f39` | `tdei-contact.md` | provisional | draft |
| `38d55e6e-a248-4c4b-86bc-1b0dc6df5f5e` | `tdei-os-connect-osm-differences.md` | explanatory | draft |

### Workflows

Base: `assistant/support/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `44ccb544-3622-467f-99ea-ac6b625431b1` | `check-gtfs-feed-pathways.md` | explanatory | draft |
| `af7c583d-5c7d-4b29-9849-a78661e61f1d` | `choose-dataset-for-arcgis.md` | provisional | draft |
| `601d1ddd-d691-4920-be36-72edff5cf8d7` | `choose-dataset-for-planning.md` | explanatory | draft |
| `4ea96d70-febf-4aaa-ab71-51a3eeea5fc0` | `choose-dataset-for-transit-stations.md` | explanatory | draft |
| `88c28d2e-8fc5-44fb-a3c5-5b3faf4df6f0` | `communicate-uncertainty.md` | provisional | draft |
| `c3df9637-60e9-4545-ae08-b0de0add9e9b` | `frame-future-plans.md` | provisional | draft |
| `f521edbe-b906-43a4-8d1b-bafefdf07e87` | `handle-unknown-questions.md` | provisional | draft |
| `1ba10def-777c-47ee-961d-44be6dd77dfd` | `internal-verification-language.md` | provisional | draft |
| `1c2bf19e-bde6-4823-8f3f-8af050c00fbd` | `introduce-related-tools.md` | provisional | draft |
| `e4bf19a2-eb7f-465f-b72c-c9f8242dc908` | `mappy-hours-referral-decision.md` | provisional | draft |

## TDEI — Assistant Knowledge Base

See [tdei/index.md](tdei/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/tdei/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `15c65282-0552-4aac-a7ac-9957cac9db20` | `index.md` | explanatory | draft |

### Concepts

Base: `assistant/tdei/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `adcb3345-4dae-4681-99c5-ddf262e0e7b7` | `api-key-rotation.md` | provisional | draft |
| `b47df565-7d16-4150-9857-39e68e12b46c` | `dataset-download-formats.md` | provisional | draft |
| `8adca011-89a3-49ac-9002-280a5c0f3f72` | `dataset-identifier.md` | provisional | draft |
| `4ec42c15-7528-4644-a1e9-1e5ec43d3720` | `dataset-level-vs-feature-level-operations.md` | provisional | draft |
| `9d80a5db-2a2e-4bdb-aa06-f27603751309` | `dataset-purpose-and-representation.md` | provisional | draft |
| `128a6560-54af-4ded-a1ec-6327d5aa0776` | `dataset-version-selection.md` | provisional | draft |
| `86d1356e-dcdf-4bbf-bd0e-a5e40b791e4b` | `dataset-visibility.md` | provisional | draft |
| `04fb07d2-c424-492d-9f70-f5f6fb4a4964` | `derived-dataset-lineage.md` | provisional | draft |
| `f9b4f5c5-d76d-4f3b-ac23-8d529e9722eb` | `environment-separation.md` | provisional | draft |
| `2fa3f991-fa78-4c2a-9ed1-0ffaf2d53496` | `external-attribute-release.md` | provisional | draft |
| `9c54d0a1-aea5-4998-9733-00d610cc1082` | `feedback-management.md` | provisional | draft |
| `23fb35f9-dba9-47b9-a160-8057c18a334d` | `file-formats.md` | explanatory | draft |
| `ad85460d-4e34-4025-9a31-754fa1b493e5` | `interoperability.md` | provisional | draft |
| `4195411a-cf4f-4713-b93e-ff79201e1139` | `interval-survey-points.md` | provisional | draft |
| `d2a3b103-8781-44ca-94e7-c3d1f94c77af` | `job-confidence-calculation.md` | provisional | draft |
| `23a0f1d2-a994-4cce-b14c-9a9979b69e0b` | `job-dataset-tag-road.md` | provisional | draft |
| `fe02cb42-0751-4abe-b56c-96217e9ae38d` | `job-dataset-union.md` | provisional | draft |
| `4cd25d97-67f4-4402-9dd9-602439f2226b` | `job-filter-dataset-by-bbox.md` | provisional | draft |
| `13f6c690-3fcb-4b8b-b0c3-217615339d79` | `job-flex-validate.md` | provisional | draft |
| `84cafed7-b46f-4a51-8579-343d18ace865` | `job-osw-convert.md` | provisional | draft |
| `e9be970d-e4ec-46e2-b13d-b38d9be90cb8` | `job-osw-validate.md` | provisional | draft |
| `ddce0105-39d5-4be4-989b-dcd61c15a764` | `job-pathways-validate.md` | provisional | draft |
| `e58ba68a-f221-4b21-b27b-367364ad998f` | `job-processing.md` | provisional | draft |
| `59b2f8e1-926e-4db6-a74c-bf43d1afe497` | `job-quality-metric-ixn.md` | provisional | draft |
| `ecc403bc-f209-4462-81bf-6ff233e26e39` | `job-quality-metric-tag.md` | provisional | draft |
| `00fa9841-8866-4e62-b655-11716bb0a426` | `job-spatial-join.md` | provisional | draft |
| `065a1945-3801-4b06-b375-8b44ab3420df` | `jurisdiction-dataset-coverage.md` | provisional | draft |
| `3ad36cf1-e63b-45d4-bf90-8a01ccdb5c10` | `mislabeled-dataset-handling.md` | provisional | draft |
| `a1109474-79ad-407c-a0dd-6e825b2ee77d` | `osw-download-contents.md` | provisional | draft |
| `d585bbf0-0b3b-43b7-95cb-b0989c1a4adb` | `osw-edges-and-nodes.md` | provisional | draft |
| `9790a0aa-44c3-428f-9b63-725de5754178` | `osw-vs-osm-format.md` | provisional | draft |
| `8c844f20-7875-40e4-a212-efe0a43de9fc` | `portal-dashboard.md` | provisional | draft |
| `d01ee31b-99ae-4050-91eb-ba27388433d7` | `project-group-roles.md` | provisional | draft |
| `c3b02f8d-955d-4d16-9107-826eb20a5176` | `project-group.md` | explanatory | draft |
| `22bff919-f050-43c0-9437-934d1ead9b49` | `release-versioning.md` | provisional | draft |
| `b84cac68-2b22-4e03-b4fb-f23caf74cff7` | `released-dataset-viewer.md` | provisional | draft |
| `c1c7fc8a-5511-43c8-a443-9716fa0878fe` | `released-dataset.md` | provisional | draft |
| `9255d973-6c1f-4557-8fc2-5e08b596dbd1` | `services-and-project-groups.md` | provisional | draft |
| `c0eb0525-d8cd-46c7-b935-2e354d07d171` | `source-and-derivative-datasets.md` | explanatory | draft |
| `9209b586-859c-43ff-b606-4b60ebfe9f0f` | `tdei-architecture.md` | provisional | draft |
| `090b5c65-73c9-4883-b7a7-b1aea5bd1d1b` | `tdei-data-security.md` | explanatory | draft |
| `819491bf-e7a8-478f-a6f0-53dc22ddd70b` | `tdei-job-processing.md` | provisional | draft |
| `6c3e53f6-6b7b-46f8-ab45-c164b8e5b29d` | `tdei-services.md` | provisional | draft |
| `08caed9b-c4f5-4693-b7a8-b7ea5373b764` | `tdei.md` | provisional | draft |
| `e2515fea-42fe-46dc-9d80-5cd5d7dc9d00` | `test-dataset-in-portal.md` | provisional | draft |

### Workflows

Base: `assistant/tdei/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `74fe06aa-3fee-40b3-8cb2-42b47b759e1d` | `access-tdei-api.md` | explanatory | draft |
| `dba68e63-4e82-41fe-96d9-167bf339fc15` | `check-dataset-currency.md` | explanatory | draft |
| `7b4fada3-5e37-4f79-9d59-556c0c06e557` | `check-project-group-membership.md` | explanatory | draft |
| `ca7a59e1-632d-4b7c-9aab-ef546332432b` | `conflate-jurisdiction-datasets.md` | provisional | draft |
| `db0d350e-7fb2-4f3d-a2b1-cfae0cd7fe24` | `convert-geodatabase-to-osw-data.md` | provisional | draft |
| `1f05899c-d9d0-4e75-928d-5f8697e65bcd` | `convert-osm-pbf-to-osw.md` | provisional | draft |
| `bced88f8-c0e9-482b-b594-abf7a4c47568` | `create-and-monitor-tdei-job.md` | provisional | draft |
| `49566ad0-966c-4d97-9e94-5bb7189d87b8` | `download-data.md` | explanatory | draft |
| `49d10064-29ce-4bd2-9646-90f345a493d6` | `download-os-connect-data.md` | official | draft |
| `f58de4ae-f2bf-4127-965b-e87a722304fb` | `download-os-connect-dataset.md` | provisional | draft |
| `d463bc73-51b5-44fe-8d69-526e6e30073e` | `integrate-external-geospatial-data.md` | explanatory | draft |
| `7cd47b84-24f2-470a-85ac-00d0feccd8e7` | `register-and-verify-tdei-account.md` | provisional | draft |
| `2f5db433-6544-4136-96a5-fa942974071e` | `use-tdei-portal.md` | explanatory | draft |
| `ed28e643-f9d8-41a7-8ec8-a17e2e63f961` | `validate-osw-dataset.md` | provisional | draft |

## Walksheds — Assistant Knowledge Base

See [walksheds/index.md](walksheds/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/walksheds/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `8afcc669-4e71-4a78-b9aa-e466bd35864d` | `index.md` | explanatory | draft |

### Concepts

Base: `assistant/walksheds/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `4f085a5e-3697-406a-9843-c50d50cdbfff` | `accessibility-islands.md` | provisional | draft |
| `9c530c4a-670b-46a5-bd2d-8504935e8164` | `accessibility-profile-inequity-analysis.md` | explanatory | draft |
| `139abb8e-9218-4513-973c-152117c20ac1` | `accessibility-profiles.md` | explanatory | draft |
| `7d1b1fd4-e720-4f22-8445-9d8c7951c056` | `accuracy-vs-straight-line.md` | provisional | draft |
| `a59f0af7-b198-4b0b-929d-8a56f1bae778` | `ada-planning.md` | provisional | draft |
| `5a78449e-ba9e-46a1-a7ba-e5669ebb7ebd` | `barrier-incorporation.md` | provisional | draft |
| `7f013105-7dea-432b-b72a-59d1f96a7b5b` | `before-after-comparison.md` | provisional | draft |
| `f1a0e5a3-6d32-44cb-8de3-d50ddefcfb56` | `bus-stop-access-analysis.md` | explanatory | draft |
| `140863cc-7ade-4fca-9ca7-549e8c792d52` | `complete-streets-planning.md` | provisional | draft |
| `4e6b7150-c8ab-4db7-bc67-3b69eb737ff1` | `crossing-effects.md` | provisional | draft |
| `75f20d9a-5236-41b7-a7f3-c0e72248efbe` | `crossing-gap-identification.md` | provisional | draft |
| `5489d6d2-92bd-46e8-97d4-9e1b091876f8` | `destination-exclusion.md` | provisional | draft |
| `796eaac8-2814-4ed0-81b8-a250829f5857` | `disconnected-network-handling.md` | provisional | draft |
| `2d2f6fea-8f98-4bc3-9c09-77f48c605997` | `downtown-revitalization.md` | provisional | draft |
| `a4c306f4-38a4-48ec-8e5f-9723c316cf15` | `economic-development.md` | provisional | draft |
| `8f2fb961-4a5e-4087-a770-4f92a9560a2d` | `elevation-effects.md` | provisional | draft |
| `5c94d178-80a2-4ae2-a7e9-11913c8f269c` | `emergency-resilience-planning.md` | provisional | draft |
| `980e9eba-923f-40eb-be49-ab0af2d2ad68` | `equity-analysis.md` | provisional | draft |
| `efac73e0-4296-40a3-b923-4b3c5fe998d2` | `external-dataset-joins.md` | provisional | draft |
| `ae27712e-8a55-4971-b6b9-6e9ac7d8950e` | `grant-applications.md` | provisional | draft |
| `0378c9a8-2c4d-4c6c-a539-6f2d6695dcad` | `hospital-access-analysis.md` | provisional | draft |
| `83c7b25f-39a1-46bb-818d-08e036ba206b` | `infrastructure-scenario-comparison.md` | provisional | draft |
| `53c458c4-656f-4996-9cb9-8840fb23a5eb` | `max-cost.md` | provisional | draft |
| `5316ffcf-f377-4389-9d00-f3859f71b233` | `neighborhood-comparison.md` | provisional | draft |
| `007890b5-c089-482e-a2bb-6b8e06992e3f` | `network-assumptions.md` | provisional | draft |
| `1c1aa0d5-0d74-425f-80de-058df7743e63` | `os-connect-data-usage.md` | explanatory | draft |
| `9624264b-fab7-4c59-a0fd-80faf87e9082` | `park-access-analysis.md` | provisional | draft |
| `be343515-c5ae-4a7c-8e51-bc5e872a5799` | `pedestrian-bottleneck-identification.md` | provisional | draft |
| `754c5070-24f7-411a-856b-b1e544509878` | `pedestrian-vs-wheelchair-walkshed.md` | explanatory | draft |
| `574b7c45-775c-464a-a31f-705057d9f6a9` | `pedestrian-walkshed.md` | provisional | draft |
| `31408e6b-881f-4e5a-8891-90d5b7429981` | `planned-capabilities.md` | provisional | draft |
| `0afbcb3c-9cfa-4dd3-b6de-db92f3fc91b7` | `planner-assumptions.md` | provisional | draft |
| `b13df74b-d458-4f8a-bc93-34fe2a0f501b` | `poi-origin-analysis-limits.md` | provisional | draft |
| `9ff35ff2-054c-498d-b8fc-5eb0346c7eb1` | `prioritization-workflows.md` | provisional | draft |
| `f847a412-fc69-4c8b-b120-47249db9e589` | `profile-variation.md` | provisional | draft |
| `9204edd8-26f0-4bdf-a5ea-1f5b0d9ccd5a` | `public-explanation.md` | provisional | draft |
| `7a8c3148-8701-4ea7-bc25-aacf538acd49` | `reachable-area.md` | provisional | draft |
| `1919bc62-04b4-4b73-a87f-59eecd38b3ed` | `rural-transportation-planning.md` | provisional | draft |
| `90aabacc-6e0d-4518-8596-cfb7a5eb4398` | `safe-routes-to-school.md` | explanatory | draft |
| `3142cd7e-1d15-4bf9-b45d-8967e8a59cb3` | `school-accessibility-analysis.md` | explanatory | draft |
| `9d95d98b-c8e6-4186-8495-0a28e570344d` | `senior-mobility-analysis.md` | provisional | draft |
| `eee64e4c-0f3c-44c9-9f02-8b9ba3be65b7` | `transit-planning.md` | provisional | draft |
| `2269d2e6-d81f-46f3-bc54-d6176e8e165d` | `travel-limits.md` | provisional | draft |
| `1e371817-fb9f-4470-a899-949f5fae22bc` | `travel-profiles.md` | explanatory | draft |
| `153153ae-ffc0-4cf0-aaa5-83204760f279` | `uncertainty-communication.md` | provisional | draft |
| `0295af74-2840-43c2-8228-d47819124e23` | `underserved-area-identification.md` | provisional | draft |
| `31b7e253-6d45-46da-b778-d5b58d0624a9` | `vision-zero.md` | provisional | draft |
| `54acc46a-b0ac-4f1d-b9f5-fc592ad481f7` | `walkshed-application-architecture.md` | provisional | draft |
| `89a3f9d6-6017-41fd-814f-ffcf49918c8d` | `walkshed-attribute-availability.md` | provisional | draft |
| `e31794c6-04da-4a09-8e70-d1548a535722` | `walkshed-batch-amenity-input.md` | provisional | draft |
| `6e304d1e-da2a-4cf1-8dfa-4f338da87654` | `walkshed-batch-concurrency.md` | provisional | draft |
| `b0df384a-bf0c-4518-897f-e69a1e87ee0f` | `walkshed-batch-failures.md` | provisional | draft |
| `efb8725e-04d5-4d40-8b05-bb818f512c8d` | `walkshed-batch-input.md` | explanatory | draft |
| `dc9750bb-08a1-4884-a6ed-329314c8d697` | `walkshed-batch-output.md` | explanatory | draft |
| `83f1704e-8797-4199-8536-b5a5fac76254` | `walkshed-batch-profiles.md` | provisional | draft |
| `470676f8-a54e-4209-bb84-57f189ad421a` | `walkshed-calculation.md` | explanatory | draft |
| `a4ab0eb4-b105-4eda-94a2-502d6dd5d459` | `walkshed-cost-factors.md` | provisional | draft |
| `e86233d6-a882-456e-8a8e-32208efb2ac3` | `walkshed-cost-function.md` | provisional | draft |
| `68f1ff89-3732-4fd3-8a1e-cb56a63f8cbf` | `walkshed-custom-cost-function-contract.md` | provisional | draft |
| `eeeac131-76ac-4a1f-a9f7-77266d6219d9` | `walkshed-custom-cost-functions.md` | provisional | draft |
| `4e478dc4-11b7-4287-a7b0-f8031c06edc7` | `walkshed-data-connectivity.md` | provisional | draft |
| `de709fed-8dbc-4074-a5b5-e55806d94c53` | `walkshed-data-issue-workflow.md` | provisional | draft |
| `dd6a067e-14b2-43f7-81e6-8719c2efcec0` | `walkshed-default-cost-model.md` | provisional | draft |
| `3c4dae86-476e-4d51-9a6d-a119b09efa91` | `walkshed-edge-attributes.md` | provisional | draft |
| `750ef049-781d-4180-b1bb-b357e62e8e6a` | `walkshed-edit-history.md` | provisional | draft |
| `7745e5d9-6adf-436a-8544-bd3f75d177df` | `walkshed-edit-limitations.md` | provisional | draft |
| `aebbd76a-d493-4672-b4cc-28713e669e0a` | `walkshed-feature-edits.md` | provisional | draft |
| `9fdf0e6c-9938-4fd8-a609-c23febdb9169` | `walkshed-interface-organization.md` | provisional | draft |
| `d1d8d6ea-4aea-4b98-8179-1cbad29025b9` | `walkshed-limitations.md` | provisional | draft |
| `ee58075d-863b-4684-b394-8b4951dbae4a` | `walkshed-map-symbols.md` | explanatory | draft |
| `be403ad0-a549-4bbb-88c1-90d3c0d2786d` | `walkshed-point-features.md` | provisional | draft |
| `5cc4abe2-a970-4e03-b745-518b26b617d4` | `walkshed-quality.md` | provisional | draft |
| `019c27d9-1acc-43e1-9728-4083a5085dc8` | `walkshed-result-statistics.md` | provisional | draft |
| `d9ddfe53-a279-4fea-a516-1dc44a5b2d29` | `walkshed-router-building.md` | provisional | draft |
| `57386715-0bd4-4e6a-a200-d57f4c8941ae` | `walkshed-router-processing.md` | provisional | draft |
| `b5d237d8-b2da-40d7-b8ca-c805470d5cfb` | `walkshed-scenario-statistics.md` | provisional | draft |
| `c900142b-239a-4bb1-b53a-c174d3b366f9` | `walkshed-scenarios.md` | provisional | draft |
| `3e79fc81-e754-4e2c-8743-254c6b04d3f7` | `walkshed-travel-cost.md` | provisional | draft |
| `6e9e7a39-14fd-4a11-8fcb-cc9eed18ac9e` | `walkshed-vs-buffer.md` | provisional | draft |
| `1219c51c-c6f9-4eb9-8957-0292f748f10f` | `walkshed.md` | explanatory | draft |
| `afada95d-a29f-4175-b38e-348ca0cbd6b0` | `walksheds-tool.md` | provisional | draft |
| `9a464d20-a02b-41b2-b1f3-080ee22ae68d` | `wheelchair-walkshed.md` | provisional | draft |

### Workflows

Base: `assistant/walksheds/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `60a4b58d-ce5d-41b3-8246-9a09fbd889fd` | `build-walkshed-router.md` | provisional | draft |
| `a54cc935-f91e-4bd7-9003-8f0f3d7dfad8` | `compare-walkshed-profiles.md` | explanatory | draft |
| `332fbe93-29f1-4bd2-aef9-66426766ed19` | `create-walkshed-scenario.md` | provisional | draft |
| `84f2c082-c041-4203-a960-24c971f45630` | `generate-walkshed.md` | provisional | draft |
| `aaad9521-c6a9-48ec-899c-b255096f14d2` | `inspect-and-edit-walkshed-feature.md` | provisional | draft |
| `cb1a245f-003c-4dc9-8563-64245a1ae0b3` | `model-infrastructure-change.md` | provisional | draft |
| `6ef3b6e2-f7cb-4e2c-9e85-987c03142768` | `run-batch-walksheds.md` | provisional | draft |
| `94429e21-4442-46ef-8725-ffe376c1809e` | `run-walkshed-batch-from-csv.md` | provisional | draft |
| `50f1da42-8293-4090-ac28-d6aa9954c221` | `save-and-compare-walkshed-scenarios.md` | provisional | draft |
| `260039e2-70aa-42dd-8b13-9b2f36da7c65` | `select-walkshed-dataset.md` | provisional | draft |

## Waykeeper — Assistant Knowledge Base

See [waykeeper/index.md](waykeeper/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/waykeeper/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `aa4e2d4c-c6ea-4f89-8e1c-40fa0ac692cb` | `index.md` | provisional | stub |

### Concepts

Base: `assistant/waykeeper/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `f1507e8d-76ef-497d-9074-075a36561d08` | `waykeeper.md` | provisional | stub |

### Workflows

Base: `assistant/waykeeper/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `66f21c66-0578-4289-8d1d-fc8bd2a9adc4` | `use-waykeeper.md` | provisional | stub |

## Workspaces — Assistant Knowledge Base

See [workspaces/index.md](workspaces/index.md) for per-topic assistant guidance and policies.

### Policies

Base: `assistant/workspaces/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `af1a8513-fb3c-4afd-841e-94dde1c99fed` | `index.md` | explanatory | draft |

### Concepts

Base: `assistant/workspaces/concept/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `20c7f4fc-1fcb-4d41-8c5a-57fbcc4683bf` | `accessibility-feature-editing.md` | provisional | draft |
| `92cf9b13-6094-4cdb-aadd-5eefc8a3dcaa` | `asr-imagery-list-repo.md` | provisional | draft |
| `802d673c-d3a5-4e79-a39e-f2647e9bdc3d` | `attribute-editing.md` | provisional | draft |
| `8cb5f06e-6a24-4cc0-b8c2-073769f7a6d6` | `aviv-scoutroute.md` | provisional | draft |
| `935c9b0c-1305-42fb-9a5d-afec7201f5bd` | `basemap-loading.md` | provisional | draft |
| `85a46b26-1ffb-4488-9051-4e268a3f01a6` | `change-authorship.md` | provisional | draft |
| `bd8adcfc-0f2f-4c7c-be33-e3613f350e4d` | `change-editor-tracking.md` | provisional | draft |
| `e932f94f-f821-422e-ab6b-2a3518fcf8c4` | `changeset-tracking.md` | provisional | draft |
| `b8059826-25f7-4427-ae3f-fba72215ea92` | `changesets.md` | provisional | draft |
| `05577303-7b19-4225-b785-5e9f32c7940a` | `collaborative-edit-management.md` | provisional | draft |
| `55fed870-32ed-42cb-8600-dd833c559e4d` | `collaborative-editing-support.md` | provisional | draft |
| `1d16529c-80a9-4094-803f-1dcede0c8336` | `collaborative-editing.md` | provisional | draft |
| `fee88a64-1584-4bb6-9c63-d1db97cc3ddf` | `community-workflow-support.md` | provisional | draft |
| `d86313df-89c4-4ebd-91b3-300e7ebca9dc` | `compatible-editors.md` | provisional | draft |
| `98ac75af-bea2-44ba-9c36-70ad84c8cf8e` | `compatible-tools.md` | provisional | draft |
| `a5bcd628-3d58-416a-bc5a-cac2ccde9004` | `continuing-feature-edits.md` | provisional | draft |
| `8d0a47ab-0d23-46a5-a1c2-40dcf44cd79f` | `custom-imagery-configuration.md` | provisional | draft |
| `1eddc192-2453-464d-bb99-207378a6f76b` | `custom-imagery.md` | provisional | draft |
| `c3edf51c-147c-4bd9-88cc-4a88fc95d71a` | `dataset-lineage-in-tdei.md` | provisional | draft |
| `3fa9ed5e-d219-4cfa-85c0-e05649f7b617` | `dataset-lineage.md` | provisional | stub |
| `a68282e8-3baa-4acf-ac9d-11d688ae646d` | `edit-attribution.md` | provisional | draft |
| `60301468-58c6-44f2-a4ae-03615b0b60af` | `edit-auditing.md` | provisional | draft |
| `ff861a75-487d-4cc1-b2b4-b8b5299d21a3` | `edit-history.md` | provisional | draft |
| `4eafe0ac-ae4a-4225-9e86-4c5fa1815d72` | `edit-metadata.md` | provisional | draft |
| `7a5c2a69-c837-46e5-9a07-de04bf4ef98f` | `edit-reviewers.md` | provisional | draft |
| `377a2e5f-06e9-4713-8d2d-a34aeb056b0b` | `edit-source-tracking.md` | provisional | draft |
| `59967ba7-bc68-4412-89bb-541db0457fef` | `edit-types.md` | provisional | draft |
| `4a879832-c6e6-48a8-81ac-f1065bf770b5` | `edit-upload-to-tdei.md` | provisional | draft |
| `8022c8f8-7019-4be9-8fdb-7489fe1fcd1d` | `editing-coordination.md` | provisional | draft |
| `6e8d733d-2d88-487b-a459-540f8eb240d4` | `export-overwrite-behavior.md` | provisional | draft |
| `691f8f6e-c407-44c7-aea2-79c56537de65` | `export-process.md` | provisional | draft |
| `49a58c6e-5226-47f2-958b-88e53fe57b8e` | `export-timing.md` | provisional | draft |
| `b7314341-6758-4642-8d41-a259866a4f33` | `export-versioning.md` | provisional | draft |
| `c891d6dc-7c7b-419d-98e9-f9a3c0914907` | `format-specific-data-generator-roles.md` | provisional | draft |
| `7721e29a-50c8-4810-96eb-994b81f4bbe8` | `geometry-editing.md` | provisional | draft |
| `11a74018-2359-4be9-87dd-278e35482312` | `gis-staff-role.md` | provisional | draft |
| `743b7223-0946-4c8f-b823-98a6e70152ed` | `gis-tool-decision.md` | provisional | draft |
| `9fa7a769-08d2-43c6-a40d-00f482049f09` | `imagery-json-configuration.md` | provisional | draft |
| `590f6c48-93a0-436b-acdb-e1d11dcdbab9` | `imagery-layer-access.md` | provisional | draft |
| `7588e129-1e1a-41a7-8734-0ae9c6866a39` | `imagery-layer-configuration-boundaries.md` | provisional | draft |
| `11cec0d3-3211-4e32-b0d4-08ce0b47a2cd` | `imagery-layer-definition.md` | provisional | draft |
| `53210438-96ab-4a05-bf4a-65b1bbbc41b2` | `imagery-layer-mechanics.md` | provisional | draft |
| `f5733eac-79a7-4ced-af6e-6a4439de5d17` | `imagery-layer-overview.md` | provisional | draft |
| `0bfbd81a-502a-4851-a71b-06b18f0bd80a` | `imagery-layers.md` | provisional | stub |
| `03b7c67c-e121-4633-a172-1f412bcbc06a` | `imagery-misconfiguration.md` | provisional | draft |
| `26bb7904-97eb-4059-9834-73d1ca82b317` | `imagery-permissions.md` | provisional | draft |
| `92405620-7a42-40be-a7b2-32e501ea6635` | `imagery-raw-json-requirement.md` | provisional | draft |
| `451d0a99-8b85-47d0-b660-5bb37cd80b07` | `imagery-resource-variation.md` | provisional | draft |
| `f73da7f3-fcf0-4d20-ac4d-676b1b1564e3` | `imagery-sources.md` | provisional | draft |
| `860e4c0a-e07e-47f0-a404-3e3aeec342d9` | `intended-audience.md` | provisional | draft |
| `b7837dec-5456-4e3e-a38e-87d7ed27d5d9` | `internal-qa-qc-data-access.md` | provisional | draft |
| `1abcbb6b-66a2-4c23-a418-6a015ceab999` | `josm.md` | provisional | draft |
| `6be91709-d64c-4d66-9cb2-01803475ddc3` | `keeping-edits-private.md` | provisional | draft |
| `1c093cb9-503d-4499-8295-3a12f55e23d6` | `manager-edit-review.md` | provisional | draft |
| `3afcf00a-fc90-48af-8f28-2761401c8c46` | `manager-role.md` | provisional | draft |
| `95abcc37-194b-471d-9974-ba0f9b9a04fb` | `mobile-point-feature-creation.md` | provisional | draft |
| `1aa276b7-21a8-47f0-8e31-b357775d49d3` | `multi-source-stewardship.md` | provisional | draft |
| `e87309e2-9ce5-40ac-944d-5d2212d312da` | `multiple-workspaces-per-dataset.md` | provisional | draft |
| `88f5eb39-d1a0-4680-9157-3ecef8f34fce` | `non-global-dataset-rationale.md` | provisional | draft |
| `045da848-bd0e-49e1-8364-6cd4b162ae68` | `notes-as-field-issue-reports.md` | provisional | draft |
| `2a273334-8212-440f-a6b2-9529b12c0c30` | `osm-api-emulation.md` | provisional | draft |
| `890f5e4b-ca48-4c8a-b49e-c2a3d9304ef0` | `osm-connection.md` | provisional | draft |
| `290a0246-bd5f-45f1-980f-071c1c531c65` | `osm-editing-emulation-rationale.md` | provisional | draft |
| `e6faef21-a235-4c53-8e66-3f744d6b44a4` | `osm-editor-benefits.md` | provisional | draft |
| `27b73b05-5428-4a61-9859-0cc2808ad148` | `osm-tool-compatibility-rationale.md` | provisional | draft |
| `055ad2f1-86d6-48c8-89ba-edd1559cfbe5` | `parallel-workspace-editing.md` | provisional | draft |
| `65d73d85-848b-449f-b803-b30fc9f9ba3a` | `post-export-behavior.md` | provisional | draft |
| `624ad449-289a-414e-8580-0ad753b563c1` | `private-osm-explained.md` | provisional | draft |
| `d8b89de0-a416-4f65-98d9-d01197a458eb` | `private-osm.md` | provisional | stub |
| `51f6b51d-3caf-4def-8352-a3ba9b033ddd` | `project-group-and-workspace-roles.md` | provisional | draft |
| `791b6ae8-46bb-4813-87b6-795097648c52` | `project-group-definition.md` | provisional | draft |
| `bfe77757-e525-4299-8dad-fe0b25ee4f8f` | `project-group-operations.md` | provisional | draft |
| `18acaf54-0272-499e-8be4-a68cfd98a639` | `project-group-referral-access.md` | provisional | draft |
| `035822ae-e931-4b1b-b96d-a6c68fefde72` | `project-groups.md` | provisional | stub |
| `3745069a-5838-47a4-9d5a-92d8ac191cc6` | `public-availability-of-quest-photos.md` | provisional | draft |
| `7b6349e8-cb29-405c-b6af-4e92d504192c` | `qa-review-support.md` | provisional | draft |
| `ebab14b0-6d9c-462e-9655-58c888838778` | `qr-code-name-change.md` | explanatory | draft |
| `7622fde6-19c3-4a11-8e4a-850a32f66a51` | `quest-definition-url-requirements.md` | provisional | draft |
| `eff61780-6d79-46f0-be56-5a612d85a908` | `rapid-imagery-integration.md` | provisional | draft |
| `03dd0763-74cb-4850-aefd-0ac01f4e4920` | `rapid-versions.md` | provisional | draft |
| `66fd8c0f-6f4f-4894-8224-53ca7f1a2dbb` | `rapid.md` | provisional | stub |
| `440a81d4-ad61-4e04-932e-befaec565511` | `raster-and-vector-basemaps.md` | provisional | draft |
| `e7a65d6d-128e-4881-b3d9-22b12b7389d0` | `recommended-publication-workflow.md` | provisional | draft |
| `ad8c6fcb-1da8-4839-8845-4c5af889faa3` | `recommended-workflows.md` | provisional | stub |
| `e57a35a2-0d42-47fd-abf7-69ab994ea041` | `review-interface.md` | provisional | stub |
| `fe334631-ca62-41b1-b4f6-0684ddc62d02` | `roles.md` | provisional | stub |
| `51b46963-5a2c-4b1d-9e8d-21e76f34f5c2` | `sandbox.md` | provisional | stub |
| `74d0f041-51ba-4de5-af68-5906d73bb777` | `source-dataset-tracing.md` | provisional | stub |
| `141cf8e7-ebbf-43db-8fd5-eed7cba54a94` | `stewardship-support.md` | provisional | stub |
| `fcde475f-1f37-4396-9de9-c630a19af968` | `target-users.md` | provisional | stub |
| `9dd8cfe2-9912-4127-882f-f31c0accfc61` | `tdei-ecosystem-fit.md` | provisional | stub |
| `70f4fa39-5c72-4751-9eed-7c0ff2cc236b` | `tdei-vs-workspaces.md` | provisional | stub |
| `01a52d4b-20dc-4828-b9be-b79b923b8e60` | `team-invitations.md` | provisional | draft |
| `4c4c81b4-bf7b-42b8-a5de-c136c599b854` | `teams-vs-project-groups.md` | provisional | draft |
| `1540374b-e992-403b-9bbd-61d57b48a163` | `teams.md` | provisional | draft |
| `7673d5e9-a8da-4d70-b425-2f87263a592c` | `tile-layers.md` | provisional | stub |
| `f8f17ead-342c-4ba6-9912-818688133b22` | `vector-map-preference.md` | provisional | stub |
| `d39455d8-d275-417b-8d23-99869e2915e8` | `vector-vs-raster-maps.md` | provisional | stub |
| `8d5016d2-0794-455a-adad-c1d3ae21fbc0` | `viewer-vs-editor-users.md` | provisional | stub |
| `7017334a-7513-4974-a8d4-37636a3cc266` | `workspace-abstention-boundaries.md` | provisional | stub |
| `a60d4275-cf02-4661-9cc1-40d36ecc539e` | `workspace-and-tdei-boundary.md` | provisional | draft |
| `5cd6f50d-4bf8-49ec-a4a3-277c6bb468ea` | `workspace-app-access-default.md` | provisional | draft |
| `da46b16f-aab5-4136-bdc9-d8316b4fd5c0` | `workspace-as-dataset-copy.md` | provisional | stub |
| `a2949a44-7dc4-4c66-9e77-22dcc4e07ad3` | `workspace-as-private-osm.md` | provisional | draft |
| `7fede7be-e034-4c79-aca6-eb01f4716c2c` | `workspace-availability-for-new-mappers.md` | provisional | draft |
| `4e8fc1fe-a7d3-4130-a071-c37610271c65` | `workspace-copy-and-divergence.md` | provisional | draft |
| `e2be6bc3-de31-4d51-b9ab-862dfdcc2cb8` | `workspace-creation-mechanics.md` | provisional | stub |
| `34430d5c-010a-42e3-b3a7-f67b5c5462a5` | `workspace-creation-methods.md` | provisional | stub |
| `87222545-eb8a-4e8e-a918-d3462951eaca` | `workspace-dashboard.md` | provisional | stub |
| `2101da94-061a-4cfb-a3bd-022da2d0914a` | `workspace-data-freshness.md` | provisional | stub |
| `05efc35b-8c38-4868-b0ef-6c2abe120dd9` | `workspace-dataset-divergence.md` | provisional | stub |
| `f3682546-e029-4fc0-8ece-e7d566fd32dd` | `workspace-duplicate-copy-risk.md` | provisional | draft |
| `9b24601c-e489-4d4a-9650-b06adb8324b6` | `workspace-editing-authority.md` | provisional | stub |
| `9ec9cef6-0635-4081-b519-f8dffe9a708a` | `workspace-editing-boundary.md` | provisional | draft |
| `b8f25f3c-5640-4e76-9c60-00339a908f46` | `workspace-export-and-publication-caveats.md` | provisional | stub |
| `4fdc6aaa-e1f6-4a51-9d44-f8fa1b8fa392` | `workspace-extract.md` | provisional | draft |
| `6ec02d37-b8ef-4919-aa7b-b3e33e2b37ef` | `workspace-id.md` | provisional | stub |
| `7bc49a18-d5ce-4c01-a99f-4561b8b49ddb` | `workspace-metadata-and-lineage.md` | provisional | draft |
| `fa5ae824-1130-4515-96db-76a4fa2e5c61` | `workspace-metadata.md` | provisional | stub |
| `bb08cf9c-20bf-4b06-8252-8bd791093584` | `workspace-per-project-model.md` | provisional | draft |
| `f88d9666-fa8a-4e10-a8ad-0d1c74b6875f` | `workspace-public-vs-private-data.md` | provisional | draft |
| `4cd21f12-6dd9-49e7-bb65-4350ae9de843` | `workspace-review-and-publication-gates.md` | provisional | draft |
| `5a0750a4-cf38-40e9-8eed-028db0af003c` | `workspace-review-interface.md` | provisional | draft |
| `5107a4c5-ef03-449d-bb7a-107a873b1a4c` | `workspace-roles-and-project-roles.md` | provisional | draft |
| `3ed3b5c7-4bec-4e82-8f0a-676f7393ce02` | `workspace-source-options.md` | provisional | draft |
| `2e3b7419-f07a-4770-b232-1f10799c536e` | `workspace-tdei-isolation.md` | provisional | stub |
| `01ed2c86-c164-45c2-aa45-f8ec8de639c1` | `workspace-team-membership.md` | provisional | draft |
| `298fc015-dc9c-41f6-a4ad-438c01f375ed` | `workspace-teams.md` | provisional | draft |
| `10fa8424-575f-4d06-b988-c879ba2fa47a` | `workspace-technical-definition.md` | provisional | stub |
| `aec7bb23-e9b3-4ae8-bb73-551582902887` | `workspaces-os-connect-relationship.md` | provisional | stub |
| `365b14fc-1c9b-4aa4-987d-32301dd2e458` | `workspaces-osm-limitations.md` | provisional | stub |
| `f9f0667d-f55e-49fd-bcde-002bb8fd5a7f` | `workspaces-tdei-portal-relationship.md` | provisional | stub |
| `077fab37-97a4-494e-a5c4-0066948ca98d` | `workspaces-tdei-separation.md` | provisional | stub |
| `2c24b2c8-2964-4425-a473-7edaff7e439b` | `workspaces-vs-gis-decision.md` | provisional | stub |
| `8de5fa11-c573-42d1-8dc8-5ab84d908bbd` | `workspaces.md` | provisional | draft |

### Workflows

Base: `assistant/workspaces/workflow/`

| UID | File | Authority Level | Publication Status |
| :-- | :--- | :-------------- | :----------------- |
| `4a67f7be-0bcb-42bb-a559-414137cc6789` | `choose-editor.md` | provisional | stub |
| `104ba052-d073-4edc-9e3c-b6f3077a4fc3` | `configure-app-enabled-workspace.md` | provisional | draft |
| `bbdf5d6a-a9ee-4a83-a0e7-3a3c65d149a4` | `configure-imagery-layers.md` | provisional | draft |
| `18a7a7a8-e0b3-4b61-ba74-eb57506b261b` | `create-a-workspace-from-tdei.md` | provisional | draft |
| `9e396bd0-b847-4f5a-9d77-48d8acc76153` | `create-workspace-from-osm.md` | provisional | draft |
| `f3c427a3-f360-4bfe-a808-981bd74208f4` | `create-workspace-from-tdei-dataset.md` | provisional | draft |
| `68dbba63-5f2c-4d43-bb91-39114a546e56` | `create-workspace-from-tdei.md` | provisional | stub |
| `299c33bf-9f17-4b43-a5e9-91cf8b24ff82` | `create-workspace.md` | provisional | stub |
| `0a1a84b6-b514-4aa8-855d-d51fe906df54` | `edit-accessibility-features-in-a-workspace.md` | provisional | draft |
| `e82a23a4-e888-4999-9454-3b870772536f` | `export-workspace-edits-to-tdei.md` | provisional | stub |
| `e6537f55-e706-4a85-bcfe-d3f11da10a17` | `export-workspace-locally.md` | provisional | draft |
| `7693f966-2c3d-4712-b725-5484d75073fa` | `export-workspace-to-tdei.md` | provisional | draft |
| `9afa9a04-a794-4066-967f-6a67dc64286d` | `export-workspace.md` | provisional | draft |
| `8ef7fda7-b7bc-46ce-96c6-c2fe01eb0cc9` | `import-external-geojson-for-reference.md` | provisional | draft |
| `9781d11f-5feb-4395-ad48-61a7f94d30de` | `import-osm-data-into-workspaces.md` | provisional | draft |
| `4c35b3d6-cbad-43e0-9cb5-6cc7b0a56540` | `invite-to-workspace-team.md` | explanatory | draft |
| `7bb47f06-a390-4389-8837-c4712bd76514` | `open-dataset-for-inspection.md` | provisional | draft |
| `cb452c73-4317-40c1-82d2-5f2fe365b58f` | `pre-export-review.md` | provisional | stub |
| `07af8eac-2ec6-428b-963d-79b6aaffaa2d` | `publish-jurisdiction-updates.md` | provisional | stub |
| `85d9b699-b1ce-4438-b4af-e859f36014c7` | `review-quest-contributions.md` | provisional | draft |
| `c17f4997-b289-43b3-a0ea-50329ed41f50` | `review-workspace-edits.md` | provisional | stub |
| `0789d812-e0dd-44bd-9b82-85c518e94c25` | `search-project-groups.md` | provisional | stub |
| `5557b51a-9b2d-4dc4-b0cc-767a4c0d1419` | `set-up-tasking-manager-project.md` | explanatory | draft |
| `bf8e1e70-e00c-4693-8e6c-714dd28bad26` | `use-workspaces-for-community-validation.md` | provisional | stub |
| `ea90f6c5-3f56-4df0-aef5-db433e5f5aa3` | `use-workspaces-for-jurisdiction-stewardship.md` | provisional | stub |
