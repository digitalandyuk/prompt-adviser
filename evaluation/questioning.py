#!/usr/bin/env python3
"""Exercise actual question-round outputs using isolated Codex CLI calls.

Claude and Antigravity editions are evaluated through Codex, not native hosts.
Only fictional fixture text and packaged skill files enter the test prompts.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DRAFT = (
    "Improve my draft prompt for {platform}: Create a 12-second, 9:16 Instagram "
    "product video for a fictional reusable bottle, using a product reference image "
    "I will supply later. Preserve its shape, colour and label; make no unsupported "
    "product or environmental claims. I have not decided the audience, visual style "
    "or exact output format. Help me choose. Do not make the video during review."
)
SEED = """Prompt completeness: 85%. Priority gaps: audience, output and role choice.
Consistency: 2/2. Missing context: 1; excess context: 0.
Source check: Offline; no live directory search available. No verified excerpt offered.
Jev is unnecessary for this single creative brief. Retain the selected model; current
model controls are unverified. Workload: light. Allowance %: Not reliably estimable.

1. **Who is the video for?**
   a) UK commuters (Recommended), to focus on everyday portability.
   b) UK gym-goers.
   c) Existing customers.
2. **Which output do you want?**
   a) A timed shot list plus a generation prompt (Recommended), for a usable production brief.
   b) A generation prompt only.
   c) A mood-board brief.
3. **Which role should guide the brief?**
   a) Product-video creative director (Recommended), for visual consistency.
   b) Performance-ad reviewer.
   c) No role.
4. **Shall I ask more?**
   a) Ask three more questions.
   b) Finalise the prompt.

