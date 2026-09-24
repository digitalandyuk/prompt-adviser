# Contributing

Open an Issue for a bug, improvement or useful prompt source. A source suggestion should identify its URL, licence, why it improves a real prompt and any platform limitation. Use fictional or fully sanitised examples. Do not submit private prompts, conversation logs, keys or business data.

For changes, edit `src/` or `references/`, run `python3 scripts/build.py` and `python3 scripts/check.py`, then open a pull request describing the behaviour and the test case. Keep the three-question and `Run this prompt` boundaries intact. Cite third-party sources and preserve their terms. Generated `dist/` files should be included so users can install without a build step.

Maintainers review and approve releases manually. Issues and pull requests are the initial update mechanism; there is no automatic collection or scheduled monitoring.
