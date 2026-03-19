---
title: Import Curb Ramp Data into the TDEI
tags:
    - Tutorial
    - External
    - User
---

<!-- @format -->

## Import Curb Ramp Data into the TDEI

This tutorial explains how to convert an existing curb ramp point dataset to OpenSidewalks (OSW) format and upload it to the TDEI Portal as a new dataset.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._{ .guides-list-ref }

---

### Prerequisites

Before you begin, you will need:

- A **TDEI Portal account**. Refer to the [TDEI Portal Account Registration Guide](../user-manual/account-registration.md) if you do not have one already.
- A modern web browser (such as Chrome, Firefox, Edge, or Safari) — required for the browser-based conversion tool in Step 2.

!!! example "Python Alternative"

    If you prefer to work via the command line, a Python script equivalent to the browser tool is provided in the **Python** tab of [Step 2](#step-2-convert-to-osw-format). It requires **Python 3.8+** and the **`pyproj`** package.

---

### Step 1: Download the Source Data

Download your curb ramp dataset from your city or agency's open data portal as a **GeoJSON** file.

The Seattle Department of Transportation (SDOT) curb ramps dataset is used as a working example, though the conversion process provided in this tutorial can be adapted for curb ramp data from any source.

1. Open the [SDOT Curb Ramps dataset](https://data.seattle.gov/dataset/Curb-Ramps/wraq-yxwb/about_data) on the Seattle Open Data Portal.

2. Under the **Access this Data** section, choose the **GeoJSON** format from the list of download options.

3. **Save** the file to a convenient location on your device, with a name such as `curb_ramps.geojson`.

    ![Dataset download options](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/dataset-download-light.png#only-light)
    ![Dataset download options](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/dataset-download-dark.png#only-dark)

??? question "Download not working?"

    If an _"Up to date download file is being generated. Please check back again later."_ or similar message appears after selecting the download button, simply wait for some time then **Refresh** (++f5++) the page. Depending on the size of the dataset, this part of the process may take anywhere from only a few seconds up to an hour or more.

    ![Dataset generating](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/dataset-generating-light.png#only-light)
    ![Dataset generating](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/dataset-generating-dark.png#only-dark)

!!! info "Using a different dataset?"

    As long as your source data is a GeoJSON file with point geometries, the conversion process in the next step can be adapted for any city. Expand the **Dataset & field mapping** section in the tool to edit the field names.

---

### Step 2: Convert to OSW Format

=== "In-Browser Converter"

    Use this browser-based converter below. Nothing else required — everything runs locally in your browser.

    <iframe src="../convert-curb-ramps/" style="width: 100%; height: 1400px; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 6px;"></iframe>

    1. Select your GeoJSON file using the file picker or by dragging it onto the upload area.
    2. The **Dataset & field mapping** section is pre-configured for the SDOT Curb Ramps dataset. If you are using a different source, expand it and update the field names and coordinate system to match your source data.
    3. Select **Convert to OSW**, then **Save OSW ZIP** once conversion is complete.

=== "Python"

    Download [**`convert-curb-ramps.py`**](convert-curb-ramps/convert-curb-ramps.py){ download="convert-curb-ramps.py" } or expand the "View Source" section below, copy the script into a new text file named **`convert-curb-ramps.py`**, and save it in the same folder as your downloaded GeoJSON file.

    ??? example "View Source: Curb Ramp Point Conversion Python Script"
        ```python title="convert-curb-ramps.py"
        --8<-- "docs/tdei/portal/tutorial/convert-curb-ramps/convert-curb-ramps.py"
        ```

    This requires **Python 3.8+** and the **`pyproj`** package to be installed (`pip install pyproj`).

    **Run the script** by opening a terminal (Command Prompt or PowerShell on Windows; Terminal on macOS/Linux), navigating to the folder containing your files, and running:

    ```ps
    python convert-curb-ramps.py curb_ramps.geojson
    ```

    Replace `curb_ramps.geojson` with the actual name of the file you downloaded in Step 1.

    You can optionally provide a custom output path as a second argument:

    ```
    python convert-curb-ramps.py curb_ramps.geojson my-output.zip
    ```

    The script prints progress and produces a `.zip` file in the same folder:

    ```
    Reading curb_ramps.geojson ...
      46,174 features found
      45,814 converted, 360 skipped (missing geometry, ID, or duplicate)
    Writing curb_ramps-osw.zip ...
    Done.
      Output     : curb_ramps-osw.zip
      Inner file : curb_ramps.nodes.geojson
      Features   : 45,814
    ```

    ![Terminal with convert-curb-ramps.py run](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/convert-curb-ramps-light.png#only-light)
    ![Terminal with convert-curb-ramps.py run](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/convert-curb-ramps-dark.png#only-dark)

    !!! warning "Adapt the script for your dataset!"

        Open `convert-curb-ramps.py` in a text editor and look for the **CONFIGURATION** section near the top of the file. Update `EXT_FIELDS` to map your dataset's field names, change `ID_FIELD` and `RAMP_WIDTH_FIELD` as needed, update `DATA_SOURCE_NAME` and `DATA_SOURCE_LICENSE` to reflect your source, and set `SOURCE_CRS` to the EPSG code of your data's coordinate system (or `None` if it is already in WGS84).

---

### Step 3: Validate the Output

Before uploading, it is recommended to validate the converted file using the TDEI Portal's **OSW - Validate** job. While not required, this confirms the file is schema-compliant and catches any issues before upload.

1. Log in to the [TDEI Portal](https://portal.tdei.us/).

2. Navigate to **Jobs** and select **Create Job**.

3. Set **Job Type** to **OSW - Validate**, upload your `.zip` file, and select **Create**.

    ![TDEI Portal create OSW - Validate job](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/validate-light.png#only-light)
    ![TDEI Portal create OSW - Validate job](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/validate-dark.png#only-dark)

4. Monitor the status on the **Jobs** page. A **Completed** status confirms the file is valid and ready to upload. A **Failed** status indicates validation errors — review the job details for error messages.

For more information, refer to the [TDEI Portal > User Manual > Jobs > OSW - Validate](../user-manual/jobs/osw-validate.md) guide.

---

### Step 4: Upload to the TDEI

Upload the resulting `.zip` file to the TDEI Portal as a new OSW dataset.

1.  Log in to the [TDEI Portal](https://portal.tdei.us/datasets) and navigate to **Datasets**. Select **Upload Dataset** in the top-right corner.

2.  Choose a **Service**: Choose an available `OSW` service, then select **Next**.

    ![Upload Dataset — Select Service step](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-01-service-light.png#only-light)
    ![Upload Dataset — Select Service step](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-01-service-dark.png#only-dark)

3.  **Attach Data File**: Drag and drop your `.zip` file onto the upload area (or select to browse), then select **Next**.

    ![Upload Dataset — Data File and Metadata step](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-02-file-light.png#only-light)
    ![Upload Dataset — Data File and Metadata step](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-02-file-dark.png#only-dark)

4.  Specify **Metadata**: Fill in the required metadata fields across the tabs:
    - **Dataset Details** tab:
        - _Dataset Name_
        - _Dataset Version_
        - _Schema Version_
        - _Collected By_
        - _Collection Date_
        - _Data Source_

    ![Upload Dataset — Dataset Details tab](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-03-details-light.png#only-light)
    ![Upload Dataset — Dataset Details tab](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-03-details-dark.png#only-dark)
    - **Data Provenance** tab:
        - _Full Dataset Name_

    ??? note "Screenshot: Data Provenance tab"

        ![Upload Dataset — Data Provenance tab](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-04-provenance-light.png#only-light)
        ![Upload Dataset — Data Provenance tab](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-04-provenance-dark.png#only-dark)

5.  **Changeset**: Leave this step empty and select **Submit** at the bottom right.

    ![Upload Dataset — Changeset step](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-05-changeset-light.png#only-light)
    ![Upload Dataset — Changeset step](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-05-changeset-dark.png#only-dark)

6.  A **Success** popup confirms the upload job was accepted. Select **Go to Jobs Page** to monitor its progress.

    ![Upload Dataset — Success popup](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-06-success-light.png#only-light)
    ![Upload Dataset — Success popup](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-06-success-dark.png#only-dark)

7.  A new **Dataset-Upload** entry will appear at the top of the Jobs list. Wait for the status to show **Completed**.

    ![Jobs page showing completed Dataset-Upload job](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-07-jobs-light.png#only-light)
    ![Jobs page showing completed Dataset-Upload job](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/upload-07-jobs-dark.png#only-dark)

    !!! info "This job may take a moment"

        Depending on the size of your dataset, the upload job may take anywhere from a few seconds to several minutes to complete. Refresh the Jobs list or the **Check Status** popup window periodically to check the status.

8.  The dataset will now be available in the **Datasets** section of the portal.

    ![TDEI Portal Datasets page](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/datasets-light.png#only-light)
    ![TDEI Portal Datasets page](../../../resources/images/tdei-portal/tutorial/curb-points-in-tdei/datasets-dark.png#only-dark)

For more details on working with datasets in the TDEI Portal, refer to the [Datasets](../user-manual/datasets.md) guide.

!!! success "You have now successfully converted and uploaded a curb ramp dataset to the TDEI!"
