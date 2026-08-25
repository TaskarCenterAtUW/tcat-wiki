---
title: Add Points Extension Dataset in Walksheds
tags:
	- Tutorial
	- External
	- User
---

<!-- @format -->

## Add Points Extension Dataset in Walksheds

This tutorial explains how to convert a GTFS feed's bus stop points to OpenSidewalks (OSW) format, upload it to the TDEI Portal, and display it as an extension (overlay) dataset in Walksheds.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Step 1: Acquire GTFS Data

Download a GTFS feed that includes the bus stops (`stops.txt`) you want to display.

As an example, this guide will use the [King County Metro GTFS feed](https://www.soundtransit.org/GTFS-KCM/google_transit.zip) from [Sound Transit's Open Transit Data](https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd/otd-downloads) page.

---

### Step 2: Convert GTFS Data to OSW Format

Convert the `stops.txt` into OpenSidewalks [Points](../../opensidewalks/schema/index.md#points).

1. Use the [GTFS-to-TDEI Converter](https://github.com/TaskarCenterAtUW/tdei-tools/blob/main/utilities/gtfs_to_tdei_converter.py) utility.

2. Run the converter with the GTFS ZIP file as the input:

    ```text
    python utilities/gtfs_to_tdei_converter.py "C:/data/google_transit.zip"
    ```

    To save the output in a specific directory, add the `-o` option:

    ```text
    python utilities/gtfs_to_tdei_converter.py "C:/data/google_transit.zip" --o "C:/data/output"
    ```

    The converter creates a dated OSW ZIP package named `YYYY-MM-DD_GTFS_OSW.zip`. This package contains the bus stop points as an OSW GeoJSON file.

---

### Step 3: Upload the OSW Dataset to TDEI

1. Open the [Upload Dataset](https://portal.tdei.us/UploadDataset) page in the TDEI Portal after signing in.

2. Follow the upload workflow to attach the generated `YYYY-MM-DD_GTFS_OSW.zip` file, provide the required dataset information, and submit the upload.

    ![TDEI Portal Upload Dataset page with the generated GTFS OSW ZIP file attached](../../resources/images/walksheds/tutorial/extension-dataset/01-tdei-portal-upload-light.avif#only-light)
    ![TDEI Portal Upload Dataset page with the generated GTFS OSW ZIP file attached](../../resources/images/walksheds/tutorial/extension-dataset/01-tdei-portal-upload-dark.avif#only-dark)

3. Open [Datasets](https://portal.tdei.us/datasets) and confirm that the uploaded dataset appears in the dataset list.

    ![TDEI Portal Datasets page showing the uploaded KCM GTFS OSW dataset](../../resources/images/walksheds/tutorial/extension-dataset/02-tdei-portal-datasets-light.avif#only-light)
    ![TDEI Portal Datasets page showing the uploaded KCM GTFS OSW dataset](../../resources/images/walksheds/tutorial/extension-dataset/02-tdei-portal-datasets-dark.avif#only-dark)

---

### Step 4: Select the Extension Dataset in Walksheds

1.  Open [Walksheds](https://walkshed.tdei.us/) and sign in.

2.  Open the Walksheds settings and select the base TDEI dataset for your analysis.

3.  Under **Select an extension TDEI dataset (overlay)**, select the uploaded GTFS dataset. Confirm that **Points** is checked under **Available extensions**.

    ![Walksheds settings showing a selected base dataset, the KCM GTFS extension dataset, and Points listed as an available extension](../../resources/images/walksheds/tutorial/extension-dataset/03-walksheds-settings-light.avif#only-light)
    ![Walksheds settings showing a selected base dataset, the KCM GTFS extension dataset, and Points listed as an available extension](../../resources/images/walksheds/tutorial/extension-dataset/03-walksheds-settings-dark.avif#only-dark)

4.  Select **Build Router** and wait for the router to finish building, then reload the page when instructed.

    !!! info "This job may take a while!"

        Depending on the size of your selected datasets, this step may take anywhere from a few seconds to 15+ minutes to complete.

---

### Step 5: Display the Bus Stop Points

1. Open **Map Legend** and expand **Points**.

2. Select the visibility control for **Points** to display the extension dataset on the map.

    <div class="only-light">
    <img-comparison-slider>
        <img class="off-glb" slot="first" src="../../resources/images/walksheds/tutorial/extension-dataset/04-walksheds-points-off-light.avif" alt="Walksheds map with the Points extension overlay hidden" />
        <img class="off-glb" slot="second" src="../../resources/images/walksheds/tutorial/extension-dataset/05-walksheds-points-on-light.avif" alt="Walksheds map with the Points extension overlay visible" />
    </img-comparison-slider>
    </div>
    <div class="only-dark">
    <img-comparison-slider>
        <img class="off-glb" slot="first" src="../../resources/images/walksheds/tutorial/extension-dataset/04-walksheds-points-off-dark.avif" alt="Walksheds map with the Points extension overlay hidden" />
        <img class="off-glb" slot="second" src="../../resources/images/walksheds/tutorial/extension-dataset/05-walksheds-points-on-dark.avif" alt="Walksheds map with the Points extension overlay visible" />
    </img-comparison-slider>
    </div>

3. Confirm that the bus stop points from the extension dataset appear on the map.

!!! success "The bus stop extension dataset's points are now displayed in Walksheds."
