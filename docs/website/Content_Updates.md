# Updating the books and website

Use the local editor at `/admin/` after starting the site and its CMS service. All edits are to local files until a remote repository and hosting service are connected. Decap’s local “Publish now” writes a file; it does not mean this website is online or approved for production.

## Edit an existing book

1. Choose Books and the title.
2. Update the hook, description paragraphs, catalog description or literary identification. Preserve the approved character names.
3. Keep its stable ID. Changing a page slug later needs a redirect.
4. Update the relevant approval state rather than claiming a changed field was already approved.
5. Save locally. With `pnpm dev`, the site rebuilds for preview. Check the book, series and catalog pages.
6. Run the content/build checks before packaging or any later deployment.

Publication order and chronology are separate. My Blue Heaven is Book Two in publication order and the prequel to Twenty-Five Dollars a Night. Its story chronology position is One. Do not renumber the series because a book is a prequel.

## Change a purchase link or publication status

Open Editions and retailer links, choose the correct book and format, and edit the URL/status. Confirm the destination’s actual title, byline, language, format and market before marking a link destination-verified. Save the check date and evidence. Do not copy a paperback ISBN onto a Kindle record. Reaching a date does not automatically make a preorder available.

## Add a book

1. Confirm its author and series exist; create either through their own collections if needed.
2. Upload its authentic cover in Images, record dimensions/alt and approval, and retain its stable image ID.
3. Create the Book with its own stable ID/slug, title, author relationship, series relationship/position, copy, cover relationship and SEO. Use null/empty optional fields rather than invented information.
4. Create its Edition records and verified retailer links. A book and its editions are separate records.
5. Add the book ID to the series publication-order list. Add chronology only when established; a new series may leave chronology empty.
6. Review the generated book, catalog, author and series pages. Templates discover records automatically; no navigation or page code needs changing.

Use the same ID and slug at first creation for simplicity. Do not create an incomplete record in the production branch: assemble a new release in a draft branch or local workspace and save related records together before building. Build validation reports missing references.

## Newsletter and journal

All primary newsletter links use `https://substack.com/@publicdomainpulppress`. The native embedded form is served by the publisher’s Substack publication and sends subscriptions to Substack. Do not create another email list or use contact-form submissions as newsletter consent.

Journal links are curated entries with a real title/date/destination. Add them through Journal links. Read the source before writing its summary; do not label a Chapter Four excerpt “the first chapter.”

## Covers and social previews

Cover masters remain unchanged. Web pages display the full image without perspective or crops. Current social images are 1200×630 compositions with intact cover fronts in `public/social/`. New book social images must be created and reviewed before its page is released; keep the same slug-based filename or update the template/content support. The current implementation does not automatically infer a new social composition from a book record. Missing social assets are detected by site checks.

## Approvals and backups

The preview includes the current eight draft web records for publisher review and remains noindex. Record final publisher and separate rights approvals only when obtained. Review privacy text against the actual hosting/form services before enabling production. Keep the source in a private repository and back up original covers/evidence independently. Version history is useful; test restoring a prior version and rebuilding.

Calder City Book Three stays off the site entirely until it is written and the publisher separately approves an announcement. It is not a hidden timed release.
