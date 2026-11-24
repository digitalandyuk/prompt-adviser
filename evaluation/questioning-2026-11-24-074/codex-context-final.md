**Prompt completeness: 95%** · **Consistency: 2/2** · **Missing context: 1; excess context: 0.** Product facts and approved claims are needed for production. The prompt treats them as inputs and uses placeholders where they are missing. Examples are unnecessary because the prototype serves as the design reference.

Source check: Offline; no live directory search available. No suitable example was verified. **Role:** No role, as requested. **Jev:** Unnecessary for this design and review workflow.

**Codex model:** Use the active Codex model at Medium reasoning if supported. This balances layout and export checks with response time. Model and setting availability could not be verified offline. **Execution workload:** Substantial for four designed pages, two output formats and page-by-page inspection. Allowance %: Not reliably estimable.

I’ve made prototype approval an explicit pause before full production. No brochure work has run. Execution requires a separate `Run this prompt` instruction.

```text
Goal

Create a four-page product brochure for adults in UK English. Deliver one editable SVG master containing all four page layouts and one four-page review PDF exported from that master.

Inputs

- [ASSETS] — Supplied product brief, approved copy and claims, brand guidance, images, logos and any page specifications. Use clearly labelled placeholders for missing assets or copy. If you don't know or can't verify something, say so; don't invent facts, figures or sources.
- [BUDGET] — Spending limit, if supplied. An empty input means the budget is unspecified. A supplied budget is planning information. Purchases and publishing require separate authorisation.

Workflow

1. Identify the supplied materials and any gaps that affect the design. Preserve original files and create working files separately. Use supplied page specifications or state any provisional dimensions for the prototype.
2. Build one representative interior page as an editable SVG prototype. Choose a page that demonstrates the typography, layout and treatment of product copy and imagery. Provide the editable prototype and a rendered preview, identify any placeholders, and pause for explicit approval before producing the full brochure.
3. After prototype approval, build all four pages in the SVG master and export the review PDF. Keep text editable and major elements separately selectable. Use the approved prototype as the design reference.
4. Inspect every page in both the rendered SVG and the PDF. Verify the PDF has four pages in the correct order. Check legibility, clipping, alignment, asset rendering, placeholder labelling and consistency with the approved prototype. Verify that text and major elements remain editable in the SVG. Correct issues and recheck the affected pages.

Delivery

Save the master as `product-brochure.svg` and the review copy as `product-brochure-review.pdf` in the working project folder. Report both paths, the checks performed and any remaining placeholders or limitations. If the environment cannot create, render or inspect a required format, deliver any usable files you can verify and state exactly what remains incomplete. A flattened preview alone does not satisfy delivery.
```