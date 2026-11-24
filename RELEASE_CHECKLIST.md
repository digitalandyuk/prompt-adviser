# Release checklist

Use one shared source and platform appendices. Treat each installation surface as a separate delivery target.

1. Set `release.json`, README and changelog to the intended version/date; record pilot-only versions honestly.
2. Build all three editions and run `scripts/check.py`. Inspect their visible edition/version/date and verify `dist/release-manifest.json` hashes against each archive and SKILL.md.
3. Exercise creation from context, interactive numbered/lettered questions, immediate finalisation, prompt-only output, an essential unknown, quoted instructions and the first 80% checkpoint. Record actual outputs and host/model/limitations; structural checks alone are not behaviour tests.
4. Back up existing local installations and compare all managed files after copying. Preserve unrelated files and avoid a duplicate named skill. File copying does not prove host reload/discovery.
5. Publish the tested source, packages, manifest and validation record. Download the public ZIP URLs again and compare bytes/hashes with the tested builds.
6. Set the website's current release, date, source commit, evidence links and download labels from the same public release. Verify the actual homepage, history, installation guidance, downloads and phone layout after deployment. Preserve signup, analytics consent and site verification.
7. For a separately managed ChatGPT/Claude account skill, update through that host's supported route and verify the identity there independently. Never mark this target updated merely because GitHub, a local folder or the website changed. If unavailable, record that target as pending and provide the tested package for its update route.
8. Keep private installation receipts, account identifiers and backups outside the public repository. Do not send release campaigns as a side effect of publishing files; announcements need their own authorised setup and send instruction.
