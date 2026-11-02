# Prompt Adviser

Current release: **0.6.0**, 2 November 2026. See the [changelog](CHANGELOG.md) and [validation record](VALIDATION.md).

An open-source skill that helps turn a draft request into a useful, executable prompt. It scores completeness, asks three focused questions per round, recommends an available model and ends with a copyable prompt. The reviewed task starts only when the user explicitly says **Run this prompt**.

It also checks contradictory instructions, missing or excessive context, example quality and model/thinking-mode fit. Finished prompts use applicable labelled sections, evidence and uncertainty rules, and proportionate agent boundaries. Consistency is scored out of 2 (higher is clearer); missing and excess context each use 0–2 (lower is better). These are editorial diagnostics, not measured performance predictions, and are not averaged into completeness.

For tool-heavy tasks, it conditionally recommends an execution plan: selective retrieval, independent parallel reads, or programmatic processing where the target host exposes eligible tools to code. It preserves evidence, coverage and approvals, retains working MCP integrations and falls back to direct calls. Simple no-tool tasks receive no extra optimisation section. This is advice for later execution, not a new runtime, app connection or guarantee of token savings. See [tool execution guidance](references/tool-execution.md) for platform limits and measurement caveats.

At the first response scoring at least 80%, the adviser checks open-source prompt directories without being asked, offers a specific “Act as” role or **No role** where useful, and considers optional Jev for repeated structured decisions. Suggestions fit inside the normal three questions when another round is due. A live source lookup uses generic task terms, not the user's private draft. If browsing is unavailable, the adviser labels its curated offline check. Completeness measures coverage, not prompt quality.

## Install

Download the appropriate archive from [`dist/`](dist/) and unzip it. The archive contains `prompt-adviser/` at its root.

- **Codex desktop or CLI:** copy that folder into `~/.agents/skills/`, the personal skill location in the [current Codex guide](https://learn.chatgpt.com/docs/build-skills), then start a new session. Invoke `$prompt-adviser` with a draft prompt. Some existing installations use `~/.codex/skills/`; if yours already discovers the skill there, avoid installing a second copy with the same name.
- **Claude Code:** copy that folder into `~/.claude/skills/`, then restart Claude Code. Invoke `/prompt-adviser` or name the skill in a request.
- **Claude.ai custom skills:** where your account offers skill uploads, upload the Claude ZIP through **Customize → Skills**. Availability and labels may vary by plan and product version.
- **Google Antigravity:** copy the Antigravity edition into `<project-root>/.agents/skills/` for one project. Antigravity's current installed customization guide also documents `~/.gemini/config/` as its global root, with skills in `skills/<name>/SKILL.md`; confirm that location for your installed version before choosing a global install. See [Google's Antigravity guide](https://codelabs.developers.google.com/getting-started-with-antigravity-skills). Native Antigravity behaviour has not yet been validated. Gemini web and AI Studio use different mechanisms.
- **ChatGPT:** ChatGPT conversations do not install a Codex skill directly. The Codex edition can still be used in Codex desktop, or its instructions can be adapted manually to a supported ChatGPT custom-instruction or GPT workflow. No automatic ChatGPT installation is claimed.

Example: `Use Prompt Adviser to improve this prompt: Create a 12-second product video for a new reusable water bottle.`

## Jev

Jev is an optional hosted service for structured decisions, such as routing, scoring and classification. It cannot replace the conversational model in ChatGPT, Codex or Claude. Prompt Adviser recommends it only where repeated decisions warrant an extra service. The package includes a small [opt-in OpenRouter helper](integrations/jev_openrouter.py) and [fictional example](examples/jev-routing.json). Verify current [Decisions API compatibility](https://openrouter.ai/docs/guides/community/jev), pricing and privacy conditions before enabling it; an API key and billed account are required. On a Mac, the helper can prompt for the key and keep it in Keychain; no key needs to appear in chat or shell history. Existing Keychain entries from earlier installs remain readable. It never calls Jev during an ordinary prompt review. See [Jev guidance](references/jev.md) for cost, privacy and use conditions.

## Develop

Edit `src/SKILL.template.md` for shared behaviour and a platform file for platform-specific guidance. Run `python3 scripts/build.py` and `python3 scripts/check.py`. All three skills and ZIPs are generated in `dist/`.

See [test cases](tests.md), [validation record](VALIDATION.md), [source and licence notes](THIRD_PARTY.md), [contribution guide](CONTRIBUTING.md) and [changelog](CHANGELOG.md). Contributions are welcome through Issues and pull requests; no prompts or usage data are sent automatically.
