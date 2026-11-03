# 02: Codex edition, shared-dependency migration

Codex-hosted fictional text simulation. Repository and runtime capabilities are fictional; no task commands were run.

## User draft

In Codex, migrate four payment adapters that all share the same client from client A to client B. Keep existing public endpoint names and make the tests pass. Work locally, do not push, publish or touch production. Think step by step before every edit, run all tools whenever possible, and verify every changed line five times. I want a finished branch with a short report, not a plan.

## Adviser: questioning

Prompt completeness: 85%. Priority gaps: exact scope, acceptance checks and safe stopping limits.

Consistency: 1/2. A local branch is compatible with no push; repeated per-line verification conflicts with an efficient task scope → retain meaningful acceptance checks and remove blanket process. Missing context: 2; excess context: 1. No examples needed unless an adapter mapping is ambiguous.

Execution strategy: one agent should retain the shared-client context; independent read-only inspections may run together. Separate agents are not justified merely by having four adapters. Keep local work resumable if it spans sessions, subject to the supplied storage location. Verify actual host capabilities at execution; no bridge or savings is assumed.

Source check: Offline; no live directory search available. No suitable open-source prompt example is verified. No role is recommended: the migration contract supplies the useful standards. Jev is unnecessary.

Model: retain the selected Codex model; version and reasoning controls are unverified offline. Execution workload: moderate, assuming four adapters rather than a wider payment redesign. Allowance %: Not reliably estimable.

1. Which repository paths and client-B mapping documentation define the migration, and where should the local branch and report be kept?
2. Which existing tests and observable checks establish completion, including any behaviour that must remain unchanged?
3. What local changes are permitted, what should require approval, and what retry or time limit should end with a blocker report?
4. Shall I ask more?

The repository has not been accessed and the migration has not run.

## User answers

Use adapters/{card,bank,wallet,refund}.ts and docs/client-b.md. Branch candidate/client-b; report MIGRATION.md in the same repo. Existing unit and contract tests must pass, endpoint names and idempotency semantics must remain. Local source/test edits are allowed, no dependency upgrades, no network changes, no pushes. Stop after 45 minutes or two failures of the same check without new evidence. Finalise.

## Adviser: finalisation

Prompt completeness: 100%. Consistency: 2/2. Missing context: 0; excess context: 0. The source paths are supplied, not inspected.

Retained shared context and task-specific tests. Removed blanket thinking, all-tool use and repeated line checks. A single progress/report file supports resumption without a new agent or scheduler. Model: retain the selected Codex model; verify available controls before using them. Workload: moderate. Allowance %: Not reliably estimable.

Assumptions: local branch creation is authorised and the documented clients exist. If either is false, report it. No reviewed task has run; execution needs `Run this prompt`.

```text
Goal
In the supplied repository, create the local branch candidate/client-b and migrate adapters/{card,bank,wallet,refund}.ts from client A to client B using docs/client-b.md.

Instructions
Inspect the relevant files and actual repository state before editing. Keep the shared-client migration in one agent context. Independent reads may run together where supported. Preserve public endpoint names and idempotency semantics. Make only the local source and test changes necessary for this migration.

Acceptance and limits
Run the existing unit and contract tests and report their actual outcomes. Do not upgrade dependencies, change network configuration, push, publish or touch production. Stop after 45 minutes or two failures of the same check without new evidence; report the blocker and remaining work.

Progress and output
Keep MIGRATION.md in this repository as a compact progress record and final report: completed and outstanding items, changed paths, test evidence, decisions, blockers and next action. On resumption, read it and verify the current branch, diff and test state before acting. An update is not completion. Finish with the local branch and report; claim completion only when the scoped migration and acceptance checks are complete.

If you don't know or can't verify something, say so; don't invent facts, figures or sources.
```
