# Prompt Adviser V2

An open-source skill that helps turn a draft request into a useful, executable prompt. It scores completeness, asks three focused questions per round, recommends an available model and ends with a copyable prompt. The reviewed task starts only when the user explicitly says **Run this prompt**.

At the first response scoring at least 80%, the adviser checks whether an open-source prompt example or optional Jev workflow would improve the draft. Suggestions fit inside the normal three questions when another round is due. It remains useful without Jev, a prompt-library connection or any external account.

## Install

Download the appropriate archive from [`dist/`](dist/) and unzip it. The archive contains `prompt-adviser-v2/` at its root.

- **Codex desktop or CLI:** copy that folder into `~/.codex/skills/`, then start a new session. Invoke `$prompt-adviser-v2` with a draft prompt.
- **Claude Code:** copy that folder into `~/.claude/skills/`, then restart Claude Code. Invoke `/prompt-adviser-v2` or name the skill in a request.
- **Claude.ai custom skills:** where your account offers skill uploads, upload the Claude ZIP through **Customize → Skills**. Availability and labels may vary by plan and product version.
- **ChatGPT:** ChatGPT conversations do not install a Codex skill directly. The Codex edition can still be used in Codex desktop, or its instructions can be adapted manually to a supported ChatGPT custom-instruction or GPT workflow. No automatic ChatGPT installation is claimed.

Example: `Use Prompt Adviser V2 to improve this prompt: Create a 12-second product video for a new reusable water bottle.`

## Jev

Jev is an optional hosted service for structured decisions, such as routing, scoring and classification. It cannot replace the conversational model in ChatGPT, Codex or Claude. Prompt Adviser can recommend it where a repeated decision workflow warrants the extra setup. A live Jev call requires a TypeSafe API key and may incur API charges. See [Jev guidance](references/jev.md) and [TypeSafe's official setup](https://docs.typesafe.ai/introduction/quickstart). Installing TypeSafe's agent skill teaches a coding agent to build integrations; it does not activate Jev for this adviser.

## Develop

Edit `src/SKILL.template.md` for shared behaviour and a platform file for platform-specific guidance. Run `python3 scripts/build.py` and `python3 scripts/check.py`. Both skills and ZIPs are generated in `dist/`.

See [test cases](tests.md), [validation record](VALIDATION.md), [source and licence notes](THIRD_PARTY.md), [contribution guide](CONTRIBUTING.md) and [changelog](CHANGELOG.md). Contributions are welcome through Issues and pull requests; no prompts or usage data are sent automatically.
