# Website UX / Design / Content Beautification Plan

Date: 2026-03-08

## 1) Goals
- Make the site feel more polished, coherent, and “designed” without adding new pages or expanding scope.
- Improve usability on mobile/keyboard and reduce friction in navigation.
- Improve clarity of messaging (what you do, what you build, how to reach you) while staying concise.
- Keep the current lightweight/static approach.

## 2) Hard Requirement (Non-Negotiable)
**Links to lœrn data security / privacy statements must remain untouched.**

Practical interpretation for implementation:
- Do **not** change the URL targets (the `href` values) of any lœrn privacy/data-security statement links.
- Cosmetic changes (styling, surrounding layout, headings) are allowed **only if** the exact `href` targets remain identical.

### Protected link patterns (must remain identical)
These are the links currently used and likely “wired” into the app / store listing / deep links:
- The lœrn privacy statement pages by locale:
  - `/de/projects/loern/privacy.html`
  - `/en/projects/loern/privacy.html`
  - `/es/projects/loern/privacy.html`
  - `/fr/projects/loern/privacy.html`
  - `/it/projects/loern/privacy.html`
  - `/nl/projects/loern/privacy.html`
- The lœrn project page CTA link (relative form) used on each locale’s lœrn page:
  - `href="loern/privacy.html"`

> If you confirm there are additional “wired” URLs (e.g., a separate “data security statement” page), add them to this protected list and treat them the same way.

### Mandatory verification step (for every PR/change set)
Before and after changes, verify protected links are unchanged:
- `grep -R --line-number 'href="loern/privacy.html"' .`
- `grep -R --line-number 'projects/loern/privacy.html' .`

Acceptance criteria for this requirement:
- The set of `href` targets for protected links is **byte-for-byte identical** before vs after.

## 3) Current Observations (Baseline)
These are the most impactful issues found during review:
- **Mobile header layout is partially implemented but not applied:** CSS expects a `.header-content` wrapper for responsive stacking, but the HTML headers don’t include it. Mobile can feel cramped.
- **Language preference isn’t persisted:** root redirect page reads `localStorage("jd_lang")`, but language switchers do not write it.
- **No active navigation state:** CSS supports `.active`, but pages don’t apply it—orientation cost is higher than necessary.
- **Keyboard focus styling is minimal:** hover states exist, but keyboard users don’t get an equally polished experience.
- **Visual hierarchy in the nav is flat:** all items are orange pills; there’s no single primary action.

## 4) Definition of Done (Project-Level)
- Navigation and language switching are consistent and predictable across all locales.
- Mobile header doesn’t overflow; primary actions remain reachable.
- Clear visible focus state for keyboard navigation.
- Copy is tightened to reduce repetition and increase clarity.
- Translation/locale polish issues removed (no stray English strings in non-English pages).
- **Protected lœrn privacy/data-security links are unchanged.**

## 5) Work Plan (Phased Backlog)
Each task includes concrete steps and acceptance criteria.

Execution note:
- This repo is duplicated static HTML per locale. For Phase 1 + Phase 3 in particular, prefer deterministic, repetitive edits (either scripted or carefully applied search/replace) to avoid locale drift.
- For every change set: run the protected-link verification greps and ensure the output matches the baseline.

File map (what exists today)
- Root:
   - `/index.html` (redirect + language detection)
   - `/style.css`
- Locales (same structure for `de`, `en`, `es`, `fr`, `it`, `nl`):
   - `/<lang>/index.html`
   - `/<lang>/about.html`
   - `/<lang>/projects.html`
   - `/<lang>/principles.html`
   - `/<lang>/contact.html`
   - `/<lang>/projects/loern.html`
   - `/<lang>/projects/loern/privacy.html` (protected statement page; do not change statement URL)
   - `/<lang>/legal/imprint.html`
   - `/<lang>/legal/privacy.html`

### Phase 0 — Safety & Baseline (0.5 day)

#### Task 0.1 — Baseline snapshot and link inventory
**Why:** Make sure changes don’t break the wired lœrn privacy links and provide a rollback reference.

Steps:
1. Record (copy/paste) outputs of the two `grep` checks under “Mandatory verification”.
2. Optionally take screenshots (desktop + mobile) of:
   - Home, Projects, lœrn project page, lœrn privacy page.

Acceptance criteria:
- Baseline `grep` outputs are saved in the PR description or a short note.
- Protected link targets are explicitly confirmed.

---

### Phase 1 — Navigation & Header Coherence (1–2 days)

#### Task 1.1 — Apply the intended header layout wrapper
**Why:** Fix mobile layout consistency and align header with page grid.

