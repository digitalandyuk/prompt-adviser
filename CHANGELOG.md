# Changelog

## 0.7.2 — 2026-11-22

- Adds the version and release date directly below the title and in YAML metadata in every installed skill.
- Introduces a shared release manifest so Codex, Claude and Antigravity packages carry the same release identity.
- Checks manifest, README, changelog, generated metadata and ZIP contents for agreement. Prompt-review behaviour is unchanged from 0.7.1.

## 0.7.1 — 2026-11-22

- Makes the same numbered question layout explicit across Codex, Claude and Antigravity, with one main decision or missing fact per question.
- Adds a/b/c choices for meaningful alternatives, supported recommendations and a free-text alternative without inventing options for unknown facts.
- Gives question 4 explicit choices to ask three more questions or finalise; supports shorthand against the latest displayed menu and clarifies partial or invalid replies.
- Preserves scoring, the automatic 80% source/role/Jev checkpoint and the separate Run this prompt boundary. Adds questioning-process checks with platform-testing limits recorded in VALIDATION.md.

## 0.7.0 — 2026-11-03

- Adds a model-specific audit of inherited thinking, blanket tool-use and repeated self-check instructions while preserving acceptance evidence and approval gates.
- Defaults to one agent, with conditional guidance for useful delegation, bounded handoffs and progressive loading of relevant skills/tools.
- Adds resumable progress guidance for long tasks without claiming to install memory, runtime continuations or permission enforcement.
- Strengthens document grounding, scoped cross-app dependency discovery, concrete creative direction and finished-file/destination requirements.
- Adds five fictional rough/structured task pairs and a manual opt-in comparison runner, separate from multi-turn adviser tests and native-host validation.
- Preserves completeness/diagnostic scores, three questions, automatic 80% source/role/Jev checkpoint, optional choices and the explicit execution boundary across all three editions. Performance gains remain unmeasured.

## 0.6.0 — 2026-11-02

- Added conditional tool execution advice without a separate score, question round or mandatory output section.
- Covers selective retrieval, safe parallel reads, bounded programmatic orchestration, preserved MCP integrations, evidence coverage and failure/approval boundaries.
- Distinguishes target-host support from vendor API capabilities and unmeasured savings from observed token/call/latency results.
- Keeps detailed guidance in a conditional reference shared by all three editions; simple no-tool prompts retain the existing review flow.

## 0.5.0 — 2026-10-31

- Added visible consistency, missing-context and excess-context diagnostics without changing the completeness calculation.
- Added checks for varied, clearly labelled examples that agree with the prompt's rules.
- Adapted guidance to model/version, surface, tools and thinking mode, with model-specific exceptions.
- Added structured final prompts, delimited source material, factual-honesty defaults and long-context ordering.
- Strengthened agent briefs with bounded persistence, verification, unattended fallback and honest completion reporting.
- Preserved three questions, the automatic 80% source/role/Jev checkpoint, user choice and the explicit execution boundary across all three editions.
- Replaced an unconditional Jev/OpenRouter compatibility claim in the shared instructions with a current-verification requirement.

## 0.4.1 — 2026-10-05

- Renamed the Codex, Claude and Antigravity skill packages and commands to Prompt Adviser.
- Kept earlier macOS Keychain credentials readable after the rename.

## 0.4.0 — 2026-10-04

- Made the first 80% prompt-source check proactive, bounded and privacy-safe, with an explicit offline fallback and a visible no-match result.
- Added an optional, user-chosen “Act as” role menu with a **No role** choice at the same checkpoint.
- Added focused image, video, research and computer-use guidance while keeping the shared skill concise.
- Added a Google Antigravity edition alongside Codex and Claude, plus expanded review scenarios and release checks.

## 0.3.2 — 2026-09-24

- Added optional macOS Keychain storage for the OpenRouter API key, with a local hidden prompt.
- Kept environment-variable support for other systems and existing setups.

## 0.3.1 — 2026-09-24

- Added OpenRouter as the supported optional Jev route in both skill editions.
- Packaged a consent-gated, dependency-free Decisions API helper and fictional example.
- Clarified that installing the skill does not create an OpenRouter key or enable paid calls.

## 0.3.0 — 2026-09-24

- One shared source builds Codex and Claude editions.
- Added selective open-source prompt-source suggestions at the first 80% question round.
- Added optional, evidence-based Jev guidance for structured decisions.
- Preserved scoring, three questions, model and workload advice, and the explicit execution boundary.
- Added release packages, contribution templates and validation checks.
