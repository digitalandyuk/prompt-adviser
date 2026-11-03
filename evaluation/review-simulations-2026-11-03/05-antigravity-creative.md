# 05: Antigravity edition, creative deliverables

Codex-hosted fictional text simulation of Antigravity. No native Google tools, image generation or website build.

## User draft

Use Antigravity to make a simple local landing page and three square promotional images for a fictional running club called Hilltop Striders. Make it premium, modern and not generic. It's for new runners in Kent, with a friendly welcome and a join button. I want files I can use, not a description. No publishing or paid services.

## Adviser: questioning

Prompt completeness: 80%. Priority gaps: visual direction, usable file requirements and approved content/assets.

Consistency: 2/2. Missing context: 2; excess context: 0. “Premium, modern and not generic” leaves meaningful visual decisions open. A reference or one selected example could help; no external style will be inserted without your choice.

The deliverable must distinguish a working local page from actual generated images. Antigravity's agent is not automatically a Gemini image-generation interface; available image tools and exports must be verified.

Source check: Offline; no live directory search available. No suitable open-source prompt example verified. Role options: community-brand designer or product designer for developer tools, plus No role. I recommend community-brand designer for a welcoming local club. Jev is unnecessary.

Model: retain the selected Antigravity model; exact version, thinking controls and image-generation access are unverified. Execution workload: moderate. Allowance %: Not reliably estimable.

1. Which local page/image formats, destination folder and fallback should apply if the host cannot generate images without a paid service?
2. What specific visual qualities or patterns should guide the design, and do you choose community-brand designer, product designer for developer tools or No role?
3. What confirmed club details, join destination and supplied assets may be used, and what must be preserved?
4. Shall I ask more?

The page and images have not been created.

## User answers

HTML/CSS and PNG, 1080 square, in the project output/club folder. If images unsupported, create SVG artwork that is clearly labelled as the fallback and PNG only if local export works. Community-brand designer. Navy, orange, generous spacing, no gradients or pill buttons. Supplied logo stays unchanged. Use only the name and Kent; no invented dates, fees or meeting places. Join button goes to the placeholder #join, visibly labelled as a draft. Finalise.

## Adviser: finalisation

Prompt completeness: 100%. Consistency: 2/2. Missing context: 0; excess context: 0. Runtime export support and logo availability remain execution checks.

Replaced vague aesthetics with chosen specifics, retained the logo constraint, and defined real files plus an honest export fallback. Model: retain the selected Antigravity model; no control change is claimed. Workload: moderate. Allowance %: Not reliably estimable.

Assumption: work stays in the supplied project and the logo will be attached. No build or generation has run. Execution requires `Run this prompt`.

```text
Role and goal
Act as a community-brand designer. Create a local landing page and three square promotional visuals for the fictional Hilltop Striders running club, welcoming new runners in Kent.

Context and design
Use navy, orange and generous spacing. Avoid gradients and pill-shaped buttons. Use the supplied logo unchanged; ask for it if missing. Use only the club name and Kent as confirmed details. Do not invent meeting places, dates or fees.

Deliverables
Save usable HTML/CSS and three 1080 × 1080 PNGs in output/club within this project. The page's Join button should point to #join and be visibly labelled as a draft. If image generation is unsupported without a paid service, create SVG artwork labelled as the fallback, and export PNGs only if a local supported export works. Report the actual files created and anything unavailable; do not present an image brief or prose as a generated PNG.

Limits and acceptance
Do not publish, deploy, use paid services or alter files outside the agreed output folder. Check the local page's narrow and wide layouts and inspect available image outputs for dimensions, legible text and logo preservation. Keep the work proportionate; use the supported local tools without adding a multi-agent process for this small page.

If you don't know or can't verify something, say so; don't invent facts, figures or sources.
```
