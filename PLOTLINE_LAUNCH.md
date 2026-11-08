# Pløtline website and account deletion

The DE/EN product, privacy and account-deletion pages are staged here. The privacy policy is explicitly a draft. No app-store URLs are invented, and no public account deployment is enabled.

## Activation

1. Finish the actual backend deployment and legal review described in `bentobla/plotline/docs/DATA_PRIVACY.md`. Confirm processor agreements, transfers, data locations, retention/backups, intended audience, accounting and credit/refund terms. Replace draft qualifications with verified facts before publication.
2. Configure the isolated public backend's exact `PUBLIC_WEB_ORIGIN`, Google server OAuth client ID, grouped Apple native App ID and Services ID, exact web redirect URI, Apple auth signing key, and refresh-token encryption key. Native and web Apple accounts must resolve to the same account ID. Register the signed Apple lifecycle webhook.
3. Set the public IDs and root HTTPS API URL in `plotline-config.js`. No secrets belong in this file. Enable only after native and web login/deletion have been tested with the real provider configuration. Do not reuse private test credentials or enable gameplay as a side effect.
4. Exercise both providers, wrong-account reauthentication, lost DELETE responses, revocation retries, status receipt download/import and expiry, same account on native/web, and app local erasure on real devices. Verify CORS rejects other origins.
5. Publish the final privacy URL and deletion URL in the app-store submissions, and run the final store-installed tests before public release.

The browser holds authentication in memory only; SDKs load on provider choice. A user must sign in, confirm deletion, and then receives a secret status receipt that can optionally be saved as a file. The status endpoint exposes no personal data. Web deletion cannot erase local data on offline devices or files already shared/imported into another app. The app has a signed-out local-cleanup option.

## Checks

Run from the repository root:

```
node --check plotline-delete.js
node --test tests/plotline-delete.test.cjs
python3 scripts/verify_plotline_links.py
python3 scripts/verify_protected_links.py
```

The automated browser-flow tests use simulated provider/backend responses. They do not replace real Google/Apple configuration and device tests. Existing lœrn/sudøku protected links are preserved. Product pages are included in the sitemap; draft privacy/deletion pages are excluded and carry `noindex,follow`.
