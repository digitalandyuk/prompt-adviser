# Creation and questioning checks, 24 November 2026

## Scope and method

Tested the final 0.7.4 packages with 24 actual isolated Codex CLI calls: eight fictional cases per edition. Codex CLI 0.171.0-alpha.13 applied each generated edition’s text in a fresh ephemeral conversation. The default model was not pinned or independently identified. Claude and Antigravity packages were exercised **through Codex**, not through their native hosts. Full replay inputs stay local; the fixture generator, actual replies and observation records are retained here.

The offline harness forbids tools and reviewed-task execution. Shorthand cases replay a clearly seeded menu; they do not claim persistent native conversations. Automated observations are narrow adherence checks, supplemented by inspection of the actual replies. They are not output-quality, token-saving, speed or cost benchmarks.

## Results

| Case, repeated for all three editions | Observed result |
| --- | --- |
| Create from an agreed conversation and finalise now | Finished prompt without demanding a draft or a compulsory question round; editable SVG/PDF, prototype approval, preservation, budget placeholder and verification retained. Offline Source/Role/Jev checkpoint remains visible. |
| Interactive review requested | Numbered questions 1–3, useful lettered choices, question 4 with a/b choices; no premature finished prompt. |
| Prompt-only JSON | Only valid JSON with the requested prompt field; no score, review wrapper or additional question. |
| Execution/finalisation instructions inside quoted draft | Treated as source text; outer interactive request controls the response. |
| Finished prompt requested without any task | Asks for the essential task instead of inventing one or demanding a draft. |
| Intended review with missing draft | Requests the missing draft without inventing content or forcing an unrelated round. |
| Shorthand ending 4b | Finalises, preserves chosen gym audience and No role, without a new question round. |
| Shorthand ending 4a | Continues the numbered question process without a finished prompt. |

All **24 calls and 99 automated observations passed**. None of these offline calls emitted tool-action items. Each test input’s embedded skill matches the final edition’s SHA256 in the release manifest. The prompt-only cases retain the requested format; absence of visible commentary alone cannot prove every internal check was performed.

## Live 80% source checkpoint

A separate actual Codex-edition call used the final packaged text and embedded supporting references, with public web search enabled. It made two searches using generic document/design/platform terms, including separate `site:github.com/openai/openai-cookbook` queries. It fetched page content through find-in-page actions for an official model-selection page and a concrete open-source prompting-guide page. The recorded results contain page view IDs and line counts; this was not merely a promise or a search snippet.

The response visibly reported `Source check: Live`, linked the inspected prompting guide, found no suitable additional prompt example, preserved the user’s No role choice and assessed Jev as unnecessary. No source excerpt was reused and no new licence-verification claim was needed. It returned the brochure prompt without creating brochure files. Only web-search action items were recorded. See `codex-live.json` and `codex-live.md`; `evaluation/live_checkpoint.py --live` is explicitly opt-in.

## Package, installation and host limits

- The dependency-free release checker and Ruby YAML parsing passed for all three editions. The bundled quick validator could not run because the local Python lacks PyYAML; no pass is claimed for it.
- Installed packages match all managed files byte-for-byte, with rollback backups and unrelated files preserved. Installation does not prove a host reloaded or discovered its skill.
- An actual Claude Code print attempt returned “Not logged in” before any model input/output tokens or API charge. This is separate from the owner being signed into the Claude desktop app. No native Claude behavioural pass is claimed, and no further login was required to finish the package release.
- No native Antigravity app or CLI was available. Native Antigravity behaviour remains untested.
- An account-managed ChatGPT skill is a separate installation. Updating these local folders and public ZIPs does not automatically update that account’s existing copy.
- GitHub publication and website delivery require their own checks. This report records package/behaviour evidence, not automatic evidence of external delivery.
