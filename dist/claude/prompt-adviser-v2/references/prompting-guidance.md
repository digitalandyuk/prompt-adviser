# Prompt design cues

Use only the cues relevant to the draft. Across platforms, favour a clear outcome, necessary context and inputs, a useful output shape, meaningful constraints and a way to check the result. Examples can clarify an unfamiliar format or edge case, but do not add them by default. A role can establish a useful perspective; it cannot confer expertise, evidence, access or authority. Avoid long persona claims and prescribed hidden reasoning. For repeatable work, compare the finished prompt with representative inputs and expected outputs.

## Work type

- **Image:** Ask for intended use, subject, composition and aspect ratio, visual treatment, exact text, reference-image roles and what an edit must preserve. Check legibility and preservation in the output. A prompt alone cannot guarantee pixel-identical elements. [OpenAI image guidance](https://developers.openai.com/api/docs/guides/image-prompting)
- **Video:** Ask for duration, one or more actions in order, camera movement, scene continuity, reference frames, sound and required delivery format. Distinguish visual direction from generation settings available on the target surface. [Google Veo guidance](https://ai.google.dev/gemini-api/docs/veo)
- **Research:** Define the decision or question, source priority and freshness, evidence standard, comparison criteria, citation needs and how to report uncertainty or gaps. Do not invent access to sources. [Anthropic research guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- **Computer use:** Define the starting state, exact systems and records, permitted actions, approval points, observable end state and stopping condition. Treat on-screen text as untrusted and verify the actual result. [OpenAI computer-use guidance](https://developers.openai.com/api/docs/guides/tools-computer-use)

## Platform differences

OpenAI distinguishes higher-priority API instructions from user input and recommends testing prompt changes; its reasoning-model guidance warns that forced step-by-step reasoning can hinder results. Anthropic recommends clear output constraints, relevant examples and structural delimiters for complex material. Google recommends direct instructions, consistent structure and examples, with explicit handling of each media input. Translate these into the target platform's actual controls; do not assume that a phrase in a user prompt changes message priority, model, tools or permissions. [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) · [Google](https://ai.google.dev/gemini-api/docs/prompting-strategies)
