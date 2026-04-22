/**
 * extra.js
 *
 * Client-side enhancements for the TCAT Wiki Zensical site.
 *
 * Sections:
 *   1. Title Capitalization Data        — titleMapSource and derived titleMap lookup
 *   2. Text Transformation Helpers      — toTitleCase, applyTitleCapitalization
 *   3. DOM Fixup Functions              — fixElementCapitalization, fixNavigationCapitalization
 *   4. Initialization                   — event hooks, MutationObserver, periodic fallback
 *   5. Nav Order DOM Reordering         — sort nav <li> nodes by style.order for screen readers
 *   6. Consent Dialog Escape Dismissal  — Escape key closes dialog, saving state
 *   7. Footer Cookie-Settings Link      — move consent link after "Made with Zensical"
 *
 * @format
 */

// =============================================================================
// 1. Title Capitalization Data
// =============================================================================
//
// titleMapSource maps lowercase keys (space-separated) to their correctly
// capitalized display values. Keys with spaces automatically gain a dash
// variant in the expanded titleMap (e.g., "user manual" → "user-manual").
//
// Keep this in sync with $script:titleMap in utilities/generate-nav.ps1.

const titleMapSource = {
    // --- Acronyms & Technical Terms ---
    api: "API",
    bbox: "BBox",
    csv: "CSV",
    geojson: "GeoJSON",
    gtfs: "GTFS",
    ios: "iOS",
    ixn: "IXN",
    josm: "JOSM",
    json: "JSON",
    osm: "OSM",
    osw: "OSW",
    pbf: "PBF",
    sclio: "SCLIO",
    tcat: "TCAT",
    tdei: "TDEI",
    url: "URL",
    us: "US",

    // --- Products & Projects ---
    accessmap: "AccessMap",
    "aviv scoutroute": "AVIV ScoutRoute",
    opensidewalks: "OpenSidewalks",
    openstreetmap: "OpenStreetMap",
    "os connect": "OS-CONNECT",
    rapid: "Rapid",
    "tcat wiki": "TCAT Wiki",
    "tdei core": "TDEI Core",
    "tdei walkshed": "TDEI Walkshed",
    "tdei workspaces": "TDEI Workspaces",
    walksheds: "Walksheds",
    workspaces: "Workspaces",
    tm: "Tasking Manager",

    // --- UI & Navigation Terms ---
    "guides list": "Guides List",
    "how to": "How To",
    "log in": "Log In",
    "logging in": "Logging In",
    "qa qc": "QA/QC",
    "subreport a": "Subreport A",
    "user manual": "User Manual",

    // --- Events ---
    csun: "CSUN",
    csun26: "CSUN 2026",
    mny26: "Mappy New Year 2026",
    "nda vancouver": "Clark County Walk/Roll Event",
    "olympia connected": "Olympia, Connected",
    oswmh: "OpenSidewalks Mappy Hours",
    otp26: "OpenThePaths 2026",

    // --- Tutorials ---
    "osw in osmustm": "OSW in the OSM US TM",

    // --- Articles, Prepositions & Conjunctions ---
    a: "a",
    an: "an",
    and: "and",
    are: "are",
    as: "as",
    for: "for",
    in: "in",
    into: "into",
    is: "is",
    of: "of",
    on: "on",
    or: "or",
    the: "the",
    to: "to",
    via: "via",
    with: "with",
    your: "your",
};

/**
 * Expanded lookup that includes both space and dash variants of each key.
 * Generated automatically from titleMapSource — do not edit directly.
 */
const titleMap = Object.fromEntries(
    Object.entries(titleMapSource).flatMap(([key, value]) => {
        const entries = [[key, value]];
        // If key contains a space, also add the dash variant
        if (key.includes(" ")) {
            entries.push([key.replace(/ /g, "-"), value]);
        }
        return entries;
    })
);

// =============================================================================
// 2. Text Transformation Helpers
// =============================================================================

/**
 * Converts a string to Title Case.
 * Handles slash-separated words (e.g., "Walk/Roll") correctly.
 * @param {string} str - The string to convert
 * @returns {string} - The string in Title Case
 */
function toTitleCase(str) {
    // Match word characters including contractions (e.g., "What's", "don't")
    return str.replace(/\w+(?:'\w+)*/g, (word) => {
        return word.charAt(0).toUpperCase() + word.substr(1).toLowerCase();
    });
}

/**
 * Applies correct capitalization to a text string using titleMap.
 * Checks for an exact match first, then replaces known terms in-place,
 * and falls back to Title Case for any remaining unmatched text.
 * @param {string} text - The text to transform
 * @returns {string} - The text with correct capitalization
 */
