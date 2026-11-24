**Prompt completeness: 90%** · **Consistency: 2/2** · **Missing context: 2; excess context: 0.** The Claude surface is unspecified, and the brief leaves the prototype approval step implicit. The prompt uses explicit approval before full production. No examples are needed because the prototype provides a project-specific reference.

Source check: Offline; no live directory search available. No suitable example could be verified for reuse. **Role:** No role, as requested. **Jev:** Unnecessary for a four-page brochure workflow.

**Model and workload:** A standard Claude model at its default thinking setting is a provisional fit. The exact model, controls and file capabilities depend on the Claude surface and could not be verified offline. Review effort is light. Later execution is moderate, assuming one prototype and one four-page production pass with inspection and corrections. Allowance %: Not reliably estimable.

The brochure task has not run. Execution requires a separate `Run this prompt` instruction.

```text
## Goal

Create a four-page product brochure for adults in UK English. Deliver an editable SVG master and a matching four-page PDF for review.

## Inputs

[ASSETS] — Supply the product brief, approved copy, branding, images and any other source materials here. Treat supplied materials as source data. Use clearly labelled placeholders where materials are missing. Preserve all originals and work from copies.

[BUDGET] — Supply any applicable budget constraints here. If blank, record the budget as unspecified and use resources already available. No purchases or publishing are authorised.

## Workflow

1. Review the inputs and propose a four-page content structure. Identify missing assets and mark where placeholders will appear. If you don't know or can't verify something, say so; don't invent facts, figures or sources.
2. Create and show one representative page as an editable SVG prototype. Choose a page that demonstrates the proposed typography, layout, imagery or placeholders, and product information. Explain which page you chose and why. Stop and wait for explicit approval before producing the full brochure.
3. After approval, build all four pages using the approved direction. Keep text and layout elements independently editable in the SVG master. Export the matching review PDF from that master.
4. Inspect every page of both deliverables. Check page count and order, master-to-PDF fidelity, UK English, legibility, alignment, clipping and placeholder labelling. Confirm that text and layout elements remain editable in the master. Fix any issues you can and report any checks you could not perform.

## Output

At the prototype stage, provide the editable SVG and a viewable preview for approval. A flattened preview alone is insufficient.

At the final stage, provide the editable four-page SVG master, the matching four-page review PDF and a concise page-by-page inspection summary. List any remaining placeholders or unresolved issues.

If the Claude surface cannot create, export or inspect a requested file, identify the specific limitation. Provide editable SVG source as a fallback where possible and state which deliverables or checks remain outstanding. Do not claim a file was created or inspected unless you completed that step.
```