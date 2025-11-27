---
title: OpenSidewalks in OpenStreetMap
tags:
    - Guide
    - External
    - User
    - OSW 0.3
---

<!-- @format -->

# OpenSidewalks in OpenStreetMap

This guide explains how to make edits to OpenStreetMap following and supporting the OpenSidewalks schema.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

## Acknowledgments

[OpenSidewalks](../index.md) is an open data project by the [Taskar Center for Accessible Technology](../../index.md) at the University of Washington in Seattle, WA, US. The project relies on the OpenStreetMap (OSM) ecosystem.

This Mapping Guide was developed with the support of the United States Department of Transportation (USDOT) ITS4US program, the Washington State Department of Transportation (WSDOT), and the Microsoft AI for Accessibility program.

_Contributors to this document include: Anat Caspi, Mario Sanchez, Jimmy Phuong, Nick Bolten, Cole Anderson, Olivia Quesada, Clifford Snow, Jessica Hamilton, Amy Bordenave, and Maddie Gugger._

© Taskar Center for Accessible Technology, 2025

## Background and Purpose

[OpenSidewalks](../index.md) (OSW) is a project that engages wide audiences in the important work of collaborative open source mapping of pedestrian pathways and related features. Our mission is to create a tooling ecosystem that supports the consistent, standardized collection of data about the pedestrian environment. This open and shared data can then be used to enable pedestrian routing applications, inform infrastructure planning, and advocate for improved walkability, accessibility, and quality of life for all.

