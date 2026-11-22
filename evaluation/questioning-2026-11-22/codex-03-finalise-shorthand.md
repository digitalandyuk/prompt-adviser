**Prompt completeness: 100%**  
**Consistency: 2/2.** The clean studio style, readable label and claim-free call to action are compatible.  
**Missing context: 0/2; excess context: 0/2.** The reference image remains a required input before writing the brief.  
**Examples:** Use zero. The reference image and shot-list requirements give Codex enough direction.

**Model and setting:** Use the intended Codex session’s default model and reasoning setting. This short creative planning task calls for minimal setup. The exact model and setting are unverified offline.  
**Execution workload:** Light for one timed production brief.  
**Allowance %: Not reliably estimable.**

I’ve left the exact call-to-action wording and shot count to Codex within the agreed constraints. I’ve assumed the brief should be delivered as Markdown in the Codex conversation.

The reviewed task has not run. Once you supply the reference image, say `Run this prompt` to authorise it.

```text
## Goal

Write a production brief for a 12-second, vertical 9:16 Instagram product video featuring a fictional reusable bottle. The audience is commuters. Use a clean studio style.

## Context

Use the supplied product reference image as the source for the bottle’s shape, colour and label. If the image is missing or inaccessible, ask for it and pause before drafting the brief.

## Rules and constraints

- Preserve the bottle’s shape, colour and label as shown in the reference image.
- Keep any product details or surfaces the image does not show out of frame.
- Include at least one shot framed and lit so the label is readable. If the reference image does not show the label clearly enough to brief that shot, ask for a clearer image before proceeding.
- Close on a product shot with a short on-screen call to action that makes no product or environmental claims. Avoid unsupported product or environmental claims throughout.
- Deliver the written brief only. If you don't know or can't verify something, say so; don't invent facts, figures or sources.

## Output format

Return a Markdown production brief in the Codex conversation. Use a shot table with start and end times, framing and action, and exact on-screen text. Mark shots without text as “None”. The shots must cover 00:00 to 00:12 without gaps or overlaps. Identify the shot that makes the label readable.
```