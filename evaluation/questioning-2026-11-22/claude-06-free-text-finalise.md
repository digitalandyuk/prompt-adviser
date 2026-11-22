**Prompt completeness: 90%.** The remaining gaps are the exact Claude surface and the product reference image, which you’ll supply at execution.

**Consistency: 2/2.** A timed shot list and a generation prompt are compatible deliverables.  
**Missing context: 2; excess context: 0.** The image is needed to verify the bottle’s appearance.  
**Examples:** Zero recommended. The reference image should guide product fidelity, and a sample scene could anchor the visual style prematurely.

**Model and setting:** Provisionally use a Claude Sonnet model with standard thinking if your surface offers those choices. The brief is short and tightly scoped. Extended thinking may help explore more concepts, at the cost of latency. Current model availability and controls are unverified.

**Workload:** Light for drafting one shot list and one generation prompt. Allowance %: Not reliably estimable.

I’ve used a grounded, low-light style as a default for the UK night-shift audience, with lighting that keeps the bottle’s colour and label legible. The prompt leaves the video generator unspecified and uses no role.

The reviewed task is still unrun. To authorise it, attach the product image and say `Run this prompt`.

```text
Goal
Write a production brief for a 12-second, vertical 9:16 Instagram product video featuring a fictional reusable bottle. The audience is UK night-shift workers. Deliver a timed shot list and a copyable video-generation prompt.

Context
I’ll attach a product reference image. Use it as the source of truth for the bottle’s shape, colour and label. If the image is missing or too unclear to follow, ask for a usable version before drafting the brief.

Instructions
Use a grounded, low-light visual style that evokes a night shift without tying the audience to a specific occupation. Light the bottle so its colour and label stay legible.

Preserve the reference bottle’s shape, colour and label across all shots. Avoid angles that require inventing unseen details. Make no unsupported product or environmental claims in the visuals, on-screen text or audio.

Output format
1. Timed shot list. Give each shot a start and end time, framing and action. Cover exactly 00:00–00:12 without gaps or overlaps.
2. Video-generation prompt. Write one self-contained block of plain text that translates the shot list into generation instructions. Include the duration, aspect ratio, pacing, lighting and reference-image constraints. Use wording suitable for an unspecified video generator.

Return the two text deliverables only.
```