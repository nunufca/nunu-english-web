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
