**Prompt completeness: 90%.** The Claude surface and destination video generator remain unspecified.

**Consistency: 2/2.** The centred, label-forward closing shot supports the studio direction and product fidelity requirements.

**Missing context: 2/2; excess context: 0/2.** The two platform details remain open. The bottle reference image is a required input for later use.

**Assumptions:** Use a standard Claude chat as the provisional drafting surface and write a generator-neutral prompt. The brief uses no role and needs no examples because the supplied image will define the bottle’s appearance.

**Model and thinking:** Provisionally use Claude Sonnet with extended thinking off, if that control is available. The task is short and well specified. The current model version and setting availability are unverified offline, and generator-specific syntax depends on the tool you choose.

**Execution workload:** Light for drafting one generator-ready prompt. Allowance %: Not reliably estimable.

The reviewed task has not run. To authorise it, say `Run this prompt`.

```text
Goal
Write one generator-ready prompt for a 12-second, 9:16 Instagram product video featuring a fictional reusable bottle. The audience is everyday commuters, and the visual direction is a clean studio product reveal.

Context
The product reference image will be supplied as an attachment. Use it as the visual reference for the bottle’s shape, colour and label. If the image is missing, ask me to attach it before drafting the generator prompt.

Instructions
Describe the visuals in timed beats that total 12 seconds. Use controlled studio lighting and framing that keep the product recognisable and the label clear. End with the bottle centred and its label facing the camera.

Rules and constraints
Preserve the bottle’s shape, colour and label throughout. Do not invent or alter label details, and do not add unsupported product or environmental claims. If a detail cannot be verified from the image, instruct the generator to preserve it as shown rather than guessing. Draft the text only.

Output format
Return one copyable video-generation prompt in plain text. Include the 12-second duration, 9:16 aspect ratio, reference-image instruction, timed visuals, closing shot and fidelity constraints. Use generator-neutral language.
```