Steps:
1. Update all pages to wrap header content with:
   - `<div class="header-content">…</div>` inside `.site-header`.
2. Ensure `brand` and `main-nav` live inside `.header-content`.
3. Confirm header max-width aligns with main content (1120px) while background can remain full-width.

Acceptance criteria:
- On ≤768px width, header items stack as intended (no overlap, no clipped controls).
- On desktop widths, brand and nav align with the page content width.
- No layout shift in the main content due to header changes.

#### Task 1.2 — Persist chosen language for future redirects
**Why:** User intent should win over browser language.

Steps:
1. In each page’s language switcher `change` handler, set:
   - `localStorage.setItem("jd_lang", lang)` in a try/catch.
2. Keep current navigation logic (it’s fine) but add the persistence write.

Acceptance criteria:
- After choosing a language (e.g., FR), visiting `/` later redirects to that language.
- If localStorage is unavailable, switching still works (no JS errors).

#### Task 1.3 — Add active page state in nav
**Why:** Reduce orientation cost and make the site feel more “finished.”

Implementation options (pick one):
- **Option A (static):** add `class="active"` to the relevant anchor on each page.
- **Option B (JS):** compute current path and apply `.active` automatically.

Acceptance criteria:
- Exactly one main navigation item shows as active on each page.
- Active state works in all locales and for nested pages (e.g., `/en/projects/loern.html`).

#### Task 1.4 — Simplify visual hierarchy in nav (CTA)
**Why:** All-orange pills compete equally; a single CTA improves clarity.

Steps:
1. Apply existing `.nav-cta` styling to one item (recommend: Contact).
2. Reduce emphasis on other nav items (e.g., less shadow, slightly more muted styling) *without introducing new colors*.

Acceptance criteria:
- One obvious “primary” navigation action exists.
- Non-CTA items remain readable and consistent.

---

### Phase 2 — Typography, Spacing, and Component Polish (1–2 days)

#### Task 2.1 — Improve long-form readability (line length + rhythm)
**Why:** The site is content-forward; readability is the design.

Steps:
1. Keep `.page.narrow` for text-heavy pages.
2. On wide pages (home), consider limiting paragraph measure (e.g., max-width in characters for text blocks) while keeping the overall page width.
3. Audit vertical spacing between sections and headings for consistency.

Acceptance criteria:
- Paragraph line length stays in a comfortable range (roughly 60–80 characters per line on desktop).
- Headings/sections feel evenly spaced (no cramped blocks, no excessive whitespace).

#### Task 2.2 — Standardize card and badge styling
**Why:** Project cards are good; they can feel more deliberate.

Steps:
1. Normalize border radius + padding tokens (keep existing palette and subtle borders).
2. Ensure card typography hierarchy: badge → title → description → link.

Acceptance criteria:
- All `.project-card` instances look consistent across pages and locales.
- Links inside cards are clearly discoverable.

---

### Phase 3 — Accessibility & Interaction Quality (0.5–1 day)

#### Task 3.1 — Add `:focus-visible` styles for interactive elements
**Why:** Keyboard users need a clear focus ring; it’s also a “quality” signal.

Steps:
1. Add a visible focus outline for:
   - `a`, `button`, `select`, and any `.btn` / `.loern-btn`.
2. Ensure focus styles don’t rely on color alone (outline + offset).

Acceptance criteria:
- Tabbing through the header clearly shows focus location.
- Focus styles appear for keyboard navigation but do not appear aggressively on mouse click (use `:focus-visible`).

#### Task 3.2 — Add a skip link
**Why:** Fixed headers + keyboard navigation benefit from a skip-to-content link.

Steps:
1. Add `<a class="skip-link" href="#main">Skip to content</a>` at top of body.
2. Add `id="main"` to the `<main>` element.
3. Style skip link to appear on focus only.

Acceptance criteria:
- Skip link is reachable via keyboard and jumps past the fixed header.
- Skip link is visually hidden until focused.

---

### Phase 4 — Content Tightening & Trust Signals (1–2 days)

#### Task 4.1 — Reduce repetition across Home/About/Principles
**Why:** The message is good, but it repeats; tightening increases impact.

Steps:
1. Rewrite the Home lead to be more concrete (what you build + for whom).
2. On About, add a short “What to expect” section (still concise) and remove redundant AI statements.
3. Keep Principles as the “philosophy source of truth”; avoid restating the same paragraphs elsewhere.