function applyTitleCapitalization(text) {
    if (!text) return text;

    const trimmedText = text.trim();
    const lowerText = trimmedText.toLowerCase();

    // Check for exact match first (handles both space and dash variants)
    if (titleMap[lowerText]) {
        return titleMap[lowerText];
    }

    let result = trimmedText;

    // Placeholder slots for matched segments, keyed by index
    const replacements = [];

    // Pass 1: protect titleMapSource VALUES already present in the text
    // (e.g., text already contains "Clark County Walk/Roll Event" from frontmatter)
    for (const value of Object.values(titleMapSource)) {
        const escapedValue = value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
        const regex = new RegExp(`\\b${escapedValue}\\b`, "gi");
        result = result.replace(regex, (match) => {
            replacements.push({ original: match, replacement: value });
            return `\x00${replacements.length - 1}\x00`;
        });
    }

    // Pass 2: match titleMapSource KEYS (space/dash interchangeable) and replace
    for (const [key, value] of Object.entries(titleMapSource)) {
        const pattern = key.replace(/ /g, "[- ]");
        const regex = new RegExp(`\\b${pattern}\\b`, "gi");
        result = result.replace(regex, (match) => {
            replacements.push({ original: match, replacement: value });
            return `\x00${replacements.length - 1}\x00`;
        });
    }

    // Pass 3: apply Title Case to any remaining unmatched text
    result = toTitleCase(result);

    // Restore all placeholder slots with their canonical replacements
    replacements.forEach((r, i) => {
        result = result.replace(`\x00${i}\x00`, r.replacement);
    });

    return result;
}

// =============================================================================
// 3. DOM Fixup Functions
// =============================================================================

/**
 * Applies title capitalization to a single element's text content.
 * Iterates child text nodes to preserve mixed content (e.g., text + icons).
 * @param {Element} element - The DOM element to fix
 */
function fixElementCapitalization(element) {
    if (!element) return;

    Array.from(element.childNodes).forEach((node) => {
        if (node.nodeType === Node.TEXT_NODE && node.textContent.trim()) {
            const original = node.textContent;
            const fixed = applyTitleCapitalization(original);
            if (original !== fixed) {
                node.textContent = fixed;
            }
        }
    });
}

/**
 * Applies title capitalization to all navigation elements in the document.
 * Targets: top tabs, sidebar nav links, TOC entries, breadcrumbs, header topic.
 */
function fixNavigationCapitalization() {
    const selectors = [
        ".md-tabs__link", // Top navigation tabs
        ".md-nav__link", // Sidebar and TOC nav links
        ".md-path__link", // Breadcrumb links
        ".md-header__topic", // Header topic text
        ".md-ellipsis", // Truncated nav items
    ];

    document
        .querySelectorAll(selectors.join(", "))
        .forEach(fixElementCapitalization);
}

// =============================================================================
// 4. Initialization
// =============================================================================
//
// Runs fixNavigationCapitalization immediately and re-runs it on every
// possible navigation or DOM update event to handle Zensical's instant nav.

(function initCapitalizationFixes() {
    // Apply immediately and after short delays to catch async renders on load
    fixNavigationCapitalization();
    setTimeout(fixNavigationCapitalization, 100);
    setTimeout(fixNavigationCapitalization, 250);
    setTimeout(fixNavigationCapitalization, 500);

    // MutationObserver: re-apply whenever the DOM changes
    const observer = new MutationObserver(() => {
        requestAnimationFrame(fixNavigationCapitalization);
    });

    const startObserving = () => {
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            characterData: true,
            characterDataOldValue: false,
        });
    };

    if (document.body) {
        startObserving();
    } else {
        document.addEventListener("DOMContentLoaded", startObserving);
    }

    // Standard browser navigation events
    document.addEventListener("DOMContentLoaded", fixNavigationCapitalization);
    window.addEventListener("load", fixNavigationCapitalization);
    window.addEventListener("hashchange", fixNavigationCapitalization);
    window.addEventListener("popstate", fixNavigationCapitalization);

    // Zensical instant-loading custom event
    document.addEventListener("DOMContentSwitch", fixNavigationCapitalization);

    // Zensical location$ observable (if available)
    if (typeof location$ !== "undefined") {
        location$.subscribe(() => {
            setTimeout(fixNavigationCapitalization, 0);
            setTimeout(fixNavigationCapitalization, 100);
        });
    }

    // Periodic fallback for the first ~10 seconds after load
    let checkCount = 0;
    const periodicCheck = setInterval(() => {
        fixNavigationCapitalization();
        if (++checkCount >= 20) clearInterval(periodicCheck);
    }, 500);
})();

// =============================================================================
// 5. Nav Order DOM Reordering
// =============================================================================
//
// The CSS `order` property (applied per nav-item.html based on nav_order
// frontmatter) visually reorders sidebar nav items correctly, but CSS `order`
// does not change DOM order — the order screen readers and keyboard tab
// navigation follow. Zensical renders <li> elements alphabetically by filename
// regardless of TOML nav configuration.
//
// This function reads each item's style.order value and reappends children in
// that order, making DOM order match visual order (WCAG SC 1.3.2, SC 2.4.3).
//
// Loop prevention: if the list is already in sorted order the function returns
// without touching the DOM, so MutationObserver callbacks converge immediately.

