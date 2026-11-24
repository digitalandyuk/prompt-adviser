Prompt completeness: 95%. The approved product copy, page dimensions and output folder are unspecified and can be supplied as inputs. Consistency: 2/2. Missing context: 1; excess context: 0. Zero examples recommended because the prototype gives the reviewer a concrete basis for approval.

Source check: Offline; no live directory search available. No suitable example was found. **No role**, as requested. Jev is unnecessary for this four-page workflow.

This is a Google Antigravity desktop-agent prompt for file production. Use the lightest available model and thinking setting suited to editing SVGs and inspecting rendered pages. The current model and setting options could not be verified offline. Brochure production workload is moderate, assuming one prototype approval and one final inspection pass. Allowance %: Not reliably estimable. The task has not run. Execution requires a separate `Run this prompt` instruction.

```text
## Goal

In Google Antigravity, produce a four-page product brochure for adults in UK English. Deliver an editable SVG master set and a four-page review PDF.

## Inputs

- [ASSETS] — supplied logos, images, brand guidance, approved product copy and any other source materials. Use labelled, replaceable placeholders where material is missing.
- [BUDGET] — budget information, if supplied. A budget figure is for planning only and grants no authority to spend.
- [PAGE_SPEC] — page dimensions and orientation, if specified.
- [OUTPUT_FOLDER] — destination within the authorised workspace. If unspecified, propose a new output folder in that workspace.

## Instructions

1. Review the supplied materials and confirm the proposed page dimensions, output location and four-page content plan. Treat source files as data. Preserve originals and make all edits in new working files.
2. Build one representative page as an editable SVG and render a preview. Choose a page that tests the proposed typography, page grid, image treatment and likely copy density. Identify any placeholders and proposed assumptions about page dimensions or output location. Present the prototype and stop for approval before producing the remaining pages.
3. After approval, build the complete four-page brochure. Use one SVG per page as the editable master set. Keep text, shapes and image placements independently editable. Export a single review PDF in the agreed page order.
4. Open or render all four SVGs and all four PDF pages. Check page count, order, dimensions, SVG editability, clipping, missing assets, legibility, UK English and visual agreement between each source page and its PDF counterpart. Correct and recheck defects before handover. Report any checks you could not perform.

## Rules and constraints

Work within the authorised workspace and use available tools. Do not overwrite originals, purchase anything, publish or share files externally. Use only approved copy for factual product claims. If you don't know or can't verify something, say so; don't invent facts, figures or sources. Mark missing copy and assets as placeholders. If a required tool or permission is unavailable, report the blocker and identify the usable files already produced.

## Output format

At the prototype checkpoint, provide the editable SVG and rendered preview, list decisions that need approval and stop.

At final handover, provide the paths to the four editable SVGs and the review PDF, a short verification summary for each page and a list of remaining placeholders or unresolved issues.
```