Acceptance criteria:
- Home/About each has a distinct purpose and minimal repeated sentences.
- Each page answers a user question quickly:
  - Home: “What do you do?”
  - About: “Who are you / how do you operate?”
  - Principles: “What do you believe / optimize for?”

#### Task 4.2 — Strengthen the Projects → lœrn conversion path
**Why:** Projects page is minimal; add clarity without bloat.

Steps:
1. Add 1–2 bullets or short lines that summarize:
   - offline-first, no accounts, on-device data (matching lœrn messaging)
2. Keep CTA clear.

Acceptance criteria:
- Projects page explains lœrn value in <10 seconds of scanning.
- No new pages or complex components introduced.

---

### Phase 5 — Localization QA Pass (0.5–1 day)

#### Task 5.1 — Remove translation leaks and normalize terminology
**Why:** Small i18n inconsistencies undermine polish.

Steps:
1. Search for English strings inside non-English folders (e.g., “Bring your own Content”).
2. Ensure consistent translation of:
   - privacy statement / Datenschutz / confidentialité…
   - offline-first
   - premium

Acceptance criteria:
- No obvious English strings remain in non-English pages unless intentionally kept as a brand/product term.
- Navigation labels remain consistent across all pages in each locale.

---

## 5A) Implementation Checklist (Mechanical, File-by-File)
This section translates each task into concrete file targets, edit recipes, and verification steps.

### Task 0.1 — Baseline snapshot and protected-link inventory
Concrete file targets:
- All locale lœrn pages: `*/projects/loern.html`
- All locale lœrn privacy statement pages: `*/projects/loern/privacy.html`

Commands to capture (before and after every PR):
- `grep -R --line-number 'href="loern/privacy.html"' .`
- `grep -R --line-number 'projects/loern/privacy.html' .`

Acceptance criteria:
- The `href` targets reported by these greps are unchanged.

### Task 1.1 — Add `.header-content` wrapper inside `.site-header`
Concrete file targets:
- All locale HTML pages that have `<header class="site-header">` (54 files total).
- Do not change `/index.html` (root redirect) because it has no site header.

Edit recipe:
1. In each target file, find:
    - `<header class="site-header">`
2. Wrap the existing header contents (brand + nav) with:
    - `<div class="header-content"> … </div>`

Verification checklist:
- Desktop: header content aligns to the same left/right as `.page`.
- Mobile (≤768px): brand and nav stack cleanly, controls are not clipped.
- Protected-link greps still match baseline.

### Task 1.2 — Persist `jd_lang` in language switcher
Concrete file targets:
- All locale HTML pages with a `lang-switch` `change` handler (practically: the same 54 files).

Edit recipe:
- In the `lang-switch` handler, after `var lang = this.value;`, add:
   - `try { localStorage.setItem("jd_lang", lang); } catch (e) {}`

Verification checklist:
- Switch to a non-default locale, then visit `/` and confirm the redirect respects the chosen language.
- No JS errors if localStorage is blocked.

### Task 1.3 — Active navigation state
Recommended approach: **shared JS** (avoids per-page manual `.active`).

Concrete file targets:
- New file: `/site.js`
- Update all 54 locale HTML files to include `site.js` with the correct relative path.

Include path rules (by folder depth):
- `/<lang>/*.html` → `<script src="../site.js"></script>`
- `/<lang>/legal/*.html` → `<script src="../../site.js"></script>`
- `/<lang>/projects/*.html` → `<script src="../../site.js"></script>`
- `/<lang>/projects/loern/*.html` → `<script src="../../../site.js"></script>`

Implementation outline for `site.js`:
- Determine page “key” from `location.pathname` (home/about/projects/principles/contact).
- Add `.active` to the matching `.main-nav a`.

Verification checklist:
- For each locale, verify exactly one nav item is active on:
   - `/<lang>/`
   - `/<lang>/about.html`
   - `/<lang>/projects.html`
   - `/<lang>/projects/loern.html`

### Task 1.4 — Nav CTA hierarchy (Contact)
Concrete file targets:
- All locale HTML pages (54 files): add `class="nav-cta"` to the Contact anchor.

Edit recipe:
- Change the Contact link from:
   - `<a href="contact.html">…</a>`
- To:
   - `<a href="contact.html" class="nav-cta">…</a>`

Verification checklist:
- Contact is visually primary in the header.
- Other nav items are still readable.

### Task 2.1 — Readability improvements (measure + rhythm)
Concrete file targets:
- `/style.css`

Edit recipe (CSS-only):
- Constrain paragraph measure on wide layouts without changing page width, e.g. via:
   - applying a `max-width` to text blocks (lead + paragraphs) inside `.page` sections
   - keeping existing tokens/palette (no new color system)

