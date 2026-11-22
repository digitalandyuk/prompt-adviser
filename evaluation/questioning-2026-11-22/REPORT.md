# Questioning-process checks, 22 November 2026

## Scope and method

Ran 18 actual model calls through the authenticated Codex CLI: six cases for each generated Codex, Claude and Antigravity edition. Each call applied the edition's packaged instructions to fictional fixture data, with external tools and reviewed-task execution forbidden. The default model was not pinned and its identity was not returned in the retained observations. These are limited adherence checks, not quality, cost or speed benchmarks.

For each edition, the first three calls form a review sequence: an actual first response, a shorthand reply selecting its displayed options and more questions, then a shorthand reply selecting the second round's options and finalisation. The preceding actual replies were replayed as explicit history in a fresh ephemeral call, rather than resumed in a persistent native chat. The other three cases use the same clearly seeded prior menu to isolate missing question 4, an invalid letter and a free-text answer outside the choices. Outputs and usage observations are retained alongside this report; the runner defines the fictional inputs and transcript construction. Full replay input files remain local because they repeat the packaged skill and prior replies.

## Results

| Observable behaviour | Codex edition | Claude edition through Codex | Antigravity edition through Codex |
| --- | --- | --- | --- |
| First round has numbered 1–3 plus question 4, with applicable lettered choices | Pass | Pass | Pass |
| Supported recommendation includes a reason; direct missing facts need no artificial choices | Pass | Pass | Pass |
| Shorthand maps to the displayed menu and 4a produces a fresh round | Pass | Pass | Pass |
| Follow-up keeps the chosen audience, deliverable and style instead of re-asking them | Pass | Pass | Pass |
| 4b produces a final copyable prompt, keeping the reviewed task unexecuted | Pass | Pass | Pass |
| Missing question 4 asks only that question and its a/b menu | Pass | Pass | Pass |
| Invalid 1z is flagged without inventing an audience | Pass | Pass | Pass |
| Free-text UK night-shift audience and No role survive finalisation | Pass | Pass | Pass |
| First 80% response visibly reports offline source check, role assessment and unnecessary Jev | Pass | Pass | Pass |

All 18 calls returned non-empty answers with no tool-action items. All 36 automated format/state observations passed. The outputs were also read for actual option mapping, focus, preservation of selections, free-text acceptance and the explicit execution boundary. The first Claude-edition round scored 75%, so its checkpoint correctly appeared in the 90% second round. The other editions showed it at 80% in the first round. No fresh live source/licence search was tested because the harness deliberately makes browsing unavailable.

## Limits

- These tests do not establish reliable behaviour in every conversation or with other user instructions.
- Claude Code 2.1.328 is installed but its authentication check reported signed out. No native Claude model conversation or Claude.ai upload test is claimed.
- No Antigravity app or CLI was available for native discovery/behaviour tests. Google Gemini's web app is a different surface.
- Codex CLI generated the responses, but installed-skill discovery/reload is separate from applying the packaged text in this harness.
- Package integrity, local file installation, GitHub delivery and website publishing are verified separately. They must not be described as native behavioural validation.
- Scoring and model advice were not calibrated in this narrow questioning-format update; no output-quality or performance improvement is claimed.
