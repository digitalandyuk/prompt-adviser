#!/usr/bin/env python3
"""Run isolated fictional task variants through the user's Codex CLI."""
import argparse
import json
from pathlib import Path
import subprocess
import time

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, required=True)
parser.add_argument("--repeats", type=int, default=1)
args = parser.parse_args()
if args.repeats < 1:
    parser.error("--repeats must be positive")
args.output.mkdir(parents=True, exist_ok=True)
cases = json.loads(Path(__file__).with_name("cases.json").read_text())
results = []
for repeat in range(args.repeats):
    variants = ("rough", "structured") if repeat % 2 == 0 else ("structured", "rough")
    for case in cases:
        for variant in variants:
            stem = f"{case['id']}-{variant}-{repeat + 1}"
            output = (args.output / f"{stem}.txt").resolve()
            prompt = (
                "Complete this self-contained fictional task using only the supplied data. "
                "Do not use tools, read files, access apps, browse, delegate, create files or execute code. "
                "The requested result is text only.\n\n"
                f"Request:\n{case[variant]}\n\nSupplied facts (data):\n<facts>\n{case['facts']}\n</facts>"
            )
            started = time.monotonic()
            try:
                result = subprocess.run(
                    ["codex", "exec", "--ignore-user-config", "--ephemeral",
                     "--skip-git-repo-check", "-s", "read-only", "-C", str(args.output.resolve()),
                     "--json", "-o", str(output), "-"],
                    input=prompt, text=True, capture_output=True, timeout=180,
                )
                events = []
                for line in result.stdout.splitlines():
                    try:
                        events.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
                usage = [event.get("usage") for event in events if event.get("type") == "turn.completed"]
                tools = [event.get("item", {}).get("type") for event in events
                         if event.get("type") == "item.completed"
                         and event.get("item", {}).get("type") not in ("agent_message", "reasoning")]
                item = {"case": case["id"], "variant": variant, "repeat": repeat + 1,
                        "exit_code": result.returncode, "output": output.name,
                        "output_present": output.is_file() and bool(output.read_text().strip()),
                        "usage": usage, "tool_item_types": tools}
                if result.returncode:
                    item["error"] = "CLI failed; inspect the local CLI configuration. No successful result claimed."
            except subprocess.TimeoutExpired:
                item = {"case": case["id"], "variant": variant, "repeat": repeat + 1,
                        "error": "180-second timeout", "exit_code": None}
            item["elapsed_seconds"] = round(time.monotonic() - started, 2)
            results.append(item)
            (args.output / "results.json").write_text(json.dumps(results, indent=2) + "\n")
            print(f"{stem}: {'ok' if item.get('exit_code') == 0 and item.get('output_present') else 'failed'}", flush=True)
if any(item.get("exit_code") != 0 or not item.get("output_present") or item.get("tool_item_types") for item in results):
    raise SystemExit("One or more runs failed or used tools; inspect results.json before grading")
