**Prompt completeness: 95%.** Visual style remains open. **Consistency: 2/2.** Missing context: 1. Excess context: 0.

I’ve left visual style as an optional input. If it’s blank, the prompt asks for a style recommendation with a brief rationale.

**Google Antigravity:** Use the desktop agent to write the production brief. Keep your current model and thinking settings. I couldn’t verify current model options offline. **Workload: light**, assuming one reference image and a text-only brief. Allowance %: Not reliably estimable.

The prompt has not been run. Execution requires `Run this prompt`.

```text
Goal
Create a timed shot list and a copyable video-generation prompt for a 12-second, vertical 9:16 Instagram product video featuring a fictional reusable bottle. The audience is UK gym-goers.

Inputs
- Product reference image: [attach image]
- Visual style: [optional]

Instructions
Use the reference image as the source of truth for the bottle’s shape, colour and label. Keep those features consistent across shots. If the image is missing, ask for it before writing the brief. If a feature is unclear, flag it for confirmation.

If no visual style is supplied, propose one that fits the audience and explain the choice in one sentence. Use that style consistently across both deliverables.

Avoid unsupported product or environmental claims in the visuals, on-screen text and any suggested voice-over. If you don't know or can't verify something, say so; don't invent facts, figures or sources.

Output format
1. Timed shot list with start and end times, framing, action and any on-screen text. Cover exactly 00:00–00:12 with no gaps or overlaps.
2. One copyable video-generation prompt that follows the shot list and includes the reference-image fidelity, duration, aspect ratio and claims constraints.

Stop after delivering the two text outputs. Do not generate or render the video.
```