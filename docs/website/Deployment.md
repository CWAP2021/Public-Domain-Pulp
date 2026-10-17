# Deployment instructions

The website is complete as a local/portable preview. This handoff does not connect PublicDomainPulp.net or publish a production website.

## Suggested managed-host route

1. Create a private GitHub repository owned by the publisher and add the clean source-project files. Do not upload node_modules, local stores, private research documents, subscriber lists or secrets.
2. Connect that repository to a publisher-owned Netlify account. Use Node 24, `pnpm build`, and publish directory `dist`. The included netlify.toml provides these settings.
3. Keep the preview flags in place. Use provider access controls for confidential preview access; noindex is an indexing preference, not password protection.
4. Review the full preview, forms and content on real devices. Confirm redirects against any existing live site before migration.
5. Complete Launch_Blockers.md and enable actual publisher-approved records/settings. Set `PDP_PRODUCTION=true` for production builds only after approvals are recorded.
6. Connect the domain after the publisher approves deployment. Inspect current DNS first, retain email records, configure HTTPS, and choose apex/www redirects. Do not replace working email DNS with website defaults.
7. Verify live book links, signup, contact, social previews, sitemap/robots and 404 behavior. Keep a rollback deployment and source backup.

A manual upload of the built dist folder is also possible; that path does not provide CMS/repository publishing. Never upload the entire source/research workspace as the public website.

## Remote Decap editor

Local editing has been verified. For remote editing, choose and configure the GitHub backend and a supported OAuth/authentication service using the publisher’s actual repository and accounts. Replace the local-only backend configuration; enable editorial workflow and branch protections appropriate to the provider. No repo name, token, client secret or existing Git Gateway service has been invented. The current remote /admin page deliberately explains the connection requirement instead of pretending remote login is configured.

Test a publisher walkthrough: add a draft book and edition, upload a cover, select author/series relationships, preview, publish to a protected branch, verify deployment, and roll back. Do not put authentication secrets into public config.json.

## Feedback delivery

The current build prepares an email draft addressed to info@publicdomainpulp.net. The form explicitly says the reader must send it in their email app. It has name, required reply email and a generous message field; it does not subscribe the reader.

To use Netlify-hosted form submission, set `PDP_FORM_MODE=netlify` and rebuild on Netlify. This emits a POST form with Netlify detection fields, honeypot and a confirmation route. Enable form detection, configure notifications to info@publicdomainpulp.net, and verify actual delivery and spam handling before switching readers to direct submission. Update the privacy page/service details to match the final setup. A successful static build does not prove receipt in an inbox.

## Newsletter

Native Substack signup works inside an iframe; the profile link remains the direct fallback and primary newsletter destination. Confirm subscription behavior under the publication’s current settings before launch. Test an actual subscription only with a publisher-controlled test address and the publisher’s authorization; no test subscriptions were submitted during this build.