Verification checklist:
- On large screens, home text doesn’t span too wide.
- On mobile, nothing becomes cramped.

### Task 2.2 — Card + badge standardization
Concrete file targets:
- `/style.css`
- Spot-check pages:
   - `*/index.html` and `*/projects.html`

Edit recipe:
- Normalize padding/radius/shadow for `.project-card` and `.status-badge`.
- Ensure link styling inside cards remains discoverable.

Verification checklist:
- Cards look consistent across locales.

### Task 3.1 — Focus-visible styles
Concrete file targets:
- `/style.css`

Edit recipe:
- Add `:focus-visible` styles for `a`, `select`, and button-like classes.

Verification checklist:
- Keyboard tabbing shows clear focus throughout header and CTAs.

### Task 3.2 — Skip link + `id="main"`
Concrete file targets:
- All 54 locale HTML files.
- `/style.css`

Edit recipe:
1. Immediately after `<body>`, insert:
    - `<a class="skip-link" href="#main">Skip to content</a>`
2. Add `id="main"` to the `<main …>` tag.
3. Style `.skip-link` to be visually hidden unless focused.

Verification checklist:
- Skip link appears on first Tab and jumps past the fixed header.

### Task 4.1 — Copy tightening across Home/About/Principles
Concrete file targets:
- `*/index.html`, `*/about.html`, `*/principles.html` across all locales.

Recommended approach:
- Extend `/scripts/update_positioning.py` (already in repo) to apply deterministic copy updates per locale, then review each locale for tone.

Verification checklist:
- Home/About read as distinct and not repetitive.

### Task 4.2 — Projects → lœrn conversion improvements
Concrete file targets:
- `*/projects.html` across all locales.

Edit recipe:
- Add 1–2 very short bullets/lines under the lœrn card describing: offline-first, no accounts, on-device data.

Verification checklist:
- Projects page remains brief.

### Task 5.1 — Localization QA + translation leak fixes
Concrete file targets:
- All non-English locales (`de`, `es`, `fr`, `it`, `nl`) across all pages.

Known concrete fix to include:
- `de/projects/loern.html`: replace the leaked English feature label “Bring your own Content” with a German equivalent.

Verification commands:
- `grep -R --line-number 'Bring your own' de es fr it nl`
- `grep -R --line-number 'Privacy statement' de es fr it nl`

Acceptance criteria:
- No unintended English strings remain in non-English pages.

---

## 6) Risks / Things to Avoid
- Do not introduce heavy JS frameworks, build steps, or new design systems.
- Do not change URL structures, especially protected lœrn privacy/data-security statement links.
- Avoid “design by addition”: prefer refinement of existing components.

## 7) Suggested Execution Order (Shortest Path to Visible Improvement)
1. Phase 1.1 (header wrapper) + 1.2 (language persistence)
2. Phase 1.3 (active nav)
3. Phase 3.1 (focus-visible) + 3.2 (skip link)
4. Phase 2.1/2.2 (readability + cards)
5. Phase 5.1 (localization QA)
6. Phase 4.x (copy pass)

## 8) Ownership / Checklist for Review
For each change set, reviewers confirm:
- Protected lœrn privacy/data-security `href`s unchanged (grep checks passed).
- Mobile header: no overlap, selects usable.
- Keyboard navigation: clear focus state.
- All locales still navigate correctly.

## Appendix A — Suggested PR Breakdown (All Phases)
To keep reviews fast and risk low:
1. PR A: Task 0.1 + 1.1 + 1.2 (header wrapper + language persistence)
2. PR B: Task 1.3 + 1.4 (active nav + CTA hierarchy)
3. PR C: Task 3.1 + 3.2 (focus-visible + skip link)
4. PR D: Task 2.1 + 2.2 (readability + cards)
5. PR E: Task 5.1 (localization QA)
6. PR F: Task 4.1 + 4.2 (copy tightening + projects messaging)

Each PR must include the protected-link grep outputs.

## Appendix B — QA Matrix (Representative Checks)
For each locale (`de`, `en`, `es`, `fr`, `it`, `nl`), check desktop + mobile:
- `/<lang>/`
- `/<lang>/about.html`
- `/<lang>/projects.html`
- `/<lang>/projects/loern.html`
- `/<lang>/projects/loern/privacy.html` (verify protected `href`s unchanged)
- `/<lang>/legal/privacy.html`

Interactions:
- Keyboard: Tab through header and CTAs; focus always visible.
- Mobile: page dropdown + language switcher are usable.
- Root redirect: language preference is respected after setting it.