You can give your own answer. The video has not been made.
"""


def question_blocks(text):
    starts = list(re.finditer(r"(?m)^\s*([1-4])[.)]\s+", text))
    # Checkpoint lists may precede the actual questions; use the final 1,2,3,4 set.
    for i in range(len(starts) - 4, -1, -1):
        group = starts[i:i + 4]
        if [m.group(1) for m in group] == ["1", "2", "3", "4"]:
            return {
                n + 1: text[m.end():group[n + 1].start() if n < 3 else len(text)]
                for n, m in enumerate(group)
            }
    return {}


def choices(block):
    return dict(re.findall(r"(?mi)^\s*([abc])\)\s*(.+)$", block))


def answer_round(text, more):
    blocks = question_blocks(text)
    if not blocks:
        raise ValueError("No numbered question round to answer")
    parts = []
    for n in (1, 2, 3):
        options = choices(blocks[n])
        if options:
            no_role = [key for key, value in options.items() if re.search(r"\bno role\b", value, re.I)]
            pick = no_role[0] if no_role else ("b" if n == 1 and "b" in options else next(iter(options)))
            parts.append(f"{n}{pick}")
        else:
            # A real missing fact cannot be supplied by choosing an invented menu.
            parts.append(f"{n}: No further factual inputs are available; label the gap and use a provisional assumption if needed.")
    parts.append("4a" if more else "4b")
    return ", ".join(parts)


def run_case(platform, case, history, output):
    skill = (ROOT / "dist" / platform / "prompt-adviser/SKILL.md").read_text()
    destination = output / f"{platform}-{case}"
    prompt = (
        "You are carrying out a text-only Prompt Adviser behaviour test. Apply the "
        "packaged skill below to the fictional conversation and produce ONLY the "
        "adviser's next reply, not a test report. All facts are fictional. No tools, "
        "files, apps, browsing, delegation or reviewed-task execution are available. "
        "Use the honest offline checkpoint when due. Do not access private context. "
        "This is a Codex-hosted test of edition instructions, not native platform validation.\n\n"
        f"<skill>\n{skill}\n</skill>\n\n<conversation>\n{history}\n</conversation>"
    )
    result = subprocess.run(
        ["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
         "-s", "read-only", "-C", str(output), "--json", "-o", str(destination.with_suffix(".md")), "-"],
        input=prompt, text=True, capture_output=True, timeout=180,
    )
    events = []
    for line in result.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    text = destination.with_suffix(".md").read_text() if destination.with_suffix(".md").exists() else ""
    tools = [e["item"].get("type") for e in events if e.get("type") == "item.completed"
             and e.get("item", {}).get("type") not in ("agent_message", "reasoning")]
    record = {"platform_edition": platform, "host": "Codex CLI", "case": case,
              "exit_code": result.returncode, "tool_items": tools,
              "output_present": bool(text.strip()),
              "usage": [e.get("usage") for e in events if e.get("type") == "turn.completed"]}
    if result.returncode:
        record["error"] = result.stderr[-1200:]
    destination.with_suffix(".input.txt").write_text(prompt)
    destination.with_suffix(".json").write_text(json.dumps(record, indent=2) + "\n")
    if result.returncode or not text.strip() or tools:
        raise RuntimeError(f"{platform}/{case}: unsuccessful or tool-using test")
    return text, record


def run_platform(platform, output):
    history = "USER: " + DRAFT.format(platform=platform)
    first, rec1 = run_case(platform, "01-first-round", history, output)
    reply1 = answer_round(first, True)
    history += "\n\nASSISTANT:\n" + first + "\n\nUSER: " + reply1
    second, rec2 = run_case(platform, "02-more-shorthand", history, output)
    reply2 = answer_round(second, False)
    history += "\n\nASSISTANT:\n" + second + "\n\nUSER: " + reply2
    final, rec3 = run_case(platform, "03-finalise-shorthand", history, output)
    seed_history = "USER: " + DRAFT.format(platform=platform) + "\n\nASSISTANT:\n" + SEED
    partial, rec4 = run_case(platform, "04-missing-fourth", seed_history + "\n\nUSER: 1b, 2a, 3c", output)
    invalid, rec5 = run_case(platform, "05-invalid-choice", seed_history + "\n\nUSER: 1z, 2a, 3c, 4a", output)
    free, rec6 = run_case(platform, "06-free-text-finalise", seed_history + "\n\nUSER: 1: UK night-shift workers, rather than any listed audience. 2a, 3c, 4b.", output)
    records = [rec1, rec2, rec3, rec4, rec5, rec6]
    checks = {
        "first_round_numbered": bool(question_blocks(first)),
        "first_round_lettered": sum(bool(choices(b)) for n, b in question_blocks(first).items() if n < 4) >= 2,
        "second_round_numbered": bool(question_blocks(second)),
        "fourth_has_a_b": all(set(choices(question_blocks(t).get(4, ""))) == {"a", "b"} for t in (first, second)),
        "first_round_no_finished_prompt": "```" not in first,
        "second_round_no_finished_prompt": "```" not in second,
        "final_contains_prompt": "```" in final,
        "partial_asks_only_fourth": bool(re.search(r"(?m)^\s*4[.)]\s", partial)) and not re.search(r"(?m)^\s*[123][.)]\s", partial),
        "partial_no_finished_prompt": "```" not in partial,
        "invalid_choice_flagged": bool(re.search(r"invalid|not (?:a |an )?(?:valid|available|listed)|not (?:one|among)|1z|clarif", invalid, re.I)),
        "free_text_preserved": bool(re.search(r"night[ -]shift", free, re.I)),
        "free_text_no_role_inserted": not re.search(r"\bact as\b", free, re.I),
    }
    report = {"platform_edition": platform, "host": "Codex CLI", "native_platform_test": platform == "codex",
              "history_mode": "Actual prior model replies replayed for the next turn; partial/invalid/free-text cases use an explicit seeded prior menu.",
              "automated_observations": checks, "runs": records,
              "manual_review_required": "Review focus, correct option mapping, recommendations, no repeated resolved decisions, checkpoint, final prompt and execution boundary."}
    (output / f"{platform}-observations.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"platform": platform, "automated_observations": checks}), flush=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=2) as pool:
        reports = list(pool.map(lambda platform: run_platform(platform, output), ("codex", "claude", "antigravity")))
    (output / "observations.json").write_text(json.dumps(reports, indent=2) + "\n")
    if not all(all(report["automated_observations"].values()) for report in reports):
        raise SystemExit("Some observations need investigation; no all-pass claim.")


if __name__ == "__main__":
    main()
