# Validation record, 24 September 2026

- Both installable skills and ZIPs were generated from the shared source.
- `scripts/check.py` passed package structure, reference, execution-boundary, question-count and public-text checks.
- Ruby's YAML parser accepted both skill frontmatters, all three Issue forms and the GitHub Actions file.
- `unzip -t` found no archive errors. Both installed local skill folders matched their generated editions.
- The five cases in `tests.md` were compared against the old and new instructions by inspection. New instructions add an 80% source/Jev checkpoint while retaining the three-question and execution boundaries. This is a design review, not a live model benchmark; prompt quality, workflow savings and latency remain unmeasured.
- The bundled `quick_validate.py` could not run because the local Python lacks PyYAML. Equivalent frontmatter and package checks above passed.
- The helper's request and response were first checked against a mocked Decisions API without a real key. A live call then used the fictional `examples/jev-routing.json` through OpenRouter with a key read from macOS Keychain. Jev returned `video` (confidence 1) for the video task and reported 356 input tokens, 41 output tokens and US$0.000014952 cost. This one expected result confirms connectivity and billing reporting, not decision accuracy across tasks. The key was not printed, stored in the repository or sent in chat.
