# Public Domain Pulp website

Complete Astro static-site preview: eight books, three series, author catalogs, About, Journal, Community, contact and utility pages. Calder City Book Three is deliberately absent.

## Review without installing anything

Open `preview/full-site/index.html` in your browser, or unzip `PublicDomainPulp_Website_Preview.zip` and open `index.html`. Follow the links to visit every page. Internet access is needed for Substack, Amazon and Spotify. The contact form prepares a draft in your email app; it does not claim to have sent a message.

## Run the source project

Use Node 24 and pnpm 11.25 or a compatible pnpm 11 release:

```sh
pnpm install
pnpm dev
```

Open the Local address printed by Astro. In a second terminal, start the local editor:

```sh
pnpm cms
```

Open `/admin/` on the same site, choose Login, and edit through the labeled forms. This Login connects only to the local file service; no cloud account is needed. Stop both services when done. The editor is not connected to GitHub or a production publishing service yet.

```sh
pnpm check:content
pnpm build
pnpm preview
pnpm test
pnpm check:launch
```

`check:launch` intentionally refuses a production release until actual copy, asset, rights and privacy approvals are recorded. It does not block the preview build. `PDP_PRODUCTION=true` triggers those release checks. No production domain has been connected.

## Content locations

- `content/books`: story copy, title, credits, series positions, cover/excerpt/playlist references and SEO.
- `content/series`: introductions, publication order and separate story chronology.
- `content/authors`: public bylines/pen names, optional approved bios.
- `content/editions`: format-specific availability, identifiers and verified retailer links.
- `content/assets`: cover and QR references; `public/covers` and `public/music` hold their actual files.
- `content/journal`: curated Substack references.
- `content/settings/site.json`: publisher email, primary newsletter destination, featured title and launch gates.

The runtime reads these separate files; it does not read the obsolete paused scaffold. `content/approval/catalog.draft.json` is retained as the initial import/provenance snapshot used by validation, not a second place to edit live copy. Never put private rights evidence or unpublished manuscripts in `public/`.

See `docs/website/Content_Updates.md`, `Deployment.md`, `Testing_Report.md`, and `Launch_Blockers.md` for the publisher handoff.
