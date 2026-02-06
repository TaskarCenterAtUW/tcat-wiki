---
title: QA/QC Reports User Manual
nav_order: 1
tags:
    - User Manual
    - External
    - User
---

<!-- @format -->

## QA/QC Reports User Manual

This documentation explains the context and goals behind as well as how to read and interpret QA/QC reports for the OS-CONNECT dataset.

---

### Understanding QA/QC Reporting for OS-CONNECT

Under the directive of the Washington State Legislature, using innovative methods developed by the Taskar Center for Accessible Technology at the University of Washington, the State has created OS-CONNECT: a comprehensive, high-resolution, and connected pedestrian network dataset.

OS-CONNECT supports Washington's broader goals around transportation equity, safety, and accessibility by providing detailed sidewalk infrastructure data across 320+ cities and counties. Continued expansion and Quality Assurance/Quality Control (QA/QC) of this dataset is foundational to offering sustainable and inclusive mobility options for all Washington residents.

The OS-CONNECT QA/QC report is a standardized analysis that evaluates the quality, completeness, and usefulness of pedestrian infrastructure data for a given jurisdiction. The purpose of the report is to help planners, transportation professionals, and community members understand whether their data is ready to support accessibility, safety, and reachability (gap-focused) transportation initiatives.

This document explains how to read and interpret QA/QC reports for the OS-CONNECT dataset.

The metrics reported are designed to answer three core questions:

1. **Is the pedestrian data complete enough to support analysis and planning?**
2. **How accessible is the network for different types of pedestrians, including manual wheelchair users?**
3. **How well-connected is the network, and where are the critical links or gaps?**

Unlike datasets used in traditional machine learning (ML) settings, the OS-CONNECT dataset is constructed without gold-standard annotations or human-labelled reference data that ML results are classically validated against. Therefore, conventional evaluation metrics such as mean Intersection over Union (mIoU), precision, and recall are not applicable.

Instead, this QA/QC framework adopts a multi-pronged approach rooted in the literature on geospatial data quality assessment. As shown in the taxonomy below, data quality can be evaluated using extrinsic, intrinsic, and machine learning-based metrics, alongside indicators of data trustworthiness and user reputation. Each section of this report corresponds to one or more of these categories, selected for their relevance to open geospatial data validation.

---

### Table of Contents

QA/QC Reports User Manual Table of Contents

#### [Data Sources and OS-CONNECT QA/QC Report Structure](structure.md)

This document explains the structure of the OS-CONNECT QA/QC reports.

#### [OS-CONNECT QA/QC Report Subsections in Detail](metrics.md)

This guide covers the details of each OS-CONNECT QA/QC report subsection and metric.

#### [Data Infrastructure for QA/QC Report Generation](infrastructure.md)

This guide details the data infrastructure system components used by OS-CONNECT QA/QC reports.
