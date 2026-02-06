---
title: Data Infrastructure for QA/QC Report Generation
nav_order: 4
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Data Infrastructure for QA/QC Report Generation

This guide details the data infrastructure system components used by OS-CONNECT QA/QC reports.

---

The UW team has developed data processing infrastructure that utilizes the TDEI and its tools (for example, "Walksheds") to generate the QA/QC reports described in this document.

The data infrastructure has been designed with the goals of consistency (results are the same as those shown by other TDEI tools given the same request), reusability (logic or data to generate a metric or the report can be re-used in subsequent analyses), maintainability (there is an alignment between the tool's implementation and the software development skills of the team) and extensibility (the tool can evolve as needs evolve) in mind.

Key system components include:

- **The routing engines**: both UW/TDEI's "Walksheds" tool, which processes OSW and routes based on pedestrian or wheelchair profiles, as well as the commercial provider HERE's router, which uses HERE's own proprietary network data related to car and sidewalk data to generate shortest paths and report metrics back on those paths.
- **Data store**: currently hosted on Azure's "blob" store, a storage area for both the PDF reports downloadable by the user as well as interim data products (the "cache") that are used in the generation of the reports themselves. Future work on the data store will make the interim data products more accessible and reusable in ways that align with future analytic needs.
- **Job orchestration and TDEI integration:** currently implemented using GitHub Actions, a layer to interface with the TDEI to prepare data for reporting, as well as update a dataset's metadata on the TDEI after a report is generated. This system component also launches, monitors, and shuts down each report generation container (described below), monitors its output, restarts it if it fails, and provides an overview of progress for the team to monitor progress.
- **Report generation container:** implemented as a Docker container, this component contains the Python scripts (described further below) that generate the report, the metrics, the maps, and make requests of the routing engines to gather the data used in the reports. Having this work "dockerized" means it can be easily reused by other components.
- **Python scripts/workflow:** Run inside the Python environment created inside the Docker container (described above), these scripts do the actual work of making requests of Overpass/OSM, Overture, and the routing engines, generate the metrics used within the reports, and also package those metrics up in the form of tables, maps and other assets used in the final PDF reports downloadable by the user. Currently, these steps are run in sequential order, using the cache to skip unnecessary steps when the same report is regenerated. Future work will include more sophisticated dependency management and interim data caching for better re-use. Future work will also include a refactoring of these scripts to make the scripts more organized and reduce repetitive steps.

Previous section: [Data Sources and OS-CONNECT QA/QC Report Structure](structure.md)
