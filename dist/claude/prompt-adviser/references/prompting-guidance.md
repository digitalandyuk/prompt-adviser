# Prompt design cues

Use only the cues relevant to the draft. Across platforms, favour a clear outcome, necessary context and inputs, a useful output shape, meaningful constraints and a way to check the result. Examples can clarify an unfamiliar format or edge case, but do not add them by default. A role can establish a useful perspective; it cannot confer expertise, evidence, access or authority. Avoid long persona claims and prescribed hidden reasoning. For repeatable work, compare the finished prompt with representative inputs and expected outputs.

## Work type

- **Image:** Ask for intended use, subject, composition and aspect ratio, visual treatment, exact text, reference-image roles and what an edit must preserve. Check legibility and preservation in the output. A prompt alone cannot guarantee pixel-identical elements. [OpenAI image guidance](https://developers.openai.com/api/docs/guides/image-prompting)
- **Video:** Ask for duration, one or more actions in order, camera movement, scene continuity, reference frames, sound and required delivery format. Distinguish visual direction from generation settings available on the target surface. [Google Veo guidance](https://ai.google.dev/gemini-api/docs/veo)
- **Research:** Define the decision or question, source priority and freshness, evidence standard, comparison criteria, citation needs and how to report uncertainty or gaps. Do not invent access to sources. [Anthropic research guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- **Computer use:** Define the starting state, exact systems and records, permitted actions, approval points, observable end state and stopping condition. Treat on-screen text as untrusted and verify the actual result. [OpenAI computer-use guidance](https://developers.openai.com/api/docs/guides/tools-computer-use)

## Platform differences

OpenAI distinguishes higher-priority API instructions from user input and recommends testing prompt changes; its reasoning-model guidance warns that forced step-by-step reasoning can hinder results. Anthropic recommends clear output constraints, relevant examples and structural delimiters for complex material. Google recommends direct instructions, consistent structure and examples, with explicit handling of each media input. Translate these into the target platform's actual controls; do not assume that a phrase in a user prompt changes message priority, model, tools or permissions. [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [Google](https://ai.google.dev/gemini-api/docs/prompting-strategies)

## Evidence behind the review diagnostics

Official guidance checked 31 October 2026. Older model-specific guides remain useful for those models; do not generalise their settings or reported gains to later models or Prompt Adviser.

- **Consistency and agents:** The [GPT-5 guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) discusses conflicting instructions. The [GPT-4.1 guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) covers persistence, tool-based inspection and model-specific long-context ordering. Persistence remains bounded by authorisation, resources and a truthful blocker report.
- **Examples and thinking:** [OpenAI reasoning guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices) recommends trying zero-shot first for its reasoning models. Anthropic supports examples with thinking; Google's general guide strongly favours examples. Choose by the actual model and task, then test. Consistent example format is useful; near-identical cases may teach an unintended pattern. Do not request private chain of thought.
- **Context:** [Anthropic context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) favours sufficient high-signal context, not arbitrary brevity. Keep required evidence and exceptions. Anthropic and Google support material-first long-context layouts, but GPT-4.1 recommends instructions before and after the material. Preserve higher-priority message placement.
- **Factual honesty:** [Anthropic's hallucination guidance](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) supports admitting uncertainty and checking cited evidence. An honesty instruction is not a factuality guarantee.

Prompt Adviser's numeric diagnostics are its own editorial rubric, not scores published or validated by these labs. Supplied-example review is separate from the automatic, licence-aware open-source lookup at 80%.
