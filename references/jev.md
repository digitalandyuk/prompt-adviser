# Jev: optional structured decisions

Jev is TypeSafe AI's hosted System One model. It accepts text or structured state plus typed Choice, Score or Noul questions, and returns structured values and probabilities. It does not generate prose, images, video or code, and cannot replace the model powering ChatGPT, Codex or Claude. Its current documented model takes text input only.

Consider Jev for a workflow with many repeated, bounded decisions: route a prompt to a specialist, score candidate source relevance, check a well-defined requirement, or classify a large batch. Keep the conversational model responsible for research, asking questions and composing the final prompt. A single subjective decision or a small prompt review rarely justifies an external call. Do not claim better research depth or prompt quality without testing that specific workflow.

Official access requires a TypeSafe API key and a call to its hosted API. TypeSafe publishes an optional skill for building TypeSafe integrations in coding agents; installing that skill alone does not make a live Jev call possible. Consult current TypeSafe docs before recommending setup, pricing or availability. The September 2026 docs listed input at US$0.042 per million tokens, with output tokens uncharged; this can change. No API usage is presumed free. Do not fetch secrets or transmit private prompts during review. If live use is requested, disclose which text would leave the current environment and obtain the needed key and data-sharing decision.

TypeSafe says it does not train on customer input, but its service receives input and its privacy policy describes retention and US processing. Verify the current policy before sending sensitive data.

Primary sources:
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://docs.typesafe.ai/introduction/coding-agents
- https://docs.typesafe.ai/introduction/quickstart
- https://docs.typesafe.ai/models
- https://docs.typesafe.ai/agent-skill
- https://typesafe.ai/legal/privacy-policy