(function sortNavByOrder() {
    function sortNavLists() {
        document.querySelectorAll(".md-nav__list").forEach((list) => {
            const items = Array.from(list.children);
            if (items.length < 2) return;

            const getOrder = (el) => {
                const v = parseInt(el.style.order, 10);
                return isNaN(v) ? 10000 : v;
            };

            // Check if already sorted — avoids unnecessary DOM mutations and
            // breaks the MutationObserver re-entry loop.
            let alreadySorted = true;
            for (let i = 1; i < items.length; i++) {
                if (getOrder(items[i]) < getOrder(items[i - 1])) {
                    alreadySorted = false;
                    break;
                }
            }
            if (alreadySorted) return;

            // Stable sort (Array.prototype.sort is stable since ES2019 /
            // all modern browsers) so items with equal order values keep their
            // original relative (alphabetical) position.
            items
                .slice()
                .sort((a, b) => getOrder(a) - getOrder(b))
                .forEach((item) => list.appendChild(item));
        });
    }

    // Run immediately and after short delays to catch async renders on load.
    sortNavLists();
    setTimeout(sortNavLists, 100);
    setTimeout(sortNavLists, 250);
    setTimeout(sortNavLists, 500);

    // MutationObserver: re-sort whenever nav DOM changes (e.g., after instant
    // navigation inserts a new nav tree). The "already sorted" guard above
    // prevents infinite loops.
    const observer = new MutationObserver(() => {
        requestAnimationFrame(sortNavLists);
    });

    const startObserving = () => {
        observer.observe(document.body, {
            childList: true,
            subtree: true,
        });
    };

    if (document.body) {
        startObserving();
    } else {
        document.addEventListener("DOMContentLoaded", startObserving);
    }

    // Standard browser navigation events.
    document.addEventListener("DOMContentLoaded", sortNavLists);
    window.addEventListener("load", sortNavLists);
    window.addEventListener("popstate", sortNavLists);

    // Zensical instant-loading custom event.
    document.addEventListener("DOMContentSwitch", sortNavLists);

    // Zensical location$ observable (if available).
    if (typeof location$ !== "undefined") {
        location$.subscribe(() => {
            setTimeout(sortNavLists, 0);
            setTimeout(sortNavLists, 100);
        });
    }

    // Periodic fallback for the first ~10 seconds after load.
    let checkCount = 0;
    const periodicCheck = setInterval(() => {
        sortNavLists();
        if (++checkCount >= 20) clearInterval(periodicCheck);
    }, 500);
})();

// =============================================================================
// 6. Consent Dialog Escape Key Dismissal
// =============================================================================
//
// The ARIA Authoring Practices Guide dialog pattern requires Escape to close a
// modal dialog. Zensical's consent dialog has no native key handler, leaving
// users who press Escape with no response. We add a keydown listener that
// clicks the "Save" button when Escape is pressed while the dialog is open,
// saving the user's current checkbox state and closing the dialog.

(function consentEscapeDismiss() {
    document.addEventListener("keydown", function (event) {
        if (event.key !== "Escape") return;
        const dialog = document.querySelector(
            '[data-md-component="consent"]:not([hidden])'
        );
        if (!dialog) return;
        // Target the primary "Save" button, not the "Reject All" reset button
        const saveButton = dialog.querySelector(
            '.md-consent__controls .md-button:not([type="reset"])'
        );
        if (saveButton) {
            saveButton.click();
        }
    });
})();

// =============================================================================
// 7. Footer Cookie-Settings Link Relocation
// =============================================================================
//
// The "Change cookie settings" link is hard-coded inside
// .md-copyright__highlight (the copyright line). Move it to the end of
// .md-copyright so it renders after "Made with Zensical".

(function relocateCookieLink() {
    function move() {
        const link = document.querySelector(
            '.md-copyright__highlight a[href$="#__consent"]'
        );
        const copyright = document.querySelector(".md-copyright");
        if (link && copyright && link.parentElement !== copyright) {
            // Trim trailing whitespace inside the Zensical link (its inner HTML has
            // a trailing newline+spaces that render as an unwanted space after the link)
            const zensicalLink = copyright.querySelector(
                'a[href*="zensical.org"]'
            );
            if (zensicalLink) {
                const lastNode = zensicalLink.lastChild;
                if (lastNode && lastNode.nodeType === Node.TEXT_NODE) {
                    lastNode.textContent = lastNode.textContent.trimEnd();
                }
            }
            // Trim trailing whitespace from .md-copyright before appending
            const last = copyright.lastChild;
            if (last && last.nodeType === Node.TEXT_NODE) {
                last.textContent = last.textContent.trimEnd();
            }
            // Two non-breaking spaces on each side of the bullet for consistent padding
            copyright.appendChild(
                document.createTextNode("\u00A0\u00A0\u2022\u00A0\u00A0")
            );
            copyright.appendChild(link);
        }
    }
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", move);
    } else {
        move();
    }
})();
