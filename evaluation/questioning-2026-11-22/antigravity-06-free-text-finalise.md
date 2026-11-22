Prompt completeness: 95%. The visual style remains open.  
Consistency: 2/2. Missing context: 1; excess context: 0.

The brief now targets UK night-shift workers and asks for a timed shot list plus a video-generation prompt. No role is included. The product reference will be required before drafting so the brief can describe the bottle faithfully. Zero examples are recommended because the supplied image should guide the product depiction.

**Model and workload.** Use the lightest available Antigravity model that can inspect the attached image, with its default thinking setting if offered. This is a short creative brief, but inspecting the reference matters for label and colour fidelity. Current model availability and settings are unverified offline. Later execution is light, assuming one supplied image and a text-only deliverable. Allowance %: Not reliably estimable.

**Assumption.** Use a quiet, realistic night-shift break as the visual direction, with enough light to show the bottle accurately. The brief leaves the workplace unspecified.

The reviewed task has not run. To authorise running the agreed prompt, say `Run this prompt`.

```text
Goal
Write a production brief for a 12-second, vertical 9:16 Instagram product video for UK night-shift workers. The product is a fictional reusable bottle.

Context
I will attach a product reference image. Use it as the source of truth for the bottle’s shape, colour and label. If the image is missing or inaccessible, ask me to attach it and stop.

Instructions
Use a quiet, realistic night-shift break as the setting. Keep the workplace unspecified and light the bottle clearly enough to show its colour and label accurately.

Rules and constraints
Preserve the bottle’s shape, colour and label throughout. If part of the label is unclear, preserve its visible appearance and avoid inventing text. Make no unsupported product or environmental claims. Produce only the written brief.

Output format
1. Timed shot list covering exactly 0:00–0:12 with no gaps or overlaps. For each shot, specify the time range, framing, action and lighting.
2. One copyable video-generation prompt that carries over the shot sequence, 12-second duration, 9:16 aspect ratio, visual direction and reference-image constraints.
```