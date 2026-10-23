---
title: Quest Types
nav_order: 5
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Quest Types

This section provides a detailed reference for each quest input type you'll encounter in AVIV ScoutRoute.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

While completing quests in AVIV ScoutRoute, you'll encounter different types of questions depending on what kind of information needs to be collected. Each question type requires a different form of input.

---

### Exclusive Choice (Single Choice)

**Purpose:** Choose exactly one answer that best represents your observation.

**How to answer:**

1. Review all available options
2. Tap an image or button to select your answer
3. The selected option will be highlighted with a **pink border**
4. Tap a different option to change your selection
5. Tap **Submit** when ready

**Example questions:**

- "What is this sidewalk's surface type?" (Concrete / Asphalt / Brick / Other)
- "Is there a curb ramp at this location?" (Yes / No)
- "What type of crossing markings are present?" (Zebra / Ladder / None / Other)

!!! tip

    If none of the options perfectly match what you observe, choose the closest reasonable match or skip the question if none of the options apply. If an "Other" option is available, select it and there may be an option to provide details in a follow-up text field.

---

### Numeric (Number Entry)

**Purpose:** Enter a specific numeric value for a measurement or count.

**How to answer:**

1. Read the question and note the expected unit (inches, feet, meters, etc.)
2. Use the on-screen keypad to enter the value
3. Verify your entry matches the requested unit
4. Tap **Submit** when ready

When a quest defines a minimum or maximum, an out-of-range value will result in the display of a validation message.

![Android numeric quest showing a value below the minimum and its validation message](../../resources/images/aviv-scoutroute/user-manual/06-quest-types/04-numeric-error-min-dark.avif){ .img-contained .img-inline style="--img-width: 25%;" } ![Android numeric quest showing a value above the maximum and its validation message](../../resources/images/aviv-scoutroute/user-manual/06-quest-types/05-numeric-error-max-dark.avif){ .img-contained .img-inline style="--img-width: 25%;" }
{: .img-row }

**Example questions:**

- "How wide is this sidewalk, in inches?"
- "How many streetlights are along this block?"
- "What is the slope percentage along this segment?"

!!! warning

    Pay careful attention to the **unit** specified in the question. Entering a measurement in the wrong unit will result in incorrect data.

---

### Multiple Choice

**Purpose:** Select one or more applicable options for questions where multiple answers may apply.

**How to answer:**

1. Review all available options
2. Tap each option that applies - selected items show a **pink border**
3. Tap a selected option again to deselect it
4. Select as many or as few options as applicable
5. Tap **Submit** when ready

**Example questions:**

- "What types of obstructions are present along this sidewalk?" (Utility poles / Overgrown vegetation / Parked vehicles / Construction barriers / None)
- "What accessibility features are present at this corner?" (Curb Ramps / Tactile Paving / Sound Signals / None)

!!! note

    For multi-select questions, it's important to select **all** applicable options, not just one.

---

### Text Entry (Free-Form / Short Answer)

**Purpose:** Provide a short description or additional details when predefined options aren't sufficient.

**How to answer:**

1. Tap the text input field
2. Type your response using the on-screen keyboard
3. Keep your response concise (maximum **255 characters**)
4. Tap **Submit** when ready

**When you may encounter this:**

- After selecting "Other" for a choice question
- When asked to describe an unusual condition
- When additional context would be helpful
- When qualitative descriptions are needed

**Example prompts:**

- "Please describe the surface material" (after selecting "Other" for surface type)
- "Describe any additional obstructions observed"

!!! tip

    Be specific but concise. Include details that would help someone understand the situation, such as "Left side asphalt, right side concrete" rather than "Two surface materials"

---

### Photo Requests

Some quests ask for a photo of the feature or location. Select **Please take a photo of the location**, use the camera screen to capture an image, and confirm it to return to the quest. The quest screen can show an upload confirmation; if a previous photo is present, the form may offer options to retake or remove it.

![Curb question with a location photo request and the Submit button](../../resources/images/aviv-scoutroute/user-manual/06-quest-types/01-photo-quest-light.avif){ .img-contained .img-inline style="--img-width: 25%;" }
![AVIV ScoutRoute camera screen ready to capture a location photo](../../resources/images/aviv-scoutroute/user-manual/06-quest-types/02-photo-capture-dark.avif){ .img-contained .img-inline style="--img-width: 25%;" }
![Curb question after a photo was uploaded successfully](../../resources/images/aviv-scoutroute/user-manual/06-quest-types/03-photo-success-light.avif){ .img-contained .img-inline style="--img-width: 25%;" }
{: .img-row }

Photo requests depend on the quest definition; not every quest asks for a photo. Follow project instructions for what may be photographed.

---

### Quest Type Summary

| Quest type           | Input method                             | When to use                                  |
| :------------------- | :--------------------------------------- | :------------------------------------------- |
| **Exclusive Choice** | Select one option                        | When one answer is requested                 |
| **Numeric Entry**    | Enter a number with the on-screen keypad | For measurements and counts                  |
| **Multi-Select**     | Select each applicable option            | When multiple conditions may apply           |
| **Free-Form Text**   | Enter a short response                   | For descriptions and "Other" explanations    |
| **Photo request**    | Capture or attach a location photo       | When the quest asks for visual documentation |

---

### What Happens After Submitting

After you submit a quest:

1. Your response is saved to the workspace
2. The quest icon disappears from the map
3. The data becomes part of the dataset

!!! success

    Thank you! Your contributions directly help improve navigation tools like AccessMap and support better pedestrian infrastructure planning!

---

### Next Steps

- Learn about [App Settings](app-settings.md) for customizing your experience
