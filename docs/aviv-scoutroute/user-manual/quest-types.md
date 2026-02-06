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

This guide provides a detailed reference for each quest input type you'll encounter in AVIV ScoutRoute.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

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

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Single select quest example | ../../resources/images/aviv-scoutroute/android/quest-single-select-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Single select quest example | ../../resources/images/aviv-scoutroute/android/quest-single-select-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Single select quest example | ../../resources/images/aviv-scoutroute/ios/quest-single-select-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Single select quest example | ../../resources/images/aviv-scoutroute/ios/quest-single-select-light.png#only-light{ width="300" } -->

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

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Numeric entry quest example | ../../resources/images/aviv-scoutroute/android/quest-numeric-entry-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Numeric entry quest example | ../../resources/images/aviv-scoutroute/android/quest-numeric-entry-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Numeric entry quest example | ../../resources/images/aviv-scoutroute/ios/quest-numeric-entry-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Numeric entry quest example | ../../resources/images/aviv-scoutroute/ios/quest-numeric-entry-light.png#only-light{ width="300" } -->

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

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Multi-select quest example | ../../resources/images/aviv-scoutroute/android/quest-multi-select-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Multi-select quest example | ../../resources/images/aviv-scoutroute/android/quest-multi-select-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Multi-select quest example | ../../resources/images/aviv-scoutroute/ios/quest-multi-select-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Multi-select quest example | ../../resources/images/aviv-scoutroute/ios/quest-multi-select-light.png#only-light{ width="300" } -->

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

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Free-form text quest example | ../../resources/images/aviv-scoutroute/android/quest-free-form-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Free-form text quest example | ../../resources/images/aviv-scoutroute/android/quest-free-form-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Free-form text quest example | ../../resources/images/aviv-scoutroute/ios/quest-free-form-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Free-form text quest example | ../../resources/images/aviv-scoutroute/ios/quest-free-form-light.png#only-light{ width="300" } -->

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

### Quest Type Summary

| Quest Type           | Input Method         | When to Use                               |
|:---------------------|:---------------------|:------------------------------------------|
| **Exclusive Choice** | Tap one option       | When only one answer can be correct       |
| **Numeric Entry**    | Keypad input         | For measurements and counts               |
| **Multi-Select**     | Tap multiple options | When multiple conditions may apply        |
| **Free-Form Text**   | Keyboard input       | For descriptions and "Other" explanations |

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