This learning resource contains material to help you create accessible pedestrian pathways data that is shared in the global, open source [OpenStreetMap](https://openstreetmap.org) database. As we continue to engage with more cities in our mission to improve and scale the documentation of pedestrian pathways, we maintain this self-paced training resource to enable the participation of mapping contributors.

Because the OpenStreetMap community is constantly evolving, mapping guidance is always changing with it. Consequently, we recommend that the use of this guide is combined with consultation with the [OpenStreetMap Wiki](https://wiki.openstreetmap.org/) as well as the local OSM community.

Thank you for your interest in OpenSidewalks. Together, we can work towards creating inclusive and accessible data about the pedestrian environment that benefits communities worldwide!

## Welcome to the OpenSidewalks project!

The [OpenSidewalks](../index.md) ([https://sidewalks.washington.edu](https://sidewalks.washington.edu)) mission is to create a tooling ecosystem that supports the consistent, standardized collection of data about pedestrian pathways such as sidewalks and crossings. This open and shared data can then be used to enable pedestrian routing applications, inform infrastructure planning, and advocate for improved walkability, accessibility and quality of life for all.

This learning resource contains material to help you create accessible pedestrian pathways data that is shared in the open source [OpenStreetMap](https://welcome.openstreetmap.org/) global database.

Your mapping contributions make a difference! Our collaboration with G3ict in the AI For Inclusive Urban Sidewalks initiative, in particular our work in Brazil and Ecuador, was recognized by the Smart City Expo World Congress 2022, earning the Living and Inclusion Award!

As we continue to engage with more cities in our mission to improve and scale the documentation of pedestrian pathways, we maintain this self-paced training resource to enable the participation of mapping contributors.

**Are you interested in contributing to the project as a mapper, or do you want to become an OpenSidewalks trainer? Would you take the lead in organizing an OpenSidewalks pedestrian mapping effort in your city, town or jurisdiction and want our project to support you?**

The materials in this resource are organized to support the onboarding of mappers who have no prior experience with OpenStreetMap tools, to teach validators how to review mapping contributions, and to provide guidance about how to organize a mapping team.

Please start by reviewing the OpenSidewalks Learning Roadmap module designed to help you enhance your individual mapping skills and maximize the productivity of your local engagements. This module provides valuable information on how to effectively utilize the material and offers guidance tailored to your specific needs.

## OpenSidewalks: Learning Roadmap

### How to use the OpenSidewalks Onboarding Guide

Thanks for joining the OpenSidewalks global mapping collaboration! Please take a moment to review this section to familiarize yourself with the topics covered in our onboarding guide. This material covers the mapping practices and data standards of the OpenSidewalks schema that lead to consistently mapped and networked data about pedestrian pathways such as sidewalks and crossings.

This guide is intended to allow OpenSidewalks advocates and mappers (of varying degrees of experience) to become familiar with OpenSidewalks mapping tools and data standards. The onboarding guide also includes lessons for more experienced mappers on how to help validate completed mapping tasks. Lastly, we offer a set of best practices for local mapping team coordinators to engage more effectively with other mapping contributors and to develop local data governance practices. This page is organized along the following topics:

-   Roadmap For All Mappers
-   Roadmap For Validators (Advanced Mappers)
-   Roadmap For Local Mapping Team Coordinators
-   The Essential Lessons

The next lesson, which completes the Learning Roadmap module, also covers how to reach out to us if you need assistance.

### Roadmap for All Mappers

The modules in the OpenSidewalks Onboarding Guide that relate to all mappers are organized into the following major topics. The modules below should be completed in the order presented and are required for new mappers.

This table below represents the entirety of modules and lessons that relate to OpenSidewalks mapping practices and data standards. The modules marked as "**(Advanced)**" are intended for advanced mappers (validators) and local mapping team coordinators.

The estimated time to complete the core modules and their associated assignments for new mappers is approximately 120 minutes (2 hours).

| Module                                                                                | Contents and Completion Estimate                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenSidewalks: Project Overview                                                       | Understand the objectives of the OpenSidewalks project and how citizen change agents and city mapping teams can contribute to the project. (6 Minutes + Assignment)                                                                                                                                                                                                                          |
| OpenSidewalks Academy: Intro To Mapping Tools                                         | Understand the open source tools and data the OpenSidewalks project uses to map and tag pedestrian features. (20 Minutes + Videos)                                                                                                                                                                                                                                                           |
| OpenSidewalks Academy: The iD Editor                                                  | Learn to use the browser-based OpenStreetMap iD Editor tool to map pedestrian pathway features and document their attributes. (20 Minutes)                                                                                                                                                                                                                                                   |
| OpenSidewalks Academy: The Tasking Manager                                            | Learn to navigate the OpenSidewalks Tasking Manager instance to contribute geolocated pedestrian pathway data to the global OpenStreetMap database. (20 Minutes + Assignment)                                                                                                                                                                                                                |
| OpenSidewalks Academy: How To Map Pedestrian Pathways                                 | Understand how OpenSidewalks breaks down mapping of pedestrian features into three distinct phases. Identify the features of a pedestrian network. Learn how to map and document the attributes of crossings, curbs, sidewalks, and footpaths. Follow the OpenSidewalks mapping guidelines to ensure data consistency. (30 Minutes + Assignments)                                            |
| OpenSidewalks Academy: Validating Completed Mapping Tasks **(Advanced)**              | Learn about the experience that qualifies mappers to validate other users' contributions, what to look for when validating completed tasks in the Tasking Manager, and how to approach corrections. Use our recommendations to organize your local validation team. (25 Minutes + Assignments)                                                                                               |
| OpenSidewalks Academy: Miscellaneous Guides and Data Quality Practices **(Advanced)** | This module contains reference material such as guidelines on how to map city intersections under different scenarios and a summary of best collaboration practices to help coordinate local mapping teams. The module also includes a glossary of pedestrian features, the list of tags by pedestrian feature, and information on how to capture your own street-level images. (20 Minutes) |

# Roadmap For Validators (Advanced Mappers)

Individuals who have gained OpenStreetMap mapping experience while contributing to the OpenSidewalks project are in a unique position to help local mapping teams review and validate completed tasks in the OpenSidewalks Tasking Manager.

These mappers will have completed the modules listed in the Roadmap For All Mappers, above.

Specifically, they should review the lessons included in the _OpenSidewalks Academy: Validating Completed Mapping Tasks In The Tasking Manager_ module which are listed in the table below.
