# Website preview testing report

Build reviewed: 17 October 2026. This is a publisher review build, not a production deployment.

## Passed

- Astro production compilation completed: 24 HTML pages, plus sitemap and robots files.
- Structured catalog validation passed for eight books, three series, two authors and nine editions. Relationships, known identifiers, cover references and retailer destinations are checked.
- Automated generated-site checks passed: 727 local references, 58 image references and 24 JSON-LD blocks. Checks include page titles, descriptions, social metadata, headings, fragments, local assets and expected book details.
- HTTP checks passed for all generated pages; an unknown route returns HTTP 404.
- Desktop homepage and mobile 375-pixel layouts were inspected in the browser. Ten representative mobile routes had no horizontal overflow or broken loaded images, including book, series, contact and community pages.
- Responsive menu opens and closes; Escape closes it. Contact fields enforce required email and message input.
- The native Substack frame displays its email field and Subscribe button. The publisher profile remains the direct fallback destination. No test subscription was submitted.
- Local Decap editor lists the catalog and exposes book fields and relationships. A temporary book-copy change was saved to disk, checked, then restored to the approved source bytes. No remote publication occurred.
- My Blue Heaven includes the supplied Spotify link and authentic QR image, its two editions, and the explicit prequel relationship. User-approved Betty Boop and Popeye wording is present.
- Unwritten Calder City Book Three is absent from public catalog and page output.

## Scope and limitations

These checks are not a certification of accessibility or legal clearance. No automated axe audit, screen-reader session, real-device test or field performance measurement was completed. A final keyboard and screen-reader review and real-phone check remain release tasks.

The feedback form currently prepares an email draft addressed to info@publicdomainpulp.net. It has not sent a message. Direct website delivery requires the documented hosting/form configuration and an end-to-end delivery test.

Retailer links retain the source-verified destinations; regional availability and checkout were not tested. Spotify playback and QR decoding were not independently tested. Newsletter delivery and confirmation email were not tested. Hosted CMS authentication, deployment and domain/DNS changes have not occurred.

The review build is excluded from search indexing. Production release checks deliberately require publisher approvals before an indexed release.
