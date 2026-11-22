**Prompt completeness: 95%.** Priority gap — visual style is assumed.

**Consistency: 2/2. Missing context: 1; excess context: 0.** The product reference image is still pending. No worked example is needed because the timed shot list specifies the format and the supplied image will establish the bottle’s appearance.

The Codex prompt produces a timed shot list and a video-generation prompt for UK night-shift workers. I’ve used a realistic, softly lit break-room setting as the visual default.

**Model and setting**  
Keep the current Codex model and reasoning setting for this short writing task. Its exact version and available settings could not be verified offline. A higher reasoning setting would add review time for a brief with a simple structure.

**Execution workload**  
Light, assuming one supplied reference image and one production brief. Allowance %: Not reliably estimable.

The reviewed task has not run. Use `Run this prompt` once the reference image is attached to authorise drafting the brief.

```text
Goal
Create a timed shot list and a ready-to-use video-generation prompt for a 12-second vertical Instagram product video featuring a fictional reusable bottle. The audience is UK night-shift workers.

Context
Use the supplied product reference image as the source of truth for the bottle’s shape, colour and label. If the image is missing or those details are unclear, ask for a suitable reference before drafting.

Instructions
Use a realistic night-shift break-room setting with soft lighting that keeps the bottle and label easy to see. Make the bottle the focus and keep its appearance consistent across every shot.

Rules and constraints
- Specify a 9:16 aspect ratio and a total runtime of exactly 12 seconds.
- Preserve the bottle’s shape, colour and label. Do not invent unreadable label text or add branding.
- Avoid unsupported product or environmental claims in visuals, captions and voice-over.
- Deliver the shot list and generation prompt as text only.

Output format
1. Timed shot list. Give the start and end time, framing and on-screen action for each shot. Cover 00:00 to 00:12 without gaps or overlaps.
2. Video-generation prompt. Provide one standalone prompt that uses the supplied image as a product reference and matches the shot list, runtime, aspect ratio and product constraints.
```