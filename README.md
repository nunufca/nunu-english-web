# Teacher Nu English Academy

A buildless static website with four pages: Home, Courses, Placement Test, and Registration.

## Preview locally

From this directory, run:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. You can also open `index.html` directly in a browser.

## Structure

- `index.html` — Home
- `courses.html` — Courses
- `placement-test.html` — Placement Test preview
- `registration.html` — Registration preview
- `assets/styles.css` — Shared responsive styling
- `assets/favicon.svg` — Academy monogram

All content is illustrative placeholder copy. Placement Test and Registration controls are disabled. There is no backend, scoring, submission, storage, analytics, or external dependency. No build step is required.

For static hosting, serve this directory as the site root. Deployment has not been configured.

## Downloading and opening on Samsung DeX / Android

Download the ZIP from the PR branch (`scaffold-teacher-nu-website`), rather than `main` until this PR is merged. Extract the entire ZIP before opening `index.html`. Keep the four HTML pages together so navigation can find sibling pages.

The original HTML links used `assets/styles.css` (plural), and the repository file had that exact name and case. `assets/style.css` (singular) is a different filename. No root-relative paths or external fonts are required.

Android file managers may open HTML through a restricted `content://` address or a document preview that cannot load sibling CSS files. This can produce an unstyled page even when the relative path is correct. The exact behavior depends on the file manager and browser. Each page now embeds the shared CSS, so its styling does not require access to `assets/`. The favicon is optional and still uses a relative file path.

For full navigation, use a normal browser with the extracted folder served over local HTTP (for example, the Python command above in an environment with Python installed). A file manager's document preview may still prevent navigation between HTML files or may not render HTML at all; embedding CSS cannot change those permissions. No hosting or deployment is needed for local HTTP preview.

## Editing styles

`assets/styles.css` is the source of truth. After editing it, run:

```sh
python3 scripts/sync_styles.py
python3 scripts/sync_styles.py --check
```

Commit the updated HTML files with the CSS. Visitors do not need Python or a build step; the checked-in HTML already contains its styles.
