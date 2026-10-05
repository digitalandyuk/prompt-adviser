# Jev: optional structured decisions

Jev is TypeSafe AI's hosted System One model. It accepts text or structured state plus typed Choice, Score or Noul questions, and returns structured values and probabilities. It does not generate prose, images, video or code, and cannot replace the model powering ChatGPT, Codex or Claude. Its current documented model takes text input only.

Consider Jev for a workflow with many repeated, bounded decisions: route a prompt to a specialist, score candidate source relevance, check a well-defined requirement, or classify a large batch. Keep the conversational model responsible for research, asking questions and composing the final prompt. A single subjective decision or a small prompt review rarely justifies an external call. Do not claim better research depth or prompt quality without testing that specific workflow.

OpenRouter is a supported route. An OpenRouter API key can call `POST https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13`; no separate TypeSafe account or key is required. The `~typesafe/jev-latest` alias follows new releases, while a pinned version supports reproducible thresholds. The endpoint is alpha, so check the official documentation before deployment. OpenRouter bills the account. On 24 September 2026 the model page listed US$0.042 per million input tokens and free output tokens; a response reports `usage.cost` in USD. Pricing may change. Do not assume API use is free or translate model pricing into workflow savings without measurement.

The packaged [OpenRouter helper](../integrations/jev_openrouter.py) sends a prepared JSON state and typed questions only when called with `--send` and a key. On a Mac, `--store-key` prompts locally and saves the key in macOS Keychain; the helper can then read that item without printing it. Elsewhere, set `OPENROUTER_API_KEY` in the process environment. See the fictional [example](../examples/jev-routing.json). It has no third-party Python dependencies and does not register an account, buy credits or make background calls. Keep the key out of the repository, shell history and chat. TypeSafe's optional coding-agent skill teaches agents to build integrations; installing it alone does not enable a live Jev call.

At the adviser's first response at or above 80% completeness, discuss Jev only if it would help the intended later workflow. Do not send the user's draft to Jev during review. For a live call, the user must choose Jev and authorise the particular state sent. Use fictional, non-sensitive state for initial validation. OpenRouter routes that state to TypeSafe.

OpenRouter says prompt retention is opt-in and off by default, but keeps usage metadata. TypeSafe receives the state and its policy describes retention and US processing. Verify both policies before sending sensitive data.

Primary sources:
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://docs.typesafe.ai/introduction/coding-agents
- https://docs.typesafe.ai/introduction/quickstart
- https://docs.typesafe.ai/models
- https://docs.typesafe.ai/agent-skill
- https://typesafe.ai/legal/privacy-policy
- https://openrouter.ai/docs/guides/community/jev
- https://openrouter.ai/docs/guides/community/jev-tutorial
- https://openrouter.ai/typesafe/jev-1.13/api
- https://openrouter.ai/docs/guides/privacy/data-collection
- https://openrouter.ai/docs/guides/privacy/provider-logging
