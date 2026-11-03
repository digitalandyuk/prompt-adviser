# Fictional task-output smoke comparison, 3 November 2026

Five fixed tasks, two curated prompt variants each, were run in ten separate ephemeral read-only Codex CLI sessions. Both variants received the same task facts and the same no-tool execution wrapper. The CLI default was requested without a model override or user configuration. The returned event stream did not identify a pinned model/version; these results must not be described as a version-controlled model benchmark. Each variant was sampled once, rough first, so order, caching and sampling effects are uncontrolled. Prompts were authored fixtures, not outputs of a Prompt Adviser interview.

All ten CLI runs returned text successfully, with no tool-action items in the event stream. Outputs and reported usage/timing are preserved here. Usage includes the CLI's own instruction overhead and cache behaviour, not just the task prompt. No billed cost was measured, and timings are not a speed comparison.

## Manual criterion inspection

| Task | Rough prompt output | Structured prompt output |
| --- | --- | --- |
| Research | Correct vendor, revised price/capacity and unknowns. Mentions approved-note date but lacks the requested passage/section evidence trail. | Same correct decision, with short supporting passages, document dates and policy section. Missing implementation/reliability evidence remains explicit. |
| Image prompt | Meets visual direction and preservation intent, but assumes the reference will be supplied without a missing-reference stop. | Includes the reference dependency and stop, specific desired/excluded patterns and no unsupported claims. |
| Video prompt | Correct timing, aspect ratio and continuity. No explicit stop for an absent product reference. | Preserves the same scope and adds the reference stop and verified-audio-support condition. |
| Coding | Correct function, with explanatory prose. | The same correct function, returned in the requested single code block. Both functions passed four separately executed normal/empty/tie/order/negative-revision checks, retaining input contents. |
| Computer-use plan | Correctly identifies the missing PO, permission limits and absent browser capability, but mainly asks for input rather than specifying the safe draft-download, verification and resumption plan. | Distinguishes a compliant final invoice from a permitted draft PDF, preserves all approval stops, and defines verification and authorised resumption without claiming execution. |

This is a non-blind manual inspection against the published fixture criteria. The structured output better exposes a few requested safeguards in these samples; the coding task shows no functional advantage. It does not establish a general Prompt Adviser quality gain, factuality guarantee, native-host compatibility, token saving or faster execution. Image/video outputs are text specifications, not generated media; the browser task is a plan, not a live interaction. More rigorous work needs repeated native-host tests, blind grading and actual adviser-generated prompts with equivalent information.
