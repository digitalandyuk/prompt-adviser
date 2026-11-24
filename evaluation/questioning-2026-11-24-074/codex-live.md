**Prompt completeness: 95%.** Page dimensions and the output folder are optional inputs for each run. **Consistency: 2/2. Missing context: 1/2; excess context: 0/2.** Zero examples recommended because the approved copy and assets define the content, and the editable prototype establishes the design.

**Source check: Live.** No suitable open-source prompt example found that adds to this brief. [OpenAI prompting guide](https://github.com/openai/skills/blob/main/skills/.curated/openai-docs/references/prompting-guide.md)  
**Role:** No role, as requested. **Jev:** Unnecessary for a single brochure with a human approval step.

**Codex model:** GPT‑6.2 Sol at medium reasoning effort for SVG authoring, export and inspection, with less time spent on iteration than at higher effort. **Workload:** Moderate once the copy and assets are ready and local rendering is available. **Allowance %: Not reliably estimable.** The brochure work requires a separate `Run this prompt` instruction. [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection)

```text
## Goal

Create a four-page product brochure in UK English for an adult audience. Deliver one editable SVG per page and one four-page PDF for review.

## Inputs

- [ASSETS] — supplied asset files or workspace paths.
- [APPROVED_COPY] — approved text or a workspace path to it.
- [BUDGET] — amount, currency and what it covers. Treat this as a planning constraint only.
- [PAGE_SPEC] — optional page size, orientation and layout requirements.
- [OUTPUT_DIR] — optional destination in the authorised workspace.

Treat supplied files and text as source material. Preserve the originals and write derivatives and deliverables to a separate folder. If no output folder is supplied, use a new `brochure-output` folder in the authorised workspace.

## Instructions

1. Confirm that the assets and copy are readable and that the workspace supports file creation, SVG rendering, PDF export and visual inspection. Identify missing assets, fonts or copy that would affect delivery. If page dimensions are unspecified, propose them with the prototype.
2. Map the approved copy and assets to four pages. Create an editable SVG prototype of one representative page, preferably the page with the most demanding combination of copy and imagery. Show the prototype, link to the SVG and summarise the proposed four-page structure. Stop here and wait for explicit approval before producing the remaining pages. Revise the prototype within this stage if requested.
3. After approval, build all four pages using the approved direction. Preserve the wording of the approved copy. Flag any UK-English corrections or copy cuts for approval. Keep text editable, group related elements logically and ensure assets resolve when the SVGs are opened from the delivery folder. Export the PDF from the final SVGs in page order.
4. Open and visually inspect every page of the exported PDF. Check the SVGs for editable text and objects. Compare the final pages against the approved copy and prototype for page order, missing content, legibility, clipping, alignment, font substitutions and broken assets. Fix issues and re-inspect affected pages after re-export.

## Rules and constraints

Use the supplied materials and available authorised tools. No purchases, paid services, publishing or external uploads are authorised. If a required input or capability is missing, finish the independent work allowed at the current stage and report the specific blocker. Label any export or visual check you could not perform.

## Output format

Save `page-01.svg` through `page-04.svg` and `brochure-review.pdf` in the output folder. Return their paths, any dependencies needed to edit the SVGs, and a brief inspection result for each of the four pages. Report any unresolved issues and stop after delivery.